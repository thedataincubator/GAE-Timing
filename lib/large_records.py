from google.appengine.ext import ndb
from .timer import timer

NUM_RECORDS = 100
NUM_FIELDS = 10
FIELD_SIZE = 10000

class LargeRecords(ndb.Model):
  t0 = ndb.TextProperty()
  t1 = ndb.TextProperty()
  t2 = ndb.TextProperty()
  t3 = ndb.TextProperty()
  t4 = ndb.TextProperty()
  t5 = ndb.TextProperty()
  t6 = ndb.TextProperty()
  t7 = ndb.TextProperty()
  t8 = ndb.TextProperty()
  t9 = ndb.TextProperty()

  @classmethod
  def initialize(cls, string):
    x = cls()
    x.t0 = string
    x.t1 = string
    x.t2 = string
    x.t3 = string
    x.t4 = string
    x.t5 = string
    x.t6 = string
    x.t7 = string
    x.t8 = string
    x.t9 = string
    return x

def large_records_seed():
  counts = LargeRecords.query().count()
  if counts < NUM_RECORDS:
    for _ in xrange(NUM_RECORDS - counts):
      LargeRecords.initialize("a" * FIELD_SIZE).put()

  return "Done"

@timer
def large_records_query():
  return str(LargeRecords.query().fetch())
