codes = {'1': 'Approved', 
    '3': 'Alternative',
    '6': 'Provisional',
    '8': 'Historical', }

def getTextLogicalStatus(value):
  final = codes.get(str(value)) + ' (' + str(value) + ') '
  return final

