import { crEl } from "/static/js/f_helpers/element_creation.mjs";
import { getPageLocalValues } from '/static/js/f_helpers/local_storage_page_helpers.mjs';

function addAddressInfoToDropdown(dropdownContainer, addressObject) {
  // Generate a table of all address info
  const infoTable = crEl('table');
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

export function addDropdownAllInfo(addressCardHtmlObject, addressObject, page_name) {
  // Get a handle on the dropdown area inside addressCardHtmlObject
  const dropdownContainer = addressCardHtmlObject.querySelector('.placeholder-for-dropdown-all-info-list');

  const newTitle = crEl('h2');
  newTitle.textContent = 'Click here for more info';


  dropdownContainer.append(newTitle);

  addAddressInfoToDropdown(dropdownContainer, addressObject);
  // Listener for click to console.log
  newTitle.addEventListener('click', () => {
  });

}