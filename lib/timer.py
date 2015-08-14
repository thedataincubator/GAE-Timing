import time
import functools

def timer(function):
  @functools.wraps(function)
  def wrapped_function():
    start= time.clock()
    result = function()
    end= time.clock()
    return str({ 'time': (end-start) / 1000, 'result': str(result)[:1000] })
  return wrapped_function
