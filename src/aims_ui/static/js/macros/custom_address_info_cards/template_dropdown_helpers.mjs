import { crEl } from "/static/js/f_helpers/element_creation.mjs";

function addAddressInfoToDropdown(dropdownContainer, addressObject) {

  // Generate a table of all address info
  const infoTable = crEl('table');
  console.log(infoTable);
  for (const [key, value] of Object.entries(addressObject)) {
    const row = crEl('tr');
    const keyCell = crEl('td');
    keyCell.textContent = key;
    const valueCell = crEl('td');
    valueCell.textContent = value;
    row.appendChild(keyCell);
    row.appendChild(valueCell);
    infoTable.appendChild(row);
  }

  dropdownContainer.appendChild(infoTable);
}

export function addDropdownAllInfo(addressCardHtmlObject, addressObject) {
  // Get a handle on the dropdown area inside addressCardHtmlObject
  const dropdownContainer = addressCardHtmlObject.querySelector('.placeholder-for-dropdown-all-info-list');

  const newTitle = crEl('h2');
  newTitle.textContent = 'Click here for more info';


  dropdownContainer.append(newTitle);

  // Listener for click to console.log
  newTitle.addEventListener('click', () => {
    addAddressInfoToDropdown(dropdownContainer, addressObject);
  });

}