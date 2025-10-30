// Remove the link from the default ons-card element

function init() {
  // Get the container
  const cardContainer = document.querySelector('#title-and-description-for-page-in-card-container');

  if (!cardContainer) {
    console.warn('Card container not found');
    return;
  }

  // Find the <a> element inside the container
  const link = cardContainer.querySelector('a.ons-card__link');

  if (link) {
    // Clone the h2 element inside the <a>
    const h2 = link.querySelector('h2');
    if (h2) {
      // Move the <h2> out of the <a> and insert it before <a>
      link.parentNode.insertBefore(h2, link);
    }

    // Remove the <a> element
    link.remove();
  } else {
    console.warn('Link element not found inside card container');
  }
}

init();