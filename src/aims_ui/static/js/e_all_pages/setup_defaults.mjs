export function getDefaultValuesForPage(page_name) {
  const defaultValues = [
    {
      'page_name': 'radiussearch',
      'lat': '51.566322',
      'lon': '-3.0272245',
      'rangekm': '10',
      'limit': '10',
    }
  ];

  for (const entry of defaultValues) {
    if (entry.page_name === page_name) {
      return entry;
    }
  }

  return {};
}
