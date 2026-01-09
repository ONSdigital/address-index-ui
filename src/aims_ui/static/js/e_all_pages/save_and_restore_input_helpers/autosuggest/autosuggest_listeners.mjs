// Helpers for saving the value of an autosuggest - more duifficult than a regular input,
// as it needs to save on click, enter selection, change etc

import { saveValueOfInput } from '../save_input_listeners.mjs';

// Remove markup from inside an element (i.e for the autosuggest suggestions)
function removeMarkupFromInsideElement(element) {
  if (!element) return '';

  const clone = element.cloneNode(true);

  // Replace <strong> with just its text content
  clone.querySelectorAll('strong').forEach(strongEl => {
    const textNode = document.createTextNode(strongEl.textContent);
    strongEl.replaceWith(textNode);
  });

  // Remove all <span>s entirely
  clone.querySelectorAll('span').forEach(spanEl => {
    spanEl.remove();
  });

  // Return the pure text
  return clone.textContent.trim();
}

export function addAutosuggestListenersToSaveOnChange(page_name, htmlId) {
  // Given an id of the autostugget input
  // the event listener must be on the *Suggestions* not the element
  // as the element itself triggers events like input, change, blur before the value is changed

  const completeContainerForClassificationFilter = document.querySelector('#complete-container-for-' + htmlId);
  const inputElement = completeContainerForClassificationFilter.querySelector('#' + htmlId);

  const classNameForSuggestionContainer = "ons-autosuggest__results";
  const suggestionContainer = completeContainerForClassificationFilter.querySelector('.' + classNameForSuggestionContainer);

  if (!suggestionContainer) { 
    console.log('No suggestion container found for autosuggest component');
    return;
  }

  suggestionContainer.addEventListener('click', event => {
    const clickedEl = event.target.closest('li');

    if (clickedEl) {
      const textFromAutosuggest = removeMarkupFromInsideElement(clickedEl);

      // Now save this value
      saveValueOfInput(inputElement.id, textFromAutosuggest, page_name);
      console.log('Saved value from autosuggest:', textFromAutosuggest);
    } else {
      console.log('Clicked outside of a suggestion <li>');
    }
  });

  // Add an event listener for keyboard selection (Enter key)
  completeContainerForClassificationFilter.addEventListener('keydown', event => {
    if (event.key === 'Enter') {
      // The suggestion that is currently focused will have ons-autosuggest__option--focused
      const focusedSuggestion = suggestionContainer.querySelector('.ons-autosuggest__option--focused');
      if (focusedSuggestion) {
        const textFromAutosuggest = removeMarkupFromInsideElement(focusedSuggestion);

        // Now save this value
        saveValueOfInput(inputElement.id, textFromAutosuggest, page_name);
        console.log('Saved value from autosuggest (keyboard):', textFromAutosuggest);
      }
    }
    else {
      // Save the content of the input element on any other key
      saveValueOfInput(inputElement.id, inputElement.value, page_name);
    }
  });
}
