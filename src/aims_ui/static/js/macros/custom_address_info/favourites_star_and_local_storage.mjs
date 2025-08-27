function getName(row) {
  const firstCell = row.children[0]; 
  let text = firstCell.textContent.replace(/\s/g,'');
  text = text.replace('Explainme','');
  return text; 
}

function toggleFavourite(row, cell) {
  const favouriteStatus = getFavouriteStatus(row, cell);
  const favourites = getFavourites();
  const name = getName(row);
  if (favourites[name]) {
    favourites[name] = !favourites[name];
  } else {
    favourites[name] = true;
  }
  localStorage.setItem('favourites', JSON.stringify(favourites));
  setFavouriteStar(row, cell);
}

function getFavouriteStatus(row, cell) {
  const name = getName(row);
  const favourites = getFavourites();
  const favSetting = favourites[name];
  if (favSetting) {
    return true;
  } else {
    return false;
  }
}

function setFavouriteStar(row, cell) {
  if (getFavouriteStatus(row, cell)) {
      // Note innerHTML is just the worst and should be removed at some point
    cell.textContent = '★';
  } else {
    cell.textContent= '☆';
  }
}

function addFavouritesColumn() {
  for (const [i, row] of [...document.querySelectorAll('.clerical-data-table tr')].entries()) {
    const cell = document.createElement(i ? "td" : "th");

    cursorPointer(cell);
    setFavouriteStar(row, cell);
    cell.classList.add('ons-table__cell');
    cell.addEventListener('click', function(){toggleFavourite(row, cell)}, false);

    // Create custom event for changing other rows
    const event = new CustomEvent('update-star', {detail: cell, bubbles:true});
    cell.addEventListener('click', function(){ cell.dispatchEvent(event); }, false);
    document.addEventListener('update-star', function(){ setFavouriteStar(row,cell); } );
    
    row.appendChild(cell);
  };
}

function addAttribute(parent, attributeName, attributeValue) {
  const tr = document.createElement('tr');
  const attName = document.createElement('td');
  const attValue = document.createElement('td');
  attName.classList.add('mars', 'ons-table__cell');
  attValue.classList.add('venus', 'ons-table__cell');
  tr.append(attName, attValue);
  attName.textContent = attributeName;
  // Again, gross, but in this case we need HTML to be pasrsed!
  attValue.innerHTML= attributeValue;
  parent.append(tr);
}

function addFavouriteAttributes() {
  const trs = document.querySelectorAll('tbody');
  for (const tbl of trs) {
    const uprn = tbl.id;
    if ( addresses[uprn] ) {
      const currentAddress = addresses[uprn];
      // For each 'Favourated' attribute, add it!
      for ( const attribute_name in currentAddress ) {
        //console.log(attribute_name, currentAddress[attribute_name]);
        //console.val(uprn          , {value: '10023117623', favourite: true});
        const attLocalData = currentAddress[attribute_name];
        if (attLocalData.favourite) {
          addAttribute(tbl, attribute_name, attLocalData.value);
        }
      }
    }
  }
}

function cursorPointer(elm) {
  elm.style = ' cursor: pointer; ';
}

function addFavouritesToResults() {
  addFavouriteAttributes();
  addFavouritesColumn();
}

addFavouritesToResults();
