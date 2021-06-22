from .endpoint import Endpoint

def get_endpoints():
  # Add new endpoints here for auto-creation on landing page
  endpoint_data = [
      {'title':'Unique Product Refference Number',
        'url':'uprn',
        'description_text' : "Search for a property via it's unique property refference number. This is a 12 didgit number which contains no characters",
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

  return endpoints

