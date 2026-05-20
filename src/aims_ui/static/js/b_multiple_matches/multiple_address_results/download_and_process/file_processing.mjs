import { getAddressAttributesSelectedByUserFromMultipleAddressAttributesPage, 
  findIfPafOrNagWasUsed,
  returnNewlineIfNotBlank
} from './helpers.mjs';


function getAddressesFromResponse(apiResponse) {
  // Given an API response (string), extract a list of all matched addresses, confidence score, document score
  // Extract the list of matched addresses
  const customAttributesSelectedByUser = getAddressAttributesSelectedByUserFromMultipleAddressAttributesPage();
  const matchedAddresses = [];

  if (apiResponse.toString() === '') {
    return [];
  }

  const jsonResponse = JSON.parse(apiResponse);
  const response = jsonResponse['response'];
  const addresses = response['addresses'];

  // Get the values needed for each address (each address comes from one submitted address)
  let i = 0;
  for (const address of addresses) {
    i = i + 1;
    const formattedAddress = address['formattedAddress'];
    const uprn = address['uprn'];
    const matchType = response.matchtype;
    const confidenceScore = address['confidenceScore'];
    const documentScore = address['underlyingScore'];
    const rank = i;
    const addressTypePafNag = findIfPafOrNagWasUsed(address);
    const airRating = address['airRating'];

    const addressToAdd = [
      formattedAddress,
      uprn,
      matchType,
      confidenceScore,
      documentScore,
      rank,
      addressTypePafNag,
      airRating,
    ];

    const finalAddressToAdd = addCustomAttributesToResponse(address,customAttributesSelectedByUser,addressToAdd);
    matchedAddresses.push(finalAddressToAdd);
  }
  return matchedAddresses;
}

function addCustomAttributesToResponse(address,customAttributes,addressToAdd) {
    // add any custom attributes that have been selected
    if (customAttributes['classification_code'] == true) {
        addressToAdd.push(address['classificationCode']);
    }
    if (customAttributes['country_code'] == true) {
        addressToAdd.push(address['countryCode']);
    }
    if (customAttributes['easting'] == true) {
        addressToAdd.push(address['geo']['easting']);
    }
    if (customAttributes['northing'] == true) {
        addressToAdd.push(address['geo']['northing']);
    }
    if (customAttributes['latitude'] == true) {
        addressToAdd.push(address['geo']['latitude']);
    }
    if (customAttributes['longitude'] == true) {
        addressToAdd.push(address['geo']['longitude']);
    }
    if (customAttributes['parent_uprn'] == true) {
        addressToAdd.push(address['parentUprn']);
    }
    if (customAttributes['lpi_logical_status'] == true) {
        addressToAdd.push(address['lpiLogicalStatus']);
    }
    if (customAttributes['formatted_address_nag'] == true) {
        addressToAdd.push(address['formattedAddressNag']);
    }
    if (customAttributes['formatted_address_paf'] == true) {
        addressToAdd.push(address['formattedAddressPaf']);
    }
    if (customAttributes['welsh_formatted_address_nag'] == true) {
        addressToAdd.push(address['welshFormattedAddressNag']);
    }
    if (customAttributes['welsh_formatted_address_paf'] == true) {
        addressToAdd.push(address['welshFormattedAddressPaf']);
    }
    return addressToAdd;
}

function arrayToCSV(data) {
  const csvRows = data.map((row) =>
    row
      .map((cell) => {
        // Escape double quotes in CSV data
        const cellString = String(cell).replace(/"/g, '""');
        // Wrap values containing commas or double quotes in double quotes
        return /,|"/.test(cellString) ? `"${cellString}"` : cellString;
      })
      .join(',')
  );

  return csvRows.join('\r\n') + returnNewlineIfNotBlank(csvRows);
}

export function getFullHeaderRowIncludingCustomAttributes(headerStatus) {
  let extra_headers = '';

  if (headerStatus.toString() !== 'False') {
    const attributesSelectedByUser = getAddressAttributesSelectedByUserFromMultipleAddressAttributesPage();
    const customAttributeOrder = [
      'classification_code',
      'country_code',
      'easting',
      'northing',
      'latitude',
      'longitude',
      'parent_uprn',
      'lpi_logical_status',
      'formatted_address_nag',
      'formatted_address_paf',
      'welsh_formatted_address_nag',
      'welsh_formatted_address_paf',
    ];

    for (const key of customAttributeOrder) {
      if (attributesSelectedByUser[key] == true) {
        extra_headers = extra_headers + ',' + key;
      }
    }

    return 'id,inputAddress,matchedAddress,uprn,matchType,confidenceScore,documentScore,rank,addressType(Paf/Nag),airRating' + extra_headers + '\n';
  }

  return '';
}

export function processRow(row) {
  // Process [id, inputAddress, APIresponse]
  // to be in same format as <5k match

  // Check not blank or header row
  if (row.length !== 3) {
    return '';
  }
  if (row[2].toString() === 'response') {
    return '';
  }

  // Get info for a single row
  const id = row[0];
  const inputAddress = row[1];
  const matchedAddresses = getAddressesFromResponse(row[2]);

  // Expand (same id and input address for each matched address)
  const finalMatches = [];
  for (const matchedAddress of matchedAddresses) {
    // Add each address with quotes for csv parsing
    const final_row = [
      id,
      inputAddress
    ];

    matchedAddress.forEach(item => final_row.push(item));

    finalMatches.push(final_row);
  }

  // If 5 addresses match, finalMatches contains an array of 5 items, each containing [ id, search address, matched address, confidence score, document score, rank]
  const csvFormat = arrayToCSV(finalMatches);
  return csvFormat;
}

export async function downloadAndProcess(url, headerStatus) {
  // Get the attributes selected locally on the 'mutliple_address_attributes' page
  let final_csv = '';

  if (headerStatus.toString() !== 'False') {
    // Start the csv with header row
    final_csv = getFullHeaderRowIncludingCustomAttributes(headerStatus);
  }

  const response = await fetch(url);
  const arrayBuffer = await response.arrayBuffer();
  // eslint-disable-next-line no-undef
  const inflated = await pako.inflate(arrayBuffer);
  const csvString = new TextDecoder().decode(inflated);
  // eslint-disable-next-line no-undef
  const parsedCSV = Papa.parse(csvString).data;

  parsedCSV.forEach((row) => {
    // Row = [id, inputAddress, APIresponse]
    final_csv = final_csv + processRow(row);
  });

  return await final_csv;
}