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

from backend.models import User
from backend.database import db
from backend.encrypt import bcrypt
import os
from backend.utils import send_welcome_email
from flask import session
from werkzeug.utils import secure_filename


def index():
    if "logged_in" in session:
        return redirect(
            url_for("my_blueprint.dashboard", user_email=session["user_email"])
        )
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
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Implement your sign-in logic here
        user = User.query.filter_by(email=email).first()

        if user is None:
            return jsonify({"error": "unauthorized"}), 401

        if not bcrypt.check_password_hash(user.password, password):
            print("hashed password not worked!")
            return jsonify({"error": "unauthorized"}), 401

        session["logged_in"] = True
        session["user_email"] = email

        # Redirect to user dashboard
        return redirect(url_for("my_blueprint.dashboard", user_email=email))


def register():
    if request.method == "POST":
        email = request.form["email"]
        owner_name = request.form["owner_name"]
        co_owner_name = request.form.get("co_owner_name")
        tower = request.form["tower"]
        floor = request.form["floor"]
        flat = request.form["flat_no"]
        password = request.form["password"]

        user_exists = (
            User.query.filter_by(email=email, password=password).first() is not None
        )
        if user_exists:
            pass

        hashed_password = bcrypt.generate_password_hash(password)
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
        try:
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for("my_blueprint.login"))
        except Exception as e:
            print(
                f"Error adding user to the database: {e}"
            )  # Add this line for debugging


def dashboard(user_email):
    if "user_email" in session and session["user_email"] == user_email:
        # Fetch user details based on the provided email
        user = User.query.filter_by(email=user_email).first()
        if user:
            return render_template("dashboard.html", user=user)

    # If user is not logged in or user_email does not match session, redirect to login
    flash("Please login to access the dashboard", "error")
    return redirect(url_for("my_blueprint.login"))


def logout():
    session.pop("user_email", None)
    session.pop("logged_in", None)
    return redirect(url_for("my_blueprint.index"))


def upload_user_image():
    print(session)
    # if 'user_email' not in session or session['user_email'] != user_email:
    #     flash('Please login to access the dashboard', 'error')
    #     return redirect(url_for('my_blueprint.login'))

    if "logged_in" in session:
        user = User.query.filter_by(email=session["user_email"]).first()

    if not user:
        flash("User not found", "error")
        return redirect(url_for("my_blueprint.login"))

    if "user_image" not in request.files:
        print("No file uploaded")
        return redirect(
            url_for("my_blueprint.dashboard", user_email=session["user_email"])
        )

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

    return redirect(url_for("my_blueprint.dashboard", user_email=session["user_email"]))


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
