// The interactive map is resizable by the user - the specified size
// should be restore from local storage on page load


import { getPageLocalValues, setPageLocalValues } from '/static/js/f_helpers/local_storage_page_helpers.mjs';
import { updateMapToFitCircle } from '/static/js/a_single_matches/radiussearch/interactive_map/map_setup.mjs';

let mapContainer;

export function setMapSizeAndResizeListeners(map) {
  // Set map size and resize listeners
  setSizeOfMapToPreviouslySetSize();
  setupResizeListeners(map);
}

function getMapSize() {
  // Returns the object containing previously set local storage values
  const localPageValues = getPageLocalValues('radiussearch');
  const previouslySetSize = localPageValues.mapSizePair;

  // Note that if there is no previously set size, this will be undefined
  return previouslySetSize;
}

function setSizeOfMapToPreviouslySetSize() {
  // Get a handle on the mapContainer 
  mapContainer = document.querySelector('#map');

  const previouslySetSize = getMapSize();

  // If a previously set size exists, apply it to the map container
  if (previouslySetSize) {
    mapContainer.style.width = previouslySetSize.width + 'px';
    mapContainer.style.height = previouslySetSize.height + 'px';
  }
}

function setMapSizeInPageStorage(sizeX, sizeY) {
  setPageLocalValues('radiussearch', { mapSizePair: { width: sizeX, height: sizeY } });
}

function setupResizeListeners(map) {
  // Observe changes to the map container's size, trigger map refresh and center search circle
  let resizeObserver = new ResizeObserver(() => {
    map.invalidateSize();
    updateMapToFitCircle();

    // Now get the px size of the map and save them
    setMapSizeInPageStorage(mapContainer.offsetWidth, mapContainer.offsetHeight);
  });

  resizeObserver.observe(mapContainer);
}