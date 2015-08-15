import requests
from urlparse import urljoin
import sys

if __name__ == '__main__':
  # seed website
  base_url = sys.argv[1]

  site_map = requests.get(urljoin(base_url, '/site-map')).json()
  seeds = [route.strip() for route in site_map if 'seed' in route]
  queries = sorted([route.strip() for route in site_map if 'query' in route])

  print "Seeding data ..."
  for route in seeds:
    requests.get(urljoin(base_url, route))

  print "Querying ..."
  for route in queries:
    print "%.6f - %s" % (requests.get(urljoin(base_url, route)).json()['time'], route)
