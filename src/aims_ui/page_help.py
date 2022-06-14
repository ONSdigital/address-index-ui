from . import app
import logging
from flask import render_template, request, session, url_for
from flask_login import login_required
from .models.get_endpoints import get_endpoints
from aims_ui import get_cached_tooltip_data

page_name = 'help'

@login_required
@app.route('/help/<subject>')
def help(subject='None'):
  print(subject)
  # Get brief descriptions from the tooltips file, but any deffinitions
  # here will get a more lengthly explanation

  url = '/help/'
  deffinitions = [
    {'title': 'UPRN',
      'url': url + 'uprn',
      'long_description': 'This is the Unique Property refference number'},

    {'title': 'Other', 'description': 'A nother thing '},
    ]

  breadcrumbs = [
      { "url": url, "text": 'Help' },
  ]

  def get_matching_tooltip(name):
      for tool_tip in get_cached_tooltip_data():
          if tool_tip.get('name').lower() ==  name.lower():
              return tool_tip.get('description', 'No description available as a tooltip')

  for deffinition in deffinitions:
      deffinition['description'] = get_matching_tooltip(deffinition.get('title'))


  return (render_template(
      'help.html',
      endpoints=get_endpoints(called_from=page_name),
      deffinitions=deffinitions,
      breadcrumbs=breadcrumbs,
  ))
