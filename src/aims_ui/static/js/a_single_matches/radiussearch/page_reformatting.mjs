export function setupHorizontalInputs() {
  // Select all of the class ons-field inside the class of match-form-container
  const inputContainer = document.querySelector('.match-form-container');
  const fields = inputContainer.querySelectorAll('.ons-field');
  const buttons = inputContainer.querySelectorAll('.ons-btn');

  // Remove the 'br' elements
  const brElements = inputContainer.querySelectorAll('br');
  brElements.forEach(br => {
    br.remove();
  });

  // Create the container
  const horizontalContainer = document.createElement('div');
  horizontalContainer.id = 'horizontalContainer';

  fields.forEach(field => {
    horizontalContainer.appendChild(field);
  });

  // Group buttons
  const newButtonContainer = document.createElement('div');
  buttons.forEach(button => {
    newButtonContainer.appendChild(button);
  });
  horizontalContainer.appendChild(newButtonContainer);
  inputContainer.appendChild(horizontalContainer);

}
