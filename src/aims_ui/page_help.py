from . import app
import logging
from flask import render_template, request, session, url_for
from flask_login import login_required
from .models.get_endpoints import get_endpoints

page_name = 'help'

@app.route('/help/<subject>')
def help(subject, methods=['GET', 'POST']):
  print(subject)

  # Get brief descriptions from the tooltips file, but any deffinitions
  # here will get a more lengthly explanation

  def getLocalUrl(name):
    return url_for('help', subject=name)

  deffinitions = [
    {'title': 'UPRN',
      'url': getLocalUrl('uprn'),
      'description': 'This is the Unique Property refference number'},

    {'title': 'Other', 'description': 'A nother thing '},
    ]

  breadcrumbs = [
      { "url": url_for('help', subject='s'), "text": 'Help' },
  ]


  return (render_template(
      'help.html',
      endpoints=get_endpoints(called_from=page_name),
      deffinitions=deffinitions,
      breadcrumbs=breadcrumbs,
  ))
