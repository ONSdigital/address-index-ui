from aims_ui import app


def get_page_location(endpoints, page_name):
  # Where all the 'page' files are stored
  all_pages_location = app.config.get('AIMS_UI_PAGES_LOCATION', '')

  # Get the selected endpoint
  for e in endpoints:
    if (e.current_selected_endpoint == e.url):
      selected_endpoint = e

  # The folder that this page is stored in (inside pages_location)
  file_location = selected_endpoint.file_location

  # page_name should match the '.html' file in the above dir
  return f'{all_pages_location}/{file_location}/{page_name}.html'
