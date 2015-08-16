import requests
from urlparse import urljoin
import sys
import time

if __name__ == '__main__':
  # seed website
  base_url = sys.argv[1]

  print "Fetching root"
  assert requests.get(urljoin(base_url, '/site-map')).status_code == 200

  print "Fetching sitemap"
  site_map = requests.get(urljoin(base_url, '/site-map')).json()
  seeds = [route.strip() for route in site_map if 'seed' in route]
  queries = sorted([route.strip() for route in site_map if 'query' in route])

  print "Seeding data ..."
  for route in seeds:
    requests.post(urljoin(base_url, route))

  print "Flushing memchace ..."
  requests.post(urljoin(base_url, "/flush_memcache"))

  print "Querying ..."
  for route in queries:
    t1 = time.time()
    response = requests.get(urljoin(base_url, route)).json()
    server_time = response['time']
    server_clock = response['clock']
    length = response['length']
    t2 = time.time()
    request_time = (t2 - t1) / 1000.
    print "%.6f - %.6f - %.6f - %10d - %s" % (request_time, server_time, server_clock, length, route)
