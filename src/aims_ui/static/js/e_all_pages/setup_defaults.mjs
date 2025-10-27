export function getDefaultValuesForPage(page_name) {
  const defaultValues = [
    {
      'page_name': 'radiussearch',
      'lat': 50.73548,
      'lng': -3.5332105,
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
