from .field import Field
from .endpoint_options import get_options
from flask import url_for


def get_fields(endpoint_name):
  # Deffine fields which are reused in many of the endpoints

  common_fields = {
      'limit':
      Field(
          'limit',
          display_title="Limit",
          classes='input--w-4',
          description='Enter the number of addresses to return (0 - 5,000)',
          previous_value='10',
      ),
      'classification':
      Field(
          'classification',
          display_title='Classification (optional)',
          description='E.g. residential, commercial, RD06',
      ),
      'epoch':
      Field('epoch',
            display_title='Epoch',
            search_type='dropdown',
            classes='input--w-4',
            dropdown_options=get_options('epoch'),
            add_default_dropdown_option=False,
            description='Feel freeto Choose and Epoch from the dropdown menu'),
      'historical':
      Field(
          'historical',
          search_type='checkbox',
          display_title='Include historical address data',
          description=
          'Check this box to include historical address data in the search. This will allow inclusion of historical data.',
      ),
      'england_boost_checkbox':
      Field(
          'eboost',
          display_title='England Boost',
          search_type='checkbox',
          description='Boost the results in favour of England Addresses',
      ),
      'wales_boost_checkbox':
      Field(
          'wboost',
          display_title='Wales Boost',
          search_type='checkbox',
          description='Boost the results in favour of Wales Addresses',
      ),
      'scotland_boost_checkbox':
      Field(
          'sboost',
          display_title='Scotland Boost',
          search_type='checkbox',
          description='Boost the results in favour of Scotland Addresses',
      ),
      'match_threshold':
      Field(
          'matchthreshold',
          display_title='Minimum match %',
          search_type='dropdown',
          previous_value='5%',
          dropdown_options=get_options('percentage_match'),
          add_default_dropdown_option=False,
      ),
      'england_boost':
      Field(
          'eboost',
          display_title='England Boost (1-10)',
          classes='input--w-4',
          description='Boost the results in favour of England Addresses',
      ),
      'wales_boost':
      Field(
          'wboost',
          display_title='Wales Boost (1-10)',
          classes='input--w-4',
          description='Boost the results in favour of Wales Addresses',
      ),
      'scotland_boost':
      Field(
          'sboost',
          display_title='Scotland Boost (1-10)',
          classes='input--w-4',
          description='Boost the results in favour of Scotland Addresses',
      ),
      'auxilary_search':
      Field(
          'includeauxiliarysearch',
          display_title='Include Auxiliary',
          description=
          'Check this box to use auxilairy data in addition to regular standard data. This may make your search results more accurate.',
          search_type='checkbox',
      ),
  }

  if endpoint_name == 'uprn':
    return ([
        Field(
            'uprn',
            display_title='To get started, enter a UPRN',
            required=True,
            description=
            'The Unique Property Reference Number consists of digits only, and refers to a single property'
        ),
        common_fields['limit'],
        common_fields['epoch'],
        common_fields['historical'],
    ])

  elif endpoint_name == 'typeahead':
    return ([
        Field(
            'name',
            display_title='Enter search string',
            required=True,
            description=
            'Specifies the address search string (e.g. "14 Acacia Avenue, Ruislip, HA4 8RG").'
        ),
        common_fields['limit'],
        common_fields['classification'],
        common_fields['epoch'],
        common_fields['england_boost'],
        common_fields['wales_boost'],
        common_fields['scotland_boost'],
        Field(
            'favourwelsh',
            search_type='checkbox',
            display_title='Flavour Welsh',
            description=
            'If you prefer the results to be flavoured Welsh tick this box',
        ),
        Field(
            'groupfullpostcodes',
            search_type='checkbox',
            display_title='Group full postcodes',
            description=
            'If you bwould like the results to be grouped by their respective full postcodes, tick this box',
        ),
        Field(
            'fallback',
            search_type='checkbox',
            display_title='Fallback',
            description=
            'Specifies whether a slow fallback query is used in the event of the main query returning no results.',
        ),
        common_fields['historical'],
        common_fields['auxilary_search'],
    ])

  elif endpoint_name == 'multiple_address':
    return ([
        common_fields['limit'],
        common_fields['epoch'],
        common_fields['historical'],
        common_fields['match_threshold'],
        Field(
          'display-type',
          search_type='radio',
          flag = False,
          display_title='How would you like your results?',
          radio_options=[
            {'id':'Download', 'text':'Download as CSV'},
            {'id':'Display', 'text':'Display in browser'},
          ],)
          
      ])
  elif endpoint_name == 'postcode':
    return ([
        Field(
            'postcode',
            display_title='To get started, enter a PostCode',
            classes='input--w-8',
            required=True,
            description=
            'A postcode is a code for post which separates houses into groups. This is often a 7 didgit letter and number combo.'
        ),
        common_fields['limit'],
        common_fields['classification'],
        common_fields['epoch'],
        common_fields['england_boost_checkbox'],
        common_fields['wales_boost_checkbox'],
        common_fields['scotland_boost_checkbox'],
        common_fields['auxilary_search'],
    ])

  elif endpoint_name == 'singlesearch':
    return ([
        Field(
            'input',
            display_title='Enter search string',
            required=True,
            description=
            'Specifies the address search string (e.g. "14 Acacia Avenue, Ruislip, HA4 8RG").'
        ),
        common_fields['classification'],
        common_fields['england_boost_checkbox'],
        common_fields['wales_boost_checkbox'],
        common_fields['scotland_boost_checkbox'],
        common_fields['epoch'],
        common_fields['match_threshold'],
        common_fields['limit'],
        common_fields['historical'],
        common_fields['auxilary_search'],
    ])

  elif endpoint_name == 'typeahead':
    pass
  else:
    raise Exception(f'No valid field found - Found {endpoint_name}')
