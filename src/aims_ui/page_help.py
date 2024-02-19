import logging
from flask import render_template, request, session, url_for
from flask_login import login_required
from aims_ui import get_cached_tooltip_data
from . import app
from .security_utils import check_user_has_access_to_page
from .models.get_endpoints import get_endpoints

page_name = 'help'


@login_required
@app.route('/help/<subject>')
def help(subject='None'):
  endpoints = get_endpoints(called_from=page_name)
  access = check_user_has_access_to_page(page_name, endpoints)
  if access != True:
    return access

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

  common = [endpoints, deffinitions, breadcrumbs]
  # Hard code here to avoid security flaws where users could potentially inject unwanted urls
  if subject == 'confidence_score':
    return return_specific_help_page('uprn', common)
  elif subject == 'submit_feedback':
    return return_specific_help_page('submit_feedback', common)
  elif subject == 'help_and_documentation':
    return return_specific_help_page('help_and_documentation', common)

  return render_template(
      'help.html',
      endpoints=endpoints,
      deffinitions=deffinitions,
  )


def return_specific_help_page(page_html_name, common):
  return render_template(
      f'./help_pages/{page_html_name}.html',
      endpoints=common[0],
      deffinitions=common[1],
      breadcrumbs=common[2],
  )
