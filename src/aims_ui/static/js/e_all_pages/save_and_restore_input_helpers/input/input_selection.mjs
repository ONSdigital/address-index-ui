
export function selectInputFromHtmlIdUsingContianer(htmlId) {
  // Get the input container
  const containerQuerySelector = '#complete-container-for-' + htmlId;
  const containerElement = document.querySelector(containerQuerySelector);

  if (!containerElement) {
    console.warn('No container element found for input Id:', containerQuerySelector);
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