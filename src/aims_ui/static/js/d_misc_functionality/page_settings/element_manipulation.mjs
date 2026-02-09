// Contain standard way to check checkboxes, select radio buttons etc.

export function checkRadioButtonByElement(radioElement) {
  if (radioElement) {
    radioElement.checked = true;
  }
}

export function checkRadioButtonById(documentId) {
  const radioElement = document.querySelector(`#${documentId}`);
  if (radioElement) {
    checkRadioButtonByElement(radioElement);
  }
}

export function checkCheckboxById(documentId) {
  const checkbox = document.querySelector(`#${documentId}`);
  if (checkbox) {
    checkbox.checked = true;
  }
}

export function uncheckCheckboxById(documentId) {
  const checkbox = document.querySelector(`#${documentId}`);
  if (checkbox) {
    checkbox.checked = false;
  }
}