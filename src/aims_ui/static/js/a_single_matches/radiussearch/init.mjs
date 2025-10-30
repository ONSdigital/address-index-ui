import { setupSubmissionFromInputs } from "./form_helpers.mjs";
import { updateMapToFitCircle, setupLatLongToMapListeners, setupMap, setupRadiusListeners, setupLatLongFromMapListeners, setupInitialMarkerLocation } from "./interactive_map/map_setup.mjs";
import { setMapSizeAndResizeListeners } from "./interactive_map/map_size.mjs";
import { setupHorizontalInputs } from "./page_reformatting.mjs";
import { setupScrollListeners, setScrollPosition } from "./scroll_helpers.mjs";
import { setupUprnSearchFunctionality } from "./uprn_helper.mjs";
import { addMatchedAddressMarkersToMap } from "./interactive_map/result_address_markers.mjs";
import { setupClearButtonFunctionality } from "/static/js/a_single_matches/radiussearch/clear_button_functionality.mjs";

function setupMapSpecificItems() {
  // Setup the interactive map and return refference to it
  const map = setupMap();

  // Add Listeners to map to update the lat/long input boxes
  setupLatLongFromMapListeners();

  // Setup listeners on the lat/long inputs themselves to update the map
  setupLatLongToMapListeners();

  // Add initial Marker - This might not be desirable behaviour in future
  setupInitialMarkerLocation();

  // When a user changes the radius, update the circle radius marker
  setupRadiusListeners();

  // Add any results that are sat in local storage onto the map!
  addMatchedAddressMarkersToMap(map);

  // Set map size and resize listeners
  setMapSizeAndResizeListeners(map);

  // Setup zoom level listeners and restore last zoom level
  //setupZoomListeners(map);
}

function setupPageSpecificItems() {
  // Take the generated Design System components and arrange them horizontally
  setupHorizontalInputs();

  // Return to last scroll postition if it was set
  setScrollPosition();

  // Listen for scrolling, save last location
  setupScrollListeners();

  // Prevent the enter key from submitting the form to search for UPRN
  // instead add listeners to handle the enter key 
  setupSubmissionFromInputs();

  // Setup clear filter button functionality
  setupClearButtonFunctionality();
}

function init() {
  console.log('RADIUS SEARCH specific scripts loaded');

  // Setup page specific items
  setupPageSpecificItems();

  // Setup map specific items
  setupMapSpecificItems();

  // Setup UPRN search button
  setupUprnSearchFunctionality();

}

window.addEventListener('DOMContentLoaded', init);
