from flask import render_template
from flask_login import login_required
from aims_ui import get_cached_tooltip_data
from aims_ui import app
from aims_ui.page_helpers.security_utils import check_user_has_access_to_page
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.page_helpers.pages_location_utils import get_page_location, get_nested_page_location

page_name = 'help'


@login_required
@app.route('/help/<subject>')
def help(subject='None'):
  endpoints = get_endpoints(called_from=page_name)
  access = check_user_has_access_to_page(page_name)
  if access != True:
    return access
  page_location = get_page_location(endpoints, page_name)

  # Get brief descriptions from the tooltips file, but any deffinitions
  # here will get a more lengthly explanation

  url = '/help/'
  deffinitions = [
      {
          'title': 'Confidence Score',
          'name': 'confidence_score',
          'url': url + 'confidence_score',
      },
      {
          'title': 'Submit Feedback',
          'name': 'submit_feedback',
          'url': url + 'submit_feedback',
      },
      {
          'title': 'Help and Documentation',
          'name': 'help_and_documentation',
          'url': url + 'help_and_documentation',
      },
  ]

  breadcrumbs = [
      {
          "url": url + 'home',
          "text": 'Help'
      },
  ]

  def get_matching_tooltip(name):
    for tool_tip in get_cached_tooltip_data():
      if tool_tip.get('name').lower() == name.lower():
        return tool_tip.get('description',
                            'No description available as a tooltip')

  for deffinition in deffinitions:
    deffinition['description'] = get_matching_tooltip(deffinition.get('name'))

  common = {
      'endpoints': endpoints,
      'deffinitions': deffinitions,
      'breadcrumbs': breadcrumbs
  }

  # Hard code here to avoid security flaws where users could potentially inject unwanted urls
  if subject == 'confidence_score':
    return return_specific_help_page('uprn', common)
  elif subject == 'submit_feedback':
    return return_specific_help_page('submit_feedback', common)
  elif subject == 'help_and_documentation':
    return return_specific_help_page('help_and_documentation', common)

  return render_template(
      page_location,
      endpoints=endpoints,
      deffinitions=deffinitions,
  )


def return_specific_help_page(page_html_name, common):
  endpoints = common.get('endpoints')

  nested_page_location = get_nested_page_location(endpoints,
                                                  page_name,
                                                  page_html_name,
                                                  subfolder='sub_help_pages')

  return render_template(
      nested_page_location,
      endpoints=endpoints,
      deffinitions=common.get('deffinitions'),
      breadcrumbs=common.get('breadcrumbs'),
  )
