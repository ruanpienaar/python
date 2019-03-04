from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

# Db Access
from grub.db import get_db

# Grub specific
import datetime
import urllib2


bp = Blueprint('orders', __name__)

@bp.route('/')
def index():
    db = get_db()
    orders = db.execute(
        'SELECT * FROM orders ORDER BY created DESC'
    ).fetchall()
    # iframe = urllib.request.urlopen("http://example.com/foo/bar").read()

    iframe = contents = urllib2.urlopen("http://example.com/foo/bar").read()    

    return render_template('orders/index.html', orders=orders, iframe=iframe)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    db = get_db()
    users = db.execute(
        'SELECT * FROM users ORDER BY username ASC'
    ).fetchall()
    if request.method == 'POST':
        order_menu = request.form['order_menu']
        orderer = request.form['orderer']
        order_date = request.form['datepicker']
        order_time = request.form['timepicker']
        currentDT = datetime.datetime.now()
        db.execute(
           'INSERT INTO orders (created, order_menu, orderer, order_date, order_time, order_status)'
           'VALUES (?, ?, ?, ?, ?, ?)',
           (currentDT, order_menu, orderer, order_date, order_time, 'ordering')
        )
        db.commit()
        return redirect(url_for('orders.index'))
    return render_template('orders/create.html', users=users)

#@bp.route('/list_topics', methods=('GET', 'POST'))
#def list_topics():
#    # b_host = 'localhost'
#    # b_port = '9092'
#    b_host = request.args.get('host')
#    b_port = request.args.get('port')
#    consumer = KafkaConsumer(bootstrap_servers=b_host+':'+b_port)
#    # print consumer.topics()
#    return render_template('broker/list_topics.html', topics=consumer.topics())