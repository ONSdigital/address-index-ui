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

  # Hard code here to avoid security flaws where users could potentially inject unwanted urls
  if subject == 'confidence_score':
    return render_template(
        './help_pages/uprn.html',
        endpoints=get_endpoints(called_from=page_name),
        deffinitions=deffinitions,
        breadcrumbs=breadcrumbs,
    )
  elif subject == 'submit_feedback':
    return render_template(
        './help_pages/submit_feedback.html',
        endpoints=get_endpoints(called_from=page_name),
        deffinitions=deffinitions,
        breadcrumbs=breadcrumbs,
    )

  else:
    return (render_template(
        'help.html',
        endpoints=get_endpoints(called_from=page_name),
        deffinitions=deffinitions,
    ))
