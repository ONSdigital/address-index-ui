// Contain standard way to check checkboxes, select radio buttons etc.

export function checkRadioButtonByElement(radioElement) {
  // Error if no element provided
  if (!radioElement) {
    console.error('No radio element provided. Received:', radioElement);
    return;
  }

  // Set to true if it exists
  radioElement.checked = true;
}

export function checkRadioButtonById(documentId) {
  const radioElement = document.querySelector(`#${documentId}`);

  if (!radioElement) {
    console.error('No radio element found with id:', documentId);
    return;
  }

  checkRadioButtonByElement(radioElement);
}

export function checkCheckboxByElement(checkboxElement) {
  // Error if no element provided
  if (!checkboxElement) {
    console.error('No checkbox element provided. Received:', checkboxElement);
    return;
  }

  // Set to true if it exists
  checkboxElement.checked = true;
}

export function checkCheckboxById(documentId) {
  const checkbox = document.querySelector(`#${documentId}`);

  if (!checkbox) {
    console.error('No checkbox element found with id:', documentId);
    return;
  }

  checkCheckboxByElement(checkbox);
}

export function uncheckCheckboxById(documentId) {
  const checkbox = document.querySelector(`#${documentId}`);

  if (!checkbox) {
    console.error('No checkbox element found with id:', documentId);
    return;
  }

  checkbox.checked = false;
}