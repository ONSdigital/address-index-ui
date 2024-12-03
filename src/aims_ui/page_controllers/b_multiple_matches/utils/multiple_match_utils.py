""" Utilities for processing multiple match responses and input files (for uprn, singlesearch, and api) """

page_name = 'multiple_match_submit'


def get_results_display_type(searchable_fields):
  # Get the 'Download' or 'Display' selected option ('Download' is default)
  display_type = 'Download'
  for field in searchable_fields:
    if field.database_name == 'display-type':
      display_type = field.get_selected_radio()
  return display_type


def get_preffered_format_of_address(adrs, all_user_input):
  address_preference = all_user_input.get('paf-nag-preference', 'default')
  default_address = adrs.formatted_address.value
  paf_address = adrs.formatted_address_paf.value
  nag_address = adrs.formatted_address_nag.value

  if address_preference == 'PAF':
    if paf_address != '':
      return 'PAF', paf_address
  elif address_preference == 'NAG':
    if nag_address != '':
      return 'NAG', nag_address
  # Default Addresses are all NAG
  return 'NAG', default_address


def remove_header_row(contents):
  """ Remove the header row from the file if it exists """
  header_rows = ['id,address', 'id,searchAddress', '<feff>id,address']
  remove_index = None
  for i in range(0, len(contents)):
    line = contents[i]
    line = line.strip().decode('utf-8')
    line = line.casefold()
    # Remove utf8-sig Byte Object Mark
    line = line.replace('\ufeff', '')
    for header_row in header_rows:
      if line == header_row.casefold():
        remove_index = i

  if remove_index != None:
    contents.pop(remove_index)
    return True
  return False


def jsonify_address(address_to_lookup):
  # If the address contains a "'" character then contain the address
  if "'" in address_to_lookup:
    return '"' + address_to_lookup + '"'
  return address_to_lookup
