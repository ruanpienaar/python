from prometheus_client import start_http_server, Gauge
#import random
import time, subprocess, re, os

# Create a metric to track time spent and requests made.
# REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
# @REQUEST_TIME.time()
# def process_request(t):
#    """A dummy function that takes some time."""
#    time.sleep(t)

g1 = Gauge('raspberry_pi_temp', 'Raspberry pi temperature')
g2 = Gauge('raspberry_pi_disk_usage', 'Raspberry pi /dev/root disk usage')

def get_temp():
    temp_string = subprocess.check_output(["vcgencmd", "measure_temp"])
    p = re.compile('temp=(.*)\'C\n')
    toks = p.split(temp_string)
    temp = toks[1]
    # print temp
    g1.set(temp)

def get_disk_usage():
    usage_percentage = subprocess.check_output( os.getcwd() + '/get_disk_usage.sh' )
    p = re.compile('(.*)%\n')
    toks = p.split(usage_percentage)
    # print usage_percentage
    disk_usage = toks[1]
    g2.set(disk_usage)
    
if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(9999)
    # Generate some requests.
    while True:
    #    process_request(random.random())
        get_temp()
        get_disk_usage()
        time.sleep(5)