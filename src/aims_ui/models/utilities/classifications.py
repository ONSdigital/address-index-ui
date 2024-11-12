from aims_ui import get_classifications_cached


def get_class_subset(code):
  class_list = get_classifications_cached()

  final_list = [code]
  for c in class_list:
    if c.get('code') == code[0]:
      final_list.append(c.get('label'))

  for c in class_list:
    if c.get('code') == code[:2]:
      final_list.append(c.get('label'))

  for c in class_list:
    if c.get('code') == code:
      final_list.append(c.get('label'))

  # Check to remove final string if identical to prior
  length = len(final_list) - 1
  final_word = final_list[length]
  final_list = [x if x != final_word else '' for x in final_list]

  final_string = ''
  for desc in final_list:
    if desc != '':
      final_string = final_string + '[' + desc + '] '

  # Add back final word as all instances have been removed
  final_string = final_string + '[' + final_word + ']'

  return final_string


def get_classification_list(code=None):
  class_list = []
  class_list = get_class_subset(code)

  return str(class_list)
