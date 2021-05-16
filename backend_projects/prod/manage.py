from flask.cli import FlaskGroup
from prod import create_app, db
import os

app = create_app()
with app.app_context():
    db.create_all()

if os.getenv("FLASK_ENV") == 'development':
    from flask_cors import CORS
    CORS(app)

cli = FlaskGroup(create_app=create_app)

@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == "__main__":
    cli()
