// Contain standard way to check checkboxes, select radio buttons etc.

export function checkRadioButton(documentId) {
  const radioButton = document.querySelector(`#${documentId}`);
  if (radioButton) {
    radioButton.checked = true;
  }
}