const regionContainerIdMap = [
  {
    'page_name': 'singlesearch',
    'region_type': 'checkboxes',
    'container_id_suffixes': ['eboost', 'wboost', 'sboost', 'nboost', 'lboost', 'mboost', 'jboost'],
    'container_prefix': 'complete-container-for-',
  },
  {
    'page_name': 'typeahead',
    'region_type': 'inputs',
    'container_id_suffixes': ['eboost', 'wboost', 'sboost', 'nboost', 'lboost', 'mboost', 'jboost'],
    'container_prefix': 'complete-container-for-',
  },
];

export function returnCurrentPageMap(page_name) {
  for (const pageConfig of regionContainerIdMap) {
    if (pageConfig.page_name === page_name) {
      return pageConfig;
    }
  }
  return {};
}

export function getFullIdsOfEachRegionContainer(currentPageMap) {
  // Given the current map, return the full Ids of each region container to add listeners to
  const fullIds = currentPageMap.container_id_suffixes.map(suffix => {
    return currentPageMap.container_prefix + suffix;
  });

  return fullIds;
}
