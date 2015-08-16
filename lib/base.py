from google.appengine.ext import ndb
from .timer import timer

class BaseModel(ndb.Model):
  NUM_RECORDS = 100
  NUM_FIELDS = 100
  FIELD_SIZE = 100

  @classmethod
  def initialize(cls, string):
    raise NotImplementedError

  @classmethod
  def seed(cls):
    counts = cls.query().count()
    if counts < cls.NUM_RECORDS:
      for _ in xrange(cls.NUM_RECORDS - counts):
        cls.initialize("a" * cls.FIELD_SIZE).put()

    return "Done"

  @classmethod
  @timer
  def full_query(cls):
    return str(cls.query().fetch())

  @classmethod
  @timer
  def projection_query(cls):
    raise NotImplementedError

  @classmethod
  def _register_endpoint(cls, app, func, methods=['GET']):
    app.add_url_rule(
      '/{cls}/{func}'.format(cls=cls.__name__, func=func.__name__),
      '{cls}.{func}'.format(cls=cls.__name__, func=func.__name__),
      func,
      methods=methods,
    )

  @classmethod
  def register(cls, app):
    cls._register_endpoint(app, cls.seed, methods=['POST'])
    cls._register_endpoint(app, cls.full_query)
    try:
      cls.projection_query()  # it's optional to specify this
      cls._register_endpoint(app, cls.projection_query)
    except NotImplementedError:
      pass
