
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
