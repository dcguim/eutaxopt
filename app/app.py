import connexion
from flask import Flask
app = Flask(__name__)


def create_app() -> connexion.FlaskApp:
    connexion_app = connexion.FlaskApp(__name__)
    connexion_app.add_api('eutaxopt.yaml')
    return connexion_app

if __name__ == '__main__':
        app = create_app()
        app.run(#threaded=True,
                host='0.0.0.0',
                port=8080)
