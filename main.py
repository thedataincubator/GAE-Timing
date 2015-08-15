"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

from google.appengine.ext import ndb
from google.appengine.ext import deferred
from lib.many_records import many_records_seed, many_records_query, many_records_projection_query
from lib.large_records import large_records_seed, large_records_query
from lib.structured_property import structured_property_seed, structured_property_query, structured_property_projection_query
from lib.repeated_records import repeated_records_seed, repeated_records_query
from simplejson import dumps

class Counter(ndb.Model):
  count = ndb.IntegerProperty(indexed=False)

def reset():
  ndb.delete_multi(Counter().query().fetch(keys_only=True, use_cache=False, use_memcache=False))

def increment():
  counter = Counter().query().get(use_cache=False, use_memcache=False)
  if not counter:
    counter = Counter(count=0)

  counter.count += 1
  counter.put()

  if counter.count < 10:
    deferred.defer(increment)

@app.route('/')
def hello():
  """Return a friendly HTTP greeting."""
  reset()
  deferred.defer(increment)
  return 'Hello World!'


@app.errorhandler(404)
def page_not_found(e):
  """Return a custom 404 error."""
  return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
  """Return a custom 500 error."""
  return 'Sorry, unexpected error: {}'.format(e), 500

app.route('/many_records/seed')(many_records_seed)
app.route('/many_records/query')(many_records_query)
app.route('/many_records/projection_query')(many_records_projection_query)
app.route('/large_records/seed')(large_records_seed)
app.route('/large_records/query')(large_records_query)
app.route('/structured_property/seed')(structured_property_seed)
app.route('/structured_property/query')(structured_property_query)
app.route('/structured_property/projection_query')(structured_property_projection_query)
app.route('/repeated_records/seed')(repeated_records_seed)
app.route('/repeated_records/query')(repeated_records_query)
