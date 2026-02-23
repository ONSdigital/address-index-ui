
const isLoadingClassName = 'ons-is-loading';

export function setupLoadButtonInit() {
  const loadButton = document.querySelector('#downloadButtonMultipleMatch');

  // Prevent default
  loadButton.addEventListener('click', (event) => async function() {
    event.preventDefault();

    // Add the loading class name
    loadButton.classList.add(isLoadingClassName);

    // Submit a post request to this url when the button is clicked
    const response = await fetch('/downloads/small_multiple_match', {
        method: 'POST',
        body: new FormData(document.querySelector('form'))
    });

    // If the response is not ok, submit the entire form as normal to trigger the default errors
    if (!response.ok) {
      console.error('There was an error starting the download:', response);
      document.querySelector('form').submit();
      return;
    }
    
    // The response should be a file, so package it as a blob and create url
    const blob = await response.blob();
    const url = URL.createObjectURL(blob);

    // Create link and trigger download
    const a = document.createElement('a');
    a.href = url;
    a.download = 'file.csv';
    a.click();

    URL.revokeObjectURL(url);

    loadButton.classList.remove(isLoadingClassName);

  }
  ());
}