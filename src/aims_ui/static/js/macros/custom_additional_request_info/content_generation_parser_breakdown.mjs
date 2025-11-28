import { crEl } from '/static/js/f_helpers/element_creation.mjs';

export function getPanelContentForTokenisedOutput(responseAttributes) {
  // Given the response attributes, generate the content for tokenised output
  const tokenisedOutput = responseAttributes.tokenisedOutput || {};

  // Create a container for all of the tokenised output
  const tokenDetailsContainer = crEl('div', 'tokenised-output-container');
  const tokenTitle = crEl('em', 'tokenised-output-title');
  tokenTitle.textContent = 'Breakdown from Address Parser: ';
  tokenDetailsContainer.append(tokenTitle);

  // The tokenised output is an object with key-value pairs
  Object.entries(tokenisedOutput).forEach(([key, value]) => {
    const tokenKeyValue = crEl('p', '', 'tokenised-output-token-value');
    tokenKeyValue.textContent = `${key}: ${value}`;

    // Add the title and paragraph to the container
    tokenDetailsContainer.append(tokenKeyValue);
  });

  return tokenDetailsContainer;
}

