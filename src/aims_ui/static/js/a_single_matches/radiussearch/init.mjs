import { setupMap, setupLatLongListeners, setupInitialMarkerLocation } from "./interactive_map.mjs";
import { setupHorizontalInputs } from "./page_reformatting.mjs";

function init() {
  console.log('RADIUS SEARCH specific scripts loaded');

  // Setup the interactive map
  setupMap();

  // Take the generated Design System components and arrange them horizontally
  setupHorizontalInputs();

  // Add Listeners to map
  setupLatLongListeners();

  // Add initial Marker - This might not be desirable behaviour in future
  setupInitialMarkerLocation();

}

window.addEventListener('load', init);
