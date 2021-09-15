from flask import url_for
from dataclasses import dataclass, field


@dataclass
class Endpoint():
  title: str
  url_title: str
  description_text: str
  title_size: int = 3
  nav_info: list = field(default_factory=lambda: [])
  selected: bool = False
  name_id: str = ''
  current_selected_endpoint: str = ''

  def __post_init__(self):
    self.url = url_for(str(self.url_title))
    if self.name_id is None and self.title:
      self.name_id = self.title
