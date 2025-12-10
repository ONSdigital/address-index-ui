import { getPagePreviouslySearchedValues,
 setPreviouslyStoredValuesForThisPage } from './set_and_get_data.mjs'

function saveValueOfInput(inputId, inputValue, page_name) {
  console.log(`Saving value of input ${inputId}: ${inputValue}`);

  // Firstly get the current pages previously stored input values
  // fallback to default values if none found
  const previouslyStoredValues = getPagePreviouslySearchedValues(page_name);

  // Now create a new object with the inputId and input value
  const valuesToMerge = {[inputId]: inputValue};

  // Now merge with the previously stored values
  const mergedValues = {...previouslyStoredValues, ...valuesToMerge};

  // Now save the new values
  setPreviouslyStoredValuesForThisPage(mergedValues, page_name);
}

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

function addEventListenerToTriggerSaveOnChangeForAutosuggestComponent(inputElement, page_name) {
  // Given an input element that's an ONS autosuggest component
  // the event listener must be on the *Suggestions* not the element
  // as the element itself triggers events like input, change, blur before the value is changed
  const completeContainerForClassificationFilter = document.querySelector('#complete-container-for-classificationfilter');

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
  });
}

export function addEventListenersToTriggerSaveOnChange(saveAndRestoreInputIds, page_name) {
  // Loop over all the ids
  for (const id of saveAndRestoreInputIds) {
    const inputElement = document.querySelector('#' + id);

    // If the element not found, skip it
    if (!inputElement) { return; }

    // If it's an autosuggest component, use a different event listener
    if (inputElement.classList.contains('ons-js-autosuggest-input')) {
      // Add an event listener to save from a suggestion - STILL REQUIRES A REGULAR INPUT LISTENER
      addEventListenerToTriggerSaveOnChangeForAutosuggestComponent(inputElement, page_name);
    } 
    inputElement.addEventListener('input', () => {
      saveValueOfInput(inputElement.id, inputElement.value, page_name);
    });
  }
}