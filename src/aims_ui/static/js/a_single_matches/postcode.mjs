export function forceCapsInput() {
  const postcodeInput = document.querySelector('#postcode');
  postcodeInput.addEventListener('input', (e) => {
    e.target.value = e.target.value.toUpperCase();
  });
}

export function init() {
  console.log('postcode specific loaded');
  forceCapsInput();
}

window.addEventListener('load', init);
