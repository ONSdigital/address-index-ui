import { getAllLinksAndParents, getNameOfJobFromCell } from './helpers.mjs';
import { downloadAndProcess } from './file_processing.mjs';
import { triggerDownloadOfFile } from "/static/js/f_helpers/download_helpers.mjs";

async function changeLinkToButton(linkParentHeaderRowCellObject) {

  // Make the Download Button
  const originalButton = document.querySelector('#downloadButtonTemplate');
  const clonedButton = originalButton.cloneNode(true);

  const cell = linkParentHeaderRowCellObject.parent;

  linkParentHeaderRowCellObject.parent.append(clonedButton);

  clonedButton.addEventListener('click', async function () {
    // Make ONS Button Spin Load
    clonedButton.classList.add('ons-is-loading');

    // Get header option status from the same row as link
    const headerStatus = linkParentHeaderRowCellObject.headerRowCell.textContent
      .trim()
      .replace(/\s+/g, ' ');

    // Get CSV content
    const csvContent = await downloadAndProcess(
      linkParentHeaderRowCellObject.link.href,
      headerStatus,
    );

    // Get the file name for the download
    const fileNameBase = getNameOfJobFromCell(
      cell,
      linkParentHeaderRowCellObject.link.textContent
    );
    const fileName = `${fileNameBase}.csv`;

    // Trigger download using shared helper function 
    triggerDownloadOfFile(fileName, 'csv', csvContent);

    // Remove the loading class as the download should now have triggered
    clonedButton.classList.remove('ons-is-loading');
  });
  linkParentHeaderRowCellObject.link.remove();
}

export async function setupResultsButtonAndProcessing() {
    // Change all links to "download" buttons
    const linksAndParents = getAllLinksAndParents();

    // Change each link to an ONS button and add listeners for managing downloads
    // Expect the links to be like: <a href="/downloads/googlefiledownload727">Download Job 727 Here</a>
    for (const linkParentHeaderRowCellObject of linksAndParents) {
       await changeLinkToButton(linkParentHeaderRowCellObject);
    }
}

