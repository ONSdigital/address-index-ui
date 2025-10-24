from flask import Response
from flask_login import login_required

from aims_ui import app
from aims_ui.api_access.direct_api_helper import uprn_lookup


@login_required
@app.route('/api/uprn/<uprn>', methods=['GET'])
def uprn_route(uprn):
  api_response = uprn_lookup(uprn)

  flask_response = Response(response=api_response.content,
                            status=api_response.status_code,
                            content_type=api_response.headers.get(
                                'Content-Type', 'application/json'))

  return flask_response
