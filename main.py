"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, url_for
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

from google.appengine.ext import ndb
from google.appengine.ext import deferred
from lib.many_records import ManyRecords
from lib.large_records import LargeRecords
from lib.structured_property import StructuredHolder
from lib.repeated_records import RepeatedRecords
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

ManyRecords.register(app)
LargeRecords.register(app)
StructuredHolder.register(app)
RepeatedRecords.register(app)

def has_no_empty_params(rule):
  defaults = rule.defaults if rule.defaults is not None else ()
  arguments = rule.arguments if rule.arguments is not None else ()
  return len(defaults) >= len(arguments)

@app.route("/site-map")
def site_map():
  return dumps([url_for(rule.endpoint)
    for rule in app.url_map.iter_rules()
    if "GET" in rule.methods and has_no_empty_params(rule)
  ])
