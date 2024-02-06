codes = {
    '1': {
        'status': 'Approved',
        'colour': '#90EE90'
    },
    '3': {
        'status': 'Alternative',
        'colour': '#FFA500'
    },
    '6': {
        'status': 'Provisional',
        'colour': '#FFFF00'
    },
    '8': {
        'status': 'Historical',
        'colour': '#ff0000'
    },
}


def getTextLogicalStatus(value):
  code_vals = codes.get(str(value))
  if code_vals:
    code_colour = code_vals.get('colour')
    final_string = code_vals.get('status') + ' (' + str(value) + ') '
    final_html = f'<div style="background-color:{code_colour};">{final_string}</div>'
    return final_html
  else:
    return '<div style="background-color:#ff0000;">None</div>'
