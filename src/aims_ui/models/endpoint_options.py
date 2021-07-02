
def get_options(option):
  """Get options for a dropdown menu"""

  if option == 'epoch':
    return (
        [str(x) for x in reversed (range (0,92)) ] )

