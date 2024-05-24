from aims_ui.page_controllers.d_misc_functionality.download_utils.autosuggest import get_autosuggest_list


def check_reverse_classification(value):
  # Check if the string value has been entered, then swap it for it's classification code
  autosuggest_list = get_autosuggest_list()
  to_return = value
  for category in autosuggest_list:
    if value == category.get('category'):
      to_return = category.get('en')

  # Append an Astrisk so that all children classification are included
  # i.e. 'R' becomes 'R*' meaning all 'Residential' like properties

  return to_return + '*'
