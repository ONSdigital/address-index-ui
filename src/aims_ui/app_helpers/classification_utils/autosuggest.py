
from .builder import get_classification_file_content_as_dict

def get_classification_autosuggest_list():
  """ Return the classifications list in the format expected by the autosuggest component """
  class_list = get_classification_file_content_as_dict()

  formatted_class_list = []
  for classification in class_list:
    formatted_class_list.append({
        'en': classification.get('code'),
        'category': classification.get('label'),
    })

  return formatted_class_list

def get_classification_autosuggest_list_reversed():
  """ Return the classifications list in the format expected by the autosuggest component with the code and label reversed for reverse searching """
  class_list = get_classification_file_content_as_dict()

  formatted_class_list = []
  for classification in class_list:
    formatted_class_list.append({
        'en': classification.get('label'),
        'category': classification.get('code'),
    })

  return formatted_class_list

def get_full_classification_autosuggest():
  """ Merge of both the reversed and normal list for autosuggest 'surfing' """

  normal_list = get_classification_autosuggest_list()
  reversed_list = get_classification_autosuggest_list_reversed()

  # Merge the two lists together
  full_list = normal_list + reversed_list

  return full_list