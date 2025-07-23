from flask import render_template, request, session
from flask_login import login_required

from aims_ui import app
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.models.get_fields import get_fields
from aims_ui.page_helpers.cookie_utils import delete_input
from aims_ui.page_helpers.pages_location_utils import get_page_location
from aims_ui.page_helpers.security_utils import check_user_has_access_to_page

page_name = 'radiussearch'


@login_required
@app.route(f'/{page_name}', methods=['GET', 'POST'])
def radiussearch():
  endpoints = get_endpoints(called_from=page_name)
  access = check_user_has_access_to_page(page_name)
  if access != True:
    return access
  page_location = get_page_location(endpoints, page_name)

  if request.method == 'GET':
    delete_input(session)
    return render_template(
        page_location,
        searchable_fields=get_fields(page_name),
        endpoints=endpoints,
    )

  # Posts - not yet handled
  searchable_fields = get_fields(page_name)
  matched_addresses = []
  return render_template(
      page_location,
      endpoints=endpoints,
      searchable_fields=searchable_fields,
     results_page=True,
      matched_addresses=matched_addresses,
      matched_address_number=len(matched_addresses),
  )
