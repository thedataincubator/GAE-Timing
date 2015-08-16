import requests
from urlparse import urljoin
import sys
import time

def fetch_result(base_url, route):
  t1 = time.time()
  response = requests.get(urljoin(base_url, route)).json()
  t2 = time.time()
  response['request_time'] = (t2 - t1) / 1000.
  response['route'] = route
  return response

def fetch_results(base_url):
  print "Fetching root"
  assert requests.get(urljoin(base_url, '/')).status_code == 200

  print "Fetching sitemap"
  site_map = requests.get(urljoin(base_url, '/site-map')).json()
  seeds = [route.strip() for route in site_map if 'seed' in route]
  queries = sorted([route.strip() for route in site_map if 'query' in route])

  print "Seeding data ..."
  for route in seeds:
    assert requests.post(urljoin(base_url, route)).status_code == 200

  print "Flushing memchace ..."
  requests.post(urljoin(base_url, "/flush_memcache"))

  print "Querying ..."
  return [fetch_result(base_url, route) for route in queries]


if __name__ == '__main__':
  # seed website
  base_url = sys.argv[1]
  results = fetch_results(base_url)

  for result in results:
    print "%.6f - %.6f - %.6f - %10d - %s" % (
      result['request_time'],
      result['time'],
      result['clock'],
      result['length'],
      result['route']
    )
