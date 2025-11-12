import { getGlobalValues } from "/static/js/f_helpers/local_storage_page_helpers.mjs";
import { setupAttributesTable } from "/static/js/macros/custom_address_info_cards/favourite_table_generation.mjs";

// What do we need to know?
  // We want the "address info" object of the current address (uprn in url)
  // This will be in the GLOBAL "mostRecentlySearchedAddresses" 
  // Also need to update this so that it's "mostRecentlyShownAddresses"! 
      // so that if a page is revisited (like singlesearch) the most recent addresses are available for this page

  // Once we have the clientside address object the scripts for populating the
    // table already exist

  // We might want to do a check of the global "breadcrmbs" to see what the previous page was? 

  // There is also a situation where a user directly navigates to the page with a UPRN
     // we need to still be able to handle this - probably put the "save custom data" into this page too?
     // but then try not to rely on that data! 
  
  // Perhaps we could actually do with two different pages? Or even just incorperating 
   // the info into the original page?


   // Ok, the first thing we will do is generate it from an assumed existing local storage
   // global

//

function getAddressObjectFromUprn(uprn) {
  // Get the most recent addresses from local storage, default to blank array if undefined
  const globalValues = getGlobalValues();
  const mostRecentlySearchedAddresses = globalValues.mostRecentlySearchedAddresses || [];

  // Compare the string UPRNs
  for (const addressObject of mostRecentlySearchedAddresses) {
    if (String(addressObject.uprn) === String(uprn)) {
      return addressObject;
    }
  }
}

function init() {
  // Get the UPRN from the URL (http://127.0.0.1:5000/address_info/1)
  const urlParts = window.location.pathname.split('/');
  const uprn = urlParts[urlParts.length - 1];

  const addressObject = getAddressObjectFromUprn(uprn);
  const addressCardHtmlObjectAlternative = document.querySelector('.address-card-pseudo-class');
  const showAllAttributes = true;

  setupAttributesTable(addressCardHtmlObjectAlternative, addressObject, showAllAttributes);
}

init();