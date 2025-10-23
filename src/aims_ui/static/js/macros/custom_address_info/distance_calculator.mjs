import { getCurrentSearchLatValue, getCurrentSearchLonValue } from '/static/js/a_single_matches/radiussearch/interactive_map/map_setup.mjs';

// Calculate distance between two lat/long pairs on Earth (haversine, great-circle)
// All lat/lon in decimal degrees. Returns distance in metres.

// https://www.movable-type.co.uk/scripts/latlong.html
function distanceInMetres(lat1, lon1, lat2, lon2) {
  // Convert degrees to radians
  const toRad = (deg) => deg * Math.PI / 180;

  const φ1 = toRad(lat1);
  const φ2 = toRad(lat2);
  const Δφ = toRad(lat2 - lat1);
  const Δλ = toRad(lon2 - lon1);

  // Mean Earth radius in metres (approximate, suitable for most applications)
  const R = 6371000; // metres

  const sinΔφ = Math.sin(Δφ / 2);
  const sinΔλ = Math.sin(Δλ / 2);

  const a = sinΔφ * sinΔφ +
            Math.cos(φ1) * Math.cos(φ2) * sinΔλ * sinΔλ;

  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

  return R * c; // metres
}

function addCommasToDistance(metres) {
  const n = Math.round(Number(metres));
  return Number.isFinite(n) ? n.toLocaleString('en-GB') : 'NA';
}

// Export this so it can be triggered on lat/lon updates
export function replaceDistancePlaceholderWithSearchValues() {
  const distanceElements = document.querySelectorAll('.distance_attribute');

  const searchLat = getCurrentSearchLatValue();
  const searchLon = getCurrentSearchLonValue();
  if (searchLat == null || searchLon == null) return;

  distanceElements.forEach((el) => {
    const myLat = parseFloat(el.getAttribute('myLat') ?? el.getAttribute('mylat'));
    const myLon = parseFloat(el.getAttribute('myLon') ?? el.getAttribute('mylon'));
    if (Number.isFinite(myLat) && Number.isFinite(myLon)) {
      const metres = distanceInMetres(myLat, myLon, searchLat, searchLon);
      el.textContent = `${addCommasToDistance(metres)} m`;
    } else {
      el.textContent = 'NA';
    }
  });

}

// Call as soon as the script itself is loaded
replaceDistancePlaceholderWithSearchValues();