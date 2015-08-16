from google.appengine.ext import ndb
from .timer import timer
from .structured_record import StructuredValue
from .base import BaseModel

class RepeatedKeyRecord(BaseModel):
  NUM_RECORDS = 100
  NUM_FIELDS = 100
  FIELD_SIZE = 100

  sv = ndb.KeyProperty(StructuredValue, repeated=True)

  @classmethod
  def initialize(cls, string):
    x = cls()
    svs = [StructuredValue.initialize(string) for _ in xrange(10)]
    x.sv = ndb.put_multi(svs)
    return x

  @classmethod
  @timer
  def full_query(cls):
    key_records = RepeatedKeyRecord.query().fetch()
    # join in with non-key-records
    keys = [ key
      for key_record in key_records
      for key in key_record.sv
    ]

    results = ndb.get_multi(keys)
    results_dict=  { r.key: r for r in results }
    for key_record in key_records:
      key_record.sv2 = [results_dict[k] for k in key_record.sv]
    return str(key_records)
