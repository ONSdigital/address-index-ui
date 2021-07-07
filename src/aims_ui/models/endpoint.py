from flask import url_for


class Endpoint():
  def __init__(self,
               title,
               url,
               description_text,
               title_size=3,
               name_id=None,
               selected=False,
               fields=None):

    self.title = title
    self.url_title = url
    self.url = url_for(str(url))
    self.description_text = description_text
    self.title_size = title_size
    self.nav_info = []
    self.fields = fields
    self.selected = selected

    if name_id is None:
      self.name_id = self.title
    else:
      self.name_id = self.title
