from .field import Field
from flask import url_for

def get_fields(endpoint_name):
  if endpoint_name == 'uprn':
    return ([
      Field('uprn',
        display_title='To get started, enter a UPRN',
        required = True,
        description='The Unique Property Reference Number is 12 didgits, and reffers to a single property'),
      Field('limit',
        display_title="Limit",
        classes='input--w-4',
        description = 'Enter the number of addresses to return (0 - 5,000)',
        previous_value = '10',),
      Field('includeauxiliarysearch',
        display_title='Include Auxiliary',
        description='Check this box to use auxilairy data in addition to regular standard data. This may make your search results more accurate.',
        search_type='checkbox',),
      Field('classification',
        display_title='Classification (optional)',
        description='E.g. residential, commercial, RD06',),
      Field('historical',
        search_type='checkbox',
        display_title='Include histprocal address data',
        description='Check this box to include historical address data in the search. This will allow inclusion of historical data.',),
        ])
  elif endpoint_name == 'typeahead':
    pass
  elif endpoint_name == 'address':
    pass
  elif endpoint_name == 'multiple_address':
    pass
  elif endpoint_name == 'postcode':
    pass
  elif endpoint_name == 'typeahead':
    pass


  

