from aims_ui import get_epoch_options_cached

def delete_input(session):
  """Remove search field data from the cookie"""
  session['previous_user_responses'] = {}


def save_input(all_user_input, session):
  """Save the values of html objects into response so they can be loaded in future"""
  session['previous_user_responses'] = all_user_input


def load_confidence_score(session, uprn):
  """Load confidence scores given UPRN"""
  cs = session.get('override_confidence_score', {})
  confidence_score = cs.get(uprn, 100)
  return confidence_score


def save_confidence_score(session, addresses):
  """Save a list of UPRNs and their confidence scores to local storage"""
  cs = {}
  for address in addresses:
    cs[address.uprn.value] = address.confidence_score.value

  session['override_confidence_score'] = cs


def load_epoch_number(session):
  """Load the epoch number given the session, return to default if undeffined"""
  epoch_version_number = session.get('epoch_version_number', {})
  if epoch_version_number == {}:
    epochs, default = (get_epoch_options_cached())
    epoch_version_number = default 
  return epoch_version_number

def save_epoch_number(session, epoch_version_number ):
  """Save the epoch number for a query to the session"""
  session['epoch_version_number'] = epoch_version_number



def load_input(all_user_input, session, searchable_fields):
  """Load stored values into html attributes (by setting their Field classes 'previous value' attribute"""
  all_previous_input = session.get('previous_user_responses', {})

  for field in searchable_fields:
    current_id = field.database_name
    if all_user_input.get(current_id) == all_previous_input.get(current_id):
      if field.search_type == 'input_box':
        field.previous_value = all_user_input.get(current_id)
      elif field.search_type == 'checkbox':
        field.checkbox_value = all_user_input.get(current_id)
      elif field.search_type == 'dropdown':
        field.set_dropdown_status(all_user_input.get(current_id))
      elif field.search_type == 'radio':
        field.set_radio_status(all_user_input.get(current_id))
      elif field.search_type == 'autosuggest':
        field.previous_value = all_user_input.get(current_id)


def get_all_inputs(searchable_fields, request):
  """Using fields, retreive values of html objects"""
  def get_val(value_html_id):
    return request.form.get(value_html_id)

  usr_input = {}
  for field in searchable_fields:
    # Check for checkboxes, convert values for true/false numerical translation
    if field.search_type == 'checkbox':
      if field.checkbox_true_value == 0:
        usr_input[field.database_name] = get_val(field.database_name)
      else:
        usr_input[field.database_name] = field.checkbox_true_value if get_val(
            field.database_name) else field.checkbox_false_value

    else:
      usr_input[field.database_name] = get_val(field.database_name)

  return usr_input


def load_save_store_inputs(
    searchable_fields,
    request,
    session,
):
  """Load previous inputs, save changed ones and re-submit"""
  # Dic of {'API name / HTML ID' : User Input }
  all_user_input = get_all_inputs(searchable_fields, request)

  # Save all_user_input into session
  save_input(all_user_input, session)

  # Load any previous values into the searchfields
  load_input(all_user_input, session, searchable_fields)

  return all_user_input
