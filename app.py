from backend import create_app, db
from backend.routes import my_blueprint
from backend.views import index

app = create_app()

app.add_url_rule('/', view_func=index)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)