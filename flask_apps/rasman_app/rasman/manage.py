import os, sys, socket, threading, subprocess, sys, tempfile, time, base64, paramiko, sqlite3

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)

from queue import Queue
queue = Queue()
ssh_hosts = []

from rasman.db import get_db

bp = Blueprint('manage', __name__)

@bp.route('/')
def index():
    db = get_db()
    pis = db.execute("SELECT * FROM hosts ORDER BY hostname").fetchall()
    os_name = os.name
    index = {
        'pis': pis,
        'local_details': [{'os_name': os_name}]
    }
    return render_template('manage/index.html', index=index)

@bp.route('/add', methods=('GET', 'POST'))
def add():
    pi = {'hostname': '', 'passwd': ''}
    error = None
    if request.method == 'POST':
        hostname = request.form['hostname']
        passwd = request.form['passwd']
        if hostname != '' and passwd != '':
            db = get_db()
            try:
                with db:
                    db.execute("INSERT INTO hosts (hostname, passwd) VALUES (?, ?)", (hostname, passwd))
                    db.commit()
            except sqlite3.IntegrityError:
                error = "Could not add host "+hostname
        else:
            error = 'Enter a valid hostname and password'
            # Print errors
            # flash(error)
            # return render_template('manage/add.html')
        if error is None:
            return redirect(url_for('index'))
        pi = {'hostname': hostname, 'passwd': passwd}
        flash(error)
    return render_template('manage/add.html', pi=pi)

@bp.route('/edit', methods=('GET', 'POST'))
def edit():
    if request.method == 'POST':
        # "UPDATE hosts SET hostname = ? WHERE hostname"
        return redirect(url_for('index'))
    db = get_db()
    hostname = request.args.get('hostname')
    pi = db.execute("SELECT * FROM hosts WHERE hostname = ?", (hostname,)).fetchone()
    print(pi)
    return render_template('manage/edit.html', pi=pi)

@bp.route('/details', methods=('GET',))
def details():
    hostname = request.args.get('hostname')
    result = ssh(hostname, "dietpi", "D4shb04rdp1", "cat /DietPi/dietpi.txt | grep SOFTWARE_CHROMIUM_AUTOSTART_URL")
    return render_template('manage/details.html', result=result)

@bp.route('/search', methods=('GET',))
def search():
    return render_template('manage/search.html')

@bp.route('/_ip_scan')
def ip_scan():
    results = {}
    for X in range(2, 255):
        ip = "192.168.10."+str(X)
        queue.put(ip)
    results = run_scanner(254)
    return jsonify(results)

# Port scanning

#def get_ip():
#    hostname = socket.gethostname()

def portscan(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(4.50)
        sock.connect((ip, port))
        return True
    except:
        print(ip, port, sys.exc_info()[0])
        return False

def worker():
    while not queue.empty():
        ip = queue.get()
        if portscan(ip, 22):
            ssh_hosts.append(ip)
        else: # Try a second time
            if portscan(ip, 22):
                ssh_hosts.append(ip)

def run_scanner(threads):
    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    return ssh_hosts

# SSH


## PASS IN LIST OF CMDS, and respond with values for each cmd
## { cmd: RESPONSE, cmd2: RESPONSE2 }
##
def ssh(host, username, passwd, cmd):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect(host, username=username, password=passwd)
    stdin, stdout, stderr = client.exec_command(cmd)
    response = ""
    for line in stdout:
        #print('... ' + line.strip('\n'))
        response += line
    client.close()
    return response