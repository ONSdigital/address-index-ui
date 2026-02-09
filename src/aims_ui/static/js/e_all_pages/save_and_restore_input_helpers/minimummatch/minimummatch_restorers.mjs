
export function restoreDropdownValueIfExists(page_name, id, pagePreviouslySearchedValues) {
  // Check to see if this id has a previously stored value

  const storedValue = pagePreviouslySearchedValues['matchthreshold'];
  console.debug('Restoring dropdown value for', id, 'with stored value:', storedValue);

  if (storedValue) {
    const dropdownContainer = document.querySelector('#complete-container-for-matchthreshold');
    const dropdownInput = dropdownContainer.querySelector('select');
    if (dropdownInput) {
      dropdownInput.value = storedValue;
    }
  }

}