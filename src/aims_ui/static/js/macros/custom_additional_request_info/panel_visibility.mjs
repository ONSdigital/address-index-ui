export function applyVisibilityOfRequestStatus(additionalRequestDetails) {

  // Check each detail - if any are true, make the panel visible 
  const settingsPanel = document.querySelector('#requestOverviewStatsPanel');
  if (!settingsPanel) {
    return;
  }

  let showPanel = false;

  for (const [key, value] of Object.entries(additionalRequestDetails)) {
    if (value === true) {
      showPanel = true;
      break;
    }
  }
  
  if (showPanel) { 
    settingsPanel.classList.remove('ons-u-hidden');
  }
}

