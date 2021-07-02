from .field import Field
from .endpoint_options import get_options
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
      Field('classification',
        display_title='Classification (optional)',
        description='E.g. residential, commercial, RD06',),
      Field('historical',
        search_type='checkbox',
        display_title='Include historical address data',
        description='Check this box to include historical address data in the search. This will allow inclusion of historical data.',), 
    Field('epoch',
        display_title='Epoch',
        search_type='dropdown',
        dropdown_options=get_options('epoch'),
        add_default_dropdown_option = False,
        description='Feel freeto Choose and Epoch from the dropdown menu'), ])


  elif endpoint_name == 'typeahead':
    pass
  elif endpoint_name == 'address':
    pass
  elif endpoint_name == 'multiple_address':
    pass
  elif endpoint_name == 'postcode':
    Field('',
        display_title='',
        required = True,
        description=''),
    Field('',
        display_title='',
        required = True,
        description=''),
    Field('',
        display_title='',
        required = True,
        description=''),
    Field('',
        display_title='',
        required = True,
        description=''),
    Field('',
        display_title='',
        required = True,
        description=''),


  elif endpoint_name == 'typeahead':
    pass


  

