import { getAllLinksAndParents, getNameOfJobFromCell } from './helpers.mjs';
import { downloadAndProcess } from './file_processing.mjs';

async function changeLinkToButton(linkParentHeaderRowCellObject) {
  // Make the Download Button
  const originalButton = document.querySelector('#downloadButtonTemplate');
  const clonedButton = originalButton.cloneNode(true);

  const cell = linkParentHeaderRowCellObject.parent;

  linkParentHeaderRowCellObject.parent.append(clonedButton);

  clonedButton.addEventListener('click', async function () {
    // Make Spin Load
    clonedButton.classList.add('ons-is-loading');

    // Get header option status from the same row as link
    const headerStatus = linkParentHeaderRowCellObject.headerRowCell.textContent
      .trim()
      .replace(/\s+/g, ' ');

    // Get CSV content
    const csv = await downloadAndProcess(
      linkParentHeaderRowCellObject.link.href,
      headerStatus,
    );

    // Make a new blob
    const blob = new Blob([csv], { type: 'text/csv' });

    // Make 'a' with link to finalised csv content, then download
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    const fileName = getNameOfJobFromCell(
      cell,
      linkParentHeaderRowCellObject.link.textContent
    );
    a.download = fileName + '.csv';
    a.click();
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

