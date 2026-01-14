
export function uprnPopulateAndRedirect() {
  // Get the url param search_uprn
  const urlParams = new URLSearchParams(window.location.search);
  const searchUprn = urlParams.get('search_uprn');

  // If the param doesn't exist, do nothing
  if (!searchUprn) { return; }

  // Get the input and set the value
  const uprnInput = document.querySelector('#uprn');
  uprnInput.value = searchUprn;

  // Trigger an input event for listeners on the input 
  const event = new Event('input');
  uprnInput.dispatchEvent(event);

  // Remove the param from the url to prevent infinite loop
  urlParams.delete('search_uprn');
  const newUrl = `${window.location.pathname}?${urlParams.toString()}`;
  window.history.replaceState(null, '', newUrl);

  // Submit the form to trigger the search
  const searchForm = document.querySelector('form');
  searchForm.submit();
}

function init() {
  uprnPopulateAndRedirect();
  console.debug('uprn specific js loaded');
}

window.addEventListener('load', init);
