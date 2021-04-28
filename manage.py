from flask.cli import FlaskGroup

from PruebaAPI import app


cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()