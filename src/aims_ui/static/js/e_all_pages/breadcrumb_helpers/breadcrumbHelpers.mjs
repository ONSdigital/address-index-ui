import { getGlobalValues, setGlobalValues } from '/static/js/f_helpers/local_storage_page_helpers.mjs';

// Sort a list of breadcrumbs by time
function sortBreadcrumbsByTime(breadcrumbList) {
  // breadcrumbs as [ {"page": "/...", "time": "2024-10-01T12:34:56.789Z"}, ... ]

  if (!breadcrumbList?.page_breadcrumbs) return breadcrumbList;

  breadcrumbList.page_breadcrumbs.sort((a, b) => 
    new Date(b.time) - new Date(a.time)
  );

  return breadcrumbList;
}

export function addMostRecentPageToStorage() {
  // Maintain a list of the last 8 pages visited
  const pageBreadcrumbs = getGlobalValues().page_breadcrumbs || [];
  const currentPage = window.location.pathname;
  const currentTime = new Date().toISOString();

  // Global values used across pages
  const newPageBreadcrumbs = {
    page_breadcrumbs: [...pageBreadcrumbs, { page: currentPage, time: currentTime }],
  };

  // Keep only the last 8 entries
  if (newPageBreadcrumbs.page_breadcrumbs.length > 8) {
    newPageBreadcrumbs.page_breadcrumbs = newPageBreadcrumbs.page_breadcrumbs.slice(-8);
  }

  // Sort by time to ensure most recent first
  const sortedBreadcrumbs = sortBreadcrumbsByTime(newPageBreadcrumbs);

  setGlobalValues(sortedBreadcrumbs);
}