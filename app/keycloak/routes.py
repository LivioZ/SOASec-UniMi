from flask import Blueprint, url_for, session, redirect
from app import oauth, kc_client_id, kc_client_secret

kc_bp = Blueprint('kc', __name__)

kc = oauth.register(
    name = 'kc',
    client_id = kc_client_id,
    client_secret = kc_client_secret,
    server_metadata_url='https://xxxx.com/auth/realms/realmname/.well-known/openid-configuration',
    client_kwargs = {'scope': 'openid'},
)

# OpenID Connect Authorization Code Flow
@kc_bp.route('/login/kc')
def kc_login():
    redirect_uri = url_for('.kc_authorize', _external=True)
    # redirect to Keycloak server
    return kc.authorize_redirect(redirect_uri)

@kc_bp.route('/authorize/kc')
def kc_authorize():
    token = kc.authorize_access_token()
    # get the roles info from the ID token
    session['login'] = {
        'name': token.get('userinfo').get('name'),
        'roles': token.get('userinfo').get('roles')
    }
    return redirect('/')


@kc_bp.route('/logout')
def logout():
    # clear the session data and logout the user from Keycloak
    session.clear()
    return redirect('https://xxxx.com/auth/realms/realmname/protocol/openid-connect/logout?redirect_uri=xxxx.com/')
