

from prometheus_api_client import PrometheusConnect
from prometheus_api_client.utils import parse_datetime
from datetime import timedelta

#start_time = parse_datetime("2d")
#end_time = parse_datetime("now")
#chunk_size = timedelta(days=1)

prom = PrometheusConnect(url ="https://prometheus.qa.hubble.superbet.com", disable_ssl=False)

# Get the list of all the metrics that the Prometheus host scrapes

my_label_config = {'job': 'spoout-snapshot'}
prom.get_current_metric_value(metric_name='beam_cpu', label_config=my_label_config)

print( prom.custom_query(query="beam_cpu{ job = 'spoout-snapshot' ") )


# metric_data = prom.get_metric_range_data(
#     "sum(beam_cpu{ job=\"spoout-snapshot\", type=\"scheduler_usage\" }) by (job)",  # this is the metric name and label config
#     start_time=start_time,
#     end_time=end_time,
#     chunk_size=chunk_size,
# )

