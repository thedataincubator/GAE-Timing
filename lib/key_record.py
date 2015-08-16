from google.appengine.ext import ndb
from .timer import timer
from .structured_record import StructuredValue
from .base import BaseModel

class KeyRecord(BaseModel):
  NUM_RECORDS = 100
  NUM_FIELDS = 100
  FIELD_SIZE = 100

  s0 = ndb.KeyProperty(StructuredValue)
  s1 = ndb.KeyProperty(StructuredValue)
  s2 = ndb.KeyProperty(StructuredValue)
  s3 = ndb.KeyProperty(StructuredValue)
  s4 = ndb.KeyProperty(StructuredValue)
  s5 = ndb.KeyProperty(StructuredValue)
  s6 = ndb.KeyProperty(StructuredValue)
  s7 = ndb.KeyProperty(StructuredValue)
  s8 = ndb.KeyProperty(StructuredValue)
  s9 = ndb.KeyProperty(StructuredValue)

  @classmethod
  def initialize(cls, string):
    x = cls()
    svs = [StructuredValue.initialize(string) for _ in xrange(10)]
    ndb.put_multi(svs)
    x.s0 = svs[0].key
    x.s1 = svs[1].key
    x.s2 = svs[2].key
    x.s3 = svs[3].key
    x.s4 = svs[4].key
    x.s5 = svs[5].key
    x.s6 = svs[6].key
    x.s7 = svs[7].key
    x.s8 = svs[8].key
    x.s9 = svs[9].key
    return x

  @classmethod
  @timer
  def full_query(cls):
    key_records = KeyRecord.query().fetch()
    # join in with non-key-records
    keys = [ key
      for key_record in key_records
      for key in (
        key_record.s0,
        key_record.s1,
        key_record.s2,
        key_record.s3,
        key_record.s4,
        key_record.s5,
        key_record.s6,
        key_record.s7,
        key_record.s8,
        key_record.s9,
      )
    ]

    results = ndb.get_multi(keys)
    return str(results) + str(key_records)

  @classmethod
  @timer
  def projection_query(cls):
    key_records = KeyRecord.query(projection=[KeyRecord.s0, KeyRecord.s1]).fetch()
    # join in with non-key-records
    keys = [ key
      for key_record in key_records
      for key in (
        key_record.s0,
        key_record.s1,
      )
    ]

    results = ndb.get_multi(keys)
    return str(results) + str(key_records)
