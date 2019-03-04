from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

# Db Access
from kritique.db import get_db

# Kafka Related imports
from kafka import KafkaConsumer

bp = Blueprint('broker', __name__)

@bp.route('/')
def index():
    db = get_db()
    brokers = db.execute(
        'SELECT * FROM broker ORDER BY hostname'
    ).fetchall()
    return render_template('broker/index.html', brokers=brokers)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        b_host = request.form['broker_hostname']
        b_port = request.form['broker_port']
        db = get_db()
        db.execute(
            'INSERT INTO broker (hostname, port)'
            'VALUES (?, ?)',
            (b_host, b_port)
        )
        db.commit()
        return redirect(url_for('broker.index'))
    return render_template('broker/create.html')

@bp.route('/list_topics', methods=('GET', 'POST'))
def list_topics():
    # b_host = 'localhost'
    # b_port = '9092'
    b_host = request.args.get('host')
    b_port = request.args.get('port')
    consumer = KafkaConsumer(bootstrap_servers=b_host+':'+b_port)
    # print consumer.topics()
    return render_template('broker/list_topics.html', topics=consumer.topics())

@bp.route('/delete_broker', methods=('POST',))
def delete_broker():
    print ""
    #     id = request.args.get('id')
    #     db = get_db()
    #     sql = 'DELETE FROM tasks WHERE id=?'
    #     cur = conn.cursor()
    #     cur.execute(sql, (id,))
