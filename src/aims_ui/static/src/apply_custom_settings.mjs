import { getAddressTitlePrefference } from './local_storage_helpers.mjs';


console.log(getAddressTitlePrefference());






function init() {
  const prefference = getAddressTitlePrefference();

}

window.addEventListener('load', init);


