export function forceCapsInput() {
  const postcodeInput = document.querySelector('#postcode');
  postcodeInput.addEventListener('input', (e) => {
    e.target.value = e.target.value.toUpperCase();
  });
}
