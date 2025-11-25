// Generate the favrouties table for each card overview
import { setGlobalValues, getFavouritesFromLocalStorage } from '/static/js/f_helpers/local_storage_page_helpers.mjs';
import { getPopulatedAttributeMap } from '/static/js/f_helpers/address_attribute_map.mjs';

const keysToShow = getFavouritesFromLocalStorage();

export function addOrRemoveAttributeFromFavourites(cellIdNameOfAttribute) {
  // Get the current favourites from local storage
  const currentFavourites = getFavouritesFromLocalStorage();

  let updatedFavourites = [];
  if (currentFavourites.includes(cellIdNameOfAttribute)) {
    updatedFavourites = currentFavourites.filter(item => item !== cellIdNameOfAttribute);
  } else {
    updatedFavourites = [...currentFavourites, cellIdNameOfAttribute];
  }

  // Save back to local storage
  setGlobalValues( { favouriteAddressAttributes: updatedFavourites } );
}

function getFavouriteStatusOfAttribute(valuePair) {
  // Given a value object, return 'true' or 'false' if it is a favourite
  // Use the initially obtained keysToShow array
  for (const favouriteKey of keysToShow) {
    if (favouriteKey === valuePair.cellId) {
      return true;
    }
  }
  return false;
}

function generateRowFromTemplate(rowClone, valuePair) {
  // Remove the "rowClone" id to avoid duplicates
  rowClone.removeAttribute('id');

  // Get handles on the name and value cells and favourite checkbox
  const nameCell = rowClone.querySelector('.attribute-name-placeholder');
  const valueCell = rowClone.querySelector('.attribute-value-placeholder');
  const favouriteCheckbox = rowClone.querySelector('.favourite-checkbox');

  // Add the class to each row for styling and handles
  valueCell.classList.add(`attribute-value-${valuePair.cellId}`);
  nameCell.classList.add(`attribute-name-${valuePair.cellId}`);
  favouriteCheckbox.classList.add(`favourite-checkbox-${valuePair.cellId}`);

  // Set the name and value for each row
  nameCell.textContent = valuePair.labelText;
  valueCell.textContent = valuePair.value || '';

  // If the HTML attribute 'checked' is present, the checkbox is ticked
  const favouriteStatus = getFavouriteStatusOfAttribute(valuePair);
  if (favouriteStatus) {
    favouriteCheckbox.setAttribute('checked', 'true');
  }

  // Add an event listener to the checkbox to handle adding/removing from favourites
  favouriteCheckbox.addEventListener('change', () => {
    addOrRemoveAttributeFromFavourites(valuePair.cellId);
  });

  // Add a tooltip for the cell name containing a description if available
  if (valuePair.description) {
    addTooltipToCell(nameCell, valuePair.description);
  }

  // Add an "explain me" link if a helpLink is available
  if (valuePair.helpLink) {
    addHelpLinkToCell(nameCell, valuePair);
  }

  return rowClone;
}

function addTooltipToCell(nameCell, descriptionText) {
  // Add the tooltip itself
  nameCell.setAttribute('title', descriptionText);

  // Add a class that changes cursor to pointer
  nameCell.classList.add('cursor-pointer');
}

function addHelpLinkToCell(nameCell, valuePair) {
  // Create link container
  const linkContainer = document.createElement('div');

  // Create the link element
  const helpLink= document.createElement('a');
  helpLink.textContent = 'Explain Me';
  helpLink.href = valuePair.helpLink;

  // Add the link to the container, the container to the cell
  linkContainer.append(helpLink);
  nameCell.append(linkContainer);
}

function getAllPairsToShow(populatedAttributeMap, showAllAttributes) {
  // Given a populated favourite, value array, return all of them or just favourites
  if (showAllAttributes) { return populatedAttributeMap; }

  return populatedAttributeMap.filter(item => keysToShow.includes(item.cellId));
}

export function setupAttributesTable(addressCardHtmlObject, addressObject, showAllAttributes=false) {
  // Get a handle on the table body
  const tableBody = addressCardHtmlObject.querySelector('#table-body-for-address-attributes');

  // Copy the example row 
  const exampleRow = addressCardHtmlObject.querySelector('#example-table-row');

  // Return { cellId: , value: labelText: } mapped object
  const populatedAttributeMap = getPopulatedAttributeMap(addressObject);

  // Filter the full info map to EITHER all attributes or just favourites
  const allPairsToShow = getAllPairsToShow(populatedAttributeMap, showAllAttributes);

  for (const valuePair of allPairsToShow) {
    // Clone the example row
    const rowClone = exampleRow.cloneNode(true);

    // Generate a new row from the template
    const newRow = generateRowFromTemplate(rowClone, valuePair);

    // Add the row to the table
    tableBody.append(newRow);
  }

  // Remove the example row
  exampleRow.remove();
}