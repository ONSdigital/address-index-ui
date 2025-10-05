
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

// This function will need updating when all values go through the "Global" local storage attribute
function getConfidenceList() {
  const defaultConfidence = [];
  const confidenceScores = localStorage.getItem('confidenceScores');
  if (confidenceScores) {
    return JSON.parse(confidenceScores);
  } else {
    localStorage.setItem('confidenceScores', JSON.stringify(defaultConfidence));
  return [];
  }
}

export function replaceOverviewTableConfidenceScoreValues() {
  const overviewTable = document.querySelector('#overviewTable');

  const confidenceScoreLabelCell = getCellFromTable(overviewTable, 'formatted_confidence_score');
  const confidenceScoreValueCell = confidenceScoreLabelCell.nextElementSibling;

  const uprnCellLabel = getCellFromTable(overviewTable, 'uprn');
  const uprnRow = uprnCellLabel.parentNode;
  const uprnCell = getSecondCell(uprnRow);
  const uprn = uprnCell.textContent;

  // Populate the "Important information" overview table 
  const confidenceList = getConfidenceList();
  for (const score of confidenceList) {
    if (String(score.uprn) === String(uprn)) {
      const newConScoreValue = Math.round(score.confidenceScore * 100) / 100
      confidenceScoreValueCell.textContent = String(newConScoreValue) + '% Match';
    }
  }

  // Populate the "Clerical Data" table for confidence and underlying score
  const clericalDataTable = document.querySelector('#clerical-data-table');

  const confidenceScoreValueCellClericalData = getCellFromTable(clericalDataTable, 'confidence_score');
  const underlyingScoreValueCellClericalData = getCellFromTable(clericalDataTable, 'underlying_score');

  // Get parent Rows
  const conScoreClericalData          = confidenceScoreValueCellClericalData.parentNode; 
  const underlyingScoreClericalData   = underlyingScoreValueCellClericalData.parentNode; 

  const conScoreClericalDataCell        = getSecondCell(conScoreClericalData);
  const underlyingScoreClericalDataCell = getSecondCell(underlyingScoreClericalData);

  for (const score of confidenceList) {
    if (String(score.uprn) === String(uprn)) {
      conScoreClericalDataCell.textContent = score.confidenceScore;
      underlyingScoreClericalDataCell.textContent = score.underlyingScore;
    }
  }

};

