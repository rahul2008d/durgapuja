from flask import (
    render_template,
    request,
    send_from_directory,
    redirect,
    url_for,
    flash,
    current_app,
    jsonify,
)

from sqlalchemy.exc import SQLAlchemyError
import re
from backend.models import User
from backend.database import db
from backend.encrypt import bcrypt
import os
from flask import session
from werkzeug.utils import secure_filename


def index():
    if "logged_in" in session and User.query.get(session["id"]) is not None:
        return redirect(url_for("my_blueprint.dashboard", id=session["user_id"]))
    return render_template("index.html")


def members():
    return render_template("members.html")


def gallery():
    return render_template("gallery.html")


def patrons():
    return render_template("patrons.html")


def login():
    return render_template("login.html")


def signin():
    try:
        # if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Validate email format
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return jsonify({"error": "Invalid email format"}), 400

        # Implement your sign-in logic here
        user = User.query.filter_by(email=email).first()

        if user is None:
            return jsonify({"error": "unauthorized"}), 401

        if not bcrypt.check_password_hash(user.password, password):
            print("hashed password not worked!")
            return jsonify({"error": "bad password"}), 401

        session["logged_in"] = True
        session["user_id"] = user.id

        return redirect(url_for("my_blueprint.dashboard", id=session["user_id"]))
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": "Database error: {}".format(str(e))}), 500
    except Exception as e:
        # Handle any other unexpected errors
        return jsonify({"error": "Unexpected error: {}".format(str(e))}), 500


def register():
    if request.method == "POST":
        try:
            # Retrieve form data
            email = request.form.get("email", "").strip()
            owner_name = request.form.get("owner_name", "").strip()
            co_owner_name = request.form.get("co_owner_name", "").strip() or None
            tower = request.form.get("tower", "").strip()
            floor = request.form.get("floor", "").strip()
            flat = request.form.get("flat_no", "").strip()
            password = request.form.get("password", "").strip()
            confirm_password = request.form.get("confirm_password", "").strip()

            # Validate email format
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return jsonify({"error": "Invalid email format"}), 400

            # Check if passwords match
            if password != confirm_password:
                return jsonify({"error": "Passwords do not match"}), 400

            # Validate required fields
            if not all([email, owner_name, tower, floor, flat, password]):
                return jsonify({"error": "All fields marked with * are required"}), 400

            # Check if user already exists
            user = User.query.filter_by(email=email).first()
            if user:
                return jsonify({"error": "Email ID already exists"}), 400

            # Hash the password
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

            # Create new user object
            new_user = User(
                email=email,
                owner_name=owner_name,
                co_owner_name=co_owner_name,
                tower=tower,
                floor=floor,
                flat=flat,
                password=hashed_password,
                user_image=None,
            )

            # Add new user to the database
            db.session.add(new_user)
            db.session.commit()

            # Redirect to login page after successful registration
            return redirect(url_for("my_blueprint.login"))

        except SQLAlchemyError as e:
            # Handle database errors
            db.session.rollback()
            return jsonify({"error": "Database error: {}".format(str(e))}), 500
        except Exception as e:
            # Handle any other unexpected errors
            return jsonify({"error": "Unexpected error: {}".format(str(e))}), 500

    # Handle GET request if necessary (e.g., rendering the registration form)
    return render_template("register.html")


def dashboard(id):
    try:
        if "logged_in" not in session:
            return redirect(url_for("my_blueprint.login"))
            # Fetch user details based on the provided email
        user_id = session["user_id"]
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            return jsonify({"error": "User not found"}), 404

        return render_template("dashboard.html", user=user)

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": "Database error: {}".format(str(e))}), 500
    except Exception as e:
        # Handle any other unexpected errors
        return jsonify({"error": "Unexpected error: {}".format(str(e))}), 500


def logout():
    try:
        session.pop("user_id", None)
        session.pop("logged_in", None)
        return redirect(url_for("my_blueprint.index"))
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": "Unexpected error: {}".format(str(e))}), 500


def upload_user_image():
    if "logged_in" in session:
        user = User.query.filter_by(email=session["user_id"]).first()

    if not user:
        flash("User not found", "error")
        return redirect(url_for("my_blueprint.login"))

    if "user_image" not in request.files:
        print("No file uploaded")
        return redirect(url_for("my_blueprint.dashboard", id=session["user_id"]))

    file = request.files["user_image"]

    filename = secure_filename(file.filename)
    file_path = os.path.join(
        current_app.root_path, "..", "frontend/static/uploads", filename
    )

    # Create the 'uploads' directory if it doesn't exist
    uploads_dir = os.path.join(current_app.root_path, "..", "frontend/static/uploads")
    os.makedirs(uploads_dir, exist_ok=True)

    # Save the file to the 'uploads' directory
    file.save(file_path)

    # Update the user's image in the database
    user.user_image = filename
    db.session.commit()

    return redirect(url_for("my_blueprint.dashboard", id=session["user_id"]))


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
