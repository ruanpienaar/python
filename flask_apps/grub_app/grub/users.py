from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

# Db Access
from grub.db import get_db

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/list', methods=('GET', 'POST'))
def list():
    db = get_db()
    users = db.execute(
        'SELECT * FROM users ORDER BY username ASC'
    ).fetchall()
    return render_template('users/index.html', users=users)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        username = request.form['username']
        print username
        db = get_db()
        db.execute(
            'INSERT INTO users (username)'
            'VALUES (?)',
            (username, )
        )
        db.commit()
        return redirect(url_for('users.list'))
    return render_template('users/create.html')