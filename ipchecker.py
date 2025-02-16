#!/usr/bin/env python
import sys
#import cookielib
#import urllib2
import json
import smtplib
import requests

default_details = '{"ip": "0.0.0.0", "latlong": "0,0", "country": "X", "city": "X", "user-agent": "UA"}'

def send_email(user, pwd, recipient, subject, body):
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        #print('successfully sent the mail')
    except:
        print("failed to send mail")


def compare_stored_ip( stored_ip ):
#    try:
        s = requests.Session()
        res = s.get("https://api.ipify.org/?format=json")
        #jsonString = res.json()
        jsonString = res.text
        #print(jsonString)
        d = json.loads(jsonString)
        #print(d)
        current_ip = d['ip']
        if stored_ip != current_ip:
            email_new_ip( current_ip )
            store_details( jsonString )
#    except:
#        print("Could not fetch IP: ", sys.exc_info()[0])

def email_new_ip( details ):
    #print(details)
    #!!!!!!!!!!!!!!  Change these details  !!!!!!!!!!!!!!
    #!!!!!!!!!!!!!! can use list for recip !!!!!!!!!!!!!!
    send_email('ruan804@gmail.com', 'Nifty2;pence', 'ruan800@gmail.com', 'Ip Change', details)

def store_details ( details ):
    f = open('.ip_json_details', 'w+')
    f.write(details)
    f.close()

try:
    f = open('.ip_json_details', 'r')
    details = f.readline()
    f.close()
    d = json.loads(details)
    compare_stored_ip( d['ip'] )
except IOError as e:
    #print "I/O error({0}): {1}".format(e.errno, e.strerror)
    f = open('.ip_json_details', 'w+')
    f.write(default_details)
    f.close()
    d = json.loads(default_details)
    compare_stored_ip( d['ip'] )
# except ValueError:
#     print "Could not convert data to an integer."
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

