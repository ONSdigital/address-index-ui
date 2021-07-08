import requests
from . import app


def api(
    url,
    called_from,
    all_user_input,
):

  if (called_from == 'uprn') or (called_from == 'postcode'):
    url = app.config.get('API_URL') + url + all_user_input.get(called_from)
    r = requests.get(url, )

  elif called_from == 'singlesearch':
    url = app.config.get('API_URL') + url
    params = {'input': all_user_input.get('input')}
    print("")
    print("Old params are")
    print(params)

    print("")
    print("All user input is ")
    print(all_user_input)
    print("")
    print("proposed:")
    proposed_params = {k: v for k, v in all_user_input.items() if v}
    proposed_params['epoch'] = ''
    print(proposed_params)

    r = requests.get(url, params=params)

  return r
