import { setSizeOfPostBodyTextBoxFromLocalStorage, showResponseAsObject, showResponseAsText, setGetPostTextboxVisibilityBasedOnDropdown, makePostTextBodyHidden, makePostTextBodyVisible, setTextObjectBasedOnRadioButtons } from './visibility_change.mjs';
import { saveValueOfInput } from '../../e_all_pages/save_and_restore_input_helpers/save_input_listeners.mjs';


function setupSizeOfPostBodyTextBoxObserver() {
  const postRequestTextBox = document.querySelector('#request-body-text-area');
  // Save the size of the body element
  const callback = function (mutationsList, observer) {
    for (let mutation of mutationsList) {
      if (
        mutation.type === 'attributes' &&
        mutation.attributeName === 'style'
      ) {
        const newStyle = postRequestTextBox.getAttribute('style');
        saveValueOfInput('post-request-body-style', newStyle, 'custom_response');
      }
    }
  };

  const observer = new MutationObserver(callback);
  const config = { attributes: true, attributeFilter: ['style'] };
  observer.observe(postRequestTextBox, config);
}

function setupTextObjectResponse(radioText, radioObj) {
  // Setup showing the user the Text or Object response including errors based on radio button selction

  // Setup the response when the radioText is selected
  radioText.addEventListener('change', () => {
    showResponseAsText();
  });

  // Setup the response when the radioObj is selected
  radioObj.addEventListener('change', () => {
    showResponseAsObject();
  });

}

function setupGetPostDropdownBehaviour(selectHtmlObject) {
  // When the dropdown option is set to POST, show the body textbox
  // When the dropdown option is set to GET, hide the body textbox

  selectHtmlObject.addEventListener('change', (e) => {
    // Use the event target value to determine if POST/GET
    const postOrGet = e.target.value;
    if (postOrGet === 'POST') {
      makePostTextBodyVisible();
    } else if (postOrGet === 'GET') {
      makePostTextBodyHidden();
    }
  });

  // Add a listener for the 'clear' button to refresh the visiblity
  document.addEventListener('refreshInputFiltersFromLocalStorage', (e) => {
    setGetPostTextboxVisibilityBasedOnDropdown(selectHtmlObject);
  });
}


function init() {
  // Get a handle on the GET/POST dropdown
  const containerForDropdown = document.querySelector('#complete-container-for-request-type');
  const selectHtmlObject = containerForDropdown.querySelector('select');

  // Get a handle on the radio buttons
  const radioText = document.querySelector('#response-type-text');
  const radioObj = document.querySelector('#response-type-object');

  // Setup the GET/POST dropdown behaviour to hide/show the body textbox
  setupGetPostDropdownBehaviour(selectHtmlObject);
  // Setup the initial visibility of the POST body textbox
  setGetPostTextboxVisibilityBasedOnDropdown(selectHtmlObject);

  // Setup the text/object radio button functionality
  setupTextObjectResponse(radioText, radioObj);
  // Setup the initial response style based on current radio button selection
  setTextObjectBasedOnRadioButtons();

  // Set initial size of POST body
  setSizeOfPostBodyTextBoxFromLocalStorage();

  // Add mutation observer to request body to save size changes
  setupSizeOfPostBodyTextBoxObserver();
}

window.addEventListener('load', init);
