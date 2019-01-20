from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

# Kafka Related imports
from kafka import KafkaConsumer

bp = Blueprint('broker', __name__, url_prefix='/broker')

@bp.route('/')
def index():
    b_host = 'localhost'
    b_port = '9092'
    brokers = [
        {
            "hostname": b_host,
            "port": b_port
        }
    ]
    return render_template('broker/index.html', brokers=brokers)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        b_host = request.form['broker_hostname']
        b_port = request.form['broker_port']
        
        return redirect(url_for('broker.index'))
    return render_template('broker/create.html')

@bp.route('/list_topics', methods=('GET', 'POST'))
def list_topics():
    b_host = 'localhost'
    b_port = '9092'
    consumer = KafkaConsumer(bootstrap_servers=b_host+':'+b_port)
    # print consumer.topics()
    return render_template('broker/list_topics.html', topics=consumer.topics())