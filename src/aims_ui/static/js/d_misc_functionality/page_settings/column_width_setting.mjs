import {
  getGlobalValues,
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';

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
  if (columnWidthValues.space_col_1) { dropdownLeftPadding.value = columnWidthValues.space_col_1; }
  if (columnWidthValues.content_col_2) { dropdownLeftContent.value = columnWidthValues.content_col_2; }
  if (columnWidthValues.space_col_3) { dropdownMiddleGap.value = columnWidthValues.space_col_3; }
  if (columnWidthValues.content_col_4 ) { dropdownRightSideContent.value = columnWidthValues.content_col_4; }

  // Add listeners to change the global setting 
  dropdownLeftPadding.addEventListener('change', () => {
    const newValue = dropdownLeftPadding.value;
    const updatedColumnWidths = { ...getGlobalValues().columnWidths, space_col_1: newValue };
    setGlobalValues({ columnWidths: updatedColumnWidths });
  });

  dropdownLeftContent.addEventListener('change', () => {
    const newValue = dropdownLeftContent.value;
    const updatedColumnWidths = { ...getGlobalValues().columnWidths, content_col_2: newValue };
    setGlobalValues({ columnWidths: updatedColumnWidths });
  });

  dropdownMiddleGap.addEventListener('change', () => {
    const newValue = dropdownMiddleGap.value;
    const updatedColumnWidths = { ...getGlobalValues().columnWidths, space_col_3: newValue };
    setGlobalValues({ columnWidths: updatedColumnWidths });
  });

  dropdownRightSideContent.addEventListener('change', () => {
    const newValue = dropdownRightSideContent.value;
    const updatedColumnWidths = { ...getGlobalValues().columnWidths, content_col_4: newValue };
    setGlobalValues({ columnWidths: updatedColumnWidths });
  });
  
}