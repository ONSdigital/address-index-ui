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

export function checkCheckbox(documentId) {
  const checkbox = document.querySelector(`#${documentId}`);
  if (checkbox) {
    checkbox.checked = true;
  }
}

export function uncheckCheckbox(documentId) {
  const checkbox = document.querySelector(`#${documentId}`);
  if (checkbox) {
    checkbox.checked = false;
  }
}