def create_table(table_headers, table_rows):
  """Given array of table headers, and an array of arrays for each row, format as table"""
  ths = [{'value': header_name} for header_name in table_headers]
  trs = [{
      'tds': [{
          'value': col_val
      } for col_val in row]
  } for row in table_rows]

  return {'ths': ths, 'trs': trs}

class Table():
  def __init__(self, title):
    self.title = title
    self.rows = []
    self.row_titles = ['UPRN', 'Name']

  def add_row(self, row):
    self.rows.append(row)



def create_hierarchey_table(table_templates):
  print(table_templates)
  print('')

  dic_tables = {}
  t_title = ''
  for t in table_templates:
    if t_title != t[0]:
      t_title = t[0]

    tmp = dic_tables.get(t_title, [] )
    tmp.append( [ t[1], t[2] ] )

    dic_tables[t_title] =tmp

  print(dic_tables)

  return final_tables 




