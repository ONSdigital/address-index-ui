import json

from . import app
from flask import render_template
from flask_login import login_required
from aims_ui.utils import Utils, Classifications, Siblings


@app.route('/result/<uprn>', methods=['GET'])
# @login_required
def result(uprn):

    endpoint = "/addresses/uprn/" + uprn
    params = {'verbose': 'true'}
    response = Utils.get_ai_response(endpoint, params)

    if response.status_code != 200:
        app.logger.error('Error getting data from AIMS - ' + str(response.status_code))
        uprn_result = ""
    else:
        uprn_result = json.loads(response.text)

    # class_list = Classifications.get_class_list()
    class_list = ''

    if uprn_result == "":
        sibling_list = ""
    else:
        sibling_list = Siblings.get_siblings(uprn_result['response']['address']['relatives'])
    # sibling_list = ""

    return render_template('result.html', uprnResult=uprn_result, classList=class_list,
                           uprn=uprn, sibling_list=sibling_list)
