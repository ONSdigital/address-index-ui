from flask import url_for
from dataclasses import dataclass, field


@dataclass
class Endpoint():
  title: str
  page_name: str
  description_text: str
  file_location: str

  # Optional fields
  title_size: int = 3
  nav_info: list = field(default_factory=lambda: [])
  selected: bool = False
  name_id: str = ''
  current_selected_endpoint: str = ''
  url: str = ''

  def __post_init__(self):
    # If url is specified then do not attempt to find url for this page
    if self.url == '':
      # Not overriden, we must find the URL automatically
      self.url = url_for(str(self.page_name))
      if self.name_id is None and self.title:
        self.name_id = self.title
