import { getPopulatedAttributeMap } from "../f_helpers/address_attribute_map.mjs";

export function setupDownloadAttributesLink() {
  // The data structure won't require mapped attributes, so just use label tex and descriptions
  const addressMap = getPopulatedAttributeMap({});

  // Create array of "attribute: description" strings
  const attributeDescriptionPairs = [];
  for (const attribute of addressMap) {
    const labelText = attribute.labelText;
    const description = attribute.description || 'No description available';
    attributeDescriptionPairs.push(`${labelText}: ${description}`);
  }

  // Convert to a string with newline after each pair
  const fileContent = attributeDescriptionPairs.join('\n\n');

  // Create a blob and a download link
  const blob = new Blob([fileContent], { type: 'text/plain' });
  const url = URL.createObjectURL(blob);

  const downloadLink = document.querySelector('#link-download-attributes');
  downloadLink.href = url;
  downloadLink.download = 'address_attributes.txt';
}
