
const isLoadingClassName = 'ons-is-loading';

function removeLoadingClass(loadButton) {
  loadButton.classList.remove(isLoadingClassName);
}

function addLoadingClass(loadButton) {
  loadButton.classList.add(isLoadingClassName);
}

export function setupLoadButtonInit() {
  const loadButton = document.querySelector('#downloadButtonMultipleMatch');

  // Prevent default
  loadButton.addEventListener('click', (event) => async function() {
    event.preventDefault();

    // Add the loading class name
    addLoadingClass(loadButton);

    // Submit a post request to this url when the button is clicked
    const response = await fetch('/downloads/small_multiple_match', {
        method: 'POST',
        body: new FormData(document.querySelector('form'))
    });

    // Detect if it's a csv file or html
    const csvContentType = 'text/csv';
    const htmlContentType = 'text/html';

    const contentType = response.headers.get('content-type');
    console.log('Got the following content type from the submission of a multiple match file: "', contentType, '"');

    // If it's a csv content type, then trigger the download 
    if (contentType.includes(csvContentType)) {
      console.log('The content type indicates this is a csv file, so triggering the download of the file');

      // The response should be a file, so package it as a blob and create url
      const blob = await response.blob();
      const url = URL.createObjectURL(blob);

      // Create link and trigger download
      const a = document.createElement('a');
      a.href = url;
      a.download = 'file.csv';
      a.click();

      URL.revokeObjectURL(url);

      // Remove loading button animation
      removeLoadingClass(loadButton);
    } else if (contentType.includes(htmlContentType)) {
      console.log('The content type indicates this is an html file, so likely an error page, so navigating to the page');

      // If it's an html content type, then navigate to the page (likely an error page)
      const text = await response.text();
      document.open();
      document.write(text);
      document.close();
    } else {
      console.log('Received a content type that is not csv or html, so not sure how to handle this response. Content type:', contentType);
    }

  }
  ());
}