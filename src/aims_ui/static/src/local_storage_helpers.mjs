
export function updateAddressFormatPrefference(pafOrNag){
  localStorage.setItem('custom_settings_address_prefference', pafOrNag);
}

export function getAddressTitlePrefference(){
  return localStorage.getItem('custom_settings_address_prefference');
}

export function setDefaultTitleChoice() {
  if (! localStorage.getItem('custom_settings_address_prefference')) {
    localStorage.setItem('custom_settings_address_prefference', 'def');
  }
}

export function getCustomColumnWidths() {
  const obj = localStorage.getItem('custom_column_width');
  return JSON.parse(obj)
}

export function setDefaultColumnWidths() {
  // Default widths of columns for the interface
  if (! localStorage.getItem('custom_column_width')) {
    const defaultValues = 
      JSON.stringify({
      'space_col_1':   1,
      'content_col_2': 4,
      'space_col_3':   1,
      'content_col_4': 5,
    });
    localStorage.setItem('custom_column_width', defaultValues);
  }
}

export function setNewColumnWidths(values) {
  const newValues = JSON.stringify(values);
  localStorage.setItem('custom_column_width', newValues);
}