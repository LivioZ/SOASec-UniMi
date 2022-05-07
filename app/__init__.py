from flask import Flask
from authlib.integrations.flask_client import OAuth
import json
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1) # trust the X-Forwarded-Proto header set: http or https

with open('app/client_secrets.json') as f:
    secrets = json.load(f)
    app.secret_key = secrets['secret_key']
    kc_client_id = secrets['kc_client_id']
    kc_client_secret = secrets['kc_client_secret']

oauth = OAuth(app)

# import and register routes
from app.main.routes import main_bp
from app.keycloak.routes import kc_bp

app.register_blueprint(main_bp)
app.register_blueprint(kc_bp)
