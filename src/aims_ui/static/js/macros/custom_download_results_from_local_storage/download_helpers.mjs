
// Helper to trigger the download of a file, given the type, content and name
export function triggerDownloadOfFile(fileName, fileType, fileContent) {
  // Create CSV Blob and trigger download
  const blob = new Blob([fileContent], { type: `text/${fileType};charset=utf-8;` });
  const url = URL.createObjectURL(blob);

  const link = document.createElement('a');
  link.href = url;
  link.setAttribute('download', fileName);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);

  // Cleanup URL object
  URL.revokeObjectURL(url);
}