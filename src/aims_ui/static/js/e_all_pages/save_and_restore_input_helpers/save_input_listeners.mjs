import { getPagePreviouslySearchedValues,
 setPreviouslyStoredValuesForThisPage } from './set_and_get_data.mjs'


export function saveValueOfInput(inputId, inputValue, page_name) {
  console.debug(`Saving value of input ${inputId}: ${inputValue}`);

  // Firstly get the current pages previously stored input values
  // fallback to default values if none found
  const previouslyStoredValues = getPagePreviouslySearchedValues(page_name);

  // Now create a new object with the inputId and input value
  const valuesToMerge = {[inputId]: inputValue};

  // Now merge with the previously stored values
  const mergedValues = {...previouslyStoredValues, ...valuesToMerge};

  // Now save the new values
  setPreviouslyStoredValuesForThisPage(mergedValues, page_name);
}

