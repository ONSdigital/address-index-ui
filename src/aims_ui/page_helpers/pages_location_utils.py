
from aims_ui import app

all_pages_location = app.config.get('AIMS_UI_PAGES_LOCATION', '')


def get_page_location(selected_endpoint):
  # The folder that this page is stored in (inside pages_location)
  file_location = selected_endpoint.get('file_location')
  page_name = selected_endpoint.get('page_name')

  # page_name should match the '.html' file in the above dir
  return f'{all_pages_location}/{file_location}/{page_name}.html'


def get_error_page_location(error_page_name):

  return f'{all_pages_location}/f_error_pages/{error_page_name}.html'


def get_nested_page_location(endpoints, parent_page_name, subpage, subfolder):
  # The folder that this page is stored in (inside pages_location)
  file_location = get_file_location_of_current_endpoint(endpoints)

  return f'{all_pages_location}/{file_location}/{subfolder}/{subpage}.html'


def get_page_location_non_endpoint(page_name):
  # For pages in the base directory (standalone)

  return f'{all_pages_location}/{page_name}.html'
