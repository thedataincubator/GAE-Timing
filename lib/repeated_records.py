from google.appengine.ext import ndb
from .timer import timer

NUM_RECORDS = 100
NUM_FIELDS = 100
FIELD_SIZE = 100

class RepeatedRecords(ndb.Model):
  a = ndb.StringProperty(repeated=True)

  @classmethod
  def initialize(cls, string):
    x = cls()
    x.a = [string] * NUM_FIELDS
    return x

def repeated_records_seed():
  counts = RepeatedRecords.query().count()
  if counts < NUM_RECORDS:
    for _ in xrange(NUM_RECORDS - counts):
      RepeatedRecords.initialize("a" * FIELD_SIZE).put()

  return "Done"

@timer
def repeated_records_query():
  return str(RepeatedRecords.query().fetch())
