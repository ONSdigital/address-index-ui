// JS to manage a clientside UPRN lookup to auto-fill lat/lon fields
import { syncPageWithCurrentInputs, updateLatLongSearchValues } from "./interactive_map/map_setup.mjs";

function makeUprnErrorPanelVisible() {
  // Make the error panel visible
  const containerForUprnLookupPanelError = document.querySelector('#complete-container-for-uprnLookupPanelError');
  containerForUprnLookupPanelError.classList.remove('invisible');

  // Now make the info panel invisible
  const containerForUprnLookupPanelInfo = document.querySelector('#complete-container-for-uprnLookupPanelInfo');
  containerForUprnLookupPanelInfo.classList.add('invisible');
}

function makeUprnInfoPanelVisible() {
  // Make the info panel visible
  const containerForUprnLookupPanelInfo = document.querySelector('#complete-container-for-uprnLookupPanelInfo');
  containerForUprnLookupPanelInfo.classList.remove('invisible');

  // Now make the error panel invisible
  const containerForUprnLookupPanelError = document.querySelector('#complete-container-for-uprnLookupPanelError');
  containerForUprnLookupPanelError.classList.add('invisible');
}

function updateUprnResponse(title, ln1 = '', ln2 = '', uprn = '') {  
  const infoContainer = document.querySelector('#complete-container-for-uprnLookupPanelInfo');
  const errorContainer = document.querySelector('#complete-container-for-uprnLookupPanelError');

  for (const container of [infoContainer, errorContainer]) {
    // Update both container to the full response
    const uprnTitle = container.querySelector('#uprn-lookup-results-title');
    const uprnInfoLn1 = container.querySelector('#uprn-lookup-results-info-ln1');
    const uprnInfoLn2 = container.querySelector('#uprn-lookup-results-info-ln2');
    uprnTitle.textContent = title;
    uprnInfoLn1.textContent = ln1;
    uprnInfoLn2.textContent = ln2;

    if (uprn) {
      const uprnLink = document.createElement('a');
      uprnLink.href = '/address_info/' + uprn;
      uprnLink.textContent = 'View Details';
      uprnInfoLn2.append(uprnLink);
    }
  }
}

function updateResponseWithError(errorTitle, errorMessage) {
  updateUprnResponse(errorTitle, errorMessage);
  makeUprnErrorPanelVisible();
}

function updateResponseWithAddressDetails(response) {
  // Get just the "address" object
  const addressDetails = response?.response.address || {};
  console.log(addressDetails);
  //
  const nameOfAddress = addressDetails?.formattedAddress || 'No formatted address found';
  const uprn = addressDetails?.uprn ? addressDetails.uprn : 'No UPRN provided';
  updateUprnResponse('Address Matched:', nameOfAddress, '', uprn);
  makeUprnInfoPanelVisible();
}

function handleUprnErrorFromResponse(response) {
  console.error('Error response from UPRN API:', response.status, response.statusText);
  updateResponseWithError(`Error looking up UPRN: ${response.status}`, `Error: ${response.statusText}`);
}

function handleUprnErrorAccessingEndpoint(err) {
  console.error('Error accessing UPRN API endpoint:', err);
  updateResponseWithError('Error accessing UPRN API endpoint', `Error: ${err.message}`);
}

function handleUprnErrorWithMessage(title, description) {
  console.error(title, description);
  updateResponseWithError(title, description);
}

async function searchForUprn() {
  const uprnInput = document.querySelector('#uprn');
  const uprn = uprnInput?.value?.trim();

  if (!uprn) {
    handleUprnErrorWithMessage('No UPRN provided', 'Please enter a UPRN to search for.');
    return null;
  }

  try {
    const response = await fetch(`/api/uprn/${encodeURIComponent(uprn)}`);

    if (!response.ok) {
      handleUprnErrorFromResponse(response);
      return null;
    }

    const data = await response.json();
    return data;

  } catch (err) {
    console.error('Error fetching UPRN data:', err);
    handleUprnErrorAccessingEndpoint(err);
    return null;
  }
}

export function getUprnInputButton() {
  // Get the UPRN input container
  const containerForUprnInput = document.querySelector('#complete-container-for-uprn');
  // The only button in the UPRN container should be the one associated with the UPRN input
  const uprnSearchButton = containerForUprnInput.querySelector('button');

  return uprnSearchButton;
}

// Firstly stop the button submitting the form when this button is clicked
export function setupUprnSearchFunctionality() {
  const uprnSearchButton = getUprnInputButton();

  // Add new click listener
  uprnSearchButton.addEventListener('click', async (e) => {
    // Submit the UPRN to the API and get the lat/lon values
    const searchResult = await searchForUprn();
    if (!searchResult) {
      return; // Error already handled in searchForUprn
    }

    // Now update the lat/lon fields if we have them
    updateResponseWithAddressDetails(searchResult);

    // Lat will be from the response.address.geo.latitude
    // Lon will be from the response.address.geo.longitude
    const lat = searchResult.response?.address?.geo?.latitude;
    const lon = searchResult.response?.address?.geo?.longitude;

    if (lat && lon) {
      console.log('Updating lat/lon inputs with:', lat, lon);
      updateLatLongSearchValues(lat, lon);

      // Now the lat/long have been updated, we need to sync the page with the new inputs
      syncPageWithCurrentInputs();
    }
  });
};