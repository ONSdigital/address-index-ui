def delete_input(session):
  """Remove search field data from the cookie"""
  session['previous_user_responses'] = {}


def save_input(all_user_input, session):
  """Save the values of html objects into response so they can be loaded in future"""
  session['previous_user_responses'] = all_user_input


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


def get_all_inputs(searchable_fields, request):
  """Using fields, retreive values of html objects"""
  def get_val(value_html_id):
    return request.form.get(value_html_id)

  usr_input = {}
  for field in searchable_fields:
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
