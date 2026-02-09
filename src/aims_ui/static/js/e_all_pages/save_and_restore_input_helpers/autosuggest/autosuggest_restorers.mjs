import { selectInputFromHtmlIdUsingContainer } from "../component_selection.mjs";

export function restoreValuesToAutosuggestInput(page_name, htmlId, pagePreviouslySearchedValues) {
  // Get the input element
  const inputElement = selectInputFromHtmlIdUsingContainer(htmlId);
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