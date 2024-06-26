from flask import Blueprint
from backend.views import (
    index,
    members,
    gallery,
    patrons,
    login,
    register,
    signin,
    dashboard,
    logout,
    upload_user_image,
    serve_react_static_file,
)

my_blueprint = Blueprint("my_blueprint", __name__)
my_blueprint.route("/", endpoint="index")(index)
my_blueprint.route("/members", endpoint="members")(members)
my_blueprint.route("/gallery", endpoint="gallery")(gallery)
my_blueprint.route("/patrons", endpoint="patrons")(patrons)
my_blueprint.route("/login-register", endpoint="login")(login)
my_blueprint.route("/register", methods=["GET", "POST"], endpoint="register")(register)
my_blueprint.route("/signin", methods=["GET", "POST"], endpoint="signin")(signin)
my_blueprint.route("/dashboard/<int:id>", endpoint="dashboard")(dashboard)
my_blueprint.route("/logout", methods=["GET", "POST"], endpoint="logout")(logout)
my_blueprint.route("/upload_image/", methods=["POST"], endpoint="upload_image")(
    upload_user_image
)


# Serve React static files
my_blueprint.route("/static/build/static/<path:filename>", methods=["GET"])(
    serve_react_static_file
)
