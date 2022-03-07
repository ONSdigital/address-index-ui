def create_table(table_headers, table_rows):
  """Given array of table headers, and an array of arrays for each row, format as table"""
  ths = [{'value': header_name} for header_name in table_headers]
  trs = [{
      'tds': [{
          'value': col_val
      } for col_val in row]
  } for row in table_rows]

  return {'ths': ths, 'trs': trs}


def create_hierarchey_table(table_templates):
  row_titles = ['UPRN', 'Name']
  dic_tables = {}
  t_title = ''
  for t in table_templates:
    if t_title != t[0]:
      t_title = t[0]

    tmp = dic_tables.get(t_title, [] )
    tmp.append( [ t[1], t[2] ] )

    dic_tables[t_title] =tmp

  final_tables = {}
  for key, value in dic_tables.items():
    nunjucks_table = create_table(row_titles, value)
    final_tables[key] = nunjucks_table

  return final_tables 




