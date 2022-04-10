from dataclasses import dataclass, field


@dataclass
class Field:
  database_name: str
  search_type: str = 'input_box'
  previous_value: str = ''
  description: str = ''
  display_title: str = ''
  accordion: bool = False
  required: bool = False
  dropdown_options: list = field(default_factory=lambda: [])
  radio_options: list = field(default_factory=lambda: [])
  search_box_visible: bool = True
  format_as_boolean: bool = False
  flag: bool = False
  checkbox_value: bool = False
  checkbox_true_value: int = 0
  checkbox_false_value: int = 0
  min_chars: int = 3
  database_association_name: str = ''
  classes: str = ''
  add_default_dropdown_option: bool = True
  show_as_table_header: bool = True
  default_radio_selection: str = ''
  only_display_in_results_page: bool = False
  autosuggest_url: str = ''
  download_url: str = ''

  def __post_init__(self):
    self.dropdown_options = self.format_dropdown_options(
        self.dropdown_options,
        add_default_option=self.add_default_dropdown_option)
    if self.search_type == 'radio':
      self.radio_options = self.format_radio_options()
      self.set_radio_status(self.default_radio_selection)

  def get_selected_radio(self):
    for radio in self.radio_options:
      if radio.get('checked'):
        return radio.get('id')

  def set_radio_status(self, value_to_select):
    # Remove previous checked state
    for radio in self.radio_options:
      if radio.get('checked', '') != '':
        radio.pop('checked')

    for radio in self.radio_options:
      if radio.get('id') == value_to_select:
        radio['checked'] = True

  def format_radio_options(self):
    final_radios = []
    for radio_option in self.radio_options:
      final_radios.append({
          'id': radio_option.get('id'),
          'label': {
              'text': radio_option.get('text'),
              'description': radio_option.get('description')
          },
          'value': radio_option.get('id')
      })

    for radio in final_radios:
      if radio.get('id') == self.previous_value:
        radio['checked'] = True

    return final_radios

  def find_and_extract(self, data):
    checkbox_present = data.get(self.unique_name) == 'other'
    filter_value = data.get(self.unique_name + '_text_box', '')
    return (checkbox_present, filter_value)

  def format_dropdown_options(self,
                              dropdown_options,
                              add_default_option=True,
                              selected_value='blank'):
    if dropdown_options != []:
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
