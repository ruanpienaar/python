#!/usr/bin/env python

import os, sys, sqlite3, datetime, threading, time
# TODO: use get opt
# getopt,

def main(args):

    # Todo:
    # maybe pass in directory, to listen for new log files being created

    # for now just take first logfile
    # scrape_logfile(args[0])
    threads = []
    for logfile in args:
        # print 'starting thread for '+logfile
        t = threading.Thread(target = scrape_logfile, args=(logfile, ))
        threads.append(t)
        # t.daemon = True
        t.start()

def scrape_logfile(logfile):
    # Close thread if else was hit after a few seconds
    conn = sqlite3.connect('scrimp.db')
    cur = conn.cursor()
    print 'started thread for '+logfile
    cur.execute("CREATE TABLE IF NOT EXISTS '%s' (id INTEGER PRIMARY KEY ASC, last_modified TEXT, data TEXT);" % logfile)
    cur.execute("select MAX(id) from '%s'" % logfile)
    max_value = cur.fetchone()
    if max_value == (None,):
        id_val = 1
    else:
        id_val = int("%s" % max_value)
    pos = 1
    with open(logfile) as f:
        while True:
            time.sleep(0.05)
            line = f.readline()
            if line:
                if pos < id_val:
                    pos += 1
                else:
                    pos += 1
                    id_val += 1
                    info = os.stat(logfile)
                    last_modified = datetime.datetime.fromtimestamp(info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                    try:
                        # Move DB queries to single thread, multiple threads lock the db
                        cur.executemany(("INSERT INTO '%s' (id, last_modified, data) VALUES (?, ?, ?)" % logfile),
                                        [(id_val, last_modified, line, )])
                        # sys.stdout.write(logfile+' . ')
                        # sys.stdout.flush()
                        # print logfile + '.'
                    except sqlite3.IntegrityError:
                        print 'Duplicate no biggie'
                    except:
                        print "Unexpected error:", sys.exc_info()[0]
                    else:
                        conn.commit()
            # else:
            #     print logfile+' else'

if __name__ == "__main__":
    # 0 is script name, take 1 onwards
     main(sys.argv[1:])