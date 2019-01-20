from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

# Db Access
from kritique.db import get_db

# Kafka Related imports
from kafka import KafkaConsumer

bp = Blueprint('topic', __name__, url_prefix='/topic')

@bp.route('/list_messages', methods=('GET', 'POST'))
def list_messages():
    b_host = request.args.get('host')
    b_port = request.args.get('port')
    topic = request.args.get('topic')
    # TODO: make a consumer module, that's generic
    consumer = KafkaConsumer(bootstrap_servers=b_host+':'+b_port,
                                     auto_offset_reset='earliest',
                                     consumer_timeout_ms=1000)
    consumer.subscribe([topic])    
    # for message in consumer:
        # print(message)
    
    # TODO: consumer.close()

    return render_template('topic/list_messages.html', topic=topic, consumer=consumer)