from flask_login import login_required
from flask import render_template, request
from aims_ui import app
from aims_ui.models.get_fields import get_fields
from aims_ui.page_helpers.security_utils import check_user_has_access_to_page
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.page_helpers.pages_location_utils import get_page_location
from aims_ui.page_helpers.google_utils import get_username, get_current_group


page_name = 'multiple_address_attributes'


@login_required
@app.route(f'/multiple_address_attributes', methods=['GET', 'POST'])
def multiple_address_attributes():
  endpoints = get_endpoints(called_from=page_name)
  access = check_user_has_access_to_page(page_name)
  if access != True:
    return access
  page_location = get_page_location(endpoints, page_name)

  current_group = get_current_group()
  bulk_limits = current_group.get('bulk_limits')

  endpoints = get_endpoints(called_from=page_name)
  searchable_fields = get_fields(page_name)

  return render_template(
      page_location,
      endpoints=endpoints,
      searchable_fields=searchable_fields,
      bulk_limits=bulk_limits,
  )
