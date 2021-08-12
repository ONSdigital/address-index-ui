def get_options(option):
  """Get options for a dropdown menu"""

  if option == 'epoch':
    return ([str(x) for x in reversed(range(0, 85))])

  elif option == 'percentage_match':
    percent_values = [1, 2, 3, 5, 10, 25, 50]
    return (['%' + str(x) for x in percent_values])
