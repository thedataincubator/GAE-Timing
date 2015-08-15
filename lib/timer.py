import time
import functools
from simplejson import dumps

def timer(function):
  @functools.wraps(function)
  def wrapped_function():
    start= time.clock()
    result = function()
    end= time.clock()
    return dumps({ 'time': (end-start) / 1000, 'result': dumps(result)[:1000] })
  return wrapped_function
