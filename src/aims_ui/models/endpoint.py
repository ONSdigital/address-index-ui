from flask import url_for

class  Endpoint():

  def __init__(self, 
      title,
      url,
      description_text,
      title_size=3,
      name_id=None,
      ):

    self.title = title
    self.url = url_for(str(url))
    self.description_text = description_text
    self.title_size =  title_size

    if name_id is None:
      self.name_id = self.title
    else:
      self.name_id = self.title

