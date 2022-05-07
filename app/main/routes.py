from flask import Blueprint, render_template, session, flash, send_from_directory, url_for, abort
import os
from app import app

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def homepage():
    # if logged in, display the correct image depending on the user's role
    if 'login' in session:
        try:
            roles = session['login']['roles']
            if 'admin-user' in roles:
                image = url_for('main.protected', filename='admin.png')
            elif 'special-user' in roles:
                image = url_for('main.protected', filename='special.jpeg')
            elif 'common-user' in roles:
                image = url_for('main.protected', filename='user.png')
        except TypeError: # when user has no roles, roles is NoneType and as such non iterable
            flash('You logged in successfully but have no roles, contact admin.', 'error')
    else:
        # if not logged in, return default welcome image
        image = url_for('static', filename='welcome.jpeg')

    return render_template("base.html", image=image)


@main_bp.route('/protected/<path:filename>')
def protected(filename):
    # return protected image only if logged in
    if 'login' in session:
        return send_from_directory(
            os.path.join(app.root_path, 'protected'), filename)
    else:
        abort(404)