from flask_mail import Message
import threading
from flask import current_app

def send_async_email(app, msg):
    with app.app_context():
        from backend import mail  # Import mail within the function to avoid circular imports
        mail.send(msg)

def send_welcome_email(to_email):
    app = current_app._get_current_object()
    msg = Message(
        subject="Thank You for Joining Us!",
        recipients=[to_email],
        body="Thank you for joining us. Stay tuned for more information."
    )
    thread = threading.Thread(target=send_async_email, args=(app, msg))
    thread.start()
