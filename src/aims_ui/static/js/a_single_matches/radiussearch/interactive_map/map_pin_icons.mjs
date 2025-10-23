
export function makePinIcon(hex) {
  const iconSvg = `
  <svg width="25" height="41" viewBox="0 0 25 41" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
        <feDropShadow dx="0" dy="1.2" stdDeviation="1.2" flood-opacity="0.35"/>
      </filter>
    </defs>
    <!-- pin body -->
    <path d="M12.5 0C5.596 0 0 5.596 0 12.5c0 8.274 11.44 20.985 11.928 21.518a1 1 0 0 0 1.144 0C13.56 33.485 25 20.774 25 12.5 25 5.596 19.404 0 12.5 0z"
          fill="${hex}" stroke="#666" filter="url(#shadow)"/>
    <!-- centre dot -->
    <circle cx="12.5" cy="12.5" r="5.2" fill="#ffffff"/>
  </svg>`;

  const url = "data:image/svg+xml;charset=UTF-8," + encodeURIComponent(iconSvg);

  return L.icon({
    iconUrl: url,
    iconSize: [25, 71],
    iconAnchor: [12, 41],
    popupAnchor: [0, -34],
  });
}