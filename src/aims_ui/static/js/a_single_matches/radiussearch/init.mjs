import { setupSubmissionFromInputs } from "./form_helpers.mjs";
import { updateMapToFitCircle, setupLatLongToMapListeners, addMatchedAddressMarkersToMap, setupMap, setupRadiusListeners, setupLatLongFromMapListeners, setupInitialMarkerLocation } from "./interactive_map/map_setup.mjs";
import { setMapSizeAndResizeListeners } from "./interactive_map/map_size.mjs";
import { setupHorizontalInputs } from "./page_reformatting.mjs";
import { setupScrollListeners, setScrollPosition } from "./scroll_helpers.mjs";
import { setupUprnSearchFunctionality } from "./uprn_helper.mjs";

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
  addMatchedAddressMarkersToMap();

  // Set map size and resize listeners
  setMapSizeAndResizeListeners(map);
}

function setupPageSpecificItems() {
  // Take the generated Design System components and arrange them horizontally
  setupHorizontalInputs();

  // Return to last scroll postition if it was set
  setScrollPosition();

  // Listen for scrolling, save last location
  setupScrollListeners();

  setupSubmissionFromInputs();
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
