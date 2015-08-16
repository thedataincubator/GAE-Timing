from google.appengine.ext import ndb
from .timer import timer
from .base import BaseModel

class RepeatedRecord(BaseModel):
  NUM_RECORDS = 100
  NUM_FIELDS = 100
  FIELD_SIZE = 100

  a = ndb.StringProperty(repeated=True)

  @classmethod
  def initialize(cls, string):
    x = cls()
    x.a = [string] * cls.NUM_FIELDS
    return x
