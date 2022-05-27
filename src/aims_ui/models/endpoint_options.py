def get_options(option):
  """Get options for a dropdown menu"""

  if option == 'percentage_match':
    percent_values = [x if x > 0 else 1 for x in range(0, 100, 5)]
    return (['%' + str(x) for x in percent_values])
