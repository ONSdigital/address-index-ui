export function getDefaultValuesForPage(page_name) {
  const defaultValues = {
    'radiussearch': {
      'lat': 50.73548,
      'lon': -3.5332105,
      'zoom': 8,
      'rangekm': '10',
      'limit': '50',
      'classificationfilter': '',
      'uprn': '',
      'input': '',
    }
  };

  if (page_name in defaultValues) {
    return defaultValues[page_name];
  }

  return {};
}

export function getDefaultFavourites() {
  return [
    'uprn',
    'parentUprn',
    'classificationCode',
    'classificationCodeList',
    'formattedConfidenceScore',
    'nagLocalCustodianName',
  ];
}