from .endpoint import Endpoint
from flask import url_for

def get_endpoints():
  # Add new endpoints here for auto-creation on landing page
  endpoint_data = [
      {'title':'Unique Property Refference Number',
        'url':'uprn',
        'description_text' : "Search for a property via it's unique property refference number. This is a 12 didgit number which contains no characters",
      },
      {'title':'Address',
        'url':'address',
        'description_text' : "Search for a property using it's address .This method of searching is more effective when the user might not know specifics about the property like it's UPRN. ",
      },
      {'title':'Postcode',
        'url':'postcode',
        'description_text' : "Search for a property using it's postcode. This is effective and a valid postcode will return a list of possible addresses.",
      },
      {'title':'Typeahead',
        'url':'typeahead',
        'description_text' : "This search types ahead. Auttosugest on steroids basically. Useful if you quickly want a user to find an address",
      },
      {'title':'Multiple Address',
        'url':'multiple_address',
        'description_text' : "Search for not just  one address. Several. Get lots of results you can haveanice look through",
      },
  ]
  
  endpoints = []

  for endpoint in endpoint_data:
    endpoints.append( Endpoint(
      endpoint.get('title'),
      endpoint.get('url'),
      endpoint.get('description_text'),
      endpoint.get('title_size',3),
      endpoint.get('name_id'),
    ) )

  nav_info = [{'title':endpoint.title, 'url':endpoint.url} for endpoint in endpoints]
  nav_info.insert(0, {'title':'Home', 'url': url_for('landing')})

  for endpoint in endpoints:
    endpoint.nav_info = nav_info

  return endpoints 

