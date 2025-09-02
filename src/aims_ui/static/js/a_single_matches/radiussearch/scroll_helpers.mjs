import { getPageLocalValues, setPageLocalValues } from '/static/js/f_helpers/local_storage_page_helpers.mjs';

// Set a listener for scrolling (via mouse or any other way) which console.logs the new scroll position
export function setupScrollListeners() {
  window.addEventListener('scroll', () => {
    saveNewScrollPosition(window.scrollY);
  });
}

function saveNewScrollPosition(newScrollY) {
  // Get the current page's values
  const pageLocalValues = getPageLocalValues('radiussearch');

  // Update the scroll position
  pageLocalValues.scrollPosition = newScrollY;

  // Save the updated values
  setPageLocalValues('radiussearch', pageLocalValues);
}

export function setScrollPosition() {
  const pageLocalValues = getPageLocalValues('radiussearch');
  if (pageLocalValues.scrollPosition) {
    // Wait until all scripts and DOM content are loaded, then scroll
    window.addEventListener('load', () => {
      window.scrollTo(0, pageLocalValues.scrollPosition);
    });
  }
}