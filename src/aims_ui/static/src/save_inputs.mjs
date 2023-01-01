// Add all the inputs into an array, ignoring dropdowns
function getInputObjects() {
  const inps = document.querySelectorAll('.ons-input');
  const final = [];
  for (const a of inps) {
    if ( ! a.classList.contains('ons-input--select') ) {
      if (! a.classList.contains('nocache') ) {
        final.push(a);
      }
    }
  }
  return final;
}

const inputs = getInputObjects();
const loc = window.location.href;
function getInputObjectValues() {
  const input_obj = {}
  for (const a of inputs) {
    input_obj[a.id] = a.value;
  }
  return input_obj
}

function saveToLocalStorage() {
  const values = JSON.stringify(getInputObjectValues());
  localStorage.setItem(loc, values);
}
function wipeLocalStorage() {
  localStorage.removeItem(loc);
}


// Add event listener to save data when the form is submitted
const form = document.querySelector('form');
form.addEventListener('submit', (e) => {
  saveToLocalStorage();
});

const clear_button = document.querySelector('#clear-form-data-button-id');
clear_button.addEventListener('click', (e) => {
  wipeLocalStorage();
});


// Load values on page load if they exist
const stored_vals = localStorage.getItem(loc);
if (stored_vals) {
  const parsed_vals = JSON.parse(stored_vals);
  for (const inp of inputs) {
    const current_val = parsed_vals[inp.id];
    if (current_val) {
      inp.value = current_val;
    }
  }
}


