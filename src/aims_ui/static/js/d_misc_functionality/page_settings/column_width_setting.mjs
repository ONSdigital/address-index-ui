import {
  getGlobalValues,
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';
import { checkCheckbox } from '/static/js/d_misc_functionality/page_settings/element_manipulation.mjs';

// Setup listeners, handlers and startup for column width setting

export function setupColumnWidthSetting() {
  // Get the value of the current global column width object
  const globalValues = getGlobalValues();
  const columnWidthValues = globalValues.columnWidths || {};

  // Get a handle on each dropdown
  const dropdownLeftPaddingId = 'column-width-left-padding-selector';
  const dropdownLeftContentId = 'column-width-left-content-selector';
  const dropdownMiddleGapId = 'column-width-middle-gap-selector';
  const dropdownRightSideContentId = 'column-width-right-side-content-selector';

  // Get a handle on each selector
  const dropdownLeftPadding = document.querySelector(`#${dropdownLeftPaddingId}`);
  const dropdownLeftContent = document.querySelector(`#${dropdownLeftContentId}`);
  const dropdownMiddleGap = document.querySelector(`#${dropdownMiddleGapId}`);
  const dropdownRightSideContent = document.querySelector(`#${dropdownRightSideContentId}`);

  // Set each dropdown to the current value
  if (columnWidthValues.leftPadding) { dropdownLeftPadding.value = columnWidthValues.leftPadding; }
  if (columnWidthValues.leftContent) { dropdownLeftContent.value = columnWidthValues.leftContent; }
  if (columnWidthValues.rightContent) { dropdownMiddleGap.value = columnWidthValues.rightContent; }
  if (columnWidthValues.rightPadding) { dropdownRightSideContent.value = columnWidthValues.rightPadding; }

  // Add listeners to change the global setting 
  dropdownLeftPadding.addEventListener('change', () => {
    const newValue = dropdownLeftPadding.value;
    const updatedColumnWidths = { ...getGlobalValues().columnWidths, leftPadding: newValue };
    setGlobalValues({ columnWidths: updatedColumnWidths });
  });

  dropdownLeftContent.addEventListener('change', () => {
    const newValue = dropdownLeftContent.value;
    const updatedColumnWidths = { ...getGlobalValues().columnWidths, leftContent: newValue };
    setGlobalValues({ columnWidths: updatedColumnWidths });
  });

  dropdownMiddleGap.addEventListener('change', () => {
    const newValue = dropdownMiddleGap.value;
    const updatedColumnWidths = { ...getGlobalValues().columnWidths, rightContent: newValue };
    setGlobalValues({ columnWidths: updatedColumnWidths });
  });

  dropdownRightSideContent.addEventListener('change', () => {
    const newValue = dropdownRightSideContent.value;
    const updatedColumnWidths = { ...getGlobalValues().columnWidths, rightPadding: newValue };
    setGlobalValues({ columnWidths: updatedColumnWidths });
  });
  
}