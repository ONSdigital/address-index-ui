from flask import Flask

from src import aims_ui
from aims_ui.models.endpoint_options import get_options


def test_get_options_percentage_match():
  # Get the percentage match generated results
  result = get_options('percentage_match')

  percent_values = [x if x > 0 else 1 for x in range(0, 100, 5)]
  final_values = ['%' + str(x) for x in percent_values]

  assert result == final_values
