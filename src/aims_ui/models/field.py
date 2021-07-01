class Field:
  def __init__(self,
               database_name,
               search_type='input_box',
               previous_value = '',
               description = '',
               display_title = '',
               search_options=None,
               accordion=False,
               required = False,
               dropdown_options=None,
               search_box_visible=True,
               format_as_boolean=False,
               checkbox_value=False,
               database_association_name='',
               classes = None,
               show_as_table_header=True):

    self.database_name = database_name # The name as it appears in a parameter
    self.search_type = search_type
    self.dropdown_options = self.format_dropdown_options(dropdown_options)
    self.accordion = accordion
    self.previous_value = previous_value
    self.search_box_visible = search_box_visible
    self.format_as_boolean = format_as_boolean
    self.checkbox_value = checkbox_value
    self.description = description
    self.display_title = display_title
    self.classes = classes
    self.required = required

  def find_and_extract(self, data):
    checkbox_present = data.get(self.unique_name) == 'other'
    filter_value = data.get(self.unique_name + '_text_box', '')
    return (checkbox_present, filter_value)


  def format_dropdown_options(self, dropdown_options, selected_value='blank'):
    if dropdown_options != None:
      final_dropdowns = [{
          'value': 'blank',
          'text': 'Select an option',
          'disabled': True,
      }]
      for option in dropdown_options:
        entry = {'value': option, 'text': option}
        final_dropdowns.append(entry)

      for each_dict in final_dropdowns:
        if each_dict['value'] == selected_value:
          each_dict['selected'] = True

      return final_dropdowns

  def refresh_dropdown_status(self, value_to_change_to):
    self.checkbox_value = value_to_change_to

  def refresh_selected_dropdown(self, selected_value):
    dropdown_values = [i.get('value') for i in self.dropdown_options]
    dropdown_values.remove('blank')
    self.dropdown_options = self.format_dropdown_options(
        dropdown_values, selected_value=selected_value)
    


