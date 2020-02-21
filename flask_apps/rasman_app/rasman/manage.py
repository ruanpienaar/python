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
    pis = db.execute("SELECT * FROM hosts").fetchall()
    # tvs = db.execute("SELECT * FROM tv").fetchall()
    os_name = os.name
    index = {
        'pis': pis
        # 'tvs': tvs
        # 'local_details': [{'os_name': os_name}]
    }
    return render_template('manage/index.html', index=index)

@bp.route('/add', methods=('GET', 'POST'))
def add():
    pi = {'hostname': '', 'description': '', 'passwd': ''}
    error = None
    if request.method == 'POST':
        hostname = request.form['hostname']
        description = request.form['description']
        passwd = request.form['passwd']
        username = request.form['username']
        if hostname != '' and passwd != '' and username != '':
            db = get_db()
            try:
                with db:
                    db.execute("INSERT INTO hosts (hostname, description, passwd, username) VALUES (?, ?, ?, ?)", (hostname, description, passwd, username))
                    db.commit()
            except sqlite3.IntegrityError:
                error = "Could not add duplicate host = "+hostname
        else:
            error = 'Enter a valid hostname and password'
        if error is None:
            return redirect(url_for('index'))
        pi = {'hostname': hostname, 'passwd': passwd, 'description': description, 'username': username}
        flash(error)
    return render_template('manage/add.html', pi=pi)

@bp.route('/edit', methods=('GET', 'POST'))
def edit():
    if request.method == 'POST':
        hostname = request.form['hostname']
        description = request.form['description']
        passwd = request.form['passwd']
        old_hostname = request.form['old_hostname']
        db = get_db()
        db.execute("UPDATE hosts SET hostname = ?, description = ?, passwd = ? WHERE hostname = ?", (hostname, description, passwd, old_hostname))
        db.commit()
        return redirect(url_for('index'))
    # db = get_db()
    hostname = request.args.get('hostname')
    # pi = db.execute("SELECT * FROM hosts WHERE hostname = ?", (hostname,)).fetchone()
    pi = get_pid_details(hostname)
    # print(pi)
    return render_template('manage/edit.html', pi=pi)

@bp.route('/details', methods=('GET', 'POST'))
def details():
    if request.method == 'POST':
        hostname = request.form['hostname']
        pi = get_pid_details(hostname)
        old_url = request.form['old_pi_url'].strip()
        new_url = request.form['pi_url'].strip()
        new_url_escp = new_url.translate(str.maketrans({"&": r"\&"}))
        sed_cmd = "sudo sed -i 's#SOFTWARE_CHROMIUM_AUTOSTART_URL="+old_url+"#SOFTWARE_CHROMIUM_AUTOSTART_URL="+new_url_escp+"#g' /DietPi/dietpi.txt && echo $?"
        # success = ssh(hostname, pi['username'], pi['passwd'], "echo success")
        # print(test)

        # if (success == 'success\n'):
        #     ok
        # else:

        r1 = ssh(hostname, "dietpi", "D4shb04rdp1", sed_cmd)
        r2 = ssh(hostname, "dietpi", "D4shb04rdp1", "sudo reboot ")
        return redirect(url_for('index'))
    hostname = request.args.get('hostname')
    pi = get_pid_details(hostname)
    # print(pi)
    if host_port_scan_and_set(pi['hostname'], pi['port']):
        get_url_cmd = "cat /DietPi/dietpi.txt | grep SOFTWARE_CHROMIUM_AUTOSTART_URL | awk -F'SOFTWARE_CHROMIUM_AUTOSTART_URL=' '{print$2}'"
        result = ssh(pi['hostname'], pi['username'], pi['passwd'], get_url_cmd)
        return render_template('manage/details.html', result=result, hostname=hostname)
    else:
        return redirect(url_for('index'))

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

# To be used on the add page, to test connectivity
@bp.route('/_host_port_scan')
def host_port_scan():
    hostname = request.args.get('hostname')
    port = request.args.get('port')
    if host_port_scan(hostname, port):
        return "true"
    else:
        return "false"

@bp.route('/_refresh_node')
def refresh_node():
    # print(request.args['hostname'])
    hostname = request.args['hostname']
    pi = get_pid_details(hostname)
    xdocheck = ssh(pi['hostname'], pi['username'], pi['passwd'], "xdotool -v || echo $?")
    if(xdocheck == '127\n'):
        return "xdotool missing on remote host.\nsudo apt install xdotool -y"
    else:
        r1 = ssh(hostname, pi['username'], pi['passwd'], "export DISPLAY=\":0\"; xdotool key ctrl+F5")
        return "Refreshed page with " + xdocheck

### Common db functions

# def host_port_scan(hostname, port):
#     if hostname_portscan(hostname, port):
#         print("Port open")
#         return True
#     else:
#         print("Port not open")
#         return False

def host_port_scan_and_set(hostname, port):
    if ip_portscan(hostname, port):
        print("Port open")
        set_can_connect(hostname, True)
        return True
    else:
        print("Port not open")
        set_can_connect(hostname, False)
        return False

def set_can_connect(hostname, can_connect):
    db = get_db()
    db.execute("UPDATE hosts SET can_connect = ?WHERE hostname = ?", (can_connect, hostname))
    db.commit()

def get_pid_details(hostname):
    db = get_db()
    pi_db_obj = db.execute("SELECT * FROM hosts WHERE hostname = ?", (hostname,)).fetchone()
    # print(pi_db_obj)
    hostname = pi_db_obj["hostname"]
    port = pi_db_obj["port"]
    can_connect = pi_db_obj["can_connect"]
    description = pi_db_obj["description"]
    username = pi_db_obj["username"]
    passwd = pi_db_obj["passwd"]
    dashboard_url = pi_db_obj["dashboard_url"]
    hostname = ''.join(hostname)
    # if port != None:
    #     port = ''.join(port)
    # can_connect = ''.join(can_connect)
    description = ''.join(description)
    username = ''.join(username)
    passwd = ''.join(passwd)
    # print(dashboard_url)
    if dashboard_url != None:
        dashboard_url = ''.join(dashboard_url)
    return {
        'hostname': hostname,
        'port': port,
        'can_connect': can_connect,
        'description': description,
        'username': username,
        'passwd': passwd,
        'dashboard_url': dashboard_url
    }

# Port scanning

#def get_ip():
#    hostname = socket.gethostname()

# def hostname_portscan(hostname, port):
#     ip_portscan(hostname, port)

def ip_portscan(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((ip, port))
        return True
    except:
        print(ip, port, sys.exc_info()[0])
        return False

def worker():
    while not queue.empty():
        ip = queue.get()
        if ip_portscan(ip, 22):

            # Get hostname for ip

            ssh_hosts.append(ip)
        else: # Try a second time
            if ip_portscan(ip, 22):
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
    response.strip('\n')
    client.close()
    return response