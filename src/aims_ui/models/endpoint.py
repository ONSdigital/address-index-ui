from dataclasses import dataclass, field

from flask import url_for


@dataclass
class Endpoint():
  title: str
  page_name: str
  description_text: str
  file_location: str

  # Optional fields
  title_size: int = 3
  nav_info: list = field(default_factory=lambda: [])
  sub_nav_endpoints: list = field(default_factory=lambda: [])
  sub_nav_info: list = field(default_factory=lambda: [])
  selected: bool = False
  name_id: str = ''
  current_selected_endpoint: str = ''
  url: str = ''
  visible_in_main_nav: bool = True
  page_name_to_match_to_main_header: str = ''

  def __post_init__(self):
    # If url is specified then do not attempt to find url for this page
    if self.url == '':
      # Not overriden, we must find the URL automatically
      self.url = url_for(str(self.page_name))
      if self.name_id is None and self.title:
        self.name_id = self.title

    # If the sub_nav_endpoints are provided, generate sub_nav_info
    if self.sub_nav_endpoints:
      for endpoint in self.sub_nav_endpoints:
        self.sub_nav_info.append({
            'text': endpoint.get('title', ''),
            'url': endpoint.get('url', ''),
        })
    
    if self.page_name_to_match_to_main_header == '':
      # Set to the url
      self.page_name_to_match_to_main_header = self.url
