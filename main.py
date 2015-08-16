"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, url_for
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

from google.appengine.api import memcache
from lib.many_record import ManyRecord
from lib.large_record import LargeRecord
from lib.structured_record import StructuredRecord
from lib.repeated_record import RepeatedRecord
from lib.key_record import KeyRecord
from lib.repeated_key_record import RepeatedKeyRecord
from simplejson import dumps

@app.route('/')
def hello():
  """Return a friendly HTTP greeting."""
  return 'Hello World!'


@app.errorhandler(404)
def page_not_found(e):
  """Return a custom 404 error."""
  return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
  """Return a custom 500 error."""
  return 'Sorry, unexpected error: {}'.format(e), 500

ManyRecord.register(app)
LargeRecord.register(app)
StructuredRecord.register(app)
RepeatedRecord.register(app)
KeyRecord.register(app)
RepeatedKeyRecord.register(app)

@app.route("/flush_memcache", methods=['POST'])
def flush_memcache():
  memcache.flush_all()
  return "Done"

def has_no_empty_params(rule):
  defaults = rule.defaults if rule.defaults is not None else ()
  arguments = rule.arguments if rule.arguments is not None else ()
  return len(defaults) >= len(arguments)

@app.route("/site-map")
def site_map():
  return dumps([url_for(rule.endpoint)
    for rule in app.url_map.iter_rules()
    if ("GET" in rule.methods or "POST" in rule.methods) and has_no_empty_params(rule)
  ])

