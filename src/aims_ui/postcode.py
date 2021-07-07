import json
import math

from . import app
from flask import render_template, request, redirect, flash
from flask_login import login_required
from aims_ui.forms.forms import PostcodeForm
from aims_ui.utils import Utils


@app.route("/postcode", methods=['GET', 'POST'])
# @login_required
def postcode_search():
    form = PostcodeForm()

    if request.method == 'POST':
        if not form.validate_on_submit():
            flash(form.errors['form_postcode'][0], 'error_postcode')
            return render_template('postcode.html',
                                   csrf_token=form.csrf_token,
                                   errors=form.form_postcode.errors)
        else:
            return redirect('/postcode/' + form.form_postcode.data)
    elif request.method == 'GET':
        return render_template('postcode.html', csrf_token=form.csrf_token)


@app.route('/postcode/<postcode>', methods=['GET', 'POST'])
# @login_required
def postcode_results(postcode):

    form = PostcodeForm()
    page = int(request.args.get('page', 1))

    if request.method == 'POST':
        app.logger.info(form.form_historical.data)
        app.logger.info(form.form_classification_filter.data)

        if not form.validate_on_submit():
            return render_template('postcode-results.html',
                                   csrf_token=form.csrf_token,
                                   errors=form.form_postcode.errors)
        else:
            if form.form_historical.data == 'y':
                historical_value = 'true'
            else:
                historical_value = 'false'
            postcode_query_params = "?classificationfilter=" + form.form_classification_filter.data + \
                                    "&historical=" + historical_value + "&verbose=true" + \
                                    "&resultsperpage=" + str(form.form_results_per_page.data)
            return redirect('/postcode/' + form.form_postcode.data + postcode_query_params)
    else:
        classificationfilter = request.args.get('classificationfilter', None)
        max_page_results = int(request.args.get('resultsperpage', 10))
        offset = (page * max_page_results) - max_page_results

        params = {'classificationfilter': classificationfilter, 'limit': max_page_results, 'offset': offset,
                  'historical': request.args.get('historical', 'True'), 'verbose': 'true',
                  'resultsperpage': request.args.get('resultsperpage', 10)}

        response = Utils.get_ai_postcode(postcode, params)

        app.logger.info('Response: ' + str(response))

        if response.status_code == 200:

            postcode_results_list = json.loads(response.text)

            if not (postcode_results_list['response']['total']) or postcode_results_list['response']['total'] == 0:
                max_page = 0
            else:
                max_page = int(math.ceil(postcode_results_list['response']['total'] / max_page_results))

            query_params = "&historical=" + request.args.get('historical', 'True') + "&verbose=true" + \
                           '&resultsperpage=' + str(request.args.get('resultsperpage', 10))
            if classificationfilter:
                query_params = query_params + "&classificationfilter=" + classificationfilter

            return render_template('postcode-results.html', postcodeResults=postcode_results_list,
                                   form=form, page=page, maxPage=max_page, queryParams=query_params,
                                   csrf_token=form.csrf_token)

        else:
            app.logger.error(str(response.status_code) + ' response from address index')

            return render_template('postcode-results.html', csrf_token=form.csrf_token)
