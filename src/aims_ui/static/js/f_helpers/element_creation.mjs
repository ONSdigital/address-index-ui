// Shorthand for document.createElement()
export function crEl(el, elementId = null, classList = []) {
  const newElement = document.createElement(el);

  if (elementId !== null) {
    newElement.id = elementId;
  }

  for (const className of classList) {
    newElement.classList.add(className);
  }

  return newElement;
}