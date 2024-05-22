from aims_ui import app

all_pages_location = app.config.get('AIMS_UI_PAGES_LOCATION', '')


def get_page_location(endpoints, page_name):

  # Get the selected endpoint
  for e in endpoints:
    if (e.current_selected_endpoint == e.url):
      selected_endpoint = e

  # The folder that this page is stored in (inside pages_location)
  file_location = selected_endpoint.file_location

  # page_name should match the '.html' file in the above dir
  return f'{all_pages_location}/{file_location}/{page_name}.html'

def get_nested_page_location(endpoints, page_name, subpage, subfolder):
  # Get the selected endpoint
  for e in endpoints:
    if (e.current_selected_endpoint == e.url):
      selected_endpoint = e

  # The folder that this page is stored in (inside pages_location)
  file_location = selected_endpoint.file_location

  return f'{all_pages_location}/{file_location}/{subfolder}/{subpage}.html'