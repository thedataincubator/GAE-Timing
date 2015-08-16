import time
import functools
from simplejson import dumps

def timer(function):
  @functools.wraps(function)
  def wrapped_function(*args, **kwargs):
    c1, t1 = time.clock(), time.time()
    result = function(*args, **kwargs)
    c2, t2 = time.clock(), time.time()
    return dumps({ 'time': (t2-t1) / 1000, 'clock': (c2-c1) / 1000, 'result': result[:1000], 'length': len(result) })
  return wrapped_function
