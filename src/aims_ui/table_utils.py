def create_table(table_headers, table_rows):
  """Given array of table headers, and an array of arrays for each row, format as table"""
  ths = [{'value': header_name} for header_name in table_headers]
  trs = [{
      'tds': [{
          'value': col_val
      } for col_val in row]
  } for row in table_rows]

  return {'ths': ths, 'trs': trs}
