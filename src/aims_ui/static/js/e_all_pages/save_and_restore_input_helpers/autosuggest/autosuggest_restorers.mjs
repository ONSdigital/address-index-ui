

export function restoreValuesToAutosuggestInput(page_name, htmlId, pagePreviouslySearchedValues) {
  // Get the input element

  const inputElement = document.querySelector('#' + htmlId);

  if (!inputElement) {
    console.warn('No input element found for Id:', htmlId);
    return;
  }

  // Get previous value
  const previousValue = pagePreviouslySearchedValues[htmlId];

  // If previous value exists, set it
  if (previousValue !== undefined) {
    inputElement.value = previousValue;
    console.debug(`Restored value for input ${htmlId} to: ${previousValue}`);
  } else {
    console.debug(`No previously stored value for input ${htmlId}`);
  }

}