"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

from google.appengine.ext import ndb
from google.appengine.ext import deferred

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
