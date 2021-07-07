import requests
import json
import re
from . import app
from flask import current_app


class Utils:

    @staticmethod
    def get_ai_response(endpoint, params=None):
        url = current_app.config['API_URL'] + endpoint
        headers = {'Authorization': current_app.config['API_JWT']}
        ai_return = requests.get(url, params=params, headers=headers)
        return ai_return

    @staticmethod
    def get_ai_postcode(postcode, params):
        endpoint = '/addresses/postcode/' + postcode
        response = Utils.get_ai_response(endpoint, params)
        return response


class Classifications(Utils):

    @staticmethod
    def get_class_list():
        classifications = Utils.get_ai_response("/classifications")
        return json.loads(classifications.text)

    @staticmethod
    def get_class_subset(code=None):

        class_call = Utils.get_ai_response("/classifications")
        class_list = json.loads(class_call.text)

        subset_list = []

        if code:

            if len(code) == 1:
                for classification in class_list['classifications']:
                    if re.match(r'^(%s)[A-Z]$' % code, classification['code']):
                        subset_list.append({"code": classification['code'].encode("utf-8"),
                                            "label": classification['label'].encode("utf-8")})
            elif len(code) == 2:
                for classification in class_list['classifications']:
                    if re.match(r'^(%s)[0-9]{2}$' % code, classification['code']):
                        subset_list.append({"code": classification['code'].encode("utf-8"),
                                            "label": classification['label'].encode("utf-8")})
            elif len(code) == 4:
                for classification in class_list['classifications']:
                    if re.match(r'^(%s)[A-Z]{2}$' % code, classification['code']):
                        subset_list.append({"code": classification['code'].encode("utf-8"),
                                            "label": classification['label'].encode("utf-8")})
        else:
            for classification in class_list['classifications']:
                if re.match(r'^[A-Z]$', classification['code']):
                    subset_list.append({"code": classification['code'].encode("utf-8"),
                                        "label": classification['label'].encode("utf-8")})

        return subset_list

    @staticmethod
    def get_child_count(code):

        count = len(Classifications.get_class_subset(code))

        return count

    @staticmethod
    def get_classification_list(code=None):

        class_list = []

        for classification in Classifications.get_class_subset(code):
            class_list.append({"code": classification['code'], "label": classification['label'],
                               "child_count": Classifications.get_child_count(classification['code'])})

        return class_list


class Siblings(Utils):

    @staticmethod
    def get_siblings(relatives):

        sibling_list = []

        for level in relatives:
            for sibling in level['siblings']:
                app.logger.info(str(sibling))
                endpoint = "/addresses/uprn/" + str(sibling)
                sibling_request = Utils.get_ai_response(endpoint, 'verbose=true')
                # sibling_request.raise_for_status()

                if sibling_request.status_code == 200:
                    sibling_result = json.loads(sibling_request.text)
                    sibling_uprn = sibling
                    sibling_address = sibling_result['response']['address']['formattedAddressNag']
                    sibling_list.append({"uprn": sibling_uprn,
                                         "address": sibling_address})
        return sibling_list
