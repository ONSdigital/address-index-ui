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
  const textAreaElement = containerElement.querySelector('textarea');

  if (!inputElement && !textAreaElement) {
    console.warn('No input or text area element found inside container:"' + containerElement + '". Are you sure the input is wrapped inside the container div and not outside?');
    return null;
  }

  // If there is no input element, return text area element
  if (!inputElement) {
    return textAreaElement;
  }

  return inputElement;
}