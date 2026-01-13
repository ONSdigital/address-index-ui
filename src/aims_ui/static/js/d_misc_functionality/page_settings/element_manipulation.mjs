// Contain standard way to check checkboxes, select radio buttons etc.

export function checkRadioButton(radioElement) {
  if (radioElement) {
    radioElement.checked = true;
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