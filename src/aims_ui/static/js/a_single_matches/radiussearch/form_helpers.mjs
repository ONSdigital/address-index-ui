// Because there are two buttons within the form, we must manually handle submitting the 
// raidus search from all inputs except the UPRN search button, and prevent
// the UPRN search button from submitting the form for the raidus search

import { getUprnInputButton } from "./uprn_helper.mjs";

// Stop the UPRN search button from submitting the form when clicked
function preventUprnButtonSubmittingForm() {
  const uprnSearchButton = getUprnInputButton();

  uprnSearchButton.removeAttribute('type');
  uprnSearchButton.addEventListener('click', (e) => {
    e.preventDefault(); // Stop the button from submitting the form
  });
}

function addListenersForEnterKeyToSubmitForm() {
  // Deffine all the input element ids that should submit the form when "Enter" is pressed
  const inputIds = ['lat', 'lon', 'rangekm', 'classificationfilter', 'input', 'limit'];

  // Get the parent which contains all input elements
  const inputContainer = document.querySelector('#full-match-form-container');

  // For each input id, add a listener to submit the form when "Enter" is pressed
  for (const id of inputIds) {
    // Get each element
    const inputElement = inputContainer.querySelector('#' + id);
    // Add an event listener for all keys
    inputElement.addEventListener('keydown', (e) => {
      // If the key is Enter
      if (e.key === 'Enter') {
        e.preventDefault();
        // Submit the form
        const form = inputElement.closest('form');
        form.requestSubmit();
      }
    });
  };
}

export function setupSubmissionFromInputs() {
  // Firstly stop the UPRN search button from submitting raidus search
  preventUprnButtonSubmittingForm();

  // Now add listeners to all other inputs to submit the form when "Enter" is pressed
  addListenersForEnterKeyToSubmitForm();
}