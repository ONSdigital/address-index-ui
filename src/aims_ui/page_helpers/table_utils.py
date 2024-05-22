def create_table(table_headers, table_rows):
  """Given array of table headers, and an array of arrays for each row, format as table"""
  ths = [{
      'value': header_name,
      'ariaSort': 'none'
  } for header_name in table_headers]
  trs = [{
      'tds': [{
          'value': col_val
      } for col_val in row]
  } for row in table_rows]

  # Remove blank ({'tds': []}) rows from the table
  tmp = []
  for row in trs:
    if str(row) != "{'tds': []}":
      tmp.append(row)

  return {'ths': ths, 'trs': tmp}


def create_hierarchy_table(table_templates):
  """Create possibly several tables of an addresses hierarchey"""
  # Example UPRN for Quaternery 15127116
  row_titles = ['Name', 'Parent UPRN', 'UPRN']
  dic_tables = {}
  t_title = ''
  for t in table_templates:
    if t_title != t[0]:
      t_title = t[0]

    tmp = dic_tables.get(t_title, [])
    uprn_link = f'<a href="/address_info/{t[2]}">{t[2]}<a>'
    parent_uprn_link = f'<a href="/address_info/{t[3]}">{t[3]}<a>'
    tmp.append([t[1], parent_uprn_link, uprn_link])

    dic_tables[t_title] = tmp

  final_tables = {}
  for key, value in dic_tables.items():
    nunjucks_table = create_table(row_titles, value)
    final_tables[key] = nunjucks_table

  return final_tables
