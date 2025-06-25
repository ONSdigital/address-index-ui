from flask import url_for

from aims_ui import get_epoch_options_cached

from .endpoint_options import get_options
from .field import Field

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
          description=
          'Enter the number of matched addresses to return if multiple matches are available (1 - 50)',
          previous_value='1',
      ),
      'file_upload':
      Field(
          'file_upload',
          search_type='file_upload',
          display_title='Upload a csv file',
          description='Please upload a csv file',
      ),
      'epoch':
      Field(
          'epoch',
          search_type='radio',
          classes=' ons-input--w-50 ',
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
          checkbox_value=True,
          description=
          'Check this box to include historical address data in the search.',
      ),
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
      'northern_ireland_boost_checkbox':
      Field(
          'nboost',
          display_title='Northern Ireland Boost',
          search_type='checkbox',
      ),
      'channel_islands_boost_checkbox':
      Field(
          'lboost',
          display_title='Isle of Man Boost',
          search_type='checkbox',
      ),
      'isle_of_man_boost_checkbox':
      Field(
          'mboost',
          display_title='Isle of Man Boost',
          search_type='checkbox',
      ),
      'offshore_boost_checkbox':
      Field(
          'jboost',
          display_title='Offshore etc. Boost',
          search_type='checkbox',
      ),
      'match_threshold':
      Field(
          'matchthreshold',
          display_title='Minimum match %',
          search_type='dropdown',
          previous_value='5%',
          classes='ons-input--w-50',
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
          classes='ons-input--w-50 ',
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
      'multiple_match_paf_nag_preference':
      Field(
          'paf-nag-preference',
          search_type='radio',
          flag=False,
          display_title='Prioritise PAF or NAG addresses?',
          default_radio_selection='PAF',
          radio_options=[
              {
                  'id':
                  'PAF',
                  'text':
                  'PAF - Addresses have PAF match first, if none found default formatting will be used'
              },
              {
                  'id':
                  'NAG',
                  'text':
                  'NAG - Addresses have NAG match first, if none found default formatting will be used'
              },
          ],
      ),
      'header_row_export':
      Field(
          'header_row_export',
          display_title='Export Header Row',
          search_type='checkbox',
          checkbox_value=True,
          description='Add a header row to the exported file.',
      ),
  }

  if endpoint_name == 'uprn':
    return ([
        Field(
            'uprn',
            display_title='To get started, enter a UPRN',
            previous_value=include_UPRN_redirect,
            classes='ons-input--w-50 ',
            required=True,
            description=
            'The Unique Property Reference Number consists of digits only, and refers to a single property'
        ),
        common_fields['epoch'],
        common_fields['historical'],
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
            description='Enter the number of addresses to return (1 - 100)',
            previous_value='10',
        ),
        common_fields['epoch'],
        Field(
            'None',
            search_type='panel-info',
            description=
            'Unlike other matches, Typeahead has variable boosts. <br><br>You can increase the value for a particular country or countries. <br><br>If for example you set Scotland Boost to 10 and type in 53 Port you get all Scottish results on screen, if you then add a c the results are all from England as there are no Scottish matches for that input.',
        ),
        Field(
            'eboost',
            display_title='England Boost (1-10)',
            classes='ons-input--w-4',
            description='Boost the results in favour of England Addresses',
            previous_value='0',
        ),
        Field(
            'wboost',
            display_title='Wales Boost (1-10)',
            classes='ons-input--w-4',
            description='Boost the results in favour of Wales Addresses',
            previous_value='0',
        ),
        Field(
            'sboost',
            display_title='Scotland Boost (1-10)',
            classes='ons-input--w-4',
            description='Boost the results in favour of Scotland Addresses',
            previous_value='0',
        ),
        Field(
            'nboost',
            display_title='Northern Ireland Boost (1-10)',
            classes='ons-input--w-4',
            description=
            'Boost the results in favour of Northern Ireland Addresses',
            previous_value='0',
        ),
        Field(
            'lboost',
            display_title='Channel Islands Boost (1-10)',
            classes='ons-input--w-4',
            description=
            'Boost the results in favour of Channel Islands Addresses',
            previous_value='0',
        ),
        Field(
            'nboost',
            display_title='Isle of Man Boost (1-10)',
            classes='ons-input--w-4',
            description='Boost the results in favour of Isle of Man Addresses',
            previous_value='0',
        ),
        Field(
            'jboost',
            display_title='Offshore etc. Boost (1-10)',
            classes='ons-input--w-4',
            description=
            'Boost the results in favour of Offshore etc. Addresses',
            previous_value='0',
        ),
        Field(
            'fallback',
            search_type='checkbox',
            only_display_in_results_page=hidden_field_class,
            display_title='Fallback',
            description=
            'Specifies whether a slow fallback query is used in the event of the main query returning no results.',
        ),
    ])

  elif endpoint_name == 'multiple_address_original':
    return ([
        Field(
            'limit',
            display_title="Limit",
            classes='ons-input--w-4',
            description=
            'Enter the number of matched addresses to return if multiple matches are available (1 - 10)',
            previous_value='5',
        ),
        common_fields['epoch'],
        common_fields['historical'],
        common_fields['match_threshold'],
        common_fields['multiple_match_paf_nag_preference'],
        common_fields['header_row_export'],
        Field(
            'display-type',
            search_type='radio',
            flag=False,
            display_title='How would you like your results?',
            default_radio_selection='Download',
            radio_options=[
                {
                    'id': 'Download',
                    'text': 'Download as CSV'
                },
                {
                    'id': 'Display',
                    'text': 'Display in browser'
                },
            ],
        ),
        common_fields['file_upload'],
    ])

  elif endpoint_name == 'uprn_multiple_match':
    return ([
        common_fields['header_row_export'],
        common_fields['file_upload'],
    ])

  elif endpoint_name == 'multiple_address':
    return ([
        Field(
            'limitperaddress',
            display_title="Limit Per Address",
            classes='ons-input--w-4',
            description=
            'Enter the number of matched addresses to return if multiple matches are available (1 - 10)',
            previous_value='1',
        ),
        Field(
            'name',
            display_title="Name (Optional)",
            description='Optional tag to organise matches (25 character max)',
            char_check_limit= {
              'limit': 25,
              "charCountOverLimitSingular": "{x} character too many",
              "charCountOverLimitPlural": "{x} characters too many",
              "charCountSingular": "You have {x} character remaining",
              "charCountPlural": "You have {x} characters remaining",
            },
            previous_value='',
        ),
        common_fields['multiple_match_paf_nag_preference'],
        common_fields['header_row_export'],
        common_fields['file_upload'],
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
        Field(
            'limit',
            display_title="Limit",
            classes='ons-input--w-4',
            description=
            'Enter the number of matched addresses to return if multiple matches are available (1 - 200)',
            previous_value='5',
        ),
        common_fields['classification'],
        common_fields['classification_help_download'],
        common_fields['epoch'],
        common_fields['historical'],
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
        Field(
            'nboost',
            display_title='Northern Ireland',
            search_type='checkbox',
            checkbox_value=True,
            checkbox_true_value=10,
            checkbox_false_value=0,
        ),
        Field(
            'lboost',
            display_title='Channel Islands',
            search_type='checkbox',
            checkbox_value=True,
            checkbox_true_value=10,
            checkbox_false_value=0,
        ),
        Field(
            'mboost',
            display_title='Isle of Man',
            search_type='checkbox',
            checkbox_value=True,
            checkbox_true_value=10,
            checkbox_false_value=0,
        ),
        Field(
            'jboost',
            display_title='Offshore etc.',
            search_type='checkbox',
            checkbox_value=True,
            checkbox_true_value=10,
            checkbox_false_value=0,
        ),
        common_fields['epoch'],
        common_fields['match_threshold'],
        common_fields['limit'],
        common_fields['historical'],
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
