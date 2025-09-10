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

export function setupSubmissionFromInputs() {
  // Firstly stop the UPRN search button from submitting raidus search
  preventUprnButtonSubmittingForm();

  // Now add listeners to all other inputs to submit the form when "Enter" is pressed
}