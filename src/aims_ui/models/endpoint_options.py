def get_options(option):
  """Get options for a dropdown menu"""

  if option == 'percentage_match':
    percent_values = [1, 2, 3, 5, 10, 25, 50, 60, 75, 80, 95]
    return (['%' + str(x) for x in percent_values])

