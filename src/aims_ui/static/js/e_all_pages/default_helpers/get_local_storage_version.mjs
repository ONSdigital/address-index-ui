// Visiting the /info endpoint will return a JSON object: {"ENV":"development","LOCAL_STORAGE_VERSION":"1","PLATFORM":null,"VERSION":"1.4.71"}

export async function getBroadcastLocalStorageVersion() {
  // Using requests api
  return fetch('/info')
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Network response was not ok: ${response.statusText}`);
      }
      return response.json();
    })
    .then((data) => {
      return data.LOCAL_STORAGE_VERSION || null;
    });
}