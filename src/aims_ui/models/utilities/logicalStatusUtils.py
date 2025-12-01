codes = {
    '1': {
        'status': '1',
        'text': 'Approved',
        'colour': '#90EE90'
    },
    '3': {
        'status': '3',
        'text': 'Alternative',
        'colour': '#FFA500'
    },
    '6': {
        'status': '6',
        'text': 'Provisional',
        'colour': '#FFFF00'
    },
    '8': {
        'status': '8',
        'text': 'Historical',
        'colour': '#ff0000'
    },
}


# Get additional lpiLogicalStatus information, empty dict if not found
def getFullLpiLogicalStatusInfo(value):
  code_vals = codes.get(str(value), {})
  return code_vals
