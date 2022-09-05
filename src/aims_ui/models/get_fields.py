from .field import Field
from .endpoint_options import get_options
from flask import url_for
from aims_ui import get_epoch_options_cached

# This will change when DS changes
hidden_field_class = ' ons-u-hidden '


def get_fields(endpoint_name, include_UPRN_redirect=False):
  # Deffine fields which are reused in many of the endpoints

  epoch_options, default_epoch = get_epoch_options_cached()

  common_fields = {
      'limit':
      Field(
          'limit',
          display_title="Limit",
          classes='ons-input--w-4',
          description='Enter the number of addresses to return (0 - 5,000)',
          previous_value='50',
      ),
      'epoch':
      Field(
          'epoch',
          search_type='radio',
          flag=False,
          display_title='Epoch',
          default_radio_selection=default_epoch,
          radio_options=epoch_options,
      ),
      'historical':
      Field(
          'historical',
          search_type='checkbox',
          display_title='Include historical address data',
          description=
          'Check this box to include historical address data in the search. This will allow inclusion of historical data.',
      ),  # REMOVED from all pages for now, as all data is always included due to 'verbose' flag
      'england_boost_checkbox':
      Field(
          'eboost',
          display_title='England Boost',
          search_type='checkbox',
      ),
      'wales_boost_checkbox':
      Field(
          'wboost',
          display_title='Wales Boost',
          search_type='checkbox',
      ),
      'scotland_boost_checkbox':
      Field(
          'sboost',
          display_title='Scotland Boost',
          search_type='checkbox',
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
      'boost-checkbox-description':
      Field(
          'None',
          search_type='label',
          display_title=
          'Boost a region. This is used as a "tie breaker" when the same address from different regions is present.',
      ),
      'england_boost':
      Field(
          'eboost',
          display_title='England Boost (1-10)',
          classes='ons-input--w-4',
          description='Boost the results in favour of England Addresses',
      ),
      'wales_boost':
      Field(
          'wboost',
          display_title='Wales Boost (1-10)',
          classes='ons-input--w-4',
          description='Boost the results in favour of Wales Addresses',
      ),
      'scotland_boost':
      Field(
          'sboost',
          display_title='Scotland Boost (1-10)',
          classes='ons-input--w-4',
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
      'classification':
      Field(
          'classificationfilter',
          search_type='autosuggest',
          display_title='Classification',
          description=
          'To further filter your results, select a classification. You can start typing the Classification Code or the Description. (I.e. "R" or "Residential")',
          autosuggest_url='/autosuggest/classification-reverse.json',
          min_chars=1,
      ),
      'classification_help_download':
      Field(
          'None',
          display_title='List of Classifications',
          description=
          'This file contains a list of classifications, explained in a universaly recognised "easy to read" csv format.',
          search_type='download',
          download_url='/downloads/classifications_list',
      ),
  }

  if endpoint_name == 'uprn':
    return ([
        Field(
            'uprn',
            display_title='To get started, enter a UPRN',
            previous_value=include_UPRN_redirect,
            required=True,
            description=
            'The Unique Property Reference Number consists of digits only, and refers to a single property'
        ),
        common_fields['epoch'],
    ])

  elif endpoint_name == 'typeahead':
    return ([
        Field(
            'None',
            search_type='label',
            display_title=
            'Adjust the following fields to see the typeahead behaviour change',
        ),
        Field(
            'limit',
            display_title="Limit",
            classes='ons-input--w-4',
            description='Enter the number of addresses to return (0 - 5,000)',
            previous_value='10',
        ),
        common_fields['epoch'],
        common_fields['england_boost'],
        common_fields['wales_boost'],
        common_fields['scotland_boost'],

        # REMOVED - left commented incase of later requirements
        #        Field(
        #            'groupfullpostcodes',
        #            search_type='checkbox',
        #            display_title='Group full postcodes',
        #            description=
        #            'If you would like the results to be grouped by their respective full postcodes, tick this box',
        #        ),
        Field(
            'fallback',
            search_type='checkbox',
            only_display_in_results_page=hidden_field_class,
            display_title='Fallback',
            description=
            'Specifies whether a slow fallback query is used in the event of the main query returning no results.',
        ),
    ])

  elif endpoint_name == 'multiple_address':
    return ([
        common_fields['limit'],
    ])
  elif endpoint_name == 'postcode':
    return ([
        Field(
            'postcode',
            display_title='To get started, enter a PostCode',
            classes='ons-input--w-8',
            required=True,
            description=
            'A postcode is a code for post which separates houses into groups. This is often a 7 digit letter and number combo.'
        ),
        common_fields['limit'],
        common_fields['classification'],
        common_fields['classification_help_download'],
        common_fields['epoch'],
    ])

  elif endpoint_name == 'singlesearch':
    fields = [
        Field(
            'input',
            display_title='Enter search string',
            classes='ons-input--w-50 nocache',
            required=True,
            description=
            'Specifies the address search string (e.g. "14 Acacia Avenue, Ruislip, HA4 8RG").'
        ),
        common_fields['classification'],
        common_fields['classification_help_download'],
        Field(
            'None',
            search_type='label',
            display_title='Include results from the following areas:',
        ),
        Field(
            'eboost',
            display_title='England',
            search_type='checkbox',
            checkbox_value=True,
            checkbox_true_value=10,
            checkbox_false_value=0,
        ),
        Field(
            'wboost',
            display_title='Wales',
            search_type='checkbox',
            checkbox_value=True,
            checkbox_true_value=10,
            checkbox_false_value=0,
        ),
        Field(
            'sboost',
            display_title='Scotland',
            search_type='checkbox',
            checkbox_value=True,
            checkbox_true_value=10,
            checkbox_false_value=0,
        ),
        common_fields['epoch'],
        common_fields['match_threshold'],
        common_fields['limit'],
    ]

    if include_UPRN_redirect != False:
      uprn_search_url = url_for('uprn')
      panel_field = Field(
          'panel',
          search_type='panel',
          description=
          f'Looking for UPRN search? <a href={uprn_search_url}?search_uprn={include_UPRN_redirect}>Try this service for UPRN searches</a>',
      )
      fields.insert(0, panel_field)

    return fields

  else:
    raise Exception(f'No valid field found - Found {endpoint_name}')
