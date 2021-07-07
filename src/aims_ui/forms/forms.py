from flask_wtf import FlaskForm

from wtforms import StringField, BooleanField, IntegerField
from aims_ui.forms.validators import ValidatePostcode


class PostcodeForm(FlaskForm):
    form_postcode = StringField('Postcode', [ValidatePostcode()])
    form_classification_filter = StringField('Classification Filter')
    form_historical = BooleanField('Include historical data?')
    form_results_per_page = IntegerField('Results per page')
