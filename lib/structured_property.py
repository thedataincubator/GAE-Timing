from google.appengine.ext import ndb
from .timer import timer

NUM_RECORDS = 100
NUM_FIELDS = 100
FIELD_SIZE = 100

class StructuredValue(ndb.Model):
  a0 = ndb.StringProperty()
  a1 = ndb.StringProperty()
  a2 = ndb.StringProperty()
  a3 = ndb.StringProperty()
  a4 = ndb.StringProperty()
  a5 = ndb.StringProperty()
  a6 = ndb.StringProperty()
  a7 = ndb.StringProperty()
  a8 = ndb.StringProperty()
  a9 = ndb.StringProperty()
  a0 = ndb.StringProperty()

  @classmethod
  def initialize(cls, string):
    x = cls()
    x.a0 = string
    x.a1 = string
    x.a2 = string
    x.a3 = string
    x.a4 = string
    x.a5 = string
    x.a6 = string
    x.a7 = string
    x.a8 = string
    x.a9 = string
    return x

class StructuredHolder(ndb.Model):
  s0 = ndb.StructuredProperty(StructuredValue)
  s1 = ndb.StructuredProperty(StructuredValue)
  s2 = ndb.StructuredProperty(StructuredValue)
  s3 = ndb.StructuredProperty(StructuredValue)
  s4 = ndb.StructuredProperty(StructuredValue)
  s5 = ndb.StructuredProperty(StructuredValue)
  s6 = ndb.StructuredProperty(StructuredValue)
  s7 = ndb.StructuredProperty(StructuredValue)
  s8 = ndb.StructuredProperty(StructuredValue)
  s9 = ndb.StructuredProperty(StructuredValue)

  @classmethod
  def initialize(cls, string):
    x = cls()
    svs = [StructuredValue.initialize(string) for _ in xrange(10)]
    ndb.put_multi(svs)
    x.s0 = svs[0]
    x.s1 = svs[1]
    x.s2 = svs[2]
    x.s3 = svs[3]
    x.s4 = svs[4]
    x.s5 = svs[5]
    x.s6 = svs[6]
    x.s7 = svs[7]
    x.s8 = svs[8]
    x.s9 = svs[9]
    return x

def structured_property_seed():
  counts = StructuredHolder.query().count()
  if counts < NUM_RECORDS:
    for _ in xrange(NUM_RECORDS - counts):
      StructuredHolder.initialize("a" * FIELD_SIZE).put()

  return "Done"

@timer
def structured_property_query():
  return str(StructuredHolder.query().fetch())

@timer
def structured_property_projection_query():
  return str(StructuredHolder.query(
    projection=(
      StructuredHolder.s0.a0,
      StructuredHolder.s0.a1,
      StructuredHolder.s0.a2,
      StructuredHolder.s0.a3,
      StructuredHolder.s0.a4,
      StructuredHolder.s0.a5,
      StructuredHolder.s0.a6,
      StructuredHolder.s0.a7,
      StructuredHolder.s0.a8,
      StructuredHolder.s0.a9,
    )
  ).fetch())
