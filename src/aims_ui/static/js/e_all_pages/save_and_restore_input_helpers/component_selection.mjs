// Functions to select components through use of the container divs

export function selectInputFromHtmlIdUsingContianer(htmlId) {
  // Get the input container
  const containerQuerySelector = '#complete-container-for-' + htmlId;
  const containerElement = document.querySelector(containerQuerySelector);

  if (!containerElement) {
    console.warn('No container element found for input Id:' + containerQuerySelector + '. Have you ensured all components have a wrapper div with the ID "complete-container-for-[htmlId]"?');
    return null;
  }

  // Get the input element
  const inputElement = containerElement.querySelector('input');

  if (!inputElement) {
    console.warn('No input element found inside container:"' + containerElement + '"');
    return null;
  }

  return inputElement;
}