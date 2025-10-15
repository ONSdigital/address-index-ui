export function restoreConfidenceScoreAndUnderlyingScore(mostRecentlySearchedAddresses) {
  // Get the confidence score to put in the table
  const currentAddress = getCurrentAddress(mostRecentlySearchedAddresses);
  const confidenceScore = currentAddress.confidenceScore;
  const underlyingScore = currentAddress.underlyingScore;

  updateOverviewTableFormattedConfidenceScore(confidenceScore);
  updateClericalDataTableWithFormattedConfidenceScoreAndUnderlyingScore(confidenceScore, underlyingScore);

};

function getCurrentUprn() {
  // Get the UPRN from the URL (... /address_info/1234567890123)
  const urlParts = window.location.pathname.split('/');
  const uprn = urlParts[urlParts.length - 1];

  return uprn;
}

// Get the address json for the UPRN in the URL
function getCurrentAddress(mostRecentlySearchedAddresses) {
  const uprn = getCurrentUprn();

  for (const address of mostRecentlySearchedAddresses) {
    if (String(address.uprn) === String(uprn)) {
      return address;
    } 
  }
}

function updateOverviewTableFormattedConfidenceScore(confidenceScore) {
  // Get a handle on the overview table
  const overviewTable = document.querySelector('#overviewTable');

  const confidenceScoreLabelCell = getCellFromTable(overviewTable, 'formatted_confidence_score');
  const confidenceScoreValueCell = confidenceScoreLabelCell.nextElementSibling;

  const newConScoreValue = Math.round(confidenceScore * 100) / 100
  confidenceScoreValueCell.textContent = String(newConScoreValue) + '% Match';
}

function updateClericalDataTableWithFormattedConfidenceScoreAndUnderlyingScore(confidenceScore, underlyingScore) {
  // Populate the "Clerical Data" table for confidence and underlying score
  const clericalDataTable = document.querySelector('#clerical-data-table');

  const confidenceScoreValueCellClericalData = getCellFromTable(clericalDataTable, 'confidence_score');
  const underlyingScoreValueCellClericalData = getCellFromTable(clericalDataTable, 'underlying_score');

  // Get parent Rows
  const conScoreClericalData          = confidenceScoreValueCellClericalData.parentNode; 
  const underlyingScoreClericalData   = underlyingScoreValueCellClericalData.parentNode; 

  const conScoreClericalDataCell        = getSecondCell(conScoreClericalData);
  const underlyingScoreClericalDataCell = getSecondCell(underlyingScoreClericalData);

  // Replace the cells with the text provided
  conScoreClericalDataCell.textContent = confidenceScore;
  underlyingScoreClericalDataCell.textContent = underlyingScore;
}

function getCellFromTable(table, rowText) {
  const rows = table.getElementsByTagName('tr');
  for (let i = 0; i < rows.length; i++) {
    const cells = rows[i].getElementsByTagName('td');
    for (let j = 0; j < cells.length; j++) {
      if ( String(cells[j].textContent).includes(rowText) ) {
        return cells[j];
      }
    }
  }
  return null;
}

function getSecondCell(row) {
  const cells = row.querySelectorAll('td');
  if (cells.length >= 2) {
    return cells[1];
  } else {
    return null;
  }
}