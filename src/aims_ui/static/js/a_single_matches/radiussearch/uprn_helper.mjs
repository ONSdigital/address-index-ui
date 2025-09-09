// JS to manage a clientside UPRN lookup to auto-fill lat/lon fields

function searchForUprnAndUpdateLatLonFields() {
  // Get the UPRN input field value
  const uprnInput = document.querySelector('#uprn');

  return {};
}

// Firstly stop the button submitting the form when this button is clicked
export function setupUprnSearchFunctionality() {
  // Get the UPRN input container
  const containerForUprnInput = document.querySelector('#complete-container-for-uprn');

  // The only button in the UPRN container should be the one associated with the UPRN input
  const uprnSearchButton = containerForUprnInput.querySelector('button');
  // Remove the "type=submit" attribute so it doesn't submit the form
  uprnSearchButton.removeAttribute('type');

  // Add new click listener
  uprnSearchButton.addEventListener('click', (e) => {
    e.preventDefault(); // Stop the button from submitting the form
    // Submit the UPRN to the API and get the lat/lon values
    searchForUprnAndUpdateLatLonFields();
  })
};