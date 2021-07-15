from dataclasses import dataclass, field

class Field:
  def __init__(self,
               database_name,
               search_type='input_box',
               previous_value='',
               description='',
               display_title='',
               search_options=None,
               accordion=False,
               required=False,
               dropdown_options=None,
               search_box_visible=True,
               format_as_boolean=False,
               checkbox_value=False,
               database_association_name='',
               classes=None,
               add_default_dropdown_option=True,
               show_as_table_header=True):

    self.database_name = database_name  # The name as it appears in a parameter
    self.search_type = search_type
    self.dropdown_options = self.format_dropdown_options(
        dropdown_options, add_default_option=add_default_dropdown_option)
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

  def format_dropdown_options(self,
                              dropdown_options,
                              add_default_option=True,
                              selected_value='blank'):
    if dropdown_options != None:
      final_dropdowns = []
      if add_default_option == True:
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

  def set_dropdown_status(self, value_to_select):
    for each_dict in self.dropdown_options:
      if each_dict['value'] == value_to_select:
        each_dict['selected'] = True
