def return_expected_csv_content_as_json():

  expected_file_content_as_json = [{
      'Concatenated': 'C',
      'Class_Desc': 'Commercial',
      'Primary_Code': 'C',
      'Secondary_Code': '',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': '',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CA',
      'Class_Desc': 'Agricultural',
      'Primary_Code': 'C',
      'Secondary_Code': 'A',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Agricultural',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CA01',
      'Class_Desc': 'Farm / Non-Residential Associated Building',
      'Primary_Code': 'C',
      'Secondary_Code': 'A',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Agricultural',
      'Tertiary_Desc': 'Farm / Non-Residential Associated Building',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CA02',
      'Class_Desc': 'Fishery',
      'Primary_Code': 'C',
      'Secondary_Code': 'A',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Agricultural',
      'Tertiary_Desc': 'Fishery',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CA02FF',
      'Class_Desc': 'Fish Farming',
      'Primary_Code': 'C',
      'Secondary_Code': 'A',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'FF',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Agricultural',
      'Tertiary_Desc': 'Fishery',
      'Quaternary_Desc': 'Fish Farming'
  }, {
      'Concatenated': 'CA02FH',
      'Class_Desc': 'Fish Hatchery',
      'Primary_Code': 'C',
      'Secondary_Code': 'A',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'FH',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Agricultural',
      'Tertiary_Desc': 'Fishery',
      'Quaternary_Desc': 'Fish Hatchery'
  }, {
      'Concatenated': 'CA02FP',
      'Class_Desc': 'Fish Processing',
      'Primary_Code': 'C',
      'Secondary_Code': 'A',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'FP',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Agricultural',
      'Tertiary_Desc': 'Fishery',
      'Quaternary_Desc': 'Fish Processing'
  }, {
      'Concatenated': 'CA02OY',
      'Class_Desc': 'Oyster / Mussel Bed',
      'Primary_Code': 'C',
      'Secondary_Code': 'A',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'OY',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Agricultural',
      'Tertiary_Desc': 'Fishery',
      'Quaternary_Desc': 'Oyster / Mussel Bed'
  }, {
      'Concatenated': 'CA03',
      'Class_Desc': 'Horticulture',
      'Primary_Code': 'C',
      'Secondary_Code': 'A',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Agricultural',
      'Tertiary_Desc': 'Horticulture',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CA03SH',
      'Class_Desc': 'Smallholding',
      'Primary_Code': 'C',
      'Secondary_Code': 'A',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'SH',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Agricultural',
      'Tertiary_Desc': 'Horticulture',
      'Quaternary_Desc': 'Smallholding'
  }, {
      'Concatenated': 'CA03VY',
      'Class_Desc': 'Vineyard',
      'Primary_Code': 'C',
      'Secondary_Code': 'A',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'VY',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Agricultural',
      'Tertiary_Desc': 'Horticulture',
      'Quaternary_Desc': 'Vineyard'
  }, {
      'Concatenated': 'CA03WB',
      'Class_Desc': 'Watercress Bed',
      'Primary_Code': 'C',
      'Secondary_Code': 'A',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'WB',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Agricultural',
      'Tertiary_Desc': 'Horticulture',
      'Quaternary_Desc': 'Watercress Bed'
  }, {
      'Concatenated': 'CA04',
      'Class_Desc': 'Slaughter House / Abattoir',
      'Primary_Code': 'C',
      'Secondary_Code': 'A',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Agricultural',
      'Tertiary_Desc': 'Slaughter House / Abattoir',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CB',
      'Class_Desc': 'Ancillary Building',
      'Primary_Code': 'C',
      'Secondary_Code': 'B',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Ancillary Building',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CC',
      'Class_Desc': 'Community Services',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CC02',
      'Class_Desc': 'Law Court',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': 'Law Court',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CC03',
      'Class_Desc': 'Prison',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': 'Prison',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CC03HD',
      'Class_Desc': 'HM Detention Centre',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'HD',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': 'Prison',
      'Quaternary_Desc': 'HM Detention Centre'
  }, {
      'Concatenated': 'CC03PR',
      'Class_Desc': 'HM Prison Service',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'PR',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': 'Prison',
      'Quaternary_Desc': 'HM Prison Service'
  }, {
      'Concatenated':
      'CC03SC',
      'Class_Desc':
      'Secure Residential Accommodation',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'C',
      'Tertiary_Code':
      '3',
      'Quaternary_Code':
      'SC',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Community Services',
      'Tertiary_Desc':
      'Prison',
      'Quaternary_Desc':
      'Secure Residential Accommodation'
  }, {
      'Concatenated': 'CC04',
      'Class_Desc': 'Public / Village Hall / Other Community Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': 'Public / Village Hall / Other Community Facility',
      'Quaternary_Desc': ''
  }, {
      'Concatenated':
      'CC04YR',
      'Class_Desc':
      'Youth Recreational / Social Club',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'C',
      'Tertiary_Code':
      '4',
      'Quaternary_Code':
      'YR',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Community Services',
      'Tertiary_Desc':
      'Public / Village Hall / Other Community Facility',
      'Quaternary_Desc':
      'Youth Recreational / Social Club'
  }, {
      'Concatenated': 'CC05',
      'Class_Desc': 'Public Convenience',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '5',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': 'Public Convenience',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CC06',
      'Class_Desc': 'Cemetery / Crematorium / Graveyard. In Current Use.',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '6',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': 'Cemetery / Crematorium / Graveyard. In Current Use.',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CC06CB',
      'Class_Desc': 'Columbarium',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'CB',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': 'Cemetery / Crematorium / Graveyard. In Current Use.',
      'Quaternary_Desc': 'Columbarium'
  }, {
      'Concatenated': 'CC06CN',
      'Class_Desc': 'Crematorium',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'CN',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': 'Cemetery / Crematorium / Graveyard. In Current Use.',
      'Quaternary_Desc': 'Crematorium'
  }, {
      'Concatenated': 'CC06CR',
      'Class_Desc': 'Chapel Of Rest',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'CR',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': 'Cemetery / Crematorium / Graveyard. In Current Use.',
      'Quaternary_Desc': 'Chapel Of Rest'
  }, {
      'Concatenated': 'CC06CY',
      'Class_Desc': 'Cemetery',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'CY',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': 'Cemetery / Crematorium / Graveyard. In Current Use.',
      'Quaternary_Desc': 'Cemetery'
  }, {
      'Concatenated': 'CC06MC',
      'Class_Desc': 'Military Cemetery',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'MC',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': 'Cemetery / Crematorium / Graveyard. In Current Use.',
      'Quaternary_Desc': 'Military Cemetery'
  }, {
      'Concatenated': 'CC06MY',
      'Class_Desc': 'Mortuary',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'MY',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': 'Cemetery / Crematorium / Graveyard. In Current Use.',
      'Quaternary_Desc': 'Mortuary'
  }, {
      'Concatenated': 'CC07',
      'Class_Desc': 'Church Hall / Religious Meeting Place / Hall',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '7',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': 'Church Hall / Religious Meeting Place / Hall',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CC08',
      'Class_Desc': 'Community Service Centre / Office',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '8',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': 'Community Service Centre / Office',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CC09',
      'Class_Desc': 'Public Household Waste Recycling Centre (HWRC)',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '9',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': 'Public Household Waste Recycling Centre (HWRC)',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CC10',
      'Class_Desc': 'Recycling Site',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '10',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': 'Recycling Site',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CC11',
      'Class_Desc': 'CCTV',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '11',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': 'CCTV',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CC12',
      'Class_Desc': 'Job Centre',
      'Primary_Code': 'C',
      'Secondary_Code': 'C',
      'Tertiary_Code': '12',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Community Services',
      'Tertiary_Desc': 'Job Centre',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CE',
      'Class_Desc': 'Education',
      'Primary_Code': 'C',
      'Secondary_Code': 'E',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Education',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CE01',
      'Class_Desc': 'College',
      'Primary_Code': 'C',
      'Secondary_Code': 'E',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Education',
      'Tertiary_Desc': 'College',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CE01FE',
      'Class_Desc': 'Further Education',
      'Primary_Code': 'C',
      'Secondary_Code': 'E',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'FE',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Education',
      'Tertiary_Desc': 'College',
      'Quaternary_Desc': 'Further Education'
  }, {
      'Concatenated': 'CE01HE',
      'Class_Desc': 'Higher Education',
      'Primary_Code': 'C',
      'Secondary_Code': 'E',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'HE',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Education',
      'Tertiary_Desc': 'College',
      'Quaternary_Desc': 'Higher Education'
  }, {
      'Concatenated': 'CE02',
      'Class_Desc': 'Children’s Nursery / Crèche',
      'Primary_Code': 'C',
      'Secondary_Code': 'E',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Education',
      'Tertiary_Desc': 'Children’s Nursery / Crèche',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CE03',
      'Class_Desc':
      'Preparatory / First / Primary / Infant / Junior / Middle School',
      'Primary_Code': 'C',
      'Secondary_Code': 'E',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Education',
      'Tertiary_Desc':
      'Preparatory / First / Primary / Infant / Junior / Middle School',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CE03FS',
      'Class_Desc': 'First School',
      'Primary_Code': 'C',
      'Secondary_Code': 'E',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'FS',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Education',
      'Tertiary_Desc':
      'Preparatory / First / Primary / Infant / Junior / Middle School',
      'Quaternary_Desc': 'First School'
  }, {
      'Concatenated': 'CE03IS',
      'Class_Desc': 'Infant School',
      'Primary_Code': 'C',
      'Secondary_Code': 'E',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'IS',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Education',
      'Tertiary_Desc':
      'Preparatory / First / Primary / Infant / Junior / Middle School',
      'Quaternary_Desc': 'Infant School'
  }, {
      'Concatenated': 'CE03JS',
      'Class_Desc': 'Junior School',
      'Primary_Code': 'C',
      'Secondary_Code': 'E',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'JS',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Education',
      'Tertiary_Desc':
      'Preparatory / First / Primary / Infant / Junior / Middle School',
      'Quaternary_Desc': 'Junior School'
  }, {
      'Concatenated': 'CE03MS',
      'Class_Desc': 'Middle School',
      'Primary_Code': 'C',
      'Secondary_Code': 'E',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'MS',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Education',
      'Tertiary_Desc':
      'Preparatory / First / Primary / Infant / Junior / Middle School',
      'Quaternary_Desc': 'Middle School'
  }, {
      'Concatenated':
      'CE03NP',
      'Class_Desc':
      'Non State Primary / Preparatory School',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'E',
      'Tertiary_Code':
      '3',
      'Quaternary_Code':
      'NP',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Education',
      'Tertiary_Desc':
      'Preparatory / First / Primary / Infant / Junior / Middle School',
      'Quaternary_Desc':
      'Non State Primary / Preparatory School'
  }, {
      'Concatenated': 'CE03PS',
      'Class_Desc': 'Primary School',
      'Primary_Code': 'C',
      'Secondary_Code': 'E',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'PS',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Education',
      'Tertiary_Desc':
      'Preparatory / First / Primary / Infant / Junior / Middle School',
      'Quaternary_Desc': 'Primary School'
  }, {
      'Concatenated': 'CE04',
      'Class_Desc': 'Secondary / High School',
      'Primary_Code': 'C',
      'Secondary_Code': 'E',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Education',
      'Tertiary_Desc': 'Secondary / High School',
      'Quaternary_Desc': ''
  }, {
      'Concatenated':
      'CE04NS',
      'Class_Desc':
      'Non State Secondary School',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'E',
      'Tertiary_Code':
      '4',
      'Quaternary_Code':
      'NS',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Education',
      'Tertiary_Desc':
      'Secondary / High School',
      'Quaternary_Desc':
      'Non State Secondary School'
  }, {
      'Concatenated': 'CE04SS',
      'Class_Desc': 'Secondary School',
      'Primary_Code': 'C',
      'Secondary_Code': 'E',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'SS',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Education',
      'Tertiary_Desc': 'Secondary / High School',
      'Quaternary_Desc': 'Secondary School'
  }, {
      'Concatenated': 'CE05',
      'Class_Desc': 'University',
      'Primary_Code': 'C',
      'Secondary_Code': 'E',
      'Tertiary_Code': '5',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Education',
      'Tertiary_Desc': 'University',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CE06',
      'Class_Desc': 'Special Needs Establishment.',
      'Primary_Code': 'C',
      'Secondary_Code': 'E',
      'Tertiary_Code': '6',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Education',
      'Tertiary_Desc': 'Special Needs Establishment.',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CE07',
      'Class_Desc': 'Other Educational Establishment',
      'Primary_Code': 'C',
      'Secondary_Code': 'E',
      'Tertiary_Code': '7',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Education',
      'Tertiary_Desc': 'Other Educational Establishment',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CH',
      'Class_Desc': 'Hotel / Motel / Boarding / Guest House',
      'Primary_Code': 'C',
      'Secondary_Code': 'H',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Hotel / Motel / Boarding / Guest House',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CH01',
      'Class_Desc':
      'Boarding / Guest House / Bed And Breakfast / Youth Hostel',
      'Primary_Code': 'C',
      'Secondary_Code': 'H',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Hotel / Motel / Boarding / Guest House',
      'Tertiary_Desc':
      'Boarding / Guest House / Bed And Breakfast / Youth Hostel',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CH01YH',
      'Class_Desc': 'Youth Hostel',
      'Primary_Code': 'C',
      'Secondary_Code': 'H',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'YH',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Hotel / Motel / Boarding / Guest House',
      'Tertiary_Desc':
      'Boarding / Guest House / Bed And Breakfast / Youth Hostel',
      'Quaternary_Desc': 'Youth Hostel'
  }, {
      'Concatenated': 'CH02',
      'Class_Desc': 'Holiday Let/Accomodation/Short-Term Let Other Than CH01',
      'Primary_Code': 'C',
      'Secondary_Code': 'H',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Hotel / Motel / Boarding / Guest House',
      'Tertiary_Desc':
      'Holiday Let/Accomodation/Short-Term Let Other Than CH01',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CH03',
      'Class_Desc': 'Hotel/Motel',
      'Primary_Code': 'C',
      'Secondary_Code': 'H',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Hotel / Motel / Boarding / Guest House',
      'Tertiary_Desc': 'Hotel/Motel',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CI',
      'Class_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CI01',
      'Class_Desc': 'Factory/Manufacturing',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CI01AW',
      'Class_Desc': 'Aircraft Works',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'AW',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Aircraft Works'
  }, {
      'Concatenated': 'CI01BB',
      'Class_Desc': 'Boat Building',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'BB',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Boat Building'
  }, {
      'Concatenated': 'CI01BR',
      'Class_Desc': 'Brick Works',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'BR',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Brick Works'
  }, {
      'Concatenated': 'CI01BW',
      'Class_Desc': 'Brewery',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'BW',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Brewery'
  }, {
      'Concatenated': 'CI01CD',
      'Class_Desc': 'Cider Manufacture',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'CD',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Cider Manufacture'
  }, {
      'Concatenated': 'CI01CM',
      'Class_Desc': 'Chemical Works',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'CM',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Chemical Works'
  }, {
      'Concatenated': 'CI01CW',
      'Class_Desc': 'Cement Works',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'CW',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Cement Works'
  }, {
      'Concatenated': 'CI01DA',
      'Class_Desc': 'Dairy Processing',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'DA',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Dairy Processing'
  }, {
      'Concatenated': 'CI01DY',
      'Class_Desc': 'Distillery',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'DY',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Distillery'
  }, {
      'Concatenated': 'CI01FL',
      'Class_Desc': 'Flour Mill',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'FL',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Flour Mill'
  }, {
      'Concatenated': 'CI01FO',
      'Class_Desc': 'Food Processing',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'FO',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Food Processing'
  }, {
      'Concatenated': 'CI01GW',
      'Class_Desc': 'Glassworks',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'GW',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Glassworks'
  }, {
      'Concatenated': 'CI01MG',
      'Class_Desc': 'Manufacturing',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'MG',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Manufacturing'
  }, {
      'Concatenated': 'CI01OH',
      'Class_Desc': 'Oast House',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'OH',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Oast House'
  }, {
      'Concatenated': 'CI01OR',
      'Class_Desc': 'Oil Refining',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'OR',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Oil Refining'
  }, {
      'Concatenated': 'CI01PG',
      'Class_Desc': 'Pottery Manufacturing',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'PG',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Pottery Manufacturing'
  }, {
      'Concatenated': 'CI01PM',
      'Class_Desc': 'Paper Mill',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'PM',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Paper Mill'
  }, {
      'Concatenated': 'CI01PW',
      'Class_Desc': 'Printing Works',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'PW',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Printing Works'
  }, {
      'Concatenated': 'CI01SR',
      'Class_Desc': 'Sugar Refinery',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'SR',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Sugar Refinery'
  }, {
      'Concatenated': 'CI01SW',
      'Class_Desc': 'Steel Works',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'SW',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Steel Works'
  }, {
      'Concatenated': 'CI01TL',
      'Class_Desc': 'Timber Mill',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'TL',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Timber Mill'
  }, {
      'Concatenated': 'CI01WN',
      'Class_Desc': 'Winery',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'WN',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Winery'
  }, {
      'Concatenated': 'CI01YD',
      'Class_Desc': 'Shipyard',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'YD',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Factory/Manufacturing',
      'Quaternary_Desc': 'Shipyard'
  }, {
      'Concatenated': 'CI02',
      'Class_Desc': 'Mineral / Ore Working / Quarry / Mine',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Mineral / Ore Working / Quarry / Mine',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CI02MA',
      'Class_Desc': 'Mineral Mining / Active',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'MA',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Mineral / Ore Working / Quarry / Mine',
      'Quaternary_Desc': 'Mineral Mining / Active'
  }, {
      'Concatenated':
      'CI02MD',
      'Class_Desc':
      'Mineral Distribution / Storage',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'I',
      'Tertiary_Code':
      '2',
      'Quaternary_Code':
      'MD',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc':
      'Mineral / Ore Working / Quarry / Mine',
      'Quaternary_Desc':
      'Mineral Distribution / Storage'
  }, {
      'Concatenated': 'CI02MP',
      'Class_Desc': 'Mineral Processing',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'MP',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Mineral / Ore Working / Quarry / Mine',
      'Quaternary_Desc': 'Mineral Processing'
  }, {
      'Concatenated':
      'CI02OA',
      'Class_Desc':
      'Oil / Gas Extraction / Active',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'I',
      'Tertiary_Code':
      '2',
      'Quaternary_Code':
      'OA',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc':
      'Mineral / Ore Working / Quarry / Mine',
      'Quaternary_Desc':
      'Oil / Gas Extraction / Active'
  }, {
      'Concatenated':
      'CI02QA',
      'Class_Desc':
      'Mineral Quarrying / Open Extraction / Active',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'I',
      'Tertiary_Code':
      '2',
      'Quaternary_Code':
      'QA',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc':
      'Mineral / Ore Working / Quarry / Mine',
      'Quaternary_Desc':
      'Mineral Quarrying / Open Extraction / Active'
  }, {
      'Concatenated': 'CI03',
      'Class_Desc': 'Workshop / Light Industrial',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Workshop / Light Industrial',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CI03GA',
      'Class_Desc': 'Servicing Garage',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'GA',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Workshop / Light Industrial',
      'Quaternary_Desc': 'Servicing Garage'
  }, {
      'Concatenated': 'CI04',
      'Class_Desc': 'Warehouse / Store / Storage Depot',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Warehouse / Store / Storage Depot',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CI04CS',
      'Class_Desc': 'Crop Handling / Storage',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'CS',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Warehouse / Store / Storage Depot',
      'Quaternary_Desc': 'Crop Handling / Storage'
  }, {
      'Concatenated':
      'CI04PL',
      'Class_Desc':
      'Postal Sorting / Distribution',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'I',
      'Tertiary_Code':
      '4',
      'Quaternary_Code':
      'PL',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc':
      'Warehouse / Store / Storage Depot',
      'Quaternary_Desc':
      'Postal Sorting / Distribution'
  }, {
      'Concatenated': 'CI04SO',
      'Class_Desc': 'Solid Fuel Storage',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'SO',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Warehouse / Store / Storage Depot',
      'Quaternary_Desc': 'Solid Fuel Storage'
  }, {
      'Concatenated': 'CI04TS',
      'Class_Desc': 'Timber Storage',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'TS',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Warehouse / Store / Storage Depot',
      'Quaternary_Desc': 'Timber Storage'
  }, {
      'Concatenated': 'CI05',
      'Class_Desc': 'Wholesale Distribution',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '5',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Wholesale Distribution',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CI05SF',
      'Class_Desc': 'Solid Fuel Distribution',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '5',
      'Quaternary_Code': 'SF',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Wholesale Distribution',
      'Quaternary_Desc': 'Solid Fuel Distribution'
  }, {
      'Concatenated': 'CI05TD',
      'Class_Desc': 'Timber Distribution',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '5',
      'Quaternary_Code': 'TD',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Wholesale Distribution',
      'Quaternary_Desc': 'Timber Distribution'
  }, {
      'Concatenated': 'CI06',
      'Class_Desc': 'Recycling Plant',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '6',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Recycling Plant',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CI07',
      'Class_Desc': 'Incinerator / Waste Transfer Station',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '7',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Incinerator / Waste Transfer Station',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CI08',
      'Class_Desc': 'Maintenance Depot',
      'Primary_Code': 'C',
      'Secondary_Code': 'I',
      'Tertiary_Code': '8',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'Tertiary_Desc': 'Maintenance Depot',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CL',
      'Class_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CL01',
      'Class_Desc': 'Amusements',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Amusements',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CL01LP',
      'Class_Desc': 'Leisure Pier',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'LP',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Amusements',
      'Quaternary_Desc': 'Leisure Pier'
  }, {
      'Concatenated': 'CL02',
      'Class_Desc': 'Holiday / Campsite',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Holiday / Campsite',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CL02CG',
      'Class_Desc': 'Camping',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'CG',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Holiday / Campsite',
      'Quaternary_Desc': 'Camping'
  }, {
      'Concatenated': 'CL02CV',
      'Class_Desc': 'Caravanning',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'CV',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Holiday / Campsite',
      'Quaternary_Desc': 'Caravanning'
  }, {
      'Concatenated': 'CL02HA',
      'Class_Desc': 'Holiday Accommodation',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'HA',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Holiday / Campsite',
      'Quaternary_Desc': 'Holiday Accommodation'
  }, {
      'Concatenated': 'CL02HO',
      'Class_Desc': 'Holiday Centre',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'HO',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Holiday / Campsite',
      'Quaternary_Desc': 'Holiday Centre'
  }, {
      'Concatenated': 'CL02YC',
      'Class_Desc': 'Youth Organisation Camp',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'YC',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Holiday / Campsite',
      'Quaternary_Desc': 'Youth Organisation Camp'
  }, {
      'Concatenated': 'CL03',
      'Class_Desc': 'Library',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Library',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CL03RR',
      'Class_Desc': 'Reading Room',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'RR',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Library',
      'Quaternary_Desc': 'Reading Room'
  }, {
      'Concatenated': 'CL04',
      'Class_Desc': 'Museum / Gallery',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Museum / Gallery',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CL04AC',
      'Class_Desc': 'Art Centre / Gallery',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'AC',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Museum / Gallery',
      'Quaternary_Desc': 'Art Centre / Gallery'
  }, {
      'Concatenated': 'CL04AM',
      'Class_Desc': 'Aviation Museum',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'AM',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Museum / Gallery',
      'Quaternary_Desc': 'Aviation Museum'
  }, {
      'Concatenated': 'CL04HG',
      'Class_Desc': 'Heritage Centre',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'HG',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Museum / Gallery',
      'Quaternary_Desc': 'Heritage Centre'
  }, {
      'Concatenated': 'CL04IM',
      'Class_Desc': 'Industrial Museum',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'IM',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Museum / Gallery',
      'Quaternary_Desc': 'Industrial Museum'
  }, {
      'Concatenated': 'CL04MM',
      'Class_Desc': 'Military Museum',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'MM',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Museum / Gallery',
      'Quaternary_Desc': 'Military Museum'
  }, {
      'Concatenated': 'CL04NM',
      'Class_Desc': 'Maritime Museum',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'NM',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Museum / Gallery',
      'Quaternary_Desc': 'Maritime Museum'
  }, {
      'Concatenated': 'CL04SM',
      'Class_Desc': 'Science Museum',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'SM',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Museum / Gallery',
      'Quaternary_Desc': 'Science Museum'
  }, {
      'Concatenated': 'CL04TM',
      'Class_Desc': 'Transport Museum',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'TM',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Museum / Gallery',
      'Quaternary_Desc': 'Transport Museum'
  }, {
      'Concatenated': 'CL06',
      'Class_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CL06AH',
      'Class_Desc': 'Athletics Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'AH',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Athletics Facility'
  }, {
      'Concatenated': 'CL06BF',
      'Class_Desc': 'Bowls Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'BF',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Bowls Facility'
  }, {
      'Concatenated': 'CL06CK',
      'Class_Desc': 'Cricket Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'CK',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Cricket Facility'
  }, {
      'Concatenated': 'CL06CU',
      'Class_Desc': 'Curling Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'CU',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Curling Facility'
  }, {
      'Concatenated':
      'CL06DS',
      'Class_Desc':
      'Diving / Swimming Facility',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'L',
      'Tertiary_Code':
      '6',
      'Quaternary_Code':
      'DS',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc':
      'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc':
      'Diving / Swimming Facility'
  }, {
      'Concatenated':
      'CL06EQ',
      'Class_Desc':
      'Equestrian Sports Facility',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'L',
      'Tertiary_Code':
      '6',
      'Quaternary_Code':
      'EQ',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc':
      'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc':
      'Equestrian Sports Facility'
  }, {
      'Concatenated': 'CL06FB',
      'Class_Desc': 'Football Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'FB',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Football Facility'
  }, {
      'Concatenated':
      'CL06FI',
      'Class_Desc':
      'Fishing / Angling Facility',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'L',
      'Tertiary_Code':
      '6',
      'Quaternary_Code':
      'FI',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc':
      'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc':
      'Fishing / Angling Facility'
  }, {
      'Concatenated': 'CL06GF',
      'Class_Desc': 'Golf Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'GF',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Golf Facility'
  }, {
      'Concatenated': 'CL06GL',
      'Class_Desc': 'Gliding Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'GL',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Gliding Facility'
  }, {
      'Concatenated':
      'CL06GR',
      'Class_Desc':
      'Greyhound Racing Facility',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'L',
      'Tertiary_Code':
      '6',
      'Quaternary_Code':
      'GR',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc':
      'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc':
      'Greyhound Racing Facility'
  }, {
      'Concatenated': 'CL06HF',
      'Class_Desc': 'Hockey Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'HF',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Hockey Facility'
  }, {
      'Concatenated': 'CL06HR',
      'Class_Desc': 'Horse Racing Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'HR',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Horse Racing Facility'
  }, {
      'Concatenated':
      'CL06HV',
      'Class_Desc':
      'Historic Vessel / Aircraft / Vehicle',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'L',
      'Tertiary_Code':
      '6',
      'Quaternary_Code':
      'HV',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc':
      'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc':
      'Historic Vessel / Aircraft / Vehicle'
  }, {
      'Concatenated':
      'CL06LS',
      'Class_Desc':
      'Activity / Leisure / Sports Centre',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'L',
      'Tertiary_Code':
      '6',
      'Quaternary_Code':
      'LS',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc':
      'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc':
      'Activity / Leisure / Sports Centre'
  }, {
      'Concatenated': 'CL06ME',
      'Class_Desc': 'Model Sports Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'ME',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Model Sports Facility'
  }, {
      'Concatenated': 'CL06MF',
      'Class_Desc': 'Motor Sports Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'MF',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Motor Sports Facility'
  }, {
      'Concatenated': 'CL06PF',
      'Class_Desc': 'Playing Field',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'PF',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Playing Field'
  }, {
      'Concatenated': 'CL06QS',
      'Class_Desc': 'Racquet Sports Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'QS',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Racquet Sports Facility'
  }, {
      'Concatenated': 'CL06RF',
      'Class_Desc': 'Rugby Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'RF',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Rugby Facility'
  }, {
      'Concatenated': 'CL06RG',
      'Class_Desc': 'Recreation Ground',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'RG',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Recreation Ground'
  }, {
      'Concatenated': 'CL06SI',
      'Class_Desc': 'Shinty Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'SI',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Shinty Facility'
  }, {
      'Concatenated': 'CL06SK',
      'Class_Desc': 'Skateboarding Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'SK',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Skateboarding Facility'
  }, {
      'Concatenated':
      'CL06SX',
      'Class_Desc':
      'Civilian Firing Facility',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'L',
      'Tertiary_Code':
      '6',
      'Quaternary_Code':
      'SX',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc':
      'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc':
      'Civilian Firing Facility'
  }, {
      'Concatenated': 'CL06TB',
      'Class_Desc': 'Tenpin Bowling Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'TB',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Tenpin Bowling Facility'
  }, {
      'Concatenated': 'CL06TN',
      'Class_Desc': 'Public Tennis Court',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'TN',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Public Tennis Court'
  }, {
      'Concatenated': 'CL06WA',
      'Class_Desc': 'Water Sports Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'WA',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Water Sports Facility'
  }, {
      'Concatenated': 'CL06WP',
      'Class_Desc': 'Winter Sports Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'WP',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Winter Sports Facility'
  }, {
      'Concatenated':
      'CL06WY',
      'Class_Desc':
      'Wildlife Sports Facility',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'L',
      'Tertiary_Code':
      '6',
      'Quaternary_Code':
      'WY',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc':
      'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc':
      'Wildlife Sports Facility'
  }, {
      'Concatenated': 'CL06YF',
      'Class_Desc': 'Cycling Sports Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'YF',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'Quaternary_Desc': 'Cycling Sports Facility'
  }, {
      'Concatenated': 'CL07',
      'Class_Desc':
      'Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '7',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc':
      'Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CL07CI',
      'Class_Desc': 'Cinema',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '7',
      'Quaternary_Code': 'CI',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc':
      'Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall',
      'Quaternary_Desc': 'Cinema'
  }, {
      'Concatenated': 'CL07EN',
      'Class_Desc': 'Entertainment Complex',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '7',
      'Quaternary_Code': 'EN',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc':
      'Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall',
      'Quaternary_Desc': 'Entertainment Complex'
  }, {
      'Concatenated':
      'CL07EX',
      'Class_Desc':
      'Conference / Exhibition Centre',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'L',
      'Tertiary_Code':
      '7',
      'Quaternary_Code':
      'EX',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc':
      'Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall',
      'Quaternary_Desc':
      'Conference / Exhibition Centre'
  }, {
      'Concatenated': 'CL07TH',
      'Class_Desc': 'Theatre',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '7',
      'Quaternary_Code': 'TH',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc':
      'Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall',
      'Quaternary_Desc': 'Theatre'
  }, {
      'Concatenated': 'CL08',
      'Class_Desc': 'Zoo / Theme Park',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '8',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Zoo / Theme Park',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CL08AK',
      'Class_Desc': 'Amusement Park',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '8',
      'Quaternary_Code': 'AK',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Zoo / Theme Park',
      'Quaternary_Desc': 'Amusement Park'
  }, {
      'Concatenated': 'CL08AQ',
      'Class_Desc': 'Aquatic Attraction',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '8',
      'Quaternary_Code': 'AQ',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Zoo / Theme Park',
      'Quaternary_Desc': 'Aquatic Attraction'
  }, {
      'Concatenated': 'CL08MX',
      'Class_Desc': 'Model Village Site',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '8',
      'Quaternary_Code': 'MX',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Zoo / Theme Park',
      'Quaternary_Desc': 'Model Village Site'
  }, {
      'Concatenated':
      'CL08WZ',
      'Class_Desc':
      'Wildlife / Zoological Park',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'L',
      'Tertiary_Code':
      '8',
      'Quaternary_Code':
      'WZ',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc':
      'Zoo / Theme Park',
      'Quaternary_Desc':
      'Wildlife / Zoological Park'
  }, {
      'Concatenated': 'CL09',
      'Class_Desc': 'Beach Hut (Recreational, Non-Residential Use Only)',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '9',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Beach Hut (Recreational, Non-Residential Use Only)',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CL10',
      'Class_Desc': 'Licensed Private Members’ Club',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '10',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Licensed Private Members’ Club',
      'Quaternary_Desc': ''
  }, {
      'Concatenated':
      'CL10RE',
      'Class_Desc':
      'Recreational / Social Club',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'L',
      'Tertiary_Code':
      '10',
      'Quaternary_Code':
      'RE',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc':
      'Licensed Private Members’ Club',
      'Quaternary_Desc':
      'Recreational / Social Club'
  }, {
      'Concatenated': 'CL11',
      'Class_Desc': 'Arena / Stadium',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '11',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Arena / Stadium',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CL11SD',
      'Class_Desc': 'Stadium',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '11',
      'Quaternary_Code': 'SD',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Arena / Stadium',
      'Quaternary_Desc': 'Stadium'
  }, {
      'Concatenated': 'CL11SJ',
      'Class_Desc': 'Showground',
      'Primary_Code': 'C',
      'Secondary_Code': 'L',
      'Tertiary_Code': '11',
      'Quaternary_Code': 'SJ',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'Tertiary_Desc': 'Arena / Stadium',
      'Quaternary_Desc': 'Showground'
  }, {
      'Concatenated': 'CM',
      'Class_Desc': 'Medical',
      'Primary_Code': 'C',
      'Secondary_Code': 'M',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Medical',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CM01',
      'Class_Desc': 'Dentist',
      'Primary_Code': 'C',
      'Secondary_Code': 'M',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Medical',
      'Tertiary_Desc': 'Dentist',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CM02',
      'Class_Desc': 'General Practice Surgery / Clinic',
      'Primary_Code': 'C',
      'Secondary_Code': 'M',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Medical',
      'Tertiary_Desc': 'General Practice Surgery / Clinic',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CM02HC',
      'Class_Desc': 'Health Centre',
      'Primary_Code': 'C',
      'Secondary_Code': 'M',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'HC',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Medical',
      'Tertiary_Desc': 'General Practice Surgery / Clinic',
      'Quaternary_Desc': 'Health Centre'
  }, {
      'Concatenated': 'CM02HL',
      'Class_Desc': 'Health Care Services',
      'Primary_Code': 'C',
      'Secondary_Code': 'M',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'HL',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Medical',
      'Tertiary_Desc': 'General Practice Surgery / Clinic',
      'Quaternary_Desc': 'Health Care Services'
  }, {
      'Concatenated': 'CM03',
      'Class_Desc': 'Hospital / Hospice',
      'Primary_Code': 'C',
      'Secondary_Code': 'M',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Medical',
      'Tertiary_Desc': 'Hospital / Hospice',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CM03HI',
      'Class_Desc': 'Hospice',
      'Primary_Code': 'C',
      'Secondary_Code': 'M',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'HI',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Medical',
      'Tertiary_Desc': 'Hospital / Hospice',
      'Quaternary_Desc': 'Hospice'
  }, {
      'Concatenated': 'CM03HP',
      'Class_Desc': 'Hospital',
      'Primary_Code': 'C',
      'Secondary_Code': 'M',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'HP',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Medical',
      'Tertiary_Desc': 'Hospital / Hospice',
      'Quaternary_Desc': 'Hospital'
  }, {
      'Concatenated': 'CM04',
      'Class_Desc': 'Medical / Testing / Research Laboratory',
      'Primary_Code': 'C',
      'Secondary_Code': 'M',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Medical',
      'Tertiary_Desc': 'Medical / Testing / Research Laboratory',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CM05',
      'Class_Desc': 'Professional Medical Service',
      'Primary_Code': 'C',
      'Secondary_Code': 'M',
      'Tertiary_Code': '5',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Medical',
      'Tertiary_Desc': 'Professional Medical Service',
      'Quaternary_Desc': ''
  }, {
      'Concatenated':
      'CM05ZS',
      'Class_Desc':
      'Assessment / Development Services',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'M',
      'Tertiary_Code':
      '5',
      'Quaternary_Code':
      'ZS',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Medical',
      'Tertiary_Desc':
      'Professional Medical Service',
      'Quaternary_Desc':
      'Assessment / Development Services'
  }, {
      'Concatenated': 'CM06',
      'Class_Desc': 'Pharmacy',
      'Primary_Code': 'C',
      'Secondary_Code': 'M',
      'Tertiary_Code': '6',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Medical',
      'Tertiary_Desc': 'Pharmacy',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CN',
      'Class_Desc': 'Animal Centre',
      'Primary_Code': 'C',
      'Secondary_Code': 'N',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Animal Centre',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CN01',
      'Class_Desc': 'Cattery / Kennel',
      'Primary_Code': 'C',
      'Secondary_Code': 'N',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Animal Centre',
      'Tertiary_Desc': 'Cattery / Kennel',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CN02',
      'Class_Desc': 'Animal Services',
      'Primary_Code': 'C',
      'Secondary_Code': 'N',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Animal Centre',
      'Tertiary_Desc': 'Animal Services',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CN02AX',
      'Class_Desc': 'Animal Quarantining',
      'Primary_Code': 'C',
      'Secondary_Code': 'N',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'AX',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Animal Centre',
      'Tertiary_Desc': 'Animal Services',
      'Quaternary_Desc': 'Animal Quarantining'
  }, {
      'Concatenated': 'CN03',
      'Class_Desc': 'Equestrian',
      'Primary_Code': 'C',
      'Secondary_Code': 'N',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Animal Centre',
      'Tertiary_Desc': 'Equestrian',
      'Quaternary_Desc': ''
  }, {
      'Concatenated':
      'CN03HB',
      'Class_Desc':
      'Horse Racing / Breeding Stable',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'N',
      'Tertiary_Code':
      '3',
      'Quaternary_Code':
      'HB',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Animal Centre',
      'Tertiary_Desc':
      'Equestrian',
      'Quaternary_Desc':
      'Horse Racing / Breeding Stable'
  }, {
      'Concatenated':
      'CN03SB',
      'Class_Desc':
      'Commercial Stabling / Riding',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'N',
      'Tertiary_Code':
      '3',
      'Quaternary_Code':
      'SB',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Animal Centre',
      'Tertiary_Desc':
      'Equestrian',
      'Quaternary_Desc':
      'Commercial Stabling / Riding'
  }, {
      'Concatenated': 'CN04',
      'Class_Desc': 'Vet / Animal Medical Treatment',
      'Primary_Code': 'C',
      'Secondary_Code': 'N',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Animal Centre',
      'Tertiary_Desc': 'Vet / Animal Medical Treatment',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CN05',
      'Class_Desc': 'Animal / Bird / Marine Sanctuary',
      'Primary_Code': 'C',
      'Secondary_Code': 'N',
      'Tertiary_Code': '5',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Animal Centre',
      'Tertiary_Desc': 'Animal / Bird / Marine Sanctuary',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CN05AN',
      'Class_Desc': 'Animal Sanctuary',
      'Primary_Code': 'C',
      'Secondary_Code': 'N',
      'Tertiary_Code': '5',
      'Quaternary_Code': 'AN',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Animal Centre',
      'Tertiary_Desc': 'Animal / Bird / Marine Sanctuary',
      'Quaternary_Desc': 'Animal Sanctuary'
  }, {
      'Concatenated': 'CN05MR',
      'Class_Desc': 'Marine Sanctuary',
      'Primary_Code': 'C',
      'Secondary_Code': 'N',
      'Tertiary_Code': '5',
      'Quaternary_Code': 'MR',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Animal Centre',
      'Tertiary_Desc': 'Animal / Bird / Marine Sanctuary',
      'Quaternary_Desc': 'Marine Sanctuary'
  }, {
      'Concatenated': 'CO',
      'Class_Desc': 'Office',
      'Primary_Code': 'C',
      'Secondary_Code': 'O',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Office',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CO01',
      'Class_Desc': 'Office / Work Studio',
      'Primary_Code': 'C',
      'Secondary_Code': 'O',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Office',
      'Tertiary_Desc': 'Office / Work Studio',
      'Quaternary_Desc': ''
  }, {
      'Concatenated':
      'CO01EM',
      'Class_Desc':
      'Embassy /, High Commission / Consulate',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'O',
      'Tertiary_Code':
      '1',
      'Quaternary_Code':
      'EM',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Office',
      'Tertiary_Desc':
      'Office / Work Studio',
      'Quaternary_Desc':
      'Embassy /, High Commission / Consulate'
  }, {
      'Concatenated': 'CO01FM',
      'Class_Desc': 'Film Studio',
      'Primary_Code': 'C',
      'Secondary_Code': 'O',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'FM',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Office',
      'Tertiary_Desc': 'Office / Work Studio',
      'Quaternary_Desc': 'Film Studio'
  }, {
      'Concatenated':
      'CO01GV',
      'Class_Desc':
      'Central Government Service',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'O',
      'Tertiary_Code':
      '1',
      'Quaternary_Code':
      'GV',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Office',
      'Tertiary_Desc':
      'Office / Work Studio',
      'Quaternary_Desc':
      'Central Government Service'
  }, {
      'Concatenated':
      'CO01LG',
      'Class_Desc':
      'Local Government Service',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'O',
      'Tertiary_Code':
      '1',
      'Quaternary_Code':
      'LG',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Office',
      'Tertiary_Desc':
      'Office / Work Studio',
      'Quaternary_Desc':
      'Local Government Service'
  }, {
      'Concatenated': 'CO02',
      'Class_Desc': 'Broadcasting (TV / Radio)',
      'Primary_Code': 'C',
      'Secondary_Code': 'O',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Office',
      'Tertiary_Desc': 'Broadcasting (TV / Radio)',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CR',
      'Class_Desc': 'Retail',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CR01',
      'Class_Desc': 'Bank / Financial Service',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Bank / Financial Service',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CR02',
      'Class_Desc': 'Retail Service Agent',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Retail Service Agent',
      'Quaternary_Desc': ''
  }, {
      'Concatenated':
      'CR02EV',
      'Class_Desc':
      'Electric Car Charging Station',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'R',
      'Tertiary_Code':
      '2',
      'Quaternary_Code':
      'EV',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Retail',
      'Tertiary_Desc':
      'Retail Service Agent',
      'Quaternary_Desc':
      'Electric Car Charging Station'
  }, {
      'Concatenated': 'CR02PO',
      'Class_Desc': 'Post Office',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'PO',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Retail Service Agent',
      'Quaternary_Desc': 'Post Office'
  }, {
      'Concatenated': 'CR04',
      'Class_Desc': 'Market (Indoor / Outdoor)',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Market (Indoor / Outdoor)',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CR04FK',
      'Class_Desc': 'Fish Market',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'FK',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Market (Indoor / Outdoor)',
      'Quaternary_Desc': 'Fish Market'
  }, {
      'Concatenated':
      'CR04FV',
      'Class_Desc':
      'Fruit / Vegetable Market',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'R',
      'Tertiary_Code':
      '4',
      'Quaternary_Code':
      'FV',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Retail',
      'Tertiary_Desc':
      'Market (Indoor / Outdoor)',
      'Quaternary_Desc':
      'Fruit / Vegetable Market'
  }, {
      'Concatenated': 'CR04LV',
      'Class_Desc': 'Livestock Market',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'LV',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Market (Indoor / Outdoor)',
      'Quaternary_Desc': 'Livestock Market'
  }, {
      'Concatenated': 'CR05',
      'Class_Desc': 'Petrol Filling Station',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '5',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Petrol Filling Station',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CR06',
      'Class_Desc': 'Public House / Bar / Nightclub',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '6',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Public House / Bar / Nightclub',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CR06BA',
      'Class_Desc': 'Bar',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '6',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Public House / Bar / Nightclub',
      'Quaternary_Desc': 'Bar'
  }, {
      'Concatenated': 'CR06NC',
      'Class_Desc': 'Nightclub',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '6',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Public House / Bar / Nightclub',
      'Quaternary_Desc': 'Nightclub'
  }, {
      'Concatenated': 'CR06PH',
      'Class_Desc': 'Public House',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '6',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Public House / Bar / Nightclub',
      'Quaternary_Desc': 'Public House'
  }, {
      'Concatenated': 'CR07',
      'Class_Desc': 'Restaurant / Cafeteria',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '7',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Restaurant / Cafeteria',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CR08',
      'Class_Desc': 'Shop / Showroom',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '8',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Shop / Showroom',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CR08CS',
      'Class_Desc': 'Convenience Store',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '8',
      'Quaternary_Code': 'CS',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Shop / Showroom',
      'Quaternary_Desc': 'Convenience Store'
  }, {
      'Concatenated': 'CR08GC',
      'Class_Desc': 'Garden Centre',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '8',
      'Quaternary_Code': 'GC',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Shop / Showroom',
      'Quaternary_Desc': 'Garden Centre'
  }, {
      'Concatenated': 'CR08SM',
      'Class_Desc': 'Supermarket',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '8',
      'Quaternary_Code': 'SM',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Shop / Showroom',
      'Quaternary_Desc': 'Supermarket'
  }, {
      'Concatenated': 'CR09',
      'Class_Desc': 'Other Licensed Premise / Vendor',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '9',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Other Licensed Premise / Vendor',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CR09BS',
      'Class_Desc': 'Betting Shop',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '9',
      'Quaternary_Code': 'BS',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Other Licensed Premise / Vendor',
      'Quaternary_Desc': 'Betting Shop'
  }, {
      'Concatenated': 'CR09OL',
      'Class_Desc': 'Off-licence',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '9',
      'Quaternary_Code': 'OL',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Other Licensed Premise / Vendor',
      'Quaternary_Desc': 'Off-licence'
  }, {
      'Concatenated': 'CR10',
      'Class_Desc': 'Fast Food Outlet / Takeaway (Hot / Cold)',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '10',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Fast Food Outlet / Takeaway (Hot / Cold)',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CR11',
      'Class_Desc': 'Automated Teller Machine (ATM)',
      'Primary_Code': 'C',
      'Secondary_Code': 'R',
      'Tertiary_Code': '11',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Retail',
      'Tertiary_Desc': 'Automated Teller Machine (ATM)',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CS',
      'Class_Desc': 'Storage Land',
      'Primary_Code': 'C',
      'Secondary_Code': 'S',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Storage Land',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CS01',
      'Class_Desc': 'General Storage Land',
      'Primary_Code': 'C',
      'Secondary_Code': 'S',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Storage Land',
      'Tertiary_Desc': 'General Storage Land',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CS02',
      'Class_Desc': 'Builders’ Yard',
      'Primary_Code': 'C',
      'Secondary_Code': 'S',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Storage Land',
      'Tertiary_Desc': 'Builders’ Yard',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CT',
      'Class_Desc': 'Transport',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CT01',
      'Class_Desc':
      'Airfield / Airstrip / Airport / Air Transport Infrastructure Facility',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc':
      'Airfield / Airstrip / Airport / Air Transport Infrastructure Facility',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CT01AF',
      'Class_Desc': 'Airfield',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'AF',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc':
      'Airfield / Airstrip / Airport / Air Transport Infrastructure Facility',
      'Quaternary_Desc': 'Airfield'
  }, {
      'Concatenated':
      'CT01AI',
      'Class_Desc':
      'Air Transport Infrastructure Services',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'T',
      'Tertiary_Code':
      '1',
      'Quaternary_Code':
      'AI',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Transport',
      'Tertiary_Desc':
      'Airfield / Airstrip / Airport / Air Transport Infrastructure Facility',
      'Quaternary_Desc':
      'Air Transport Infrastructure Services'
  }, {
      'Concatenated': 'CT01AP',
      'Class_Desc': 'Airport',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'AP',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc':
      'Airfield / Airstrip / Airport / Air Transport Infrastructure Facility',
      'Quaternary_Desc': 'Airport'
  }, {
      'Concatenated': 'CT01AY',
      'Class_Desc': 'Air Passenger Terminal',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'AY',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc':
      'Airfield / Airstrip / Airport / Air Transport Infrastructure Facility',
      'Quaternary_Desc': 'Air Passenger Terminal'
  }, {
      'Concatenated': 'CT01HS',
      'Class_Desc': 'Helicopter Station',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'HS',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc':
      'Airfield / Airstrip / Airport / Air Transport Infrastructure Facility',
      'Quaternary_Desc': 'Helicopter Station'
  }, {
      'Concatenated': 'CT01HT',
      'Class_Desc': 'Heliport / Helipad',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'HT',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc':
      'Airfield / Airstrip / Airport / Air Transport Infrastructure Facility',
      'Quaternary_Desc': 'Heliport / Helipad'
  }, {
      'Concatenated': 'CT02',
      'Class_Desc': 'Bus Shelter',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Bus Shelter',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CT03',
      'Class_Desc':
      'Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc':
      'Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CT03PK',
      'Class_Desc': 'Public Park And Ride',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'PK',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc':
      'Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site',
      'Quaternary_Desc': 'Public Park And Ride'
  }, {
      'Concatenated': 'CT03PP',
      'Class_Desc': 'Public Car Parking',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'PP',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc':
      'Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site',
      'Quaternary_Desc': 'Public Car Parking'
  }, {
      'Concatenated': 'CT03PU',
      'Class_Desc': 'Public Coach Parking',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'PU',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc':
      'Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site',
      'Quaternary_Desc': 'Public Coach Parking'
  }, {
      'Concatenated':
      'CT03VP',
      'Class_Desc':
      'Public Commercial Vehicle Parking',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'T',
      'Tertiary_Code':
      '3',
      'Quaternary_Code':
      'VP',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Transport',
      'Tertiary_Desc':
      'Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site',
      'Quaternary_Desc':
      'Public Commercial Vehicle Parking'
  }, {
      'Concatenated': 'CT04',
      'Class_Desc': 'Goods Freight Handling / Terminal',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Goods Freight Handling / Terminal',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CT04AE',
      'Class_Desc': 'Air Freight Terminal',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'AE',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Goods Freight Handling / Terminal',
      'Quaternary_Desc': 'Air Freight Terminal'
  }, {
      'Concatenated': 'CT04CF',
      'Class_Desc': 'Container Freight',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'CF',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Goods Freight Handling / Terminal',
      'Quaternary_Desc': 'Container Freight'
  }, {
      'Concatenated': 'CT04RH',
      'Class_Desc': 'Road Freight Transport',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'RH',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Goods Freight Handling / Terminal',
      'Quaternary_Desc': 'Road Freight Transport'
  }, {
      'Concatenated': 'CT04RT',
      'Class_Desc': 'Rail Freight Transport',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'RT',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Goods Freight Handling / Terminal',
      'Quaternary_Desc': 'Rail Freight Transport'
  }, {
      'Concatenated': 'CT05',
      'Class_Desc': 'Marina',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '5',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Marina',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CT06',
      'Class_Desc': 'Mooring',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '6',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Mooring',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CT07',
      'Class_Desc': 'Railway Asset',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '7',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Railway Asset',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CT08',
      'Class_Desc': 'Station / Interchange / Terminal / Halt',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '8',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Station / Interchange / Terminal / Halt',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CT08BC',
      'Class_Desc': 'Bus / Coach Station',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '8',
      'Quaternary_Code': 'BC',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Station / Interchange / Terminal / Halt',
      'Quaternary_Desc': 'Bus / Coach Station'
  }, {
      'Concatenated': 'CT08RS',
      'Class_Desc': 'Railway Station',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '8',
      'Quaternary_Code': 'RS',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Station / Interchange / Terminal / Halt',
      'Quaternary_Desc': 'Railway Station'
  }, {
      'Concatenated': 'CT08VH',
      'Class_Desc': 'Vehicular Rail Terminal',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '8',
      'Quaternary_Code': 'VH',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Station / Interchange / Terminal / Halt',
      'Quaternary_Desc': 'Vehicular Rail Terminal'
  }, {
      'Concatenated': 'CT09',
      'Class_Desc': 'Transport Track / Way',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '9',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Transport Track / Way',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CT09CL',
      'Class_Desc': 'Cliff Railway',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '9',
      'Quaternary_Code': 'CL',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Transport Track / Way',
      'Quaternary_Desc': 'Cliff Railway'
  }, {
      'Concatenated':
      'CT09CX',
      'Class_Desc':
      'Chair Lift / Cable Car / Ski Tow',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'T',
      'Tertiary_Code':
      '9',
      'Quaternary_Code':
      'CX',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Transport',
      'Tertiary_Desc':
      'Transport Track / Way',
      'Quaternary_Desc':
      'Chair Lift / Cable Car / Ski Tow'
  }, {
      'Concatenated': 'CT09MO',
      'Class_Desc': 'Monorail',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '9',
      'Quaternary_Code': 'MO',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Transport Track / Way',
      'Quaternary_Desc': 'Monorail'
  }, {
      'Concatenated': 'CT10',
      'Class_Desc': 'Vehicle Storage',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '10',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Vehicle Storage',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CT10BG',
      'Class_Desc': 'Boat Storage',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '10',
      'Quaternary_Code': 'BG',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Vehicle Storage',
      'Quaternary_Desc': 'Boat Storage'
  }, {
      'Concatenated': 'CT10BU',
      'Class_Desc': 'Bus / Coach Depot',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '10',
      'Quaternary_Code': 'BU',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Vehicle Storage',
      'Quaternary_Desc': 'Bus / Coach Depot'
  }, {
      'Concatenated': 'CT11',
      'Class_Desc': 'Transport Related Infrastructure',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '11',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Transport Related Infrastructure',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CT11AD',
      'Class_Desc': 'Aqueduct',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '11',
      'Quaternary_Code': 'AD',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Transport Related Infrastructure',
      'Quaternary_Desc': 'Aqueduct'
  }, {
      'Concatenated': 'CT11CA',
      'Class_Desc': 'Road Bridge Over Canal',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '11',
      'Quaternary_Code': 'CA',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Transport Related Infrastructure',
      'Quaternary_Desc': 'Road Bridge Over Canal'
  }, {
      'Concatenated': 'CT11LK',
      'Class_Desc': 'Lock',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '11',
      'Quaternary_Code': 'LK',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Transport Related Infrastructure',
      'Quaternary_Desc': 'Lock'
  }, {
      'Concatenated':
      'CT11MU',
      'Class_Desc':
      'Road Bridge Over Multiple',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'T',
      'Tertiary_Code':
      '11',
      'Quaternary_Code':
      'MU',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Transport',
      'Tertiary_Desc':
      'Transport Related Infrastructure',
      'Quaternary_Desc':
      'Road Bridge Over Multiple'
  }, {
      'Concatenated':
      'CT11NN',
      'Class_Desc':
      'Road Bridge Over No Network',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'T',
      'Tertiary_Code':
      '11',
      'Quaternary_Code':
      'MN',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Transport',
      'Tertiary_Desc':
      'Transport Related Infrastructure',
      'Quaternary_Desc':
      'Road Bridge Over No Network'
  }, {
      'Concatenated': 'CT11PA',
      'Class_Desc': 'Road Bridge Over Path',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '11',
      'Quaternary_Code': 'PA',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Transport Related Infrastructure',
      'Quaternary_Desc': 'Road Bridge Over Path'
  }, {
      'Concatenated':
      'CT11RA',
      'Class_Desc':
      'Road Bridge Over Railway',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'T',
      'Tertiary_Code':
      '11',
      'Quaternary_Code':
      'RA',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Transport',
      'Tertiary_Desc':
      'Transport Related Infrastructure',
      'Quaternary_Desc':
      'Road Bridge Over Railway'
  }, {
      'Concatenated': 'CT11RO',
      'Class_Desc': 'Road Bridge Over Road',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '11',
      'Quaternary_Code': 'RO',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Transport Related Infrastructure',
      'Quaternary_Desc': 'Road Bridge Over Road'
  }, {
      'Concatenated': 'CT11WA',
      'Class_Desc': 'Road Bridge Over Water',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '11',
      'Quaternary_Code': 'WA',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Transport Related Infrastructure',
      'Quaternary_Desc': 'Road Bridge Over Water'
  }, {
      'Concatenated': 'CT11WE',
      'Class_Desc': 'Weir',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '11',
      'Quaternary_Code': 'WE',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Transport Related Infrastructure',
      'Quaternary_Desc': 'Weir'
  }, {
      'Concatenated':
      'CT11WG',
      'Class_Desc':
      'Weighbridge / Load Gauge',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'T',
      'Tertiary_Code':
      '11',
      'Quaternary_Code':
      'WG',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Transport',
      'Tertiary_Desc':
      'Transport Related Infrastructure',
      'Quaternary_Desc':
      'Weighbridge / Load Gauge'
  }, {
      'Concatenated': 'CT12',
      'Class_Desc': 'Overnight Lorry Park',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '12',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc': 'Overnight Lorry Park',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CT13',
      'Class_Desc':
      'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '13',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc':
      'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay',
      'Quaternary_Desc': ''
  }, {
      'Concatenated':
      'CT13FR',
      'Class_Desc':
      'Passenger Ferry Terminal',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'T',
      'Tertiary_Code':
      '13',
      'Quaternary_Code':
      'FR',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Transport',
      'Tertiary_Desc':
      'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay',
      'Quaternary_Desc':
      'Passenger Ferry Terminal'
  }, {
      'Concatenated':
      'CT13NB',
      'Class_Desc':
      'Non-Tanker Nautical Berthing',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'T',
      'Tertiary_Code':
      '13',
      'Quaternary_Code':
      'NB',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Transport',
      'Tertiary_Desc':
      'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay',
      'Quaternary_Desc':
      'Non-Tanker Nautical Berthing'
  }, {
      'Concatenated':
      'CT13NF',
      'Class_Desc':
      'Nautical Refuelling Facility',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'T',
      'Tertiary_Code':
      '13',
      'Quaternary_Code':
      'NF',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Transport',
      'Tertiary_Desc':
      'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay',
      'Quaternary_Desc':
      'Nautical Refuelling Facility'
  }, {
      'Concatenated': 'CT13SA',
      'Class_Desc': 'Slipway',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '13',
      'Quaternary_Code': 'SA',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc':
      'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay',
      'Quaternary_Desc': 'Slipway'
  }, {
      'Concatenated': 'CT13SP',
      'Class_Desc': 'Ship Passenger Terminal',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '13',
      'Quaternary_Code': 'SP',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc':
      'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay',
      'Quaternary_Desc': 'Ship Passenger Terminal'
  }, {
      'Concatenated': 'CT13TK',
      'Class_Desc': 'Tanker Berthing',
      'Primary_Code': 'C',
      'Secondary_Code': 'T',
      'Tertiary_Code': '13',
      'Quaternary_Code': 'TK',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Transport',
      'Tertiary_Desc':
      'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay',
      'Quaternary_Desc': 'Tanker Berthing'
  }, {
      'Concatenated':
      'CT13VF',
      'Class_Desc':
      'Vehicular Ferry Terminal',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'T',
      'Tertiary_Code':
      '13',
      'Quaternary_Code':
      'VF',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Transport',
      'Tertiary_Desc':
      'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay',
      'Quaternary_Desc':
      'Vehicular Ferry Terminal'
  }, {
      'Concatenated': 'CU',
      'Class_Desc': 'Utility',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CU01',
      'Class_Desc': 'Electricity Sub-Station',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Electricity Sub-Station',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CU02',
      'Class_Desc': 'Landfill',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Landfill',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CU03',
      'Class_Desc': 'Power Station / Energy Production',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Power Station / Energy Production',
      'Quaternary_Desc': ''
  }, {
      'Concatenated':
      'CU03ED',
      'Class_Desc':
      'Electricity Distribution Facility',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'U',
      'Tertiary_Code':
      '3',
      'Quaternary_Code':
      'ED',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Utility',
      'Tertiary_Desc':
      'Power Station / Energy Production',
      'Quaternary_Desc':
      'Electricity Distribution Facility'
  }, {
      'Concatenated':
      'CU03EP',
      'Class_Desc':
      'Electricity Production Facility',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'U',
      'Tertiary_Code':
      '3',
      'Quaternary_Code':
      'EP',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Utility',
      'Tertiary_Desc':
      'Power Station / Energy Production',
      'Quaternary_Desc':
      'Electricity Production Facility'
  }, {
      'Concatenated': 'CU03WF',
      'Class_Desc': 'Wind Farm',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'WF',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Power Station / Energy Production',
      'Quaternary_Desc': 'Wind Farm'
  }, {
      'Concatenated': 'CU03WU',
      'Class_Desc': 'Wind Turbine',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'WU',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Power Station / Energy Production',
      'Quaternary_Desc': 'Wind Turbine'
  }, {
      'Concatenated': 'CU04',
      'Class_Desc': 'Pump House / Pumping Station / Water Tower',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Pump House / Pumping Station / Water Tower',
      'Quaternary_Desc': ''
  }, {
      'Concatenated':
      'CU04WC',
      'Class_Desc':
      'Water Controlling / Pumping',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'U',
      'Tertiary_Code':
      '4',
      'Quaternary_Code':
      'WC',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Utility',
      'Tertiary_Desc':
      'Pump House / Pumping Station / Water Tower',
      'Quaternary_Desc':
      'Water Controlling / Pumping'
  }, {
      'Concatenated':
      'CU04WD',
      'Class_Desc':
      'Water Distribution / Pumping',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'U',
      'Tertiary_Code':
      '4',
      'Quaternary_Code':
      'WD',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Utility',
      'Tertiary_Desc':
      'Pump House / Pumping Station / Water Tower',
      'Quaternary_Desc':
      'Water Distribution / Pumping'
  }, {
      'Concatenated':
      'CU04WM',
      'Class_Desc':
      'Water Quality Monitoring',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'U',
      'Tertiary_Code':
      '4',
      'Quaternary_Code':
      'WM',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Utility',
      'Tertiary_Desc':
      'Pump House / Pumping Station / Water Tower',
      'Quaternary_Desc':
      'Water Quality Monitoring'
  }, {
      'Concatenated': 'CU04WS',
      'Class_Desc': 'Water Storage',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'WS',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Pump House / Pumping Station / Water Tower',
      'Quaternary_Desc': 'Water Storage'
  }, {
      'Concatenated':
      'CU04WW',
      'Class_Desc':
      'Waste Water Distribution / Pumping',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'U',
      'Tertiary_Code':
      '4',
      'Quaternary_Code':
      'WW',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Utility',
      'Tertiary_Desc':
      'Pump House / Pumping Station / Water Tower',
      'Quaternary_Desc':
      'Waste Water Distribution / Pumping'
  }, {
      'Concatenated': 'CU06',
      'Class_Desc': 'Telecommunication',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '6',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Telecommunication',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CU06TE',
      'Class_Desc': 'Telecommunications Mast',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'TE',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Telecommunication',
      'Quaternary_Desc': 'Telecommunications Mast'
  }, {
      'Concatenated': 'CU06TX',
      'Class_Desc': 'Telephone Exchange',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '6',
      'Quaternary_Code': 'TX',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Telecommunication',
      'Quaternary_Desc': 'Telephone Exchange'
  }, {
      'Concatenated': 'CU07',
      'Class_Desc': 'Water / Waste Water / Sewage Treatment Works',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '7',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Water / Waste Water / Sewage Treatment Works',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CU07WR',
      'Class_Desc': 'Waste Water Treatment',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '7',
      'Quaternary_Code': 'WR',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Water / Waste Water / Sewage Treatment Works',
      'Quaternary_Desc': 'Waste Water Treatment'
  }, {
      'Concatenated': 'CU07WT',
      'Class_Desc': 'Water Treatment',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '7',
      'Quaternary_Code': 'WT',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Water / Waste Water / Sewage Treatment Works',
      'Quaternary_Desc': 'Water Treatment'
  }, {
      'Concatenated': 'CU08',
      'Class_Desc': 'Gas / Oil Storage / Distribution',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '8',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Gas / Oil Storage / Distribution',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CU08GG',
      'Class_Desc': 'Gas Governor',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '8',
      'Quaternary_Code': 'GG',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Gas / Oil Storage / Distribution',
      'Quaternary_Desc': 'Gas Governor'
  }, {
      'Concatenated': 'CU08GH',
      'Class_Desc': 'Gas Holder',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '8',
      'Quaternary_Code': 'GH',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Gas / Oil Storage / Distribution',
      'Quaternary_Desc': 'Gas Holder'
  }, {
      'Concatenated': 'CU08OT',
      'Class_Desc': 'Oil Terminal',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '8',
      'Quaternary_Code': 'OT',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Gas / Oil Storage / Distribution',
      'Quaternary_Desc': 'Oil Terminal'
  }, {
      'Concatenated': 'CU09',
      'Class_Desc': 'Other Utility Use',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '9',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Other Utility Use',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CU09CQ',
      'Class_Desc': 'Cable Terminal Station',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '9',
      'Quaternary_Code': 'CQ',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Other Utility Use',
      'Quaternary_Desc': 'Cable Terminal Station'
  }, {
      'Concatenated': 'CU09OV',
      'Class_Desc': 'Observatory',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '9',
      'Quaternary_Code': 'OV',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Other Utility Use',
      'Quaternary_Desc': 'Observatory'
  }, {
      'Concatenated': 'CU09RA',
      'Class_Desc': 'Radar Station',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '9',
      'Quaternary_Code': 'RA',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Other Utility Use',
      'Quaternary_Desc': 'Radar Station'
  }, {
      'Concatenated': 'CU09SE',
      'Class_Desc': 'Satellite Earth Station',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '9',
      'Quaternary_Code': 'SE',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Other Utility Use',
      'Quaternary_Desc': 'Satellite Earth Station'
  }, {
      'Concatenated': 'CU10',
      'Class_Desc': 'Waste Management',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '10',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Waste Management',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CU11',
      'Class_Desc': 'Telephone Box',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '11',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Telephone Box',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CU11OP',
      'Class_Desc': 'Other Public Telephones',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '11',
      'Quaternary_Code': 'OP',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Telephone Box',
      'Quaternary_Desc': 'Other Public Telephones'
  }, {
      'Concatenated': 'CU12',
      'Class_Desc': 'Dam',
      'Primary_Code': 'C',
      'Secondary_Code': 'U',
      'Tertiary_Code': '12',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Utility',
      'Tertiary_Desc': 'Dam',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CX',
      'Class_Desc': 'Emergency / Rescue Service',
      'Primary_Code': 'C',
      'Secondary_Code': 'X',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Emergency / Rescue Service',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CX01',
      'Class_Desc': 'Police / Transport Police / Station',
      'Primary_Code': 'C',
      'Secondary_Code': 'X',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Emergency / Rescue Service',
      'Tertiary_Desc': 'Police / Transport Police / Station',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CX01PT',
      'Class_Desc': 'Police Training',
      'Primary_Code': 'C',
      'Secondary_Code': 'X',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'PT',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Emergency / Rescue Service',
      'Tertiary_Desc': 'Police / Transport Police / Station',
      'Quaternary_Desc': 'Police Training'
  }, {
      'Concatenated': 'CX02',
      'Class_Desc': 'Fire Station',
      'Primary_Code': 'C',
      'Secondary_Code': 'X',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Emergency / Rescue Service',
      'Tertiary_Desc': 'Fire Station',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CX02FT',
      'Class_Desc': 'Fire Service Training',
      'Primary_Code': 'C',
      'Secondary_Code': 'X',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'FT',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Emergency / Rescue Service',
      'Tertiary_Desc': 'Fire Station',
      'Quaternary_Desc': 'Fire Service Training'
  }, {
      'Concatenated': 'CX03',
      'Class_Desc': 'Ambulance Station',
      'Primary_Code': 'C',
      'Secondary_Code': 'X',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Emergency / Rescue Service',
      'Tertiary_Desc': 'Ambulance Station',
      'Quaternary_Desc': ''
  }, {
      'Concatenated':
      'CX03AA',
      'Class_Desc':
      'Air Sea Rescue / Air Ambulance',
      'Primary_Code':
      'C',
      'Secondary_Code':
      'X',
      'Tertiary_Code':
      '3',
      'Quaternary_Code':
      'AA',
      'Primary_Desc':
      'Commercial',
      'Secondary_Desc':
      'Emergency / Rescue Service',
      'Tertiary_Desc':
      'Ambulance Station',
      'Quaternary_Desc':
      'Air Sea Rescue / Air Ambulance'
  }, {
      'Concatenated': 'CX04',
      'Class_Desc': 'Lifeboat Services / Station',
      'Primary_Code': 'C',
      'Secondary_Code': 'X',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Emergency / Rescue Service',
      'Tertiary_Desc': 'Lifeboat Services / Station',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CX05',
      'Class_Desc': 'Coastguard Rescue / Lookout / Station',
      'Primary_Code': 'C',
      'Secondary_Code': 'X',
      'Tertiary_Code': '5',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Emergency / Rescue Service',
      'Tertiary_Desc': 'Coastguard Rescue / Lookout / Station',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CX06',
      'Class_Desc': 'Mountain Rescue Station',
      'Primary_Code': 'C',
      'Secondary_Code': 'X',
      'Tertiary_Code': '6',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Emergency / Rescue Service',
      'Tertiary_Desc': 'Mountain Rescue Station',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CX07',
      'Class_Desc': 'Lighthouse',
      'Primary_Code': 'C',
      'Secondary_Code': 'X',
      'Tertiary_Code': '7',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Emergency / Rescue Service',
      'Tertiary_Desc': 'Lighthouse',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CX08',
      'Class_Desc': 'Police Box / Kiosk',
      'Primary_Code': 'C',
      'Secondary_Code': 'X',
      'Tertiary_Code': '8',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Emergency / Rescue Service',
      'Tertiary_Desc': 'Police Box / Kiosk',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CZ',
      'Class_Desc': 'Information',
      'Primary_Code': 'C',
      'Secondary_Code': 'Z',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Information',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CZ01',
      'Class_Desc': 'Advertising Hoarding',
      'Primary_Code': 'C',
      'Secondary_Code': 'Z',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Information',
      'Tertiary_Desc': 'Advertising Hoarding',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CZ02',
      'Class_Desc': 'Tourist Information Signage',
      'Primary_Code': 'C',
      'Secondary_Code': 'Z',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Information',
      'Tertiary_Desc': 'Tourist Information Signage',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'CZ02VI',
      'Class_Desc': 'Visitor Information',
      'Primary_Code': 'C',
      'Secondary_Code': 'Z',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'VI',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Information',
      'Tertiary_Desc': 'Tourist Information Signage',
      'Quaternary_Desc': 'Visitor Information'
  }, {
      'Concatenated': 'CZ03',
      'Class_Desc': 'Traffic Information Signage',
      'Primary_Code': 'C',
      'Secondary_Code': 'Z',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Commercial',
      'Secondary_Desc': 'Information',
      'Tertiary_Desc': 'Traffic Information Signage',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'L',
      'Class_Desc': 'Land',
      'Primary_Code': 'L',
      'Secondary_Code': '',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': '',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LA',
      'Class_Desc':
      'Agricultural - Applicable to land in farm ownership and not run as a separate business enterprise',
      'Primary_Code': 'L',
      'Secondary_Code': 'A',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc':
      'Agricultural - Applicable to land in farm ownership and not run as a separate business enterprise',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LA01',
      'Class_Desc': 'Grazing Land',
      'Primary_Code': 'L',
      'Secondary_Code': 'A',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc':
      'Agricultural - Applicable to land in farm ownership and not run as a separate business enterprise',
      'Tertiary_Desc': 'Grazing Land',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LA02',
      'Class_Desc': 'Permanent Crop / Crop Rotation',
      'Primary_Code': 'L',
      'Secondary_Code': 'A',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc':
      'Agricultural - Applicable to land in farm ownership and not run as a separate business enterprise',
      'Tertiary_Desc': 'Permanent Crop / Crop Rotation',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LA02OC',
      'Class_Desc': 'Orchard',
      'Primary_Code': 'L',
      'Secondary_Code': 'A',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'OC',
      'Primary_Desc': 'Land',
      'Secondary_Desc':
      'Agricultural - Applicable to land in farm ownership and not run as a separate business enterprise',
      'Tertiary_Desc': 'Permanent Crop / Crop Rotation',
      'Quaternary_Desc': 'Orchard'
  }, {
      'Concatenated': 'LB',
      'Class_Desc': 'Ancillary Building',
      'Primary_Code': 'L',
      'Secondary_Code': 'B',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Ancillary Building',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LB99AV',
      'Class_Desc': 'Aviary / Dovecot / Cage',
      'Primary_Code': 'L',
      'Secondary_Code': 'B',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'AV',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Ancillary Building',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Aviary / Dovecot / Cage'
  }, {
      'Concatenated': 'LB99BD',
      'Class_Desc': 'Bandstand',
      'Primary_Code': 'L',
      'Secondary_Code': 'B',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'BD',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Ancillary Building',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Bandstand'
  }, {
      'Concatenated':
      'LB99PI',
      'Class_Desc':
      'Pavilion / Changing Room',
      'Primary_Code':
      'L',
      'Secondary_Code':
      'B',
      'Tertiary_Code':
      '99',
      'Quaternary_Code':
      'PI',
      'Primary_Desc':
      'Land',
      'Secondary_Desc':
      'Ancillary Building',
      'Tertiary_Desc':
      '',
      'Quaternary_Desc':
      'Pavilion / Changing Room'
  }, {
      'Concatenated':
      'LB99SV',
      'Class_Desc':
      'Sports Viewing Structure',
      'Primary_Code':
      'L',
      'Secondary_Code':
      'B',
      'Tertiary_Code':
      '99',
      'Quaternary_Code':
      'SV',
      'Primary_Desc':
      'Land',
      'Secondary_Desc':
      'Ancillary Building',
      'Tertiary_Desc':
      '',
      'Quaternary_Desc':
      'Sports Viewing Structure'
  }, {
      'Concatenated': 'LC',
      'Class_Desc': 'Burial Ground',
      'Primary_Code': 'L',
      'Secondary_Code': 'C',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Burial Ground',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LC01',
      'Class_Desc': 'Historic / Disused Cemetery / Graveyard',
      'Primary_Code': 'L',
      'Secondary_Code': 'C',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Burial Ground',
      'Tertiary_Desc': 'Historic / Disused Cemetery / Graveyard',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LD',
      'Class_Desc': 'Development',
      'Primary_Code': 'L',
      'Secondary_Code': 'D',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Development',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LD01',
      'Class_Desc': 'Development Site',
      'Primary_Code': 'L',
      'Secondary_Code': 'D',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Development',
      'Tertiary_Desc': 'Development Site',
      'Quaternary_Desc': ''
  }, {
      'Concatenated':
      'LD01CC',
      'Class_Desc':
      'Commercial Construction Site',
      'Primary_Code':
      'L',
      'Secondary_Code':
      'D',
      'Tertiary_Code':
      '1',
      'Quaternary_Code':
      'CC',
      'Primary_Desc':
      'Land',
      'Secondary_Desc':
      'Development',
      'Tertiary_Desc':
      'Development Site',
      'Quaternary_Desc':
      'Commercial Construction Site'
  }, {
      'Concatenated':
      'LD01CO',
      'Class_Desc':
      'Community Construction Site',
      'Primary_Code':
      'L',
      'Secondary_Code':
      'D',
      'Tertiary_Code':
      '1',
      'Quaternary_Code':
      'CO',
      'Primary_Desc':
      'Land',
      'Secondary_Desc':
      'Development',
      'Tertiary_Desc':
      'Development Site',
      'Quaternary_Desc':
      'Community Construction Site'
  }, {
      'Concatenated':
      'LD01RN',
      'Class_Desc':
      'Residential Construction Site',
      'Primary_Code':
      'L',
      'Secondary_Code':
      'D',
      'Tertiary_Code':
      '1',
      'Quaternary_Code':
      'RN',
      'Primary_Desc':
      'Land',
      'Secondary_Desc':
      'Development',
      'Tertiary_Desc':
      'Development Site',
      'Quaternary_Desc':
      'Residential Construction Site'
  }, {
      'Concatenated':
      'LD01TC',
      'Class_Desc':
      'Transport Construction Site',
      'Primary_Code':
      'L',
      'Secondary_Code':
      'D',
      'Tertiary_Code':
      '1',
      'Quaternary_Code':
      'TC',
      'Primary_Desc':
      'Land',
      'Secondary_Desc':
      'Development',
      'Tertiary_Desc':
      'Development Site',
      'Quaternary_Desc':
      'Transport Construction Site'
  }, {
      'Concatenated': 'LF',
      'Class_Desc': 'Forestry',
      'Primary_Code': 'L',
      'Secondary_Code': 'F',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Forestry',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LF02',
      'Class_Desc': 'Forest / Arboretum / Pinetum (Managed / Unmanaged)',
      'Primary_Code': 'L',
      'Secondary_Code': 'F',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Forestry',
      'Tertiary_Desc': 'Forest / Arboretum / Pinetum (Managed / Unmanaged)',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LF02AU',
      'Class_Desc': 'Arboretum',
      'Primary_Code': 'L',
      'Secondary_Code': 'F',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'AU',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Forestry',
      'Tertiary_Desc': 'Forest / Arboretum / Pinetum (Managed / Unmanaged)',
      'Quaternary_Desc': 'Arboretum'
  }, {
      'Concatenated': 'LF03',
      'Class_Desc': 'Woodland',
      'Primary_Code': 'L',
      'Secondary_Code': 'F',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Forestry',
      'Tertiary_Desc': 'Woodland',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LL',
      'Class_Desc': 'Allotment',
      'Primary_Code': 'L',
      'Secondary_Code': 'L',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Allotment',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LM',
      'Class_Desc': 'Amenity - Open areas not attracting visitors',
      'Primary_Code': 'L',
      'Secondary_Code': 'M',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Amenity - Open areas not attracting visitors',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LM01',
      'Class_Desc': 'Landscaped Roundabout',
      'Primary_Code': 'L',
      'Secondary_Code': 'M',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Amenity - Open areas not attracting visitors',
      'Tertiary_Desc': 'Landscaped Roundabout',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LM02',
      'Class_Desc': 'Verge / Central Reservation',
      'Primary_Code': 'L',
      'Secondary_Code': 'M',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Amenity - Open areas not attracting visitors',
      'Tertiary_Desc': 'Verge / Central Reservation',
      'Quaternary_Desc': ''
  }, {
      'Concatenated':
      'LM02NV',
      'Class_Desc':
      'Natural Central Reservation',
      'Primary_Code':
      'L',
      'Secondary_Code':
      'M',
      'Tertiary_Code':
      '2',
      'Quaternary_Code':
      'NV',
      'Primary_Desc':
      'Land',
      'Secondary_Desc':
      'Amenity - Open areas not attracting visitors',
      'Tertiary_Desc':
      'Verge / Central Reservation',
      'Quaternary_Desc':
      'Natural Central Reservation'
  }, {
      'Concatenated': 'LM02VE',
      'Class_Desc': 'Natural Verge',
      'Primary_Code': 'L',
      'Secondary_Code': 'M',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'VE',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Amenity - Open areas not attracting visitors',
      'Tertiary_Desc': 'Verge / Central Reservation',
      'Quaternary_Desc': 'Natural Verge'
  }, {
      'Concatenated': 'LM03',
      'Class_Desc': 'Maintained Amenity Land',
      'Primary_Code': 'L',
      'Secondary_Code': 'M',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Amenity - Open areas not attracting visitors',
      'Tertiary_Desc': 'Maintained Amenity Land',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LM04',
      'Class_Desc': 'Maintained Surfaced Area',
      'Primary_Code': 'L',
      'Secondary_Code': 'M',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Amenity - Open areas not attracting visitors',
      'Tertiary_Desc': 'Maintained Surfaced Area',
      'Quaternary_Desc': ''
  }, {
      'Concatenated':
      'LM04MV',
      'Class_Desc':
      'Made Central Reservation',
      'Primary_Code':
      'L',
      'Secondary_Code':
      'M',
      'Tertiary_Code':
      '4',
      'Quaternary_Code':
      'MV',
      'Primary_Desc':
      'Land',
      'Secondary_Desc':
      'Amenity - Open areas not attracting visitors',
      'Tertiary_Desc':
      'Maintained Surfaced Area',
      'Quaternary_Desc':
      'Made Central Reservation'
  }, {
      'Concatenated': 'LM04PV',
      'Class_Desc': 'Pavement',
      'Primary_Code': 'L',
      'Secondary_Code': 'M',
      'Tertiary_Code': '4',
      'Quaternary_Code': 'PV',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Amenity - Open areas not attracting visitors',
      'Tertiary_Desc': 'Maintained Surfaced Area',
      'Quaternary_Desc': 'Pavement'
  }, {
      'Concatenated': 'LO',
      'Class_Desc': 'Open Space',
      'Primary_Code': 'L',
      'Secondary_Code': 'O',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Open Space',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LO01',
      'Class_Desc': 'Heath / Moorland',
      'Primary_Code': 'L',
      'Secondary_Code': 'O',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Open Space',
      'Tertiary_Desc': 'Heath / Moorland',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LP',
      'Class_Desc': 'Park',
      'Primary_Code': 'L',
      'Secondary_Code': 'P',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Park',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LP01',
      'Class_Desc': 'Public Park / Garden',
      'Primary_Code': 'L',
      'Secondary_Code': 'P',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Park',
      'Tertiary_Desc': 'Public Park / Garden',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LP02',
      'Class_Desc': 'Public Open Space / Nature Reserve',
      'Primary_Code': 'L',
      'Secondary_Code': 'P',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Park',
      'Tertiary_Desc': 'Public Open Space / Nature Reserve',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LP03',
      'Class_Desc': 'Playground',
      'Primary_Code': 'L',
      'Secondary_Code': 'P',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Park',
      'Tertiary_Desc': 'Playground',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LP03PA',
      'Class_Desc': 'Play Area',
      'Primary_Code': 'L',
      'Secondary_Code': 'P',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'PA',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Park',
      'Tertiary_Desc': 'Playground',
      'Quaternary_Desc': 'Play Area'
  }, {
      'Concatenated': 'LP03PD',
      'Class_Desc': 'Paddling Pool',
      'Primary_Code': 'L',
      'Secondary_Code': 'P',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'PD',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Park',
      'Tertiary_Desc': 'Playground',
      'Quaternary_Desc': 'Paddling Pool'
  }, {
      'Concatenated': 'LP04',
      'Class_Desc': 'Private Park / Garden',
      'Primary_Code': 'L',
      'Secondary_Code': 'P',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Park',
      'Tertiary_Desc': 'Private Park / Garden',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LU',
      'Class_Desc': 'Unused Land',
      'Primary_Code': 'L',
      'Secondary_Code': 'U',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Unused Land',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LU01',
      'Class_Desc': 'Vacant / Derelict Land',
      'Primary_Code': 'L',
      'Secondary_Code': 'U',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Unused Land',
      'Tertiary_Desc': 'Vacant / Derelict Land',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LW',
      'Class_Desc': 'Water',
      'Primary_Code': 'L',
      'Secondary_Code': 'W',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Water',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LW01',
      'Class_Desc': 'Lake / Reservoir',
      'Primary_Code': 'L',
      'Secondary_Code': 'W',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Water',
      'Tertiary_Desc': 'Lake / Reservoir',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LW01BP',
      'Class_Desc': 'Balancing Pond',
      'Primary_Code': 'L',
      'Secondary_Code': 'W',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'BP',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Water',
      'Tertiary_Desc': 'Lake / Reservoir',
      'Quaternary_Desc': 'Balancing Pond'
  }, {
      'Concatenated': 'LW01BV',
      'Class_Desc': 'Buried Reservoir',
      'Primary_Code': 'L',
      'Secondary_Code': 'W',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'BV',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Water',
      'Tertiary_Desc': 'Lake / Reservoir',
      'Quaternary_Desc': 'Buried Reservoir'
  }, {
      'Concatenated': 'LW02',
      'Class_Desc': 'Named Pond',
      'Primary_Code': 'L',
      'Secondary_Code': 'W',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Water',
      'Tertiary_Desc': 'Named Pond',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LW02DE',
      'Class_Desc': 'Dew Pond',
      'Primary_Code': 'L',
      'Secondary_Code': 'W',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'DE',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Water',
      'Tertiary_Desc': 'Named Pond',
      'Quaternary_Desc': 'Dew Pond'
  }, {
      'Concatenated': 'LW02DP',
      'Class_Desc': 'Decoy Pond',
      'Primary_Code': 'L',
      'Secondary_Code': 'W',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'DP',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Water',
      'Tertiary_Desc': 'Named Pond',
      'Quaternary_Desc': 'Decoy Pond'
  }, {
      'Concatenated': 'LW02IW',
      'Class_Desc': 'Static Water',
      'Primary_Code': 'L',
      'Secondary_Code': 'W',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'IW',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Water',
      'Tertiary_Desc': 'Named Pond',
      'Quaternary_Desc': 'Static Water'
  }, {
      'Concatenated': 'LW03',
      'Class_Desc': 'Waterway',
      'Primary_Code': 'L',
      'Secondary_Code': 'W',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Water',
      'Tertiary_Desc': 'Waterway',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'LW03DR',
      'Class_Desc': 'Drain',
      'Primary_Code': 'L',
      'Secondary_Code': 'W',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'DR',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Water',
      'Tertiary_Desc': 'Waterway',
      'Quaternary_Desc': 'Drain'
  }, {
      'Concatenated': 'LW03LR',
      'Class_Desc': 'Leats / Races',
      'Primary_Code': 'L',
      'Secondary_Code': 'W',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'LR',
      'Primary_Desc': 'Land',
      'Secondary_Desc': 'Water',
      'Tertiary_Desc': 'Waterway',
      'Quaternary_Desc': 'Leats / Races'
  }, {
      'Concatenated': 'M',
      'Class_Desc': 'Military',
      'Primary_Code': 'M',
      'Secondary_Code': '',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Military',
      'Secondary_Desc': '',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'MA',
      'Class_Desc': 'Army',
      'Primary_Code': 'M',
      'Secondary_Code': 'A',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Military',
      'Secondary_Desc': 'Army',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'MA99AG',
      'Class_Desc': 'Army Military Storage',
      'Primary_Code': 'M',
      'Secondary_Code': 'A',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'AG',
      'Primary_Desc': 'Military',
      'Secondary_Desc': 'Army',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Army Military Storage'
  }, {
      'Concatenated': 'MA99AR',
      'Class_Desc': 'Army Military Range',
      'Primary_Code': 'M',
      'Secondary_Code': 'A',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'AR',
      'Primary_Desc': 'Military',
      'Secondary_Desc': 'Army',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Army Military Range'
  }, {
      'Concatenated': 'MA99AS',
      'Class_Desc': 'Army Site',
      'Primary_Code': 'M',
      'Secondary_Code': 'A',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'AS',
      'Primary_Desc': 'Military',
      'Secondary_Desc': 'Army',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Army Site'
  }, {
      'Concatenated': 'MA99AT',
      'Class_Desc': 'Army Military Training',
      'Primary_Code': 'M',
      'Secondary_Code': 'A',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'AT',
      'Primary_Desc': 'Military',
      'Secondary_Desc': 'Army',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Army Military Training'
  }, {
      'Concatenated': 'MB',
      'Class_Desc': 'Ancillary Building',
      'Primary_Code': 'M',
      'Secondary_Code': 'B',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Military',
      'Secondary_Desc': 'Ancillary Building',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'MB99TG',
      'Class_Desc': 'Military Target',
      'Primary_Code': 'M',
      'Secondary_Code': 'B',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'TG',
      'Primary_Desc': 'Military',
      'Secondary_Desc': 'Ancillary Building',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Military Target'
  }, {
      'Concatenated': 'MF',
      'Class_Desc': 'Air Force',
      'Primary_Code': 'M',
      'Secondary_Code': 'F',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Military',
      'Secondary_Desc': 'Air Force',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated':
      'MF99UG',
      'Class_Desc':
      'Air Force Military Storage',
      'Primary_Code':
      'M',
      'Secondary_Code':
      'F',
      'Tertiary_Code':
      '99',
      'Quaternary_Code':
      'UG',
      'Primary_Desc':
      'Military',
      'Secondary_Desc':
      'Air Force',
      'Tertiary_Desc':
      '',
      'Quaternary_Desc':
      'Air Force Military Storage'
  }, {
      'Concatenated':
      'MF99UR',
      'Class_Desc':
      'Air Force Military Range',
      'Primary_Code':
      'M',
      'Secondary_Code':
      'F',
      'Tertiary_Code':
      '99',
      'Quaternary_Code':
      'UR',
      'Primary_Desc':
      'Military',
      'Secondary_Desc':
      'Air Force',
      'Tertiary_Desc':
      '',
      'Quaternary_Desc':
      'Air Force Military Range'
  }, {
      'Concatenated': 'MF99US',
      'Class_Desc': 'Air Force Site',
      'Primary_Code': 'M',
      'Secondary_Code': 'F',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'US',
      'Primary_Desc': 'Military',
      'Secondary_Desc': 'Air Force',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Air Force Site'
  }, {
      'Concatenated':
      'MF99UT',
      'Class_Desc':
      'Air Force Military Training',
      'Primary_Code':
      'M',
      'Secondary_Code':
      'F',
      'Tertiary_Code':
      '99',
      'Quaternary_Code':
      'UT',
      'Primary_Desc':
      'Military',
      'Secondary_Desc':
      'Air Force',
      'Tertiary_Desc':
      '',
      'Quaternary_Desc':
      'Air Force Military Training'
  }, {
      'Concatenated': 'MG',
      'Class_Desc': 'Defence Estates',
      'Primary_Code': 'M',
      'Secondary_Code': 'G',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Military',
      'Secondary_Desc': 'Defence Estates',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'MN',
      'Class_Desc': 'Navy',
      'Primary_Code': 'M',
      'Secondary_Code': 'N',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Military',
      'Secondary_Desc': 'Navy',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'MN99VG',
      'Class_Desc': 'Naval Military Storage',
      'Primary_Code': 'M',
      'Secondary_Code': 'N',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'VG',
      'Primary_Desc': 'Military',
      'Secondary_Desc': 'Navy',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Naval Military Storage'
  }, {
      'Concatenated': 'MN99VR',
      'Class_Desc': 'Naval Military Range',
      'Primary_Code': 'M',
      'Secondary_Code': 'N',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'VR',
      'Primary_Desc': 'Military',
      'Secondary_Desc': 'Navy',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Naval Military Range'
  }, {
      'Concatenated': 'MN99VS',
      'Class_Desc': 'Naval Site',
      'Primary_Code': 'M',
      'Secondary_Code': 'N',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'VS',
      'Primary_Desc': 'Military',
      'Secondary_Desc': 'Navy',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Naval Site'
  }, {
      'Concatenated': 'MN99VT',
      'Class_Desc': 'Naval Military Training',
      'Primary_Code': 'M',
      'Secondary_Code': 'N',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'VT',
      'Primary_Desc': 'Military',
      'Secondary_Desc': 'Navy',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Naval Military Training'
  }, {
      'Concatenated': 'O',
      'Class_Desc': 'Other (Ordnance Survey Only)',
      'Primary_Code': 'O',
      'Secondary_Code': '',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': '',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OA',
      'Class_Desc': 'Aid To Navigation',
      'Primary_Code': 'O',
      'Secondary_Code': 'A',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Aid To Navigation',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OA01',
      'Class_Desc': 'Aid To Aeronautical Navigation',
      'Primary_Code': 'O',
      'Secondary_Code': 'A',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Aid To Navigation',
      'Tertiary_Desc': 'Aid To Aeronautical Navigation',
      'Quaternary_Desc': ''
  }, {
      'Concatenated':
      'OA01AL',
      'Class_Desc':
      'Aeronautical Navigation Beacon / Light',
      'Primary_Code':
      'O',
      'Secondary_Code':
      'A',
      'Tertiary_Code':
      '1',
      'Quaternary_Code':
      'AL',
      'Primary_Desc':
      'Other (Ordnance Survey Only)',
      'Secondary_Desc':
      'Aid To Navigation',
      'Tertiary_Desc':
      'Aid To Aeronautical Navigation',
      'Quaternary_Desc':
      'Aeronautical Navigation Beacon / Light'
  }, {
      'Concatenated': 'OA01LL',
      'Class_Desc': 'Landing Light',
      'Primary_Code': 'O',
      'Secondary_Code': 'A',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'LL',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Aid To Navigation',
      'Tertiary_Desc': 'Aid To Aeronautical Navigation',
      'Quaternary_Desc': 'Landing Light'
  }, {
      'Concatenated': 'OA01SQ',
      'Class_Desc': 'Signal Square',
      'Primary_Code': 'O',
      'Secondary_Code': 'A',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'SQ',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Aid To Navigation',
      'Tertiary_Desc': 'Aid To Aeronautical Navigation',
      'Quaternary_Desc': 'Signal Square'
  }, {
      'Concatenated': 'OA01WK',
      'Class_Desc': 'Wind Sock / Wind Tee',
      'Primary_Code': 'O',
      'Secondary_Code': 'A',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'WK',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Aid To Navigation',
      'Tertiary_Desc': 'Aid To Aeronautical Navigation',
      'Quaternary_Desc': 'Wind Sock / Wind Tee'
  }, {
      'Concatenated': 'OA02',
      'Class_Desc': 'Aid To Nautical Navigation',
      'Primary_Code': 'O',
      'Secondary_Code': 'A',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Aid To Navigation',
      'Tertiary_Desc': 'Aid To Nautical Navigation',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OA02DM',
      'Class_Desc': 'Daymark',
      'Primary_Code': 'O',
      'Secondary_Code': 'A',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'DM',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Aid To Navigation',
      'Tertiary_Desc': 'Aid To Nautical Navigation',
      'Quaternary_Desc': 'Daymark'
  }, {
      'Concatenated': 'OA02FG',
      'Class_Desc': 'Fog Horn Warning',
      'Primary_Code': 'O',
      'Secondary_Code': 'A',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'FG',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Aid To Navigation',
      'Tertiary_Desc': 'Aid To Nautical Navigation',
      'Quaternary_Desc': 'Fog Horn Warning'
  }, {
      'Concatenated':
      'OA02NL',
      'Class_Desc':
      'Nautical Navigation Beacon / Light',
      'Primary_Code':
      'O',
      'Secondary_Code':
      'A',
      'Tertiary_Code':
      '2',
      'Quaternary_Code':
      'NL',
      'Primary_Desc':
      'Other (Ordnance Survey Only)',
      'Secondary_Desc':
      'Aid To Navigation',
      'Tertiary_Desc':
      'Aid To Nautical Navigation',
      'Quaternary_Desc':
      'Nautical Navigation Beacon / Light'
  }, {
      'Concatenated': 'OA03',
      'Class_Desc': 'Aid To Road Navigation',
      'Primary_Code': 'O',
      'Secondary_Code': 'A',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Aid To Navigation',
      'Tertiary_Desc': 'Aid To Road Navigation',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OA03GP',
      'Class_Desc': 'Guide Post',
      'Primary_Code': 'O',
      'Secondary_Code': 'A',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'GP',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Aid To Navigation',
      'Tertiary_Desc': 'Aid To Road Navigation',
      'Quaternary_Desc': 'Guide Post'
  }, {
      'Concatenated': 'OC',
      'Class_Desc': 'Coastal Protection / Flood Prevention',
      'Primary_Code': 'O',
      'Secondary_Code': 'C',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Coastal Protection / Flood Prevention',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OC01',
      'Class_Desc': 'Boulder Wall / Sea Wall',
      'Primary_Code': 'O',
      'Secondary_Code': 'C',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Coastal Protection / Flood Prevention',
      'Tertiary_Desc': 'Boulder Wall / Sea Wall',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OC02',
      'Class_Desc': 'Flood Gate / Flood Sluice Gate / Flood Valve',
      'Primary_Code': 'O',
      'Secondary_Code': 'C',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Coastal Protection / Flood Prevention',
      'Tertiary_Desc': 'Flood Gate / Flood Sluice Gate / Flood Valve',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OC03',
      'Class_Desc': 'Groyne',
      'Primary_Code': 'O',
      'Secondary_Code': 'C',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Coastal Protection / Flood Prevention',
      'Tertiary_Desc': 'Groyne',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OC04',
      'Class_Desc': 'Rip-Rap',
      'Primary_Code': 'O',
      'Secondary_Code': 'C',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Coastal Protection / Flood Prevention',
      'Tertiary_Desc': 'Rip-Rap',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OE',
      'Class_Desc': 'Emergency Support',
      'Primary_Code': 'O',
      'Secondary_Code': 'E',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Emergency Support',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OE01',
      'Class_Desc': 'Beach Office / First Aid Facility',
      'Primary_Code': 'O',
      'Secondary_Code': 'E',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Emergency Support',
      'Tertiary_Desc': 'Beach Office / First Aid Facility',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OE02',
      'Class_Desc': 'Emergency Telephone (Non Motorway)',
      'Primary_Code': 'O',
      'Secondary_Code': 'E',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Emergency Support',
      'Tertiary_Desc': 'Emergency Telephone (Non Motorway)',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OE03',
      'Class_Desc':
      'Fire Alarm Structure / Fire Observation Tower / Fire Beater Facility',
      'Primary_Code': 'O',
      'Secondary_Code': 'E',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Emergency Support',
      'Tertiary_Desc':
      'Fire Alarm Structure / Fire Observation Tower / Fire Beater Facility',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OE04',
      'Class_Desc':
      'Emergency Equipment Point / Emergency Siren / Warning Flag',
      'Primary_Code': 'O',
      'Secondary_Code': 'E',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Emergency Support',
      'Tertiary_Desc':
      'Emergency Equipment Point / Emergency Siren / Warning Flag',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OE05',
      'Class_Desc': 'Lifeguard Facility',
      'Primary_Code': 'O',
      'Secondary_Code': 'E',
      'Tertiary_Code': '5',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Emergency Support',
      'Tertiary_Desc': 'Lifeguard Facility',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OE06',
      'Class_Desc': 'LIfe / Belt / Buoy / Float / Jacket / Safety Rope',
      'Primary_Code': 'O',
      'Secondary_Code': 'E',
      'Tertiary_Code': '6',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Emergency Support',
      'Tertiary_Desc': 'LIfe / Belt / Buoy / Float / Jacket / Safety Rope',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OF',
      'Class_Desc': 'Street Furniture',
      'Primary_Code': 'O',
      'Secondary_Code': 'F',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Street Furniture',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OG',
      'Class_Desc': 'Agricultural Support Objects',
      'Primary_Code': 'O',
      'Secondary_Code': 'G',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Agricultural Support Objects',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OG01',
      'Class_Desc': 'Fish Ladder / Lock / Pen / Trap',
      'Primary_Code': 'O',
      'Secondary_Code': 'G',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Agricultural Support Objects',
      'Tertiary_Desc': 'Fish Ladder / Lock / Pen / Trap',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OG02',
      'Class_Desc': 'Livestock Pen / Dip',
      'Primary_Code': 'O',
      'Secondary_Code': 'G',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Agricultural Support Objects',
      'Tertiary_Desc': 'Livestock Pen / Dip',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OG03',
      'Class_Desc': 'Currick',
      'Primary_Code': 'O',
      'Secondary_Code': 'G',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Agricultural Support Objects',
      'Tertiary_Desc': 'Currick',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OG04',
      'Class_Desc': 'Slurry Bed / Pit',
      'Primary_Code': 'O',
      'Secondary_Code': 'G',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Agricultural Support Objects',
      'Tertiary_Desc': 'Slurry Bed / Pit',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OH',
      'Class_Desc': 'Historical Site / Object',
      'Primary_Code': 'O',
      'Secondary_Code': 'H',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Historical Site / Object',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OH01',
      'Class_Desc': 'Historic Structure / Object',
      'Primary_Code': 'O',
      'Secondary_Code': 'H',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Historical Site / Object',
      'Tertiary_Desc': 'Historic Structure / Object',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OI',
      'Class_Desc': 'Industrial Support',
      'Primary_Code': 'O',
      'Secondary_Code': 'I',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Industrial Support',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OI01',
      'Class_Desc': 'Adit / Incline / Level',
      'Primary_Code': 'O',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Industrial Support',
      'Tertiary_Desc': 'Adit / Incline / Level',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OI02',
      'Class_Desc': 'Caisson / Dry Dock / Grid',
      'Primary_Code': 'O',
      'Secondary_Code': 'I',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Industrial Support',
      'Tertiary_Desc': 'Caisson / Dry Dock / Grid',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OI03',
      'Class_Desc': 'Channel / Conveyor / Conduit / Pipe',
      'Primary_Code': 'O',
      'Secondary_Code': 'I',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Industrial Support',
      'Tertiary_Desc': 'Channel / Conveyor / Conduit / Pipe',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OI04',
      'Class_Desc': 'Chimney / Flue',
      'Primary_Code': 'O',
      'Secondary_Code': 'I',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Industrial Support',
      'Tertiary_Desc': 'Chimney / Flue',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OI05',
      'Class_Desc': 'Crane / Hoist / Winch / Material Elevator',
      'Primary_Code': 'O',
      'Secondary_Code': 'I',
      'Tertiary_Code': '5',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Industrial Support',
      'Tertiary_Desc': 'Crane / Hoist / Winch / Material Elevator',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OI06',
      'Class_Desc': 'Flare Stack',
      'Primary_Code': 'O',
      'Secondary_Code': 'I',
      'Tertiary_Code': '6',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Industrial Support',
      'Tertiary_Desc': 'Flare Stack',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OI07',
      'Class_Desc': 'Hopper / Silo / Cistern / Tank',
      'Primary_Code': 'O',
      'Secondary_Code': 'I',
      'Tertiary_Code': '7',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Industrial Support',
      'Tertiary_Desc': 'Hopper / Silo / Cistern / Tank',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OI08',
      'Class_Desc':
      'Grab / Skip / Other Industrial Waste Machinery / Discharging',
      'Primary_Code': 'O',
      'Secondary_Code': 'I',
      'Tertiary_Code': '8',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Industrial Support',
      'Tertiary_Desc':
      'Grab / Skip / Other Industrial Waste Machinery / Discharging',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OI09',
      'Class_Desc': 'Kiln / Oven / Smelter',
      'Primary_Code': 'O',
      'Secondary_Code': 'I',
      'Tertiary_Code': '9',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Industrial Support',
      'Tertiary_Desc': 'Kiln / Oven / Smelter',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OI10',
      'Class_Desc': 'Manhole / Shaft',
      'Primary_Code': 'O',
      'Secondary_Code': 'I',
      'Tertiary_Code': '10',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Industrial Support',
      'Tertiary_Desc': 'Manhole / Shaft',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OI11',
      'Class_Desc': 'Industrial Overflow / Sluice / Valve / Valve Housing',
      'Primary_Code': 'O',
      'Secondary_Code': 'I',
      'Tertiary_Code': '11',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Industrial Support',
      'Tertiary_Desc': 'Industrial Overflow / Sluice / Valve / Valve Housing',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OI12',
      'Class_Desc': 'Cooling Tower',
      'Primary_Code': 'O',
      'Secondary_Code': 'I',
      'Tertiary_Code': '12',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Industrial Support',
      'Tertiary_Desc': 'Cooling Tower',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OI13',
      'Class_Desc': 'Solar Panel / Waterwheel',
      'Primary_Code': 'O',
      'Secondary_Code': 'I',
      'Tertiary_Code': '13',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Industrial Support',
      'Tertiary_Desc': 'Solar Panel / Waterwheel',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OI14',
      'Class_Desc': 'Telephone Pole / Post',
      'Primary_Code': 'O',
      'Secondary_Code': 'I',
      'Tertiary_Code': '14',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Industrial Support',
      'Tertiary_Desc': 'Telephone Pole / Post',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OI15',
      'Class_Desc': 'Electricity Distribution Pole / Pylon',
      'Primary_Code': 'O',
      'Secondary_Code': 'I',
      'Tertiary_Code': '15',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Industrial Support',
      'Tertiary_Desc': 'Electricity Distribution Pole / Pylon',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ON',
      'Class_Desc': 'Significant Natural Object',
      'Primary_Code': 'O',
      'Secondary_Code': 'N',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Significant Natural Object',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ON01',
      'Class_Desc': 'Boundary / Significant / Historic Tree / Pollard',
      'Primary_Code': 'O',
      'Secondary_Code': 'N',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Significant Natural Object',
      'Tertiary_Desc': 'Boundary / Significant / Historic Tree / Pollard',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ON02',
      'Class_Desc': 'Boundary / Significant Rock / Boulder',
      'Primary_Code': 'O',
      'Secondary_Code': 'N',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Significant Natural Object',
      'Tertiary_Desc': 'Boundary / Significant Rock / Boulder',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ON03',
      'Class_Desc': 'Natural Hole (Blow / Shake / Swallow)',
      'Primary_Code': 'O',
      'Secondary_Code': 'N',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Significant Natural Object',
      'Tertiary_Desc': 'Natural Hole (Blow / Shake / Swallow)',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OO',
      'Class_Desc': 'Ornamental / Cultural Object',
      'Primary_Code': 'O',
      'Secondary_Code': 'O',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Ornamental / Cultural Object',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OO02',
      'Class_Desc': 'Mausoleum / Tomb / Grave',
      'Primary_Code': 'O',
      'Secondary_Code': 'O',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Ornamental / Cultural Object',
      'Tertiary_Desc': 'Mausoleum / Tomb / Grave',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OO03',
      'Class_Desc': 'Simple Ornamental Object',
      'Primary_Code': 'O',
      'Secondary_Code': 'O',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Ornamental / Cultural Object',
      'Tertiary_Desc': 'Simple Ornamental Object',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OO04',
      'Class_Desc': 'Maze',
      'Primary_Code': 'O',
      'Secondary_Code': 'O',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Ornamental / Cultural Object',
      'Tertiary_Desc': 'Maze',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OP',
      'Class_Desc': 'Sport / Leisure Support',
      'Primary_Code': 'O',
      'Secondary_Code': 'P',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Sport / Leisure Support',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OP01',
      'Class_Desc': 'Butt / Hide',
      'Primary_Code': 'O',
      'Secondary_Code': 'P',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Sport / Leisure Support',
      'Tertiary_Desc': 'Butt / Hide',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OP02',
      'Class_Desc': 'Gallop / Ride',
      'Primary_Code': 'O',
      'Secondary_Code': 'P',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Sport / Leisure Support',
      'Tertiary_Desc': 'Gallop / Ride',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OP03',
      'Class_Desc': 'Miniature Railway',
      'Primary_Code': 'O',
      'Secondary_Code': 'P',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Sport / Leisure Support',
      'Tertiary_Desc': 'Miniature Railway',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OR',
      'Class_Desc': 'Royal Mail Infrastructure',
      'Primary_Code': 'O',
      'Secondary_Code': 'R',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Royal Mail Infrastructure',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OR01',
      'Class_Desc': 'Postal Box',
      'Primary_Code': 'O',
      'Secondary_Code': 'R',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Royal Mail Infrastructure',
      'Tertiary_Desc': 'Postal Box',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OR02',
      'Class_Desc': 'Postal Delivery Box / Pouch',
      'Primary_Code': 'O',
      'Secondary_Code': 'R',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Royal Mail Infrastructure',
      'Tertiary_Desc': 'Postal Delivery Box / Pouch',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OR03',
      'Class_Desc': 'PO Box',
      'Primary_Code': 'O',
      'Secondary_Code': 'R',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Royal Mail Infrastructure',
      'Tertiary_Desc': 'PO Box',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OR04',
      'Class_Desc': 'Additional Mail / Packet Addressee',
      'Primary_Code': 'O',
      'Secondary_Code': 'R',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Royal Mail Infrastructure',
      'Tertiary_Desc': 'Additional Mail / Packet Addressee',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OS',
      'Class_Desc': 'Scientific / Observation Support',
      'Primary_Code': 'O',
      'Secondary_Code': 'S',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Scientific / Observation Support',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OS01',
      'Class_Desc': 'Meteorological Station / Equipment',
      'Primary_Code': 'O',
      'Secondary_Code': 'S',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Scientific / Observation Support',
      'Tertiary_Desc': 'Meteorological Station / Equipment',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OS02',
      'Class_Desc': 'Radar / Satellite Infrastructure',
      'Primary_Code': 'O',
      'Secondary_Code': 'S',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Scientific / Observation Support',
      'Tertiary_Desc': 'Radar / Satellite Infrastructure',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OS03',
      'Class_Desc': 'Telescope / Observation Infrastructure / Astronomy',
      'Primary_Code': 'O',
      'Secondary_Code': 'S',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Scientific / Observation Support',
      'Tertiary_Desc': 'Telescope / Observation Infrastructure / Astronomy',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT',
      'Class_Desc': 'Transport Support',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT01',
      'Class_Desc': 'Cattle Grid / Ford',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Cattle Grid / Ford',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT02',
      'Class_Desc': 'Elevator / Escalator / Steps',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Elevator / Escalator / Steps',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT03',
      'Class_Desc': 'Footbridge / Walkway',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Footbridge / Walkway',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT04',
      'Class_Desc': 'Pole / Post / Bollard (Restricting Vehicular Access)',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Pole / Post / Bollard (Restricting Vehicular Access)',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT05',
      'Class_Desc': 'Subway / Underpass',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '5',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Subway / Underpass',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT06',
      'Class_Desc': 'Customs Inspection Facility',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '6',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Customs Inspection Facility',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT07',
      'Class_Desc': 'Lay-By',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '7',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Lay-By',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT08',
      'Class_Desc': 'Level Crossing',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '8',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Level Crossing',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT09',
      'Class_Desc': 'Mail Pick Up',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '9',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Mail Pick Up',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT10',
      'Class_Desc': 'Railway Pedestrian Crossing',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '10',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Railway Pedestrian Crossing',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT11',
      'Class_Desc': 'Railway Buffer',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '11',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Railway Buffer',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT12',
      'Class_Desc': 'Rail Drag',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '12',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Rail Drag',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT13',
      'Class_Desc': 'Rail Infrastructure Services',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '13',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Rail Infrastructure Services',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT14',
      'Class_Desc': 'Rail Kilometre Distance Marker',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '14',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Rail Kilometre Distance Marker',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT15',
      'Class_Desc': 'Railway Lighting',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '15',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Railway Lighting',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT16',
      'Class_Desc': 'Rail Mile Distance Marker',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '16',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Rail Mile Distance Marker',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT17',
      'Class_Desc': 'Railway Turntable',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '17',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Railway Turntable',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT18',
      'Class_Desc': 'Rail Weighbridge',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '18',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Rail Weighbridge',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT19',
      'Class_Desc': 'Rail Signalling',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '19',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Rail Signalling',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT20',
      'Class_Desc': 'Railway Traverse',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '20',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Railway Traverse',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT21',
      'Class_Desc': 'Goods Tramway',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '21',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Goods Tramway',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT22',
      'Class_Desc': 'Road Drag',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '22',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Road Drag',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT23',
      'Class_Desc': 'Vehicle Dip',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '23',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Vehicle Dip',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT24',
      'Class_Desc': 'Road Turntable',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '24',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Road Turntable',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT25',
      'Class_Desc': 'Road Mile Distance Marker',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '25',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Road Mile Distance Marker',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT26',
      'Class_Desc': 'Road Kilometre Distance Marker',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '26',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Road Kilometre Distance Marker',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OT27',
      'Class_Desc': 'Road Infrastructure Services',
      'Primary_Code': 'O',
      'Secondary_Code': 'T',
      'Tertiary_Code': '27',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Transport Support',
      'Tertiary_Desc': 'Road Infrastructure Services',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OU',
      'Class_Desc': 'Unsupported Site',
      'Primary_Code': 'O',
      'Secondary_Code': 'U',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Unsupported Site',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OU01',
      'Class_Desc': 'Cycle Parking Facility',
      'Primary_Code': 'O',
      'Secondary_Code': 'U',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Unsupported Site',
      'Tertiary_Desc': 'Cycle Parking Facility',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OU04',
      'Class_Desc': 'Picnic / Barbeque Site',
      'Primary_Code': 'O',
      'Secondary_Code': 'U',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Unsupported Site',
      'Tertiary_Desc': 'Picnic / Barbeque Site',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OU05',
      'Class_Desc': 'Travelling Persons Site',
      'Primary_Code': 'O',
      'Secondary_Code': 'U',
      'Tertiary_Code': '5',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Unsupported Site',
      'Tertiary_Desc': 'Travelling Persons Site',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'OU08',
      'Class_Desc': 'Shelter (Not Including Bus Shelter)',
      'Primary_Code': 'O',
      'Secondary_Code': 'U',
      'Tertiary_Code': '8',
      'Quaternary_Code': '',
      'Primary_Desc': 'Other (Ordnance Survey Only)',
      'Secondary_Desc': 'Unsupported Site',
      'Tertiary_Desc': 'Shelter (Not Including Bus Shelter)',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'P',
      'Class_Desc': 'Parent Shell',
      'Primary_Code': 'P',
      'Secondary_Code': '',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Parent Shell',
      'Secondary_Desc': '',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'PP',
      'Class_Desc': 'Property Shell',
      'Primary_Code': 'P',
      'Secondary_Code': 'P',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Parent Shell',
      'Secondary_Desc': 'Property Shell',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'PS',
      'Class_Desc': 'Street Record',
      'Primary_Code': 'P',
      'Secondary_Code': 'S',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Parent Shell',
      'Secondary_Desc': 'Street Record',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'R',
      'Class_Desc': 'Residential',
      'Primary_Code': 'R',
      'Secondary_Code': '',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': '',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RB',
      'Class_Desc': 'Ancillary Building',
      'Primary_Code': 'R',
      'Secondary_Code': 'B',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Ancillary Building',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RC',
      'Class_Desc': 'Car Park Space',
      'Primary_Code': 'R',
      'Secondary_Code': 'C',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Car Park Space',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RC01',
      'Class_Desc': 'Allocated Parking',
      'Primary_Code': 'R',
      'Secondary_Code': 'C',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Car Park Space',
      'Tertiary_Desc': 'Allocated Parking',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RD',
      'Class_Desc': 'Dwelling',
      'Primary_Code': 'R',
      'Secondary_Code': 'D',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Dwelling',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RD01',
      'Class_Desc': 'Caravan',
      'Primary_Code': 'R',
      'Secondary_Code': 'D',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Dwelling',
      'Tertiary_Desc': 'Caravan',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RD02',
      'Class_Desc': 'Detached',
      'Primary_Code': 'R',
      'Secondary_Code': 'D',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Dwelling',
      'Tertiary_Desc': 'Detached',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RD03',
      'Class_Desc': 'Semi-Detached',
      'Primary_Code': 'R',
      'Secondary_Code': 'D',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Dwelling',
      'Tertiary_Desc': 'Semi-Detached',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RD04',
      'Class_Desc': 'Terraced',
      'Primary_Code': 'R',
      'Secondary_Code': 'D',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Dwelling',
      'Tertiary_Desc': 'Terraced',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RD06',
      'Class_Desc': 'Self Contained Flat (Includes Maisonette / Apartment)',
      'Primary_Code': 'R',
      'Secondary_Code': 'D',
      'Tertiary_Code': '6',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Dwelling',
      'Tertiary_Desc': 'Self Contained Flat (Includes Maisonette / Apartment)',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RD07',
      'Class_Desc': 'House Boat',
      'Primary_Code': 'R',
      'Secondary_Code': 'D',
      'Tertiary_Code': '7',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Dwelling',
      'Tertiary_Desc': 'House Boat',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RD08',
      'Class_Desc': 'Sheltered Accommodation',
      'Primary_Code': 'R',
      'Secondary_Code': 'D',
      'Tertiary_Code': '8',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Dwelling',
      'Tertiary_Desc': 'Sheltered Accommodation',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RD10',
      'Class_Desc': 'Privately Owned Holiday Caravan / Chalet',
      'Primary_Code': 'R',
      'Secondary_Code': 'D',
      'Tertiary_Code': '10',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Dwelling',
      'Tertiary_Desc': 'Privately Owned Holiday Caravan / Chalet',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RG',
      'Class_Desc': 'Garage',
      'Primary_Code': 'R',
      'Secondary_Code': 'G',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Garage',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RG02',
      'Class_Desc': 'Lock-Up Garage / Garage Court',
      'Primary_Code': 'R',
      'Secondary_Code': 'G',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Garage',
      'Tertiary_Desc': 'Lock-Up Garage / Garage Court',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RH',
      'Class_Desc': 'House In Multiple Occupation',
      'Primary_Code': 'R',
      'Secondary_Code': 'H',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'House In Multiple Occupation',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RH01',
      'Class_Desc': 'HMO Parent',
      'Primary_Code': 'R',
      'Secondary_Code': 'H',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'House In Multiple Occupation',
      'Tertiary_Desc': 'HMO Parent',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RH02',
      'Class_Desc': 'HMO Bedsit / Other Non Self Contained Accommodation',
      'Primary_Code': 'R',
      'Secondary_Code': 'H',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'House In Multiple Occupation',
      'Tertiary_Desc': 'HMO Bedsit / Other Non Self Contained Accommodation',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RH03',
      'Class_Desc': 'HMO Not Further Divided',
      'Primary_Code': 'R',
      'Secondary_Code': 'H',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'House In Multiple Occupation',
      'Tertiary_Desc': 'HMO Not Further Divided',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RI',
      'Class_Desc': 'Residential Institution',
      'Primary_Code': 'R',
      'Secondary_Code': 'I',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Residential Institution',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RI01',
      'Class_Desc': 'Care / Nursing Home',
      'Primary_Code': 'R',
      'Secondary_Code': 'I',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Residential Institution',
      'Tertiary_Desc': 'Care / Nursing Home',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RI02',
      'Class_Desc': 'Communal Residence',
      'Primary_Code': 'R',
      'Secondary_Code': 'I',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Residential Institution',
      'Tertiary_Desc': 'Communal Residence',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'RI02NC',
      'Class_Desc': 'Non-Commercial Lodgings',
      'Primary_Code': 'R',
      'Secondary_Code': 'I',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'NC',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Residential Institution',
      'Tertiary_Desc': 'Communal Residence',
      'Quaternary_Desc': 'Non-Commercial Lodgings'
  }, {
      'Concatenated': 'RI02RC',
      'Class_Desc': 'Religious Community',
      'Primary_Code': 'R',
      'Secondary_Code': 'I',
      'Tertiary_Code': '2',
      'Quaternary_Code': 'RC',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Residential Institution',
      'Tertiary_Desc': 'Communal Residence',
      'Quaternary_Desc': 'Religious Community'
  }, {
      'Concatenated': 'RI03',
      'Class_Desc': 'Residential Education',
      'Primary_Code': 'R',
      'Secondary_Code': 'I',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Residential',
      'Secondary_Desc': 'Residential Institution',
      'Tertiary_Desc': 'Residential Education',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'U',
      'Class_Desc': 'Unclassified',
      'Primary_Code': 'U',
      'Secondary_Code': '',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Unclassified',
      'Secondary_Desc': '',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'UC',
      'Class_Desc': 'Awaiting Classification',
      'Primary_Code': 'U',
      'Secondary_Code': 'C',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Unclassified',
      'Secondary_Desc': 'Awaiting Classification',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'UP',
      'Class_Desc': 'Pending Internal Investigation',
      'Primary_Code': 'U',
      'Secondary_Code': 'P',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Unclassified',
      'Secondary_Desc': 'Pending Internal Investigation',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'X',
      'Class_Desc': 'Dual Use',
      'Primary_Code': 'X',
      'Secondary_Code': '',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Dual Use',
      'Secondary_Desc': '',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'Z',
      'Class_Desc': 'Object of Interest',
      'Primary_Code': 'Z',
      'Secondary_Code': '',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': '',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ZA',
      'Class_Desc': 'Archaeological Dig Site',
      'Primary_Code': 'Z',
      'Secondary_Code': 'A',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Archaeological Dig Site',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ZM',
      'Class_Desc': 'Monument',
      'Primary_Code': 'Z',
      'Secondary_Code': 'M',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Monument',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ZM01',
      'Class_Desc': 'Obelisk / Milestone / Standing Stone',
      'Primary_Code': 'Z',
      'Secondary_Code': 'M',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Monument',
      'Tertiary_Desc': 'Obelisk / Milestone / Standing Stone',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ZM01OB',
      'Class_Desc': 'Obelisk',
      'Primary_Code': 'Z',
      'Secondary_Code': 'M',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'OB',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Monument',
      'Tertiary_Desc': 'Obelisk / Milestone / Standing Stone',
      'Quaternary_Desc': 'Obelisk'
  }, {
      'Concatenated': 'ZM01ST',
      'Class_Desc': 'Standing Stone',
      'Primary_Code': 'Z',
      'Secondary_Code': 'M',
      'Tertiary_Code': '1',
      'Quaternary_Code': 'ST',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Monument',
      'Tertiary_Desc': 'Obelisk / Milestone / Standing Stone',
      'Quaternary_Desc': 'Standing Stone'
  }, {
      'Concatenated': 'ZM02',
      'Class_Desc': 'Memorial / Market Cross',
      'Primary_Code': 'Z',
      'Secondary_Code': 'M',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Monument',
      'Tertiary_Desc': 'Memorial / Market Cross',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ZM03',
      'Class_Desc': 'Statue',
      'Primary_Code': 'Z',
      'Secondary_Code': 'M',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Monument',
      'Tertiary_Desc': 'Statue',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ZM04',
      'Class_Desc': 'Castle / Historic Ruin',
      'Primary_Code': 'Z',
      'Secondary_Code': 'M',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Monument',
      'Tertiary_Desc': 'Castle / Historic Ruin',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ZM05',
      'Class_Desc': 'Other Structure',
      'Primary_Code': 'Z',
      'Secondary_Code': 'M',
      'Tertiary_Code': '5',
      'Quaternary_Code': '',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Monument',
      'Tertiary_Desc': 'Other Structure',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ZM05BS',
      'Class_Desc': 'Boundary Stone',
      'Primary_Code': 'Z',
      'Secondary_Code': 'M',
      'Tertiary_Code': '5',
      'Quaternary_Code': 'BS',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Monument',
      'Tertiary_Desc': 'Other Structure',
      'Quaternary_Desc': 'Boundary Stone'
  }, {
      'Concatenated': 'ZM05CE',
      'Class_Desc': 'Cascade / Fountain',
      'Primary_Code': 'Z',
      'Secondary_Code': 'M',
      'Tertiary_Code': '5',
      'Quaternary_Code': 'CE',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Monument',
      'Tertiary_Desc': 'Other Structure',
      'Quaternary_Desc': 'Cascade / Fountain'
  }, {
      'Concatenated':
      'ZM05PN',
      'Class_Desc':
      'Permanent Art Display / Sculpture',
      'Primary_Code':
      'Z',
      'Secondary_Code':
      'M',
      'Tertiary_Code':
      '5',
      'Quaternary_Code':
      'PN',
      'Primary_Desc':
      'Object of Interest',
      'Secondary_Desc':
      'Monument',
      'Tertiary_Desc':
      'Other Structure',
      'Quaternary_Desc':
      'Permanent Art Display / Sculpture'
  }, {
      'Concatenated': 'ZM05WI',
      'Class_Desc': 'Windmill (Inactive)',
      'Primary_Code': 'Z',
      'Secondary_Code': 'M',
      'Tertiary_Code': '5',
      'Quaternary_Code': 'WI',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Monument',
      'Tertiary_Desc': 'Other Structure',
      'Quaternary_Desc': 'Windmill (Inactive)'
  }, {
      'Concatenated': 'ZS',
      'Class_Desc': 'Stately Home',
      'Primary_Code': 'Z',
      'Secondary_Code': 'S',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Stately Home',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ZU',
      'Class_Desc': 'Underground Feature',
      'Primary_Code': 'Z',
      'Secondary_Code': 'U',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Underground Feature',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ZU01',
      'Class_Desc': 'Cave',
      'Primary_Code': 'Z',
      'Secondary_Code': 'U',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Underground Feature',
      'Tertiary_Desc': 'Cave',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ZU04',
      'Class_Desc': 'Pothole / Natural Hole',
      'Primary_Code': 'Z',
      'Secondary_Code': 'U',
      'Tertiary_Code': '4',
      'Quaternary_Code': '',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Underground Feature',
      'Tertiary_Desc': 'Pothole / Natural Hole',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ZV',
      'Class_Desc': 'Other Underground Feature',
      'Primary_Code': 'Z',
      'Secondary_Code': 'V',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Other Underground Feature',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ZV01',
      'Class_Desc': 'Cellar',
      'Primary_Code': 'Z',
      'Secondary_Code': 'V',
      'Tertiary_Code': '1',
      'Quaternary_Code': '',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Other Underground Feature',
      'Tertiary_Desc': 'Cellar',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ZV02',
      'Class_Desc': 'Disused Mine',
      'Primary_Code': 'Z',
      'Secondary_Code': 'V',
      'Tertiary_Code': '2',
      'Quaternary_Code': '',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Other Underground Feature',
      'Tertiary_Desc': 'Disused Mine',
      'Quaternary_Desc': ''
  }, {
      'Concatenated':
      'ZV02MI',
      'Class_Desc':
      'Mineral Mining / Inactive',
      'Primary_Code':
      'Z',
      'Secondary_Code':
      'V',
      'Tertiary_Code':
      '2',
      'Quaternary_Code':
      'MI',
      'Primary_Desc':
      'Object of Interest',
      'Secondary_Desc':
      'Other Underground Feature',
      'Tertiary_Desc':
      'Disused Mine',
      'Quaternary_Desc':
      'Mineral Mining / Inactive'
  }, {
      'Concatenated':
      'ZV02OI',
      'Class_Desc':
      'Oil And / Gas Extraction/ Inactive',
      'Primary_Code':
      'Z',
      'Secondary_Code':
      'V',
      'Tertiary_Code':
      '2',
      'Quaternary_Code':
      'OI',
      'Primary_Desc':
      'Object of Interest',
      'Secondary_Desc':
      'Other Underground Feature',
      'Tertiary_Desc':
      'Disused Mine',
      'Quaternary_Desc':
      'Oil And / Gas Extraction/ Inactive'
  }, {
      'Concatenated':
      'ZV02QI',
      'Class_Desc':
      'Mineral Quarrying And / Open Extraction / Inactive',
      'Primary_Code':
      'Z',
      'Secondary_Code':
      'V',
      'Tertiary_Code':
      '2',
      'Quaternary_Code':
      'QI',
      'Primary_Desc':
      'Object of Interest',
      'Secondary_Desc':
      'Other Underground Feature',
      'Tertiary_Desc':
      'Disused Mine',
      'Quaternary_Desc':
      'Mineral Quarrying And / Open Extraction / Inactive'
  }, {
      'Concatenated': 'ZV03',
      'Class_Desc': 'Well / Spring',
      'Primary_Code': 'Z',
      'Secondary_Code': 'V',
      'Tertiary_Code': '3',
      'Quaternary_Code': '',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Other Underground Feature',
      'Tertiary_Desc': 'Well / Spring',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ZV03SG',
      'Class_Desc': 'Spring',
      'Primary_Code': 'Z',
      'Secondary_Code': 'V',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'SG',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Other Underground Feature',
      'Tertiary_Desc': 'Well / Spring',
      'Quaternary_Desc': 'Spring'
  }, {
      'Concatenated': 'ZV03WL',
      'Class_Desc': 'Well',
      'Primary_Code': 'Z',
      'Secondary_Code': 'V',
      'Tertiary_Code': '3',
      'Quaternary_Code': 'WL',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Other Underground Feature',
      'Tertiary_Desc': 'Well / Spring',
      'Quaternary_Desc': 'Well'
  }, {
      'Concatenated': 'ZW',
      'Class_Desc': 'Place Of Worship',
      'Primary_Code': 'Z',
      'Secondary_Code': 'W',
      'Tertiary_Code': '',
      'Quaternary_Code': '',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Place Of Worship',
      'Tertiary_Desc': '',
      'Quaternary_Desc': ''
  }, {
      'Concatenated': 'ZW99AB',
      'Class_Desc': 'Abbey',
      'Primary_Code': 'Z',
      'Secondary_Code': 'W',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'AB',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Place Of Worship',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Abbey'
  }, {
      'Concatenated': 'ZW99CA',
      'Class_Desc': 'Cathedral',
      'Primary_Code': 'Z',
      'Secondary_Code': 'W',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'CA',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Place Of Worship',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Cathedral'
  }, {
      'Concatenated': 'ZW99CH',
      'Class_Desc': 'Church',
      'Primary_Code': 'Z',
      'Secondary_Code': 'W',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'CH',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Place Of Worship',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Church'
  }, {
      'Concatenated': 'ZW99CP',
      'Class_Desc': 'Chapel',
      'Primary_Code': 'Z',
      'Secondary_Code': 'W',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'CP',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Place Of Worship',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Chapel'
  }, {
      'Concatenated': 'ZW99GU',
      'Class_Desc': 'Gurdwara',
      'Primary_Code': 'Z',
      'Secondary_Code': 'W',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'GU',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Place Of Worship',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Gurdwara'
  }, {
      'Concatenated': 'ZW99KH',
      'Class_Desc': 'Kingdom Hall',
      'Primary_Code': 'Z',
      'Secondary_Code': 'W',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'KH',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Place Of Worship',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Kingdom Hall'
  }, {
      'Concatenated': 'ZW99LG',
      'Class_Desc': 'Lych Gate',
      'Primary_Code': 'Z',
      'Secondary_Code': 'W',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'LG',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Place Of Worship',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Lych Gate'
  }, {
      'Concatenated': 'ZW99MQ',
      'Class_Desc': 'Mosque',
      'Primary_Code': 'Z',
      'Secondary_Code': 'W',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'MQ',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Place Of Worship',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Mosque'
  }, {
      'Concatenated': 'ZW99MT',
      'Class_Desc': 'Minster',
      'Primary_Code': 'Z',
      'Secondary_Code': 'W',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'MT',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Place Of Worship',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Minster'
  }, {
      'Concatenated': 'ZW99SU',
      'Class_Desc': 'Stupa',
      'Primary_Code': 'Z',
      'Secondary_Code': 'W',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'SU',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Place Of Worship',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Stupa'
  }, {
      'Concatenated': 'ZW99SY',
      'Class_Desc': 'Synagogue',
      'Primary_Code': 'Z',
      'Secondary_Code': 'W',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'SY',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Place Of Worship',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Synagogue'
  }, {
      'Concatenated': 'ZW99TP',
      'Class_Desc': 'Temple',
      'Primary_Code': 'Z',
      'Secondary_Code': 'W',
      'Tertiary_Code': '99',
      'Quaternary_Code': 'TP',
      'Primary_Desc': 'Object of Interest',
      'Secondary_Desc': 'Place Of Worship',
      'Tertiary_Desc': '',
      'Quaternary_Desc': 'Temple'
  }]

  return expected_file_content_as_json


def return_expected_csv_content_with_updated_key_names_and_handled_ancillary_values(
):
  expected_json = [{
      'code': 'C',
      'label': 'Commercial',
      'primary_code': 'C',
      'secondary_code': '',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': '',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'CA',
      'label': 'Agricultural',
      'primary_code': 'C',
      'secondary_code': 'A',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Agricultural',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'CA01',
      'label': 'Farm / Non-Residential Associated Building',
      'primary_code': 'C',
      'secondary_code': 'A',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Agricultural',
      'tertiary_desc': 'Farm / Non-Residential Associated Building',
      'quaternary_desc': ''
  }, {
      'code': 'CA02',
      'label': 'Fishery',
      'primary_code': 'C',
      'secondary_code': 'A',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Agricultural',
      'tertiary_desc': 'Fishery',
      'quaternary_desc': ''
  }, {
      'code': 'CA02FF',
      'label': 'Fish Farming',
      'primary_code': 'C',
      'secondary_code': 'A',
      'tertiary_code': '2',
      'quaternary_code': 'FF',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Agricultural',
      'tertiary_desc': 'Fishery',
      'quaternary_desc': 'Fish Farming'
  }, {
      'code': 'CA02FH',
      'label': 'Fish Hatchery',
      'primary_code': 'C',
      'secondary_code': 'A',
      'tertiary_code': '2',
      'quaternary_code': 'FH',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Agricultural',
      'tertiary_desc': 'Fishery',
      'quaternary_desc': 'Fish Hatchery'
  }, {
      'code': 'CA02FP',
      'label': 'Fish Processing',
      'primary_code': 'C',
      'secondary_code': 'A',
      'tertiary_code': '2',
      'quaternary_code': 'FP',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Agricultural',
      'tertiary_desc': 'Fishery',
      'quaternary_desc': 'Fish Processing'
  }, {
      'code': 'CA02OY',
      'label': 'Oyster / Mussel Bed',
      'primary_code': 'C',
      'secondary_code': 'A',
      'tertiary_code': '2',
      'quaternary_code': 'OY',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Agricultural',
      'tertiary_desc': 'Fishery',
      'quaternary_desc': 'Oyster / Mussel Bed'
  }, {
      'code': 'CA03',
      'label': 'Horticulture',
      'primary_code': 'C',
      'secondary_code': 'A',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Agricultural',
      'tertiary_desc': 'Horticulture',
      'quaternary_desc': ''
  }, {
      'code': 'CA03SH',
      'label': 'Smallholding',
      'primary_code': 'C',
      'secondary_code': 'A',
      'tertiary_code': '3',
      'quaternary_code': 'SH',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Agricultural',
      'tertiary_desc': 'Horticulture',
      'quaternary_desc': 'Smallholding'
  }, {
      'code': 'CA03VY',
      'label': 'Vineyard',
      'primary_code': 'C',
      'secondary_code': 'A',
      'tertiary_code': '3',
      'quaternary_code': 'VY',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Agricultural',
      'tertiary_desc': 'Horticulture',
      'quaternary_desc': 'Vineyard'
  }, {
      'code': 'CA03WB',
      'label': 'Watercress Bed',
      'primary_code': 'C',
      'secondary_code': 'A',
      'tertiary_code': '3',
      'quaternary_code': 'WB',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Agricultural',
      'tertiary_desc': 'Horticulture',
      'quaternary_desc': 'Watercress Bed'
  }, {
      'code': 'CA04',
      'label': 'Slaughter House / Abattoir',
      'primary_code': 'C',
      'secondary_code': 'A',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Agricultural',
      'tertiary_desc': 'Slaughter House / Abattoir',
      'quaternary_desc': ''
  }, {
      'code': 'CB',
      'label': 'Commercial Ancillary Building',
      'primary_code': 'C',
      'secondary_code': 'B',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Ancillary Building',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'CC',
      'label': 'Community Services',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'CC02',
      'label': 'Law Court',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Law Court',
      'quaternary_desc': ''
  }, {
      'code': 'CC03',
      'label': 'Prison',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Prison',
      'quaternary_desc': ''
  }, {
      'code': 'CC03HD',
      'label': 'HM Detention Centre',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '3',
      'quaternary_code': 'HD',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Prison',
      'quaternary_desc': 'HM Detention Centre'
  }, {
      'code': 'CC03PR',
      'label': 'HM Prison Service',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '3',
      'quaternary_code': 'PR',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Prison',
      'quaternary_desc': 'HM Prison Service'
  }, {
      'code': 'CC03SC',
      'label': 'Secure Residential Accommodation',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '3',
      'quaternary_code': 'SC',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Prison',
      'quaternary_desc': 'Secure Residential Accommodation'
  }, {
      'code': 'CC04',
      'label': 'Public / Village Hall / Other Community Facility',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Public / Village Hall / Other Community Facility',
      'quaternary_desc': ''
  }, {
      'code': 'CC04YR',
      'label': 'Youth Recreational / Social Club',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '4',
      'quaternary_code': 'YR',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Public / Village Hall / Other Community Facility',
      'quaternary_desc': 'Youth Recreational / Social Club'
  }, {
      'code': 'CC05',
      'label': 'Public Convenience',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '5',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Public Convenience',
      'quaternary_desc': ''
  }, {
      'code': 'CC06',
      'label': 'Cemetery / Crematorium / Graveyard. In Current Use.',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '6',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Cemetery / Crematorium / Graveyard. In Current Use.',
      'quaternary_desc': ''
  }, {
      'code': 'CC06CB',
      'label': 'Columbarium',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '6',
      'quaternary_code': 'CB',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Cemetery / Crematorium / Graveyard. In Current Use.',
      'quaternary_desc': 'Columbarium'
  }, {
      'code': 'CC06CN',
      'label': 'Crematorium',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '6',
      'quaternary_code': 'CN',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Cemetery / Crematorium / Graveyard. In Current Use.',
      'quaternary_desc': 'Crematorium'
  }, {
      'code': 'CC06CR',
      'label': 'Chapel Of Rest',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '6',
      'quaternary_code': 'CR',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Cemetery / Crematorium / Graveyard. In Current Use.',
      'quaternary_desc': 'Chapel Of Rest'
  }, {
      'code': 'CC06CY',
      'label': 'Cemetery',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '6',
      'quaternary_code': 'CY',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Cemetery / Crematorium / Graveyard. In Current Use.',
      'quaternary_desc': 'Cemetery'
  }, {
      'code': 'CC06MC',
      'label': 'Military Cemetery',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '6',
      'quaternary_code': 'MC',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Cemetery / Crematorium / Graveyard. In Current Use.',
      'quaternary_desc': 'Military Cemetery'
  }, {
      'code': 'CC06MY',
      'label': 'Mortuary',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '6',
      'quaternary_code': 'MY',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Cemetery / Crematorium / Graveyard. In Current Use.',
      'quaternary_desc': 'Mortuary'
  }, {
      'code': 'CC07',
      'label': 'Church Hall / Religious Meeting Place / Hall',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '7',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Church Hall / Religious Meeting Place / Hall',
      'quaternary_desc': ''
  }, {
      'code': 'CC08',
      'label': 'Community Service Centre / Office',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '8',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Community Service Centre / Office',
      'quaternary_desc': ''
  }, {
      'code': 'CC09',
      'label': 'Public Household Waste Recycling Centre (HWRC)',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '9',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Public Household Waste Recycling Centre (HWRC)',
      'quaternary_desc': ''
  }, {
      'code': 'CC10',
      'label': 'Recycling Site',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '10',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Recycling Site',
      'quaternary_desc': ''
  }, {
      'code': 'CC11',
      'label': 'CCTV',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '11',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'CCTV',
      'quaternary_desc': ''
  }, {
      'code': 'CC12',
      'label': 'Job Centre',
      'primary_code': 'C',
      'secondary_code': 'C',
      'tertiary_code': '12',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Community Services',
      'tertiary_desc': 'Job Centre',
      'quaternary_desc': ''
  }, {
      'code': 'CE',
      'label': 'Education',
      'primary_code': 'C',
      'secondary_code': 'E',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Education',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'CE01',
      'label': 'College',
      'primary_code': 'C',
      'secondary_code': 'E',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Education',
      'tertiary_desc': 'College',
      'quaternary_desc': ''
  }, {
      'code': 'CE01FE',
      'label': 'Further Education',
      'primary_code': 'C',
      'secondary_code': 'E',
      'tertiary_code': '1',
      'quaternary_code': 'FE',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Education',
      'tertiary_desc': 'College',
      'quaternary_desc': 'Further Education'
  }, {
      'code': 'CE01HE',
      'label': 'Higher Education',
      'primary_code': 'C',
      'secondary_code': 'E',
      'tertiary_code': '1',
      'quaternary_code': 'HE',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Education',
      'tertiary_desc': 'College',
      'quaternary_desc': 'Higher Education'
  }, {
      'code': 'CE02',
      'label': 'Children’s Nursery / Crèche',
      'primary_code': 'C',
      'secondary_code': 'E',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Education',
      'tertiary_desc': 'Children’s Nursery / Crèche',
      'quaternary_desc': ''
  }, {
      'code': 'CE03',
      'label':
      'Preparatory / First / Primary / Infant / Junior / Middle School',
      'primary_code': 'C',
      'secondary_code': 'E',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Education',
      'tertiary_desc':
      'Preparatory / First / Primary / Infant / Junior / Middle School',
      'quaternary_desc': ''
  }, {
      'code': 'CE03FS',
      'label': 'First School',
      'primary_code': 'C',
      'secondary_code': 'E',
      'tertiary_code': '3',
      'quaternary_code': 'FS',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Education',
      'tertiary_desc':
      'Preparatory / First / Primary / Infant / Junior / Middle School',
      'quaternary_desc': 'First School'
  }, {
      'code': 'CE03IS',
      'label': 'Infant School',
      'primary_code': 'C',
      'secondary_code': 'E',
      'tertiary_code': '3',
      'quaternary_code': 'IS',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Education',
      'tertiary_desc':
      'Preparatory / First / Primary / Infant / Junior / Middle School',
      'quaternary_desc': 'Infant School'
  }, {
      'code': 'CE03JS',
      'label': 'Junior School',
      'primary_code': 'C',
      'secondary_code': 'E',
      'tertiary_code': '3',
      'quaternary_code': 'JS',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Education',
      'tertiary_desc':
      'Preparatory / First / Primary / Infant / Junior / Middle School',
      'quaternary_desc': 'Junior School'
  }, {
      'code': 'CE03MS',
      'label': 'Middle School',
      'primary_code': 'C',
      'secondary_code': 'E',
      'tertiary_code': '3',
      'quaternary_code': 'MS',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Education',
      'tertiary_desc':
      'Preparatory / First / Primary / Infant / Junior / Middle School',
      'quaternary_desc': 'Middle School'
  }, {
      'code': 'CE03NP',
      'label': 'Non State Primary / Preparatory School',
      'primary_code': 'C',
      'secondary_code': 'E',
      'tertiary_code': '3',
      'quaternary_code': 'NP',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Education',
      'tertiary_desc':
      'Preparatory / First / Primary / Infant / Junior / Middle School',
      'quaternary_desc': 'Non State Primary / Preparatory School'
  }, {
      'code': 'CE03PS',
      'label': 'Primary School',
      'primary_code': 'C',
      'secondary_code': 'E',
      'tertiary_code': '3',
      'quaternary_code': 'PS',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Education',
      'tertiary_desc':
      'Preparatory / First / Primary / Infant / Junior / Middle School',
      'quaternary_desc': 'Primary School'
  }, {
      'code': 'CE04',
      'label': 'Secondary / High School',
      'primary_code': 'C',
      'secondary_code': 'E',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Education',
      'tertiary_desc': 'Secondary / High School',
      'quaternary_desc': ''
  }, {
      'code': 'CE04NS',
      'label': 'Non State Secondary School',
      'primary_code': 'C',
      'secondary_code': 'E',
      'tertiary_code': '4',
      'quaternary_code': 'NS',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Education',
      'tertiary_desc': 'Secondary / High School',
      'quaternary_desc': 'Non State Secondary School'
  }, {
      'code': 'CE04SS',
      'label': 'Secondary School',
      'primary_code': 'C',
      'secondary_code': 'E',
      'tertiary_code': '4',
      'quaternary_code': 'SS',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Education',
      'tertiary_desc': 'Secondary / High School',
      'quaternary_desc': 'Secondary School'
  }, {
      'code': 'CE05',
      'label': 'University',
      'primary_code': 'C',
      'secondary_code': 'E',
      'tertiary_code': '5',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Education',
      'tertiary_desc': 'University',
      'quaternary_desc': ''
  }, {
      'code': 'CE06',
      'label': 'Special Needs Establishment.',
      'primary_code': 'C',
      'secondary_code': 'E',
      'tertiary_code': '6',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Education',
      'tertiary_desc': 'Special Needs Establishment.',
      'quaternary_desc': ''
  }, {
      'code': 'CE07',
      'label': 'Other Educational Establishment',
      'primary_code': 'C',
      'secondary_code': 'E',
      'tertiary_code': '7',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Education',
      'tertiary_desc': 'Other Educational Establishment',
      'quaternary_desc': ''
  }, {
      'code': 'CH',
      'label': 'Hotel / Motel / Boarding / Guest House',
      'primary_code': 'C',
      'secondary_code': 'H',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Hotel / Motel / Boarding / Guest House',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'CH01',
      'label': 'Boarding / Guest House / Bed And Breakfast / Youth Hostel',
      'primary_code': 'C',
      'secondary_code': 'H',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Hotel / Motel / Boarding / Guest House',
      'tertiary_desc':
      'Boarding / Guest House / Bed And Breakfast / Youth Hostel',
      'quaternary_desc': ''
  }, {
      'code': 'CH01YH',
      'label': 'Youth Hostel',
      'primary_code': 'C',
      'secondary_code': 'H',
      'tertiary_code': '1',
      'quaternary_code': 'YH',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Hotel / Motel / Boarding / Guest House',
      'tertiary_desc':
      'Boarding / Guest House / Bed And Breakfast / Youth Hostel',
      'quaternary_desc': 'Youth Hostel'
  }, {
      'code': 'CH02',
      'label': 'Holiday Let/Accomodation/Short-Term Let Other Than CH01',
      'primary_code': 'C',
      'secondary_code': 'H',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Hotel / Motel / Boarding / Guest House',
      'tertiary_desc':
      'Holiday Let/Accomodation/Short-Term Let Other Than CH01',
      'quaternary_desc': ''
  }, {
      'code': 'CH03',
      'label': 'Hotel/Motel',
      'primary_code': 'C',
      'secondary_code': 'H',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Hotel / Motel / Boarding / Guest House',
      'tertiary_desc': 'Hotel/Motel',
      'quaternary_desc': ''
  }, {
      'code': 'CI',
      'label':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'CI01',
      'label': 'Factory/Manufacturing',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': ''
  }, {
      'code': 'CI01AW',
      'label': 'Aircraft Works',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'AW',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Aircraft Works'
  }, {
      'code': 'CI01BB',
      'label': 'Boat Building',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'BB',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Boat Building'
  }, {
      'code': 'CI01BR',
      'label': 'Brick Works',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'BR',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Brick Works'
  }, {
      'code': 'CI01BW',
      'label': 'Brewery',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'BW',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Brewery'
  }, {
      'code': 'CI01CD',
      'label': 'Cider Manufacture',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'CD',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Cider Manufacture'
  }, {
      'code': 'CI01CM',
      'label': 'Chemical Works',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'CM',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Chemical Works'
  }, {
      'code': 'CI01CW',
      'label': 'Cement Works',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'CW',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Cement Works'
  }, {
      'code': 'CI01DA',
      'label': 'Dairy Processing',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'DA',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Dairy Processing'
  }, {
      'code': 'CI01DY',
      'label': 'Distillery',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'DY',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Distillery'
  }, {
      'code': 'CI01FL',
      'label': 'Flour Mill',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'FL',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Flour Mill'
  }, {
      'code': 'CI01FO',
      'label': 'Food Processing',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'FO',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Food Processing'
  }, {
      'code': 'CI01GW',
      'label': 'Glassworks',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'GW',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Glassworks'
  }, {
      'code': 'CI01MG',
      'label': 'Manufacturing',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'MG',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Manufacturing'
  }, {
      'code': 'CI01OH',
      'label': 'Oast House',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'OH',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Oast House'
  }, {
      'code': 'CI01OR',
      'label': 'Oil Refining',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'OR',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Oil Refining'
  }, {
      'code': 'CI01PG',
      'label': 'Pottery Manufacturing',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'PG',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Pottery Manufacturing'
  }, {
      'code': 'CI01PM',
      'label': 'Paper Mill',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'PM',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Paper Mill'
  }, {
      'code': 'CI01PW',
      'label': 'Printing Works',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'PW',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Printing Works'
  }, {
      'code': 'CI01SR',
      'label': 'Sugar Refinery',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'SR',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Sugar Refinery'
  }, {
      'code': 'CI01SW',
      'label': 'Steel Works',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'SW',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Steel Works'
  }, {
      'code': 'CI01TL',
      'label': 'Timber Mill',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'TL',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Timber Mill'
  }, {
      'code': 'CI01WN',
      'label': 'Winery',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'WN',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Winery'
  }, {
      'code': 'CI01YD',
      'label': 'Shipyard',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': 'YD',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Factory/Manufacturing',
      'quaternary_desc': 'Shipyard'
  }, {
      'code': 'CI02',
      'label': 'Mineral / Ore Working / Quarry / Mine',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Mineral / Ore Working / Quarry / Mine',
      'quaternary_desc': ''
  }, {
      'code': 'CI02MA',
      'label': 'Mineral Mining / Active',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '2',
      'quaternary_code': 'MA',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Mineral / Ore Working / Quarry / Mine',
      'quaternary_desc': 'Mineral Mining / Active'
  }, {
      'code': 'CI02MD',
      'label': 'Mineral Distribution / Storage',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '2',
      'quaternary_code': 'MD',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Mineral / Ore Working / Quarry / Mine',
      'quaternary_desc': 'Mineral Distribution / Storage'
  }, {
      'code': 'CI02MP',
      'label': 'Mineral Processing',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '2',
      'quaternary_code': 'MP',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Mineral / Ore Working / Quarry / Mine',
      'quaternary_desc': 'Mineral Processing'
  }, {
      'code': 'CI02OA',
      'label': 'Oil / Gas Extraction / Active',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '2',
      'quaternary_code': 'OA',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Mineral / Ore Working / Quarry / Mine',
      'quaternary_desc': 'Oil / Gas Extraction / Active'
  }, {
      'code':
      'CI02QA',
      'label':
      'Mineral Quarrying / Open Extraction / Active',
      'primary_code':
      'C',
      'secondary_code':
      'I',
      'tertiary_code':
      '2',
      'quaternary_code':
      'QA',
      'primary_desc':
      'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc':
      'Mineral / Ore Working / Quarry / Mine',
      'quaternary_desc':
      'Mineral Quarrying / Open Extraction / Active'
  }, {
      'code': 'CI03',
      'label': 'Workshop / Light Industrial',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Workshop / Light Industrial',
      'quaternary_desc': ''
  }, {
      'code': 'CI03GA',
      'label': 'Servicing Garage',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '3',
      'quaternary_code': 'GA',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Workshop / Light Industrial',
      'quaternary_desc': 'Servicing Garage'
  }, {
      'code': 'CI04',
      'label': 'Warehouse / Store / Storage Depot',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Warehouse / Store / Storage Depot',
      'quaternary_desc': ''
  }, {
      'code': 'CI04CS',
      'label': 'Crop Handling / Storage',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '4',
      'quaternary_code': 'CS',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Warehouse / Store / Storage Depot',
      'quaternary_desc': 'Crop Handling / Storage'
  }, {
      'code': 'CI04PL',
      'label': 'Postal Sorting / Distribution',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '4',
      'quaternary_code': 'PL',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Warehouse / Store / Storage Depot',
      'quaternary_desc': 'Postal Sorting / Distribution'
  }, {
      'code': 'CI04SO',
      'label': 'Solid Fuel Storage',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '4',
      'quaternary_code': 'SO',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Warehouse / Store / Storage Depot',
      'quaternary_desc': 'Solid Fuel Storage'
  }, {
      'code': 'CI04TS',
      'label': 'Timber Storage',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '4',
      'quaternary_code': 'TS',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Warehouse / Store / Storage Depot',
      'quaternary_desc': 'Timber Storage'
  }, {
      'code': 'CI05',
      'label': 'Wholesale Distribution',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '5',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Wholesale Distribution',
      'quaternary_desc': ''
  }, {
      'code': 'CI05SF',
      'label': 'Solid Fuel Distribution',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '5',
      'quaternary_code': 'SF',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Wholesale Distribution',
      'quaternary_desc': 'Solid Fuel Distribution'
  }, {
      'code': 'CI05TD',
      'label': 'Timber Distribution',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '5',
      'quaternary_code': 'TD',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Wholesale Distribution',
      'quaternary_desc': 'Timber Distribution'
  }, {
      'code': 'CI06',
      'label': 'Recycling Plant',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '6',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Recycling Plant',
      'quaternary_desc': ''
  }, {
      'code': 'CI07',
      'label': 'Incinerator / Waste Transfer Station',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '7',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Incinerator / Waste Transfer Station',
      'quaternary_desc': ''
  }, {
      'code': 'CI08',
      'label': 'Maintenance Depot',
      'primary_code': 'C',
      'secondary_code': 'I',
      'tertiary_code': '8',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites',
      'tertiary_desc': 'Maintenance Depot',
      'quaternary_desc': ''
  }, {
      'code': 'CL',
      'label': 'Leisure - Applicable to recreational sites and enterprises',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'CL01',
      'label': 'Amusements',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Amusements',
      'quaternary_desc': ''
  }, {
      'code': 'CL01LP',
      'label': 'Leisure Pier',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '1',
      'quaternary_code': 'LP',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Amusements',
      'quaternary_desc': 'Leisure Pier'
  }, {
      'code': 'CL02',
      'label': 'Holiday / Campsite',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Holiday / Campsite',
      'quaternary_desc': ''
  }, {
      'code': 'CL02CG',
      'label': 'Camping',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '2',
      'quaternary_code': 'CG',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Holiday / Campsite',
      'quaternary_desc': 'Camping'
  }, {
      'code': 'CL02CV',
      'label': 'Caravanning',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '2',
      'quaternary_code': 'CV',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Holiday / Campsite',
      'quaternary_desc': 'Caravanning'
  }, {
      'code': 'CL02HA',
      'label': 'Holiday Accommodation',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '2',
      'quaternary_code': 'HA',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Holiday / Campsite',
      'quaternary_desc': 'Holiday Accommodation'
  }, {
      'code': 'CL02HO',
      'label': 'Holiday Centre',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '2',
      'quaternary_code': 'HO',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Holiday / Campsite',
      'quaternary_desc': 'Holiday Centre'
  }, {
      'code': 'CL02YC',
      'label': 'Youth Organisation Camp',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '2',
      'quaternary_code': 'YC',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Holiday / Campsite',
      'quaternary_desc': 'Youth Organisation Camp'
  }, {
      'code': 'CL03',
      'label': 'Library',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Library',
      'quaternary_desc': ''
  }, {
      'code': 'CL03RR',
      'label': 'Reading Room',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '3',
      'quaternary_code': 'RR',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Library',
      'quaternary_desc': 'Reading Room'
  }, {
      'code': 'CL04',
      'label': 'Museum / Gallery',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Museum / Gallery',
      'quaternary_desc': ''
  }, {
      'code': 'CL04AC',
      'label': 'Art Centre / Gallery',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '4',
      'quaternary_code': 'AC',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Museum / Gallery',
      'quaternary_desc': 'Art Centre / Gallery'
  }, {
      'code': 'CL04AM',
      'label': 'Aviation Museum',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '4',
      'quaternary_code': 'AM',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Museum / Gallery',
      'quaternary_desc': 'Aviation Museum'
  }, {
      'code': 'CL04HG',
      'label': 'Heritage Centre',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '4',
      'quaternary_code': 'HG',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Museum / Gallery',
      'quaternary_desc': 'Heritage Centre'
  }, {
      'code': 'CL04IM',
      'label': 'Industrial Museum',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '4',
      'quaternary_code': 'IM',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Museum / Gallery',
      'quaternary_desc': 'Industrial Museum'
  }, {
      'code': 'CL04MM',
      'label': 'Military Museum',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '4',
      'quaternary_code': 'MM',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Museum / Gallery',
      'quaternary_desc': 'Military Museum'
  }, {
      'code': 'CL04NM',
      'label': 'Maritime Museum',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '4',
      'quaternary_code': 'NM',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Museum / Gallery',
      'quaternary_desc': 'Maritime Museum'
  }, {
      'code': 'CL04SM',
      'label': 'Science Museum',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '4',
      'quaternary_code': 'SM',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Museum / Gallery',
      'quaternary_desc': 'Science Museum'
  }, {
      'code': 'CL04TM',
      'label': 'Transport Museum',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '4',
      'quaternary_code': 'TM',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Museum / Gallery',
      'quaternary_desc': 'Transport Museum'
  }, {
      'code': 'CL06',
      'label': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': ''
  }, {
      'code': 'CL06AH',
      'label': 'Athletics Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'AH',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Athletics Facility'
  }, {
      'code': 'CL06BF',
      'label': 'Bowls Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'BF',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Bowls Facility'
  }, {
      'code': 'CL06CK',
      'label': 'Cricket Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'CK',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Cricket Facility'
  }, {
      'code': 'CL06CU',
      'label': 'Curling Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'CU',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Curling Facility'
  }, {
      'code': 'CL06DS',
      'label': 'Diving / Swimming Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'DS',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Diving / Swimming Facility'
  }, {
      'code': 'CL06EQ',
      'label': 'Equestrian Sports Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'EQ',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Equestrian Sports Facility'
  }, {
      'code': 'CL06FB',
      'label': 'Football Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'FB',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Football Facility'
  }, {
      'code': 'CL06FI',
      'label': 'Fishing / Angling Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'FI',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Fishing / Angling Facility'
  }, {
      'code': 'CL06GF',
      'label': 'Golf Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'GF',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Golf Facility'
  }, {
      'code': 'CL06GL',
      'label': 'Gliding Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'GL',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Gliding Facility'
  }, {
      'code': 'CL06GR',
      'label': 'Greyhound Racing Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'GR',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Greyhound Racing Facility'
  }, {
      'code': 'CL06HF',
      'label': 'Hockey Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'HF',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Hockey Facility'
  }, {
      'code': 'CL06HR',
      'label': 'Horse Racing Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'HR',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Horse Racing Facility'
  }, {
      'code': 'CL06HV',
      'label': 'Historic Vessel / Aircraft / Vehicle',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'HV',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Historic Vessel / Aircraft / Vehicle'
  }, {
      'code': 'CL06LS',
      'label': 'Activity / Leisure / Sports Centre',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'LS',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Activity / Leisure / Sports Centre'
  }, {
      'code': 'CL06ME',
      'label': 'Model Sports Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'ME',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Model Sports Facility'
  }, {
      'code': 'CL06MF',
      'label': 'Motor Sports Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'MF',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Motor Sports Facility'
  }, {
      'code': 'CL06PF',
      'label': 'Playing Field',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'PF',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Playing Field'
  }, {
      'code': 'CL06QS',
      'label': 'Racquet Sports Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'QS',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Racquet Sports Facility'
  }, {
      'code': 'CL06RF',
      'label': 'Rugby Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'RF',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Rugby Facility'
  }, {
      'code': 'CL06RG',
      'label': 'Recreation Ground',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'RG',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Recreation Ground'
  }, {
      'code': 'CL06SI',
      'label': 'Shinty Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'SI',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Shinty Facility'
  }, {
      'code': 'CL06SK',
      'label': 'Skateboarding Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'SK',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Skateboarding Facility'
  }, {
      'code': 'CL06SX',
      'label': 'Civilian Firing Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'SX',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Civilian Firing Facility'
  }, {
      'code': 'CL06TB',
      'label': 'Tenpin Bowling Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'TB',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Tenpin Bowling Facility'
  }, {
      'code': 'CL06TN',
      'label': 'Public Tennis Court',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'TN',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Public Tennis Court'
  }, {
      'code': 'CL06WA',
      'label': 'Water Sports Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'WA',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Water Sports Facility'
  }, {
      'code': 'CL06WP',
      'label': 'Winter Sports Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'WP',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Winter Sports Facility'
  }, {
      'code': 'CL06WY',
      'label': 'Wildlife Sports Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'WY',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Wildlife Sports Facility'
  }, {
      'code': 'CL06YF',
      'label': 'Cycling Sports Facility',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '6',
      'quaternary_code': 'YF',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Indoor / Outdoor Leisure / Sporting Activity / Centre',
      'quaternary_desc': 'Cycling Sports Facility'
  }, {
      'code': 'CL07',
      'label':
      'Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '7',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc':
      'Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall',
      'quaternary_desc': ''
  }, {
      'code': 'CL07CI',
      'label': 'Cinema',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '7',
      'quaternary_code': 'CI',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc':
      'Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall',
      'quaternary_desc': 'Cinema'
  }, {
      'code': 'CL07EN',
      'label': 'Entertainment Complex',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '7',
      'quaternary_code': 'EN',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc':
      'Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall',
      'quaternary_desc': 'Entertainment Complex'
  }, {
      'code': 'CL07EX',
      'label': 'Conference / Exhibition Centre',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '7',
      'quaternary_code': 'EX',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc':
      'Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall',
      'quaternary_desc': 'Conference / Exhibition Centre'
  }, {
      'code': 'CL07TH',
      'label': 'Theatre',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '7',
      'quaternary_code': 'TH',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc':
      'Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall',
      'quaternary_desc': 'Theatre'
  }, {
      'code': 'CL08',
      'label': 'Zoo / Theme Park',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '8',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Zoo / Theme Park',
      'quaternary_desc': ''
  }, {
      'code': 'CL08AK',
      'label': 'Amusement Park',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '8',
      'quaternary_code': 'AK',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Zoo / Theme Park',
      'quaternary_desc': 'Amusement Park'
  }, {
      'code': 'CL08AQ',
      'label': 'Aquatic Attraction',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '8',
      'quaternary_code': 'AQ',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Zoo / Theme Park',
      'quaternary_desc': 'Aquatic Attraction'
  }, {
      'code': 'CL08MX',
      'label': 'Model Village Site',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '8',
      'quaternary_code': 'MX',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Zoo / Theme Park',
      'quaternary_desc': 'Model Village Site'
  }, {
      'code': 'CL08WZ',
      'label': 'Wildlife / Zoological Park',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '8',
      'quaternary_code': 'WZ',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Zoo / Theme Park',
      'quaternary_desc': 'Wildlife / Zoological Park'
  }, {
      'code': 'CL09',
      'label': 'Beach Hut (Recreational, Non-Residential Use Only)',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '9',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Beach Hut (Recreational, Non-Residential Use Only)',
      'quaternary_desc': ''
  }, {
      'code': 'CL10',
      'label': 'Licensed Private Members’ Club',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '10',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Licensed Private Members’ Club',
      'quaternary_desc': ''
  }, {
      'code': 'CL10RE',
      'label': 'Recreational / Social Club',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '10',
      'quaternary_code': 'RE',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Licensed Private Members’ Club',
      'quaternary_desc': 'Recreational / Social Club'
  }, {
      'code': 'CL11',
      'label': 'Arena / Stadium',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '11',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Arena / Stadium',
      'quaternary_desc': ''
  }, {
      'code': 'CL11SD',
      'label': 'Stadium',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '11',
      'quaternary_code': 'SD',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Arena / Stadium',
      'quaternary_desc': 'Stadium'
  }, {
      'code': 'CL11SJ',
      'label': 'Showground',
      'primary_code': 'C',
      'secondary_code': 'L',
      'tertiary_code': '11',
      'quaternary_code': 'SJ',
      'primary_desc': 'Commercial',
      'secondary_desc':
      'Leisure - Applicable to recreational sites and enterprises',
      'tertiary_desc': 'Arena / Stadium',
      'quaternary_desc': 'Showground'
  }, {
      'code': 'CM',
      'label': 'Medical',
      'primary_code': 'C',
      'secondary_code': 'M',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Medical',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'CM01',
      'label': 'Dentist',
      'primary_code': 'C',
      'secondary_code': 'M',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Medical',
      'tertiary_desc': 'Dentist',
      'quaternary_desc': ''
  }, {
      'code': 'CM02',
      'label': 'General Practice Surgery / Clinic',
      'primary_code': 'C',
      'secondary_code': 'M',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Medical',
      'tertiary_desc': 'General Practice Surgery / Clinic',
      'quaternary_desc': ''
  }, {
      'code': 'CM02HC',
      'label': 'Health Centre',
      'primary_code': 'C',
      'secondary_code': 'M',
      'tertiary_code': '2',
      'quaternary_code': 'HC',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Medical',
      'tertiary_desc': 'General Practice Surgery / Clinic',
      'quaternary_desc': 'Health Centre'
  }, {
      'code': 'CM02HL',
      'label': 'Health Care Services',
      'primary_code': 'C',
      'secondary_code': 'M',
      'tertiary_code': '2',
      'quaternary_code': 'HL',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Medical',
      'tertiary_desc': 'General Practice Surgery / Clinic',
      'quaternary_desc': 'Health Care Services'
  }, {
      'code': 'CM03',
      'label': 'Hospital / Hospice',
      'primary_code': 'C',
      'secondary_code': 'M',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Medical',
      'tertiary_desc': 'Hospital / Hospice',
      'quaternary_desc': ''
  }, {
      'code': 'CM03HI',
      'label': 'Hospice',
      'primary_code': 'C',
      'secondary_code': 'M',
      'tertiary_code': '3',
      'quaternary_code': 'HI',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Medical',
      'tertiary_desc': 'Hospital / Hospice',
      'quaternary_desc': 'Hospice'
  }, {
      'code': 'CM03HP',
      'label': 'Hospital',
      'primary_code': 'C',
      'secondary_code': 'M',
      'tertiary_code': '3',
      'quaternary_code': 'HP',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Medical',
      'tertiary_desc': 'Hospital / Hospice',
      'quaternary_desc': 'Hospital'
  }, {
      'code': 'CM04',
      'label': 'Medical / Testing / Research Laboratory',
      'primary_code': 'C',
      'secondary_code': 'M',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Medical',
      'tertiary_desc': 'Medical / Testing / Research Laboratory',
      'quaternary_desc': ''
  }, {
      'code': 'CM05',
      'label': 'Professional Medical Service',
      'primary_code': 'C',
      'secondary_code': 'M',
      'tertiary_code': '5',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Medical',
      'tertiary_desc': 'Professional Medical Service',
      'quaternary_desc': ''
  }, {
      'code': 'CM05ZS',
      'label': 'Assessment / Development Services',
      'primary_code': 'C',
      'secondary_code': 'M',
      'tertiary_code': '5',
      'quaternary_code': 'ZS',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Medical',
      'tertiary_desc': 'Professional Medical Service',
      'quaternary_desc': 'Assessment / Development Services'
  }, {
      'code': 'CM06',
      'label': 'Pharmacy',
      'primary_code': 'C',
      'secondary_code': 'M',
      'tertiary_code': '6',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Medical',
      'tertiary_desc': 'Pharmacy',
      'quaternary_desc': ''
  }, {
      'code': 'CN',
      'label': 'Animal Centre',
      'primary_code': 'C',
      'secondary_code': 'N',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Animal Centre',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'CN01',
      'label': 'Cattery / Kennel',
      'primary_code': 'C',
      'secondary_code': 'N',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Animal Centre',
      'tertiary_desc': 'Cattery / Kennel',
      'quaternary_desc': ''
  }, {
      'code': 'CN02',
      'label': 'Animal Services',
      'primary_code': 'C',
      'secondary_code': 'N',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Animal Centre',
      'tertiary_desc': 'Animal Services',
      'quaternary_desc': ''
  }, {
      'code': 'CN02AX',
      'label': 'Animal Quarantining',
      'primary_code': 'C',
      'secondary_code': 'N',
      'tertiary_code': '2',
      'quaternary_code': 'AX',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Animal Centre',
      'tertiary_desc': 'Animal Services',
      'quaternary_desc': 'Animal Quarantining'
  }, {
      'code': 'CN03',
      'label': 'Equestrian',
      'primary_code': 'C',
      'secondary_code': 'N',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Animal Centre',
      'tertiary_desc': 'Equestrian',
      'quaternary_desc': ''
  }, {
      'code': 'CN03HB',
      'label': 'Horse Racing / Breeding Stable',
      'primary_code': 'C',
      'secondary_code': 'N',
      'tertiary_code': '3',
      'quaternary_code': 'HB',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Animal Centre',
      'tertiary_desc': 'Equestrian',
      'quaternary_desc': 'Horse Racing / Breeding Stable'
  }, {
      'code': 'CN03SB',
      'label': 'Commercial Stabling / Riding',
      'primary_code': 'C',
      'secondary_code': 'N',
      'tertiary_code': '3',
      'quaternary_code': 'SB',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Animal Centre',
      'tertiary_desc': 'Equestrian',
      'quaternary_desc': 'Commercial Stabling / Riding'
  }, {
      'code': 'CN04',
      'label': 'Vet / Animal Medical Treatment',
      'primary_code': 'C',
      'secondary_code': 'N',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Animal Centre',
      'tertiary_desc': 'Vet / Animal Medical Treatment',
      'quaternary_desc': ''
  }, {
      'code': 'CN05',
      'label': 'Animal / Bird / Marine Sanctuary',
      'primary_code': 'C',
      'secondary_code': 'N',
      'tertiary_code': '5',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Animal Centre',
      'tertiary_desc': 'Animal / Bird / Marine Sanctuary',
      'quaternary_desc': ''
  }, {
      'code': 'CN05AN',
      'label': 'Animal Sanctuary',
      'primary_code': 'C',
      'secondary_code': 'N',
      'tertiary_code': '5',
      'quaternary_code': 'AN',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Animal Centre',
      'tertiary_desc': 'Animal / Bird / Marine Sanctuary',
      'quaternary_desc': 'Animal Sanctuary'
  }, {
      'code': 'CN05MR',
      'label': 'Marine Sanctuary',
      'primary_code': 'C',
      'secondary_code': 'N',
      'tertiary_code': '5',
      'quaternary_code': 'MR',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Animal Centre',
      'tertiary_desc': 'Animal / Bird / Marine Sanctuary',
      'quaternary_desc': 'Marine Sanctuary'
  }, {
      'code': 'CO',
      'label': 'Office',
      'primary_code': 'C',
      'secondary_code': 'O',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Office',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'CO01',
      'label': 'Office / Work Studio',
      'primary_code': 'C',
      'secondary_code': 'O',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Office',
      'tertiary_desc': 'Office / Work Studio',
      'quaternary_desc': ''
  }, {
      'code': 'CO01EM',
      'label': 'Embassy /, High Commission / Consulate',
      'primary_code': 'C',
      'secondary_code': 'O',
      'tertiary_code': '1',
      'quaternary_code': 'EM',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Office',
      'tertiary_desc': 'Office / Work Studio',
      'quaternary_desc': 'Embassy /, High Commission / Consulate'
  }, {
      'code': 'CO01FM',
      'label': 'Film Studio',
      'primary_code': 'C',
      'secondary_code': 'O',
      'tertiary_code': '1',
      'quaternary_code': 'FM',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Office',
      'tertiary_desc': 'Office / Work Studio',
      'quaternary_desc': 'Film Studio'
  }, {
      'code': 'CO01GV',
      'label': 'Central Government Service',
      'primary_code': 'C',
      'secondary_code': 'O',
      'tertiary_code': '1',
      'quaternary_code': 'GV',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Office',
      'tertiary_desc': 'Office / Work Studio',
      'quaternary_desc': 'Central Government Service'
  }, {
      'code': 'CO01LG',
      'label': 'Local Government Service',
      'primary_code': 'C',
      'secondary_code': 'O',
      'tertiary_code': '1',
      'quaternary_code': 'LG',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Office',
      'tertiary_desc': 'Office / Work Studio',
      'quaternary_desc': 'Local Government Service'
  }, {
      'code': 'CO02',
      'label': 'Broadcasting (TV / Radio)',
      'primary_code': 'C',
      'secondary_code': 'O',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Office',
      'tertiary_desc': 'Broadcasting (TV / Radio)',
      'quaternary_desc': ''
  }, {
      'code': 'CR',
      'label': 'Retail',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'CR01',
      'label': 'Bank / Financial Service',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Bank / Financial Service',
      'quaternary_desc': ''
  }, {
      'code': 'CR02',
      'label': 'Retail Service Agent',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Retail Service Agent',
      'quaternary_desc': ''
  }, {
      'code': 'CR02EV',
      'label': 'Electric Car Charging Station',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '2',
      'quaternary_code': 'EV',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Retail Service Agent',
      'quaternary_desc': 'Electric Car Charging Station'
  }, {
      'code': 'CR02PO',
      'label': 'Post Office',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '2',
      'quaternary_code': 'PO',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Retail Service Agent',
      'quaternary_desc': 'Post Office'
  }, {
      'code': 'CR04',
      'label': 'Market (Indoor / Outdoor)',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Market (Indoor / Outdoor)',
      'quaternary_desc': ''
  }, {
      'code': 'CR04FK',
      'label': 'Fish Market',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '4',
      'quaternary_code': 'FK',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Market (Indoor / Outdoor)',
      'quaternary_desc': 'Fish Market'
  }, {
      'code': 'CR04FV',
      'label': 'Fruit / Vegetable Market',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '4',
      'quaternary_code': 'FV',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Market (Indoor / Outdoor)',
      'quaternary_desc': 'Fruit / Vegetable Market'
  }, {
      'code': 'CR04LV',
      'label': 'Livestock Market',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '4',
      'quaternary_code': 'LV',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Market (Indoor / Outdoor)',
      'quaternary_desc': 'Livestock Market'
  }, {
      'code': 'CR05',
      'label': 'Petrol Filling Station',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '5',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Petrol Filling Station',
      'quaternary_desc': ''
  }, {
      'code': 'CR06',
      'label': 'Public House / Bar / Nightclub',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '6',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Public House / Bar / Nightclub',
      'quaternary_desc': ''
  }, {
      'code': 'CR06BA',
      'label': 'Bar',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '6',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Public House / Bar / Nightclub',
      'quaternary_desc': 'Bar'
  }, {
      'code': 'CR06NC',
      'label': 'Nightclub',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '6',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Public House / Bar / Nightclub',
      'quaternary_desc': 'Nightclub'
  }, {
      'code': 'CR06PH',
      'label': 'Public House',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '6',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Public House / Bar / Nightclub',
      'quaternary_desc': 'Public House'
  }, {
      'code': 'CR07',
      'label': 'Restaurant / Cafeteria',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '7',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Restaurant / Cafeteria',
      'quaternary_desc': ''
  }, {
      'code': 'CR08',
      'label': 'Shop / Showroom',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '8',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Shop / Showroom',
      'quaternary_desc': ''
  }, {
      'code': 'CR08CS',
      'label': 'Convenience Store',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '8',
      'quaternary_code': 'CS',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Shop / Showroom',
      'quaternary_desc': 'Convenience Store'
  }, {
      'code': 'CR08GC',
      'label': 'Garden Centre',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '8',
      'quaternary_code': 'GC',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Shop / Showroom',
      'quaternary_desc': 'Garden Centre'
  }, {
      'code': 'CR08SM',
      'label': 'Supermarket',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '8',
      'quaternary_code': 'SM',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Shop / Showroom',
      'quaternary_desc': 'Supermarket'
  }, {
      'code': 'CR09',
      'label': 'Other Licensed Premise / Vendor',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '9',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Other Licensed Premise / Vendor',
      'quaternary_desc': ''
  }, {
      'code': 'CR09BS',
      'label': 'Betting Shop',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '9',
      'quaternary_code': 'BS',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Other Licensed Premise / Vendor',
      'quaternary_desc': 'Betting Shop'
  }, {
      'code': 'CR09OL',
      'label': 'Off-licence',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '9',
      'quaternary_code': 'OL',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Other Licensed Premise / Vendor',
      'quaternary_desc': 'Off-licence'
  }, {
      'code': 'CR10',
      'label': 'Fast Food Outlet / Takeaway (Hot / Cold)',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '10',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Fast Food Outlet / Takeaway (Hot / Cold)',
      'quaternary_desc': ''
  }, {
      'code': 'CR11',
      'label': 'Automated Teller Machine (ATM)',
      'primary_code': 'C',
      'secondary_code': 'R',
      'tertiary_code': '11',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Retail',
      'tertiary_desc': 'Automated Teller Machine (ATM)',
      'quaternary_desc': ''
  }, {
      'code': 'CS',
      'label': 'Storage Land',
      'primary_code': 'C',
      'secondary_code': 'S',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Storage Land',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'CS01',
      'label': 'General Storage Land',
      'primary_code': 'C',
      'secondary_code': 'S',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Storage Land',
      'tertiary_desc': 'General Storage Land',
      'quaternary_desc': ''
  }, {
      'code': 'CS02',
      'label': 'Builders’ Yard',
      'primary_code': 'C',
      'secondary_code': 'S',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Storage Land',
      'tertiary_desc': 'Builders’ Yard',
      'quaternary_desc': ''
  }, {
      'code': 'CT',
      'label': 'Transport',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'CT01',
      'label':
      'Airfield / Airstrip / Airport / Air Transport Infrastructure Facility',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Airfield / Airstrip / Airport / Air Transport Infrastructure Facility',
      'quaternary_desc': ''
  }, {
      'code': 'CT01AF',
      'label': 'Airfield',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '1',
      'quaternary_code': 'AF',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Airfield / Airstrip / Airport / Air Transport Infrastructure Facility',
      'quaternary_desc': 'Airfield'
  }, {
      'code': 'CT01AI',
      'label': 'Air Transport Infrastructure Services',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '1',
      'quaternary_code': 'AI',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Airfield / Airstrip / Airport / Air Transport Infrastructure Facility',
      'quaternary_desc': 'Air Transport Infrastructure Services'
  }, {
      'code': 'CT01AP',
      'label': 'Airport',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '1',
      'quaternary_code': 'AP',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Airfield / Airstrip / Airport / Air Transport Infrastructure Facility',
      'quaternary_desc': 'Airport'
  }, {
      'code': 'CT01AY',
      'label': 'Air Passenger Terminal',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '1',
      'quaternary_code': 'AY',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Airfield / Airstrip / Airport / Air Transport Infrastructure Facility',
      'quaternary_desc': 'Air Passenger Terminal'
  }, {
      'code': 'CT01HS',
      'label': 'Helicopter Station',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '1',
      'quaternary_code': 'HS',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Airfield / Airstrip / Airport / Air Transport Infrastructure Facility',
      'quaternary_desc': 'Helicopter Station'
  }, {
      'code': 'CT01HT',
      'label': 'Heliport / Helipad',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '1',
      'quaternary_code': 'HT',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Airfield / Airstrip / Airport / Air Transport Infrastructure Facility',
      'quaternary_desc': 'Heliport / Helipad'
  }, {
      'code': 'CT02',
      'label': 'Bus Shelter',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Bus Shelter',
      'quaternary_desc': ''
  }, {
      'code': 'CT03',
      'label':
      'Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site',
      'quaternary_desc': ''
  }, {
      'code': 'CT03PK',
      'label': 'Public Park And Ride',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '3',
      'quaternary_code': 'PK',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site',
      'quaternary_desc': 'Public Park And Ride'
  }, {
      'code': 'CT03PP',
      'label': 'Public Car Parking',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '3',
      'quaternary_code': 'PP',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site',
      'quaternary_desc': 'Public Car Parking'
  }, {
      'code': 'CT03PU',
      'label': 'Public Coach Parking',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '3',
      'quaternary_code': 'PU',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site',
      'quaternary_desc': 'Public Coach Parking'
  }, {
      'code': 'CT03VP',
      'label': 'Public Commercial Vehicle Parking',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '3',
      'quaternary_code': 'VP',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site',
      'quaternary_desc': 'Public Commercial Vehicle Parking'
  }, {
      'code': 'CT04',
      'label': 'Goods Freight Handling / Terminal',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Goods Freight Handling / Terminal',
      'quaternary_desc': ''
  }, {
      'code': 'CT04AE',
      'label': 'Air Freight Terminal',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '4',
      'quaternary_code': 'AE',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Goods Freight Handling / Terminal',
      'quaternary_desc': 'Air Freight Terminal'
  }, {
      'code': 'CT04CF',
      'label': 'Container Freight',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '4',
      'quaternary_code': 'CF',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Goods Freight Handling / Terminal',
      'quaternary_desc': 'Container Freight'
  }, {
      'code': 'CT04RH',
      'label': 'Road Freight Transport',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '4',
      'quaternary_code': 'RH',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Goods Freight Handling / Terminal',
      'quaternary_desc': 'Road Freight Transport'
  }, {
      'code': 'CT04RT',
      'label': 'Rail Freight Transport',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '4',
      'quaternary_code': 'RT',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Goods Freight Handling / Terminal',
      'quaternary_desc': 'Rail Freight Transport'
  }, {
      'code': 'CT05',
      'label': 'Marina',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '5',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Marina',
      'quaternary_desc': ''
  }, {
      'code': 'CT06',
      'label': 'Mooring',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '6',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Mooring',
      'quaternary_desc': ''
  }, {
      'code': 'CT07',
      'label': 'Railway Asset',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '7',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Railway Asset',
      'quaternary_desc': ''
  }, {
      'code': 'CT08',
      'label': 'Station / Interchange / Terminal / Halt',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '8',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Station / Interchange / Terminal / Halt',
      'quaternary_desc': ''
  }, {
      'code': 'CT08BC',
      'label': 'Bus / Coach Station',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '8',
      'quaternary_code': 'BC',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Station / Interchange / Terminal / Halt',
      'quaternary_desc': 'Bus / Coach Station'
  }, {
      'code': 'CT08RS',
      'label': 'Railway Station',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '8',
      'quaternary_code': 'RS',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Station / Interchange / Terminal / Halt',
      'quaternary_desc': 'Railway Station'
  }, {
      'code': 'CT08VH',
      'label': 'Vehicular Rail Terminal',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '8',
      'quaternary_code': 'VH',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Station / Interchange / Terminal / Halt',
      'quaternary_desc': 'Vehicular Rail Terminal'
  }, {
      'code': 'CT09',
      'label': 'Transport Track / Way',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '9',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Transport Track / Way',
      'quaternary_desc': ''
  }, {
      'code': 'CT09CL',
      'label': 'Cliff Railway',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '9',
      'quaternary_code': 'CL',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Transport Track / Way',
      'quaternary_desc': 'Cliff Railway'
  }, {
      'code': 'CT09CX',
      'label': 'Chair Lift / Cable Car / Ski Tow',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '9',
      'quaternary_code': 'CX',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Transport Track / Way',
      'quaternary_desc': 'Chair Lift / Cable Car / Ski Tow'
  }, {
      'code': 'CT09MO',
      'label': 'Monorail',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '9',
      'quaternary_code': 'MO',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Transport Track / Way',
      'quaternary_desc': 'Monorail'
  }, {
      'code': 'CT10',
      'label': 'Vehicle Storage',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '10',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Vehicle Storage',
      'quaternary_desc': ''
  }, {
      'code': 'CT10BG',
      'label': 'Boat Storage',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '10',
      'quaternary_code': 'BG',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Vehicle Storage',
      'quaternary_desc': 'Boat Storage'
  }, {
      'code': 'CT10BU',
      'label': 'Bus / Coach Depot',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '10',
      'quaternary_code': 'BU',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Vehicle Storage',
      'quaternary_desc': 'Bus / Coach Depot'
  }, {
      'code': 'CT11',
      'label': 'Transport Related Infrastructure',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '11',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Transport Related Infrastructure',
      'quaternary_desc': ''
  }, {
      'code': 'CT11AD',
      'label': 'Aqueduct',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '11',
      'quaternary_code': 'AD',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Transport Related Infrastructure',
      'quaternary_desc': 'Aqueduct'
  }, {
      'code': 'CT11CA',
      'label': 'Road Bridge Over Canal',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '11',
      'quaternary_code': 'CA',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Transport Related Infrastructure',
      'quaternary_desc': 'Road Bridge Over Canal'
  }, {
      'code': 'CT11LK',
      'label': 'Lock',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '11',
      'quaternary_code': 'LK',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Transport Related Infrastructure',
      'quaternary_desc': 'Lock'
  }, {
      'code': 'CT11MU',
      'label': 'Road Bridge Over Multiple',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '11',
      'quaternary_code': 'MU',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Transport Related Infrastructure',
      'quaternary_desc': 'Road Bridge Over Multiple'
  }, {
      'code': 'CT11NN',
      'label': 'Road Bridge Over No Network',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '11',
      'quaternary_code': 'MN',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Transport Related Infrastructure',
      'quaternary_desc': 'Road Bridge Over No Network'
  }, {
      'code': 'CT11PA',
      'label': 'Road Bridge Over Path',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '11',
      'quaternary_code': 'PA',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Transport Related Infrastructure',
      'quaternary_desc': 'Road Bridge Over Path'
  }, {
      'code': 'CT11RA',
      'label': 'Road Bridge Over Railway',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '11',
      'quaternary_code': 'RA',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Transport Related Infrastructure',
      'quaternary_desc': 'Road Bridge Over Railway'
  }, {
      'code': 'CT11RO',
      'label': 'Road Bridge Over Road',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '11',
      'quaternary_code': 'RO',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Transport Related Infrastructure',
      'quaternary_desc': 'Road Bridge Over Road'
  }, {
      'code': 'CT11WA',
      'label': 'Road Bridge Over Water',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '11',
      'quaternary_code': 'WA',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Transport Related Infrastructure',
      'quaternary_desc': 'Road Bridge Over Water'
  }, {
      'code': 'CT11WE',
      'label': 'Weir',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '11',
      'quaternary_code': 'WE',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Transport Related Infrastructure',
      'quaternary_desc': 'Weir'
  }, {
      'code': 'CT11WG',
      'label': 'Weighbridge / Load Gauge',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '11',
      'quaternary_code': 'WG',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Transport Related Infrastructure',
      'quaternary_desc': 'Weighbridge / Load Gauge'
  }, {
      'code': 'CT12',
      'label': 'Overnight Lorry Park',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '12',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc': 'Overnight Lorry Park',
      'quaternary_desc': ''
  }, {
      'code': 'CT13',
      'label':
      'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '13',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay',
      'quaternary_desc': ''
  }, {
      'code': 'CT13FR',
      'label': 'Passenger Ferry Terminal',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '13',
      'quaternary_code': 'FR',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay',
      'quaternary_desc': 'Passenger Ferry Terminal'
  }, {
      'code': 'CT13NB',
      'label': 'Non-Tanker Nautical Berthing',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '13',
      'quaternary_code': 'NB',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay',
      'quaternary_desc': 'Non-Tanker Nautical Berthing'
  }, {
      'code': 'CT13NF',
      'label': 'Nautical Refuelling Facility',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '13',
      'quaternary_code': 'NF',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay',
      'quaternary_desc': 'Nautical Refuelling Facility'
  }, {
      'code': 'CT13SA',
      'label': 'Slipway',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '13',
      'quaternary_code': 'SA',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay',
      'quaternary_desc': 'Slipway'
  }, {
      'code': 'CT13SP',
      'label': 'Ship Passenger Terminal',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '13',
      'quaternary_code': 'SP',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay',
      'quaternary_desc': 'Ship Passenger Terminal'
  }, {
      'code': 'CT13TK',
      'label': 'Tanker Berthing',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '13',
      'quaternary_code': 'TK',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay',
      'quaternary_desc': 'Tanker Berthing'
  }, {
      'code': 'CT13VF',
      'label': 'Vehicular Ferry Terminal',
      'primary_code': 'C',
      'secondary_code': 'T',
      'tertiary_code': '13',
      'quaternary_code': 'VF',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Transport',
      'tertiary_desc':
      'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay',
      'quaternary_desc': 'Vehicular Ferry Terminal'
  }, {
      'code': 'CU',
      'label': 'Utility',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'CU01',
      'label': 'Electricity Sub-Station',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Electricity Sub-Station',
      'quaternary_desc': ''
  }, {
      'code': 'CU02',
      'label': 'Landfill',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Landfill',
      'quaternary_desc': ''
  }, {
      'code': 'CU03',
      'label': 'Power Station / Energy Production',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Power Station / Energy Production',
      'quaternary_desc': ''
  }, {
      'code': 'CU03ED',
      'label': 'Electricity Distribution Facility',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '3',
      'quaternary_code': 'ED',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Power Station / Energy Production',
      'quaternary_desc': 'Electricity Distribution Facility'
  }, {
      'code': 'CU03EP',
      'label': 'Electricity Production Facility',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '3',
      'quaternary_code': 'EP',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Power Station / Energy Production',
      'quaternary_desc': 'Electricity Production Facility'
  }, {
      'code': 'CU03WF',
      'label': 'Wind Farm',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '3',
      'quaternary_code': 'WF',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Power Station / Energy Production',
      'quaternary_desc': 'Wind Farm'
  }, {
      'code': 'CU03WU',
      'label': 'Wind Turbine',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '3',
      'quaternary_code': 'WU',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Power Station / Energy Production',
      'quaternary_desc': 'Wind Turbine'
  }, {
      'code': 'CU04',
      'label': 'Pump House / Pumping Station / Water Tower',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Pump House / Pumping Station / Water Tower',
      'quaternary_desc': ''
  }, {
      'code': 'CU04WC',
      'label': 'Water Controlling / Pumping',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '4',
      'quaternary_code': 'WC',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Pump House / Pumping Station / Water Tower',
      'quaternary_desc': 'Water Controlling / Pumping'
  }, {
      'code': 'CU04WD',
      'label': 'Water Distribution / Pumping',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '4',
      'quaternary_code': 'WD',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Pump House / Pumping Station / Water Tower',
      'quaternary_desc': 'Water Distribution / Pumping'
  }, {
      'code': 'CU04WM',
      'label': 'Water Quality Monitoring',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '4',
      'quaternary_code': 'WM',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Pump House / Pumping Station / Water Tower',
      'quaternary_desc': 'Water Quality Monitoring'
  }, {
      'code': 'CU04WS',
      'label': 'Water Storage',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '4',
      'quaternary_code': 'WS',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Pump House / Pumping Station / Water Tower',
      'quaternary_desc': 'Water Storage'
  }, {
      'code': 'CU04WW',
      'label': 'Waste Water Distribution / Pumping',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '4',
      'quaternary_code': 'WW',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Pump House / Pumping Station / Water Tower',
      'quaternary_desc': 'Waste Water Distribution / Pumping'
  }, {
      'code': 'CU06',
      'label': 'Telecommunication',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '6',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Telecommunication',
      'quaternary_desc': ''
  }, {
      'code': 'CU06TE',
      'label': 'Telecommunications Mast',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '6',
      'quaternary_code': 'TE',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Telecommunication',
      'quaternary_desc': 'Telecommunications Mast'
  }, {
      'code': 'CU06TX',
      'label': 'Telephone Exchange',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '6',
      'quaternary_code': 'TX',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Telecommunication',
      'quaternary_desc': 'Telephone Exchange'
  }, {
      'code': 'CU07',
      'label': 'Water / Waste Water / Sewage Treatment Works',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '7',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Water / Waste Water / Sewage Treatment Works',
      'quaternary_desc': ''
  }, {
      'code': 'CU07WR',
      'label': 'Waste Water Treatment',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '7',
      'quaternary_code': 'WR',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Water / Waste Water / Sewage Treatment Works',
      'quaternary_desc': 'Waste Water Treatment'
  }, {
      'code': 'CU07WT',
      'label': 'Water Treatment',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '7',
      'quaternary_code': 'WT',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Water / Waste Water / Sewage Treatment Works',
      'quaternary_desc': 'Water Treatment'
  }, {
      'code': 'CU08',
      'label': 'Gas / Oil Storage / Distribution',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '8',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Gas / Oil Storage / Distribution',
      'quaternary_desc': ''
  }, {
      'code': 'CU08GG',
      'label': 'Gas Governor',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '8',
      'quaternary_code': 'GG',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Gas / Oil Storage / Distribution',
      'quaternary_desc': 'Gas Governor'
  }, {
      'code': 'CU08GH',
      'label': 'Gas Holder',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '8',
      'quaternary_code': 'GH',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Gas / Oil Storage / Distribution',
      'quaternary_desc': 'Gas Holder'
  }, {
      'code': 'CU08OT',
      'label': 'Oil Terminal',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '8',
      'quaternary_code': 'OT',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Gas / Oil Storage / Distribution',
      'quaternary_desc': 'Oil Terminal'
  }, {
      'code': 'CU09',
      'label': 'Other Utility Use',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '9',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Other Utility Use',
      'quaternary_desc': ''
  }, {
      'code': 'CU09CQ',
      'label': 'Cable Terminal Station',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '9',
      'quaternary_code': 'CQ',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Other Utility Use',
      'quaternary_desc': 'Cable Terminal Station'
  }, {
      'code': 'CU09OV',
      'label': 'Observatory',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '9',
      'quaternary_code': 'OV',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Other Utility Use',
      'quaternary_desc': 'Observatory'
  }, {
      'code': 'CU09RA',
      'label': 'Radar Station',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '9',
      'quaternary_code': 'RA',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Other Utility Use',
      'quaternary_desc': 'Radar Station'
  }, {
      'code': 'CU09SE',
      'label': 'Satellite Earth Station',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '9',
      'quaternary_code': 'SE',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Other Utility Use',
      'quaternary_desc': 'Satellite Earth Station'
  }, {
      'code': 'CU10',
      'label': 'Waste Management',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '10',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Waste Management',
      'quaternary_desc': ''
  }, {
      'code': 'CU11',
      'label': 'Telephone Box',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '11',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Telephone Box',
      'quaternary_desc': ''
  }, {
      'code': 'CU11OP',
      'label': 'Other Public Telephones',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '11',
      'quaternary_code': 'OP',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Telephone Box',
      'quaternary_desc': 'Other Public Telephones'
  }, {
      'code': 'CU12',
      'label': 'Dam',
      'primary_code': 'C',
      'secondary_code': 'U',
      'tertiary_code': '12',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Utility',
      'tertiary_desc': 'Dam',
      'quaternary_desc': ''
  }, {
      'code': 'CX',
      'label': 'Emergency / Rescue Service',
      'primary_code': 'C',
      'secondary_code': 'X',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Emergency / Rescue Service',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'CX01',
      'label': 'Police / Transport Police / Station',
      'primary_code': 'C',
      'secondary_code': 'X',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Emergency / Rescue Service',
      'tertiary_desc': 'Police / Transport Police / Station',
      'quaternary_desc': ''
  }, {
      'code': 'CX01PT',
      'label': 'Police Training',
      'primary_code': 'C',
      'secondary_code': 'X',
      'tertiary_code': '1',
      'quaternary_code': 'PT',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Emergency / Rescue Service',
      'tertiary_desc': 'Police / Transport Police / Station',
      'quaternary_desc': 'Police Training'
  }, {
      'code': 'CX02',
      'label': 'Fire Station',
      'primary_code': 'C',
      'secondary_code': 'X',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Emergency / Rescue Service',
      'tertiary_desc': 'Fire Station',
      'quaternary_desc': ''
  }, {
      'code': 'CX02FT',
      'label': 'Fire Service Training',
      'primary_code': 'C',
      'secondary_code': 'X',
      'tertiary_code': '2',
      'quaternary_code': 'FT',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Emergency / Rescue Service',
      'tertiary_desc': 'Fire Station',
      'quaternary_desc': 'Fire Service Training'
  }, {
      'code': 'CX03',
      'label': 'Ambulance Station',
      'primary_code': 'C',
      'secondary_code': 'X',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Emergency / Rescue Service',
      'tertiary_desc': 'Ambulance Station',
      'quaternary_desc': ''
  }, {
      'code': 'CX03AA',
      'label': 'Air Sea Rescue / Air Ambulance',
      'primary_code': 'C',
      'secondary_code': 'X',
      'tertiary_code': '3',
      'quaternary_code': 'AA',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Emergency / Rescue Service',
      'tertiary_desc': 'Ambulance Station',
      'quaternary_desc': 'Air Sea Rescue / Air Ambulance'
  }, {
      'code': 'CX04',
      'label': 'Lifeboat Services / Station',
      'primary_code': 'C',
      'secondary_code': 'X',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Emergency / Rescue Service',
      'tertiary_desc': 'Lifeboat Services / Station',
      'quaternary_desc': ''
  }, {
      'code': 'CX05',
      'label': 'Coastguard Rescue / Lookout / Station',
      'primary_code': 'C',
      'secondary_code': 'X',
      'tertiary_code': '5',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Emergency / Rescue Service',
      'tertiary_desc': 'Coastguard Rescue / Lookout / Station',
      'quaternary_desc': ''
  }, {
      'code': 'CX06',
      'label': 'Mountain Rescue Station',
      'primary_code': 'C',
      'secondary_code': 'X',
      'tertiary_code': '6',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Emergency / Rescue Service',
      'tertiary_desc': 'Mountain Rescue Station',
      'quaternary_desc': ''
  }, {
      'code': 'CX07',
      'label': 'Lighthouse',
      'primary_code': 'C',
      'secondary_code': 'X',
      'tertiary_code': '7',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Emergency / Rescue Service',
      'tertiary_desc': 'Lighthouse',
      'quaternary_desc': ''
  }, {
      'code': 'CX08',
      'label': 'Police Box / Kiosk',
      'primary_code': 'C',
      'secondary_code': 'X',
      'tertiary_code': '8',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Emergency / Rescue Service',
      'tertiary_desc': 'Police Box / Kiosk',
      'quaternary_desc': ''
  }, {
      'code': 'CZ',
      'label': 'Information',
      'primary_code': 'C',
      'secondary_code': 'Z',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Information',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'CZ01',
      'label': 'Advertising Hoarding',
      'primary_code': 'C',
      'secondary_code': 'Z',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Information',
      'tertiary_desc': 'Advertising Hoarding',
      'quaternary_desc': ''
  }, {
      'code': 'CZ02',
      'label': 'Tourist Information Signage',
      'primary_code': 'C',
      'secondary_code': 'Z',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Information',
      'tertiary_desc': 'Tourist Information Signage',
      'quaternary_desc': ''
  }, {
      'code': 'CZ02VI',
      'label': 'Visitor Information',
      'primary_code': 'C',
      'secondary_code': 'Z',
      'tertiary_code': '2',
      'quaternary_code': 'VI',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Information',
      'tertiary_desc': 'Tourist Information Signage',
      'quaternary_desc': 'Visitor Information'
  }, {
      'code': 'CZ03',
      'label': 'Traffic Information Signage',
      'primary_code': 'C',
      'secondary_code': 'Z',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Commercial',
      'secondary_desc': 'Information',
      'tertiary_desc': 'Traffic Information Signage',
      'quaternary_desc': ''
  }, {
      'code': 'L',
      'label': 'Land',
      'primary_code': 'L',
      'secondary_code': '',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': '',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'LA',
      'label':
      'Agricultural - Applicable to land in farm ownership and not run as a separate business enterprise',
      'primary_code': 'L',
      'secondary_code': 'A',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc':
      'Agricultural - Applicable to land in farm ownership and not run as a separate business enterprise',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'LA01',
      'label': 'Grazing Land',
      'primary_code': 'L',
      'secondary_code': 'A',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc':
      'Agricultural - Applicable to land in farm ownership and not run as a separate business enterprise',
      'tertiary_desc': 'Grazing Land',
      'quaternary_desc': ''
  }, {
      'code': 'LA02',
      'label': 'Permanent Crop / Crop Rotation',
      'primary_code': 'L',
      'secondary_code': 'A',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc':
      'Agricultural - Applicable to land in farm ownership and not run as a separate business enterprise',
      'tertiary_desc': 'Permanent Crop / Crop Rotation',
      'quaternary_desc': ''
  }, {
      'code': 'LA02OC',
      'label': 'Orchard',
      'primary_code': 'L',
      'secondary_code': 'A',
      'tertiary_code': '2',
      'quaternary_code': 'OC',
      'primary_desc': 'Land',
      'secondary_desc':
      'Agricultural - Applicable to land in farm ownership and not run as a separate business enterprise',
      'tertiary_desc': 'Permanent Crop / Crop Rotation',
      'quaternary_desc': 'Orchard'
  }, {
      'code': 'LB',
      'label': 'Land Ancillary Building',
      'primary_code': 'L',
      'secondary_code': 'B',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Ancillary Building',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'LB99AV',
      'label': 'Aviary / Dovecot / Cage',
      'primary_code': 'L',
      'secondary_code': 'B',
      'tertiary_code': '99',
      'quaternary_code': 'AV',
      'primary_desc': 'Land',
      'secondary_desc': 'Ancillary Building',
      'tertiary_desc': '',
      'quaternary_desc': 'Aviary / Dovecot / Cage'
  }, {
      'code': 'LB99BD',
      'label': 'Bandstand',
      'primary_code': 'L',
      'secondary_code': 'B',
      'tertiary_code': '99',
      'quaternary_code': 'BD',
      'primary_desc': 'Land',
      'secondary_desc': 'Ancillary Building',
      'tertiary_desc': '',
      'quaternary_desc': 'Bandstand'
  }, {
      'code': 'LB99PI',
      'label': 'Pavilion / Changing Room',
      'primary_code': 'L',
      'secondary_code': 'B',
      'tertiary_code': '99',
      'quaternary_code': 'PI',
      'primary_desc': 'Land',
      'secondary_desc': 'Ancillary Building',
      'tertiary_desc': '',
      'quaternary_desc': 'Pavilion / Changing Room'
  }, {
      'code': 'LB99SV',
      'label': 'Sports Viewing Structure',
      'primary_code': 'L',
      'secondary_code': 'B',
      'tertiary_code': '99',
      'quaternary_code': 'SV',
      'primary_desc': 'Land',
      'secondary_desc': 'Ancillary Building',
      'tertiary_desc': '',
      'quaternary_desc': 'Sports Viewing Structure'
  }, {
      'code': 'LC',
      'label': 'Burial Ground',
      'primary_code': 'L',
      'secondary_code': 'C',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Burial Ground',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'LC01',
      'label': 'Historic / Disused Cemetery / Graveyard',
      'primary_code': 'L',
      'secondary_code': 'C',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Burial Ground',
      'tertiary_desc': 'Historic / Disused Cemetery / Graveyard',
      'quaternary_desc': ''
  }, {
      'code': 'LD',
      'label': 'Development',
      'primary_code': 'L',
      'secondary_code': 'D',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Development',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'LD01',
      'label': 'Development Site',
      'primary_code': 'L',
      'secondary_code': 'D',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Development',
      'tertiary_desc': 'Development Site',
      'quaternary_desc': ''
  }, {
      'code': 'LD01CC',
      'label': 'Commercial Construction Site',
      'primary_code': 'L',
      'secondary_code': 'D',
      'tertiary_code': '1',
      'quaternary_code': 'CC',
      'primary_desc': 'Land',
      'secondary_desc': 'Development',
      'tertiary_desc': 'Development Site',
      'quaternary_desc': 'Commercial Construction Site'
  }, {
      'code': 'LD01CO',
      'label': 'Community Construction Site',
      'primary_code': 'L',
      'secondary_code': 'D',
      'tertiary_code': '1',
      'quaternary_code': 'CO',
      'primary_desc': 'Land',
      'secondary_desc': 'Development',
      'tertiary_desc': 'Development Site',
      'quaternary_desc': 'Community Construction Site'
  }, {
      'code': 'LD01RN',
      'label': 'Residential Construction Site',
      'primary_code': 'L',
      'secondary_code': 'D',
      'tertiary_code': '1',
      'quaternary_code': 'RN',
      'primary_desc': 'Land',
      'secondary_desc': 'Development',
      'tertiary_desc': 'Development Site',
      'quaternary_desc': 'Residential Construction Site'
  }, {
      'code': 'LD01TC',
      'label': 'Transport Construction Site',
      'primary_code': 'L',
      'secondary_code': 'D',
      'tertiary_code': '1',
      'quaternary_code': 'TC',
      'primary_desc': 'Land',
      'secondary_desc': 'Development',
      'tertiary_desc': 'Development Site',
      'quaternary_desc': 'Transport Construction Site'
  }, {
      'code': 'LF',
      'label': 'Forestry',
      'primary_code': 'L',
      'secondary_code': 'F',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Forestry',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'LF02',
      'label': 'Forest / Arboretum / Pinetum (Managed / Unmanaged)',
      'primary_code': 'L',
      'secondary_code': 'F',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Forestry',
      'tertiary_desc': 'Forest / Arboretum / Pinetum (Managed / Unmanaged)',
      'quaternary_desc': ''
  }, {
      'code': 'LF02AU',
      'label': 'Arboretum',
      'primary_code': 'L',
      'secondary_code': 'F',
      'tertiary_code': '2',
      'quaternary_code': 'AU',
      'primary_desc': 'Land',
      'secondary_desc': 'Forestry',
      'tertiary_desc': 'Forest / Arboretum / Pinetum (Managed / Unmanaged)',
      'quaternary_desc': 'Arboretum'
  }, {
      'code': 'LF03',
      'label': 'Woodland',
      'primary_code': 'L',
      'secondary_code': 'F',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Forestry',
      'tertiary_desc': 'Woodland',
      'quaternary_desc': ''
  }, {
      'code': 'LL',
      'label': 'Allotment',
      'primary_code': 'L',
      'secondary_code': 'L',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Allotment',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'LM',
      'label': 'Amenity - Open areas not attracting visitors',
      'primary_code': 'L',
      'secondary_code': 'M',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Amenity - Open areas not attracting visitors',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'LM01',
      'label': 'Landscaped Roundabout',
      'primary_code': 'L',
      'secondary_code': 'M',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Amenity - Open areas not attracting visitors',
      'tertiary_desc': 'Landscaped Roundabout',
      'quaternary_desc': ''
  }, {
      'code': 'LM02',
      'label': 'Verge / Central Reservation',
      'primary_code': 'L',
      'secondary_code': 'M',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Amenity - Open areas not attracting visitors',
      'tertiary_desc': 'Verge / Central Reservation',
      'quaternary_desc': ''
  }, {
      'code': 'LM02NV',
      'label': 'Natural Central Reservation',
      'primary_code': 'L',
      'secondary_code': 'M',
      'tertiary_code': '2',
      'quaternary_code': 'NV',
      'primary_desc': 'Land',
      'secondary_desc': 'Amenity - Open areas not attracting visitors',
      'tertiary_desc': 'Verge / Central Reservation',
      'quaternary_desc': 'Natural Central Reservation'
  }, {
      'code': 'LM02VE',
      'label': 'Natural Verge',
      'primary_code': 'L',
      'secondary_code': 'M',
      'tertiary_code': '2',
      'quaternary_code': 'VE',
      'primary_desc': 'Land',
      'secondary_desc': 'Amenity - Open areas not attracting visitors',
      'tertiary_desc': 'Verge / Central Reservation',
      'quaternary_desc': 'Natural Verge'
  }, {
      'code': 'LM03',
      'label': 'Maintained Amenity Land',
      'primary_code': 'L',
      'secondary_code': 'M',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Amenity - Open areas not attracting visitors',
      'tertiary_desc': 'Maintained Amenity Land',
      'quaternary_desc': ''
  }, {
      'code': 'LM04',
      'label': 'Maintained Surfaced Area',
      'primary_code': 'L',
      'secondary_code': 'M',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Amenity - Open areas not attracting visitors',
      'tertiary_desc': 'Maintained Surfaced Area',
      'quaternary_desc': ''
  }, {
      'code': 'LM04MV',
      'label': 'Made Central Reservation',
      'primary_code': 'L',
      'secondary_code': 'M',
      'tertiary_code': '4',
      'quaternary_code': 'MV',
      'primary_desc': 'Land',
      'secondary_desc': 'Amenity - Open areas not attracting visitors',
      'tertiary_desc': 'Maintained Surfaced Area',
      'quaternary_desc': 'Made Central Reservation'
  }, {
      'code': 'LM04PV',
      'label': 'Pavement',
      'primary_code': 'L',
      'secondary_code': 'M',
      'tertiary_code': '4',
      'quaternary_code': 'PV',
      'primary_desc': 'Land',
      'secondary_desc': 'Amenity - Open areas not attracting visitors',
      'tertiary_desc': 'Maintained Surfaced Area',
      'quaternary_desc': 'Pavement'
  }, {
      'code': 'LO',
      'label': 'Open Space',
      'primary_code': 'L',
      'secondary_code': 'O',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Open Space',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'LO01',
      'label': 'Heath / Moorland',
      'primary_code': 'L',
      'secondary_code': 'O',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Open Space',
      'tertiary_desc': 'Heath / Moorland',
      'quaternary_desc': ''
  }, {
      'code': 'LP',
      'label': 'Park',
      'primary_code': 'L',
      'secondary_code': 'P',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Park',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'LP01',
      'label': 'Public Park / Garden',
      'primary_code': 'L',
      'secondary_code': 'P',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Park',
      'tertiary_desc': 'Public Park / Garden',
      'quaternary_desc': ''
  }, {
      'code': 'LP02',
      'label': 'Public Open Space / Nature Reserve',
      'primary_code': 'L',
      'secondary_code': 'P',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Park',
      'tertiary_desc': 'Public Open Space / Nature Reserve',
      'quaternary_desc': ''
  }, {
      'code': 'LP03',
      'label': 'Playground',
      'primary_code': 'L',
      'secondary_code': 'P',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Park',
      'tertiary_desc': 'Playground',
      'quaternary_desc': ''
  }, {
      'code': 'LP03PA',
      'label': 'Play Area',
      'primary_code': 'L',
      'secondary_code': 'P',
      'tertiary_code': '3',
      'quaternary_code': 'PA',
      'primary_desc': 'Land',
      'secondary_desc': 'Park',
      'tertiary_desc': 'Playground',
      'quaternary_desc': 'Play Area'
  }, {
      'code': 'LP03PD',
      'label': 'Paddling Pool',
      'primary_code': 'L',
      'secondary_code': 'P',
      'tertiary_code': '3',
      'quaternary_code': 'PD',
      'primary_desc': 'Land',
      'secondary_desc': 'Park',
      'tertiary_desc': 'Playground',
      'quaternary_desc': 'Paddling Pool'
  }, {
      'code': 'LP04',
      'label': 'Private Park / Garden',
      'primary_code': 'L',
      'secondary_code': 'P',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Park',
      'tertiary_desc': 'Private Park / Garden',
      'quaternary_desc': ''
  }, {
      'code': 'LU',
      'label': 'Unused Land',
      'primary_code': 'L',
      'secondary_code': 'U',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Unused Land',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'LU01',
      'label': 'Vacant / Derelict Land',
      'primary_code': 'L',
      'secondary_code': 'U',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Unused Land',
      'tertiary_desc': 'Vacant / Derelict Land',
      'quaternary_desc': ''
  }, {
      'code': 'LW',
      'label': 'Water',
      'primary_code': 'L',
      'secondary_code': 'W',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Water',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'LW01',
      'label': 'Lake / Reservoir',
      'primary_code': 'L',
      'secondary_code': 'W',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Water',
      'tertiary_desc': 'Lake / Reservoir',
      'quaternary_desc': ''
  }, {
      'code': 'LW01BP',
      'label': 'Balancing Pond',
      'primary_code': 'L',
      'secondary_code': 'W',
      'tertiary_code': '1',
      'quaternary_code': 'BP',
      'primary_desc': 'Land',
      'secondary_desc': 'Water',
      'tertiary_desc': 'Lake / Reservoir',
      'quaternary_desc': 'Balancing Pond'
  }, {
      'code': 'LW01BV',
      'label': 'Buried Reservoir',
      'primary_code': 'L',
      'secondary_code': 'W',
      'tertiary_code': '1',
      'quaternary_code': 'BV',
      'primary_desc': 'Land',
      'secondary_desc': 'Water',
      'tertiary_desc': 'Lake / Reservoir',
      'quaternary_desc': 'Buried Reservoir'
  }, {
      'code': 'LW02',
      'label': 'Named Pond',
      'primary_code': 'L',
      'secondary_code': 'W',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Water',
      'tertiary_desc': 'Named Pond',
      'quaternary_desc': ''
  }, {
      'code': 'LW02DE',
      'label': 'Dew Pond',
      'primary_code': 'L',
      'secondary_code': 'W',
      'tertiary_code': '2',
      'quaternary_code': 'DE',
      'primary_desc': 'Land',
      'secondary_desc': 'Water',
      'tertiary_desc': 'Named Pond',
      'quaternary_desc': 'Dew Pond'
  }, {
      'code': 'LW02DP',
      'label': 'Decoy Pond',
      'primary_code': 'L',
      'secondary_code': 'W',
      'tertiary_code': '2',
      'quaternary_code': 'DP',
      'primary_desc': 'Land',
      'secondary_desc': 'Water',
      'tertiary_desc': 'Named Pond',
      'quaternary_desc': 'Decoy Pond'
  }, {
      'code': 'LW02IW',
      'label': 'Static Water',
      'primary_code': 'L',
      'secondary_code': 'W',
      'tertiary_code': '2',
      'quaternary_code': 'IW',
      'primary_desc': 'Land',
      'secondary_desc': 'Water',
      'tertiary_desc': 'Named Pond',
      'quaternary_desc': 'Static Water'
  }, {
      'code': 'LW03',
      'label': 'Waterway',
      'primary_code': 'L',
      'secondary_code': 'W',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Land',
      'secondary_desc': 'Water',
      'tertiary_desc': 'Waterway',
      'quaternary_desc': ''
  }, {
      'code': 'LW03DR',
      'label': 'Drain',
      'primary_code': 'L',
      'secondary_code': 'W',
      'tertiary_code': '3',
      'quaternary_code': 'DR',
      'primary_desc': 'Land',
      'secondary_desc': 'Water',
      'tertiary_desc': 'Waterway',
      'quaternary_desc': 'Drain'
  }, {
      'code': 'LW03LR',
      'label': 'Leats / Races',
      'primary_code': 'L',
      'secondary_code': 'W',
      'tertiary_code': '3',
      'quaternary_code': 'LR',
      'primary_desc': 'Land',
      'secondary_desc': 'Water',
      'tertiary_desc': 'Waterway',
      'quaternary_desc': 'Leats / Races'
  }, {
      'code': 'M',
      'label': 'Military',
      'primary_code': 'M',
      'secondary_code': '',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Military',
      'secondary_desc': '',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'MA',
      'label': 'Army',
      'primary_code': 'M',
      'secondary_code': 'A',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Military',
      'secondary_desc': 'Army',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'MA99AG',
      'label': 'Army Military Storage',
      'primary_code': 'M',
      'secondary_code': 'A',
      'tertiary_code': '99',
      'quaternary_code': 'AG',
      'primary_desc': 'Military',
      'secondary_desc': 'Army',
      'tertiary_desc': '',
      'quaternary_desc': 'Army Military Storage'
  }, {
      'code': 'MA99AR',
      'label': 'Army Military Range',
      'primary_code': 'M',
      'secondary_code': 'A',
      'tertiary_code': '99',
      'quaternary_code': 'AR',
      'primary_desc': 'Military',
      'secondary_desc': 'Army',
      'tertiary_desc': '',
      'quaternary_desc': 'Army Military Range'
  }, {
      'code': 'MA99AS',
      'label': 'Army Site',
      'primary_code': 'M',
      'secondary_code': 'A',
      'tertiary_code': '99',
      'quaternary_code': 'AS',
      'primary_desc': 'Military',
      'secondary_desc': 'Army',
      'tertiary_desc': '',
      'quaternary_desc': 'Army Site'
  }, {
      'code': 'MA99AT',
      'label': 'Army Military Training',
      'primary_code': 'M',
      'secondary_code': 'A',
      'tertiary_code': '99',
      'quaternary_code': 'AT',
      'primary_desc': 'Military',
      'secondary_desc': 'Army',
      'tertiary_desc': '',
      'quaternary_desc': 'Army Military Training'
  }, {
      'code': 'MB',
      'label': 'Military Ancillary Building',
      'primary_code': 'M',
      'secondary_code': 'B',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Military',
      'secondary_desc': 'Ancillary Building',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'MB99TG',
      'label': 'Military Target',
      'primary_code': 'M',
      'secondary_code': 'B',
      'tertiary_code': '99',
      'quaternary_code': 'TG',
      'primary_desc': 'Military',
      'secondary_desc': 'Ancillary Building',
      'tertiary_desc': '',
      'quaternary_desc': 'Military Target'
  }, {
      'code': 'MF',
      'label': 'Air Force',
      'primary_code': 'M',
      'secondary_code': 'F',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Military',
      'secondary_desc': 'Air Force',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'MF99UG',
      'label': 'Air Force Military Storage',
      'primary_code': 'M',
      'secondary_code': 'F',
      'tertiary_code': '99',
      'quaternary_code': 'UG',
      'primary_desc': 'Military',
      'secondary_desc': 'Air Force',
      'tertiary_desc': '',
      'quaternary_desc': 'Air Force Military Storage'
  }, {
      'code': 'MF99UR',
      'label': 'Air Force Military Range',
      'primary_code': 'M',
      'secondary_code': 'F',
      'tertiary_code': '99',
      'quaternary_code': 'UR',
      'primary_desc': 'Military',
      'secondary_desc': 'Air Force',
      'tertiary_desc': '',
      'quaternary_desc': 'Air Force Military Range'
  }, {
      'code': 'MF99US',
      'label': 'Air Force Site',
      'primary_code': 'M',
      'secondary_code': 'F',
      'tertiary_code': '99',
      'quaternary_code': 'US',
      'primary_desc': 'Military',
      'secondary_desc': 'Air Force',
      'tertiary_desc': '',
      'quaternary_desc': 'Air Force Site'
  }, {
      'code': 'MF99UT',
      'label': 'Air Force Military Training',
      'primary_code': 'M',
      'secondary_code': 'F',
      'tertiary_code': '99',
      'quaternary_code': 'UT',
      'primary_desc': 'Military',
      'secondary_desc': 'Air Force',
      'tertiary_desc': '',
      'quaternary_desc': 'Air Force Military Training'
  }, {
      'code': 'MG',
      'label': 'Defence Estates',
      'primary_code': 'M',
      'secondary_code': 'G',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Military',
      'secondary_desc': 'Defence Estates',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'MN',
      'label': 'Navy',
      'primary_code': 'M',
      'secondary_code': 'N',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Military',
      'secondary_desc': 'Navy',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'MN99VG',
      'label': 'Naval Military Storage',
      'primary_code': 'M',
      'secondary_code': 'N',
      'tertiary_code': '99',
      'quaternary_code': 'VG',
      'primary_desc': 'Military',
      'secondary_desc': 'Navy',
      'tertiary_desc': '',
      'quaternary_desc': 'Naval Military Storage'
  }, {
      'code': 'MN99VR',
      'label': 'Naval Military Range',
      'primary_code': 'M',
      'secondary_code': 'N',
      'tertiary_code': '99',
      'quaternary_code': 'VR',
      'primary_desc': 'Military',
      'secondary_desc': 'Navy',
      'tertiary_desc': '',
      'quaternary_desc': 'Naval Military Range'
  }, {
      'code': 'MN99VS',
      'label': 'Naval Site',
      'primary_code': 'M',
      'secondary_code': 'N',
      'tertiary_code': '99',
      'quaternary_code': 'VS',
      'primary_desc': 'Military',
      'secondary_desc': 'Navy',
      'tertiary_desc': '',
      'quaternary_desc': 'Naval Site'
  }, {
      'code': 'MN99VT',
      'label': 'Naval Military Training',
      'primary_code': 'M',
      'secondary_code': 'N',
      'tertiary_code': '99',
      'quaternary_code': 'VT',
      'primary_desc': 'Military',
      'secondary_desc': 'Navy',
      'tertiary_desc': '',
      'quaternary_desc': 'Naval Military Training'
  }, {
      'code': 'O',
      'label': 'Other (Ordnance Survey Only)',
      'primary_code': 'O',
      'secondary_code': '',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': '',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'OA',
      'label': 'Aid To Navigation',
      'primary_code': 'O',
      'secondary_code': 'A',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Aid To Navigation',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'OA01',
      'label': 'Aid To Aeronautical Navigation',
      'primary_code': 'O',
      'secondary_code': 'A',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Aid To Navigation',
      'tertiary_desc': 'Aid To Aeronautical Navigation',
      'quaternary_desc': ''
  }, {
      'code': 'OA01AL',
      'label': 'Aeronautical Navigation Beacon / Light',
      'primary_code': 'O',
      'secondary_code': 'A',
      'tertiary_code': '1',
      'quaternary_code': 'AL',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Aid To Navigation',
      'tertiary_desc': 'Aid To Aeronautical Navigation',
      'quaternary_desc': 'Aeronautical Navigation Beacon / Light'
  }, {
      'code': 'OA01LL',
      'label': 'Landing Light',
      'primary_code': 'O',
      'secondary_code': 'A',
      'tertiary_code': '1',
      'quaternary_code': 'LL',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Aid To Navigation',
      'tertiary_desc': 'Aid To Aeronautical Navigation',
      'quaternary_desc': 'Landing Light'
  }, {
      'code': 'OA01SQ',
      'label': 'Signal Square',
      'primary_code': 'O',
      'secondary_code': 'A',
      'tertiary_code': '1',
      'quaternary_code': 'SQ',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Aid To Navigation',
      'tertiary_desc': 'Aid To Aeronautical Navigation',
      'quaternary_desc': 'Signal Square'
  }, {
      'code': 'OA01WK',
      'label': 'Wind Sock / Wind Tee',
      'primary_code': 'O',
      'secondary_code': 'A',
      'tertiary_code': '1',
      'quaternary_code': 'WK',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Aid To Navigation',
      'tertiary_desc': 'Aid To Aeronautical Navigation',
      'quaternary_desc': 'Wind Sock / Wind Tee'
  }, {
      'code': 'OA02',
      'label': 'Aid To Nautical Navigation',
      'primary_code': 'O',
      'secondary_code': 'A',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Aid To Navigation',
      'tertiary_desc': 'Aid To Nautical Navigation',
      'quaternary_desc': ''
  }, {
      'code': 'OA02DM',
      'label': 'Daymark',
      'primary_code': 'O',
      'secondary_code': 'A',
      'tertiary_code': '2',
      'quaternary_code': 'DM',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Aid To Navigation',
      'tertiary_desc': 'Aid To Nautical Navigation',
      'quaternary_desc': 'Daymark'
  }, {
      'code': 'OA02FG',
      'label': 'Fog Horn Warning',
      'primary_code': 'O',
      'secondary_code': 'A',
      'tertiary_code': '2',
      'quaternary_code': 'FG',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Aid To Navigation',
      'tertiary_desc': 'Aid To Nautical Navigation',
      'quaternary_desc': 'Fog Horn Warning'
  }, {
      'code': 'OA02NL',
      'label': 'Nautical Navigation Beacon / Light',
      'primary_code': 'O',
      'secondary_code': 'A',
      'tertiary_code': '2',
      'quaternary_code': 'NL',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Aid To Navigation',
      'tertiary_desc': 'Aid To Nautical Navigation',
      'quaternary_desc': 'Nautical Navigation Beacon / Light'
  }, {
      'code': 'OA03',
      'label': 'Aid To Road Navigation',
      'primary_code': 'O',
      'secondary_code': 'A',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Aid To Navigation',
      'tertiary_desc': 'Aid To Road Navigation',
      'quaternary_desc': ''
  }, {
      'code': 'OA03GP',
      'label': 'Guide Post',
      'primary_code': 'O',
      'secondary_code': 'A',
      'tertiary_code': '3',
      'quaternary_code': 'GP',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Aid To Navigation',
      'tertiary_desc': 'Aid To Road Navigation',
      'quaternary_desc': 'Guide Post'
  }, {
      'code': 'OC',
      'label': 'Coastal Protection / Flood Prevention',
      'primary_code': 'O',
      'secondary_code': 'C',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Coastal Protection / Flood Prevention',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'OC01',
      'label': 'Boulder Wall / Sea Wall',
      'primary_code': 'O',
      'secondary_code': 'C',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Coastal Protection / Flood Prevention',
      'tertiary_desc': 'Boulder Wall / Sea Wall',
      'quaternary_desc': ''
  }, {
      'code': 'OC02',
      'label': 'Flood Gate / Flood Sluice Gate / Flood Valve',
      'primary_code': 'O',
      'secondary_code': 'C',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Coastal Protection / Flood Prevention',
      'tertiary_desc': 'Flood Gate / Flood Sluice Gate / Flood Valve',
      'quaternary_desc': ''
  }, {
      'code': 'OC03',
      'label': 'Groyne',
      'primary_code': 'O',
      'secondary_code': 'C',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Coastal Protection / Flood Prevention',
      'tertiary_desc': 'Groyne',
      'quaternary_desc': ''
  }, {
      'code': 'OC04',
      'label': 'Rip-Rap',
      'primary_code': 'O',
      'secondary_code': 'C',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Coastal Protection / Flood Prevention',
      'tertiary_desc': 'Rip-Rap',
      'quaternary_desc': ''
  }, {
      'code': 'OE',
      'label': 'Emergency Support',
      'primary_code': 'O',
      'secondary_code': 'E',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Emergency Support',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'OE01',
      'label': 'Beach Office / First Aid Facility',
      'primary_code': 'O',
      'secondary_code': 'E',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Emergency Support',
      'tertiary_desc': 'Beach Office / First Aid Facility',
      'quaternary_desc': ''
  }, {
      'code': 'OE02',
      'label': 'Emergency Telephone (Non Motorway)',
      'primary_code': 'O',
      'secondary_code': 'E',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Emergency Support',
      'tertiary_desc': 'Emergency Telephone (Non Motorway)',
      'quaternary_desc': ''
  }, {
      'code': 'OE03',
      'label':
      'Fire Alarm Structure / Fire Observation Tower / Fire Beater Facility',
      'primary_code': 'O',
      'secondary_code': 'E',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Emergency Support',
      'tertiary_desc':
      'Fire Alarm Structure / Fire Observation Tower / Fire Beater Facility',
      'quaternary_desc': ''
  }, {
      'code': 'OE04',
      'label': 'Emergency Equipment Point / Emergency Siren / Warning Flag',
      'primary_code': 'O',
      'secondary_code': 'E',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Emergency Support',
      'tertiary_desc':
      'Emergency Equipment Point / Emergency Siren / Warning Flag',
      'quaternary_desc': ''
  }, {
      'code': 'OE05',
      'label': 'Lifeguard Facility',
      'primary_code': 'O',
      'secondary_code': 'E',
      'tertiary_code': '5',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Emergency Support',
      'tertiary_desc': 'Lifeguard Facility',
      'quaternary_desc': ''
  }, {
      'code': 'OE06',
      'label': 'LIfe / Belt / Buoy / Float / Jacket / Safety Rope',
      'primary_code': 'O',
      'secondary_code': 'E',
      'tertiary_code': '6',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Emergency Support',
      'tertiary_desc': 'LIfe / Belt / Buoy / Float / Jacket / Safety Rope',
      'quaternary_desc': ''
  }, {
      'code': 'OF',
      'label': 'Street Furniture',
      'primary_code': 'O',
      'secondary_code': 'F',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Street Furniture',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'OG',
      'label': 'Agricultural Support Objects',
      'primary_code': 'O',
      'secondary_code': 'G',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Agricultural Support Objects',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'OG01',
      'label': 'Fish Ladder / Lock / Pen / Trap',
      'primary_code': 'O',
      'secondary_code': 'G',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Agricultural Support Objects',
      'tertiary_desc': 'Fish Ladder / Lock / Pen / Trap',
      'quaternary_desc': ''
  }, {
      'code': 'OG02',
      'label': 'Livestock Pen / Dip',
      'primary_code': 'O',
      'secondary_code': 'G',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Agricultural Support Objects',
      'tertiary_desc': 'Livestock Pen / Dip',
      'quaternary_desc': ''
  }, {
      'code': 'OG03',
      'label': 'Currick',
      'primary_code': 'O',
      'secondary_code': 'G',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Agricultural Support Objects',
      'tertiary_desc': 'Currick',
      'quaternary_desc': ''
  }, {
      'code': 'OG04',
      'label': 'Slurry Bed / Pit',
      'primary_code': 'O',
      'secondary_code': 'G',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Agricultural Support Objects',
      'tertiary_desc': 'Slurry Bed / Pit',
      'quaternary_desc': ''
  }, {
      'code': 'OH',
      'label': 'Historical Site / Object',
      'primary_code': 'O',
      'secondary_code': 'H',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Historical Site / Object',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'OH01',
      'label': 'Historic Structure / Object',
      'primary_code': 'O',
      'secondary_code': 'H',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Historical Site / Object',
      'tertiary_desc': 'Historic Structure / Object',
      'quaternary_desc': ''
  }, {
      'code': 'OI',
      'label': 'Industrial Support',
      'primary_code': 'O',
      'secondary_code': 'I',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Industrial Support',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'OI01',
      'label': 'Adit / Incline / Level',
      'primary_code': 'O',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Industrial Support',
      'tertiary_desc': 'Adit / Incline / Level',
      'quaternary_desc': ''
  }, {
      'code': 'OI02',
      'label': 'Caisson / Dry Dock / Grid',
      'primary_code': 'O',
      'secondary_code': 'I',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Industrial Support',
      'tertiary_desc': 'Caisson / Dry Dock / Grid',
      'quaternary_desc': ''
  }, {
      'code': 'OI03',
      'label': 'Channel / Conveyor / Conduit / Pipe',
      'primary_code': 'O',
      'secondary_code': 'I',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Industrial Support',
      'tertiary_desc': 'Channel / Conveyor / Conduit / Pipe',
      'quaternary_desc': ''
  }, {
      'code': 'OI04',
      'label': 'Chimney / Flue',
      'primary_code': 'O',
      'secondary_code': 'I',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Industrial Support',
      'tertiary_desc': 'Chimney / Flue',
      'quaternary_desc': ''
  }, {
      'code': 'OI05',
      'label': 'Crane / Hoist / Winch / Material Elevator',
      'primary_code': 'O',
      'secondary_code': 'I',
      'tertiary_code': '5',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Industrial Support',
      'tertiary_desc': 'Crane / Hoist / Winch / Material Elevator',
      'quaternary_desc': ''
  }, {
      'code': 'OI06',
      'label': 'Flare Stack',
      'primary_code': 'O',
      'secondary_code': 'I',
      'tertiary_code': '6',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Industrial Support',
      'tertiary_desc': 'Flare Stack',
      'quaternary_desc': ''
  }, {
      'code': 'OI07',
      'label': 'Hopper / Silo / Cistern / Tank',
      'primary_code': 'O',
      'secondary_code': 'I',
      'tertiary_code': '7',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Industrial Support',
      'tertiary_desc': 'Hopper / Silo / Cistern / Tank',
      'quaternary_desc': ''
  }, {
      'code': 'OI08',
      'label': 'Grab / Skip / Other Industrial Waste Machinery / Discharging',
      'primary_code': 'O',
      'secondary_code': 'I',
      'tertiary_code': '8',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Industrial Support',
      'tertiary_desc':
      'Grab / Skip / Other Industrial Waste Machinery / Discharging',
      'quaternary_desc': ''
  }, {
      'code': 'OI09',
      'label': 'Kiln / Oven / Smelter',
      'primary_code': 'O',
      'secondary_code': 'I',
      'tertiary_code': '9',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Industrial Support',
      'tertiary_desc': 'Kiln / Oven / Smelter',
      'quaternary_desc': ''
  }, {
      'code': 'OI10',
      'label': 'Manhole / Shaft',
      'primary_code': 'O',
      'secondary_code': 'I',
      'tertiary_code': '10',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Industrial Support',
      'tertiary_desc': 'Manhole / Shaft',
      'quaternary_desc': ''
  }, {
      'code': 'OI11',
      'label': 'Industrial Overflow / Sluice / Valve / Valve Housing',
      'primary_code': 'O',
      'secondary_code': 'I',
      'tertiary_code': '11',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Industrial Support',
      'tertiary_desc': 'Industrial Overflow / Sluice / Valve / Valve Housing',
      'quaternary_desc': ''
  }, {
      'code': 'OI12',
      'label': 'Cooling Tower',
      'primary_code': 'O',
      'secondary_code': 'I',
      'tertiary_code': '12',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Industrial Support',
      'tertiary_desc': 'Cooling Tower',
      'quaternary_desc': ''
  }, {
      'code': 'OI13',
      'label': 'Solar Panel / Waterwheel',
      'primary_code': 'O',
      'secondary_code': 'I',
      'tertiary_code': '13',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Industrial Support',
      'tertiary_desc': 'Solar Panel / Waterwheel',
      'quaternary_desc': ''
  }, {
      'code': 'OI14',
      'label': 'Telephone Pole / Post',
      'primary_code': 'O',
      'secondary_code': 'I',
      'tertiary_code': '14',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Industrial Support',
      'tertiary_desc': 'Telephone Pole / Post',
      'quaternary_desc': ''
  }, {
      'code': 'OI15',
      'label': 'Electricity Distribution Pole / Pylon',
      'primary_code': 'O',
      'secondary_code': 'I',
      'tertiary_code': '15',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Industrial Support',
      'tertiary_desc': 'Electricity Distribution Pole / Pylon',
      'quaternary_desc': ''
  }, {
      'code': 'ON',
      'label': 'Significant Natural Object',
      'primary_code': 'O',
      'secondary_code': 'N',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Significant Natural Object',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'ON01',
      'label': 'Boundary / Significant / Historic Tree / Pollard',
      'primary_code': 'O',
      'secondary_code': 'N',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Significant Natural Object',
      'tertiary_desc': 'Boundary / Significant / Historic Tree / Pollard',
      'quaternary_desc': ''
  }, {
      'code': 'ON02',
      'label': 'Boundary / Significant Rock / Boulder',
      'primary_code': 'O',
      'secondary_code': 'N',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Significant Natural Object',
      'tertiary_desc': 'Boundary / Significant Rock / Boulder',
      'quaternary_desc': ''
  }, {
      'code': 'ON03',
      'label': 'Natural Hole (Blow / Shake / Swallow)',
      'primary_code': 'O',
      'secondary_code': 'N',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Significant Natural Object',
      'tertiary_desc': 'Natural Hole (Blow / Shake / Swallow)',
      'quaternary_desc': ''
  }, {
      'code': 'OO',
      'label': 'Ornamental / Cultural Object',
      'primary_code': 'O',
      'secondary_code': 'O',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Ornamental / Cultural Object',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'OO02',
      'label': 'Mausoleum / Tomb / Grave',
      'primary_code': 'O',
      'secondary_code': 'O',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Ornamental / Cultural Object',
      'tertiary_desc': 'Mausoleum / Tomb / Grave',
      'quaternary_desc': ''
  }, {
      'code': 'OO03',
      'label': 'Simple Ornamental Object',
      'primary_code': 'O',
      'secondary_code': 'O',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Ornamental / Cultural Object',
      'tertiary_desc': 'Simple Ornamental Object',
      'quaternary_desc': ''
  }, {
      'code': 'OO04',
      'label': 'Maze',
      'primary_code': 'O',
      'secondary_code': 'O',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Ornamental / Cultural Object',
      'tertiary_desc': 'Maze',
      'quaternary_desc': ''
  }, {
      'code': 'OP',
      'label': 'Sport / Leisure Support',
      'primary_code': 'O',
      'secondary_code': 'P',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Sport / Leisure Support',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'OP01',
      'label': 'Butt / Hide',
      'primary_code': 'O',
      'secondary_code': 'P',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Sport / Leisure Support',
      'tertiary_desc': 'Butt / Hide',
      'quaternary_desc': ''
  }, {
      'code': 'OP02',
      'label': 'Gallop / Ride',
      'primary_code': 'O',
      'secondary_code': 'P',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Sport / Leisure Support',
      'tertiary_desc': 'Gallop / Ride',
      'quaternary_desc': ''
  }, {
      'code': 'OP03',
      'label': 'Miniature Railway',
      'primary_code': 'O',
      'secondary_code': 'P',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Sport / Leisure Support',
      'tertiary_desc': 'Miniature Railway',
      'quaternary_desc': ''
  }, {
      'code': 'OR',
      'label': 'Royal Mail Infrastructure',
      'primary_code': 'O',
      'secondary_code': 'R',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Royal Mail Infrastructure',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'OR01',
      'label': 'Postal Box',
      'primary_code': 'O',
      'secondary_code': 'R',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Royal Mail Infrastructure',
      'tertiary_desc': 'Postal Box',
      'quaternary_desc': ''
  }, {
      'code': 'OR02',
      'label': 'Postal Delivery Box / Pouch',
      'primary_code': 'O',
      'secondary_code': 'R',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Royal Mail Infrastructure',
      'tertiary_desc': 'Postal Delivery Box / Pouch',
      'quaternary_desc': ''
  }, {
      'code': 'OR03',
      'label': 'PO Box',
      'primary_code': 'O',
      'secondary_code': 'R',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Royal Mail Infrastructure',
      'tertiary_desc': 'PO Box',
      'quaternary_desc': ''
  }, {
      'code': 'OR04',
      'label': 'Additional Mail / Packet Addressee',
      'primary_code': 'O',
      'secondary_code': 'R',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Royal Mail Infrastructure',
      'tertiary_desc': 'Additional Mail / Packet Addressee',
      'quaternary_desc': ''
  }, {
      'code': 'OS',
      'label': 'Scientific / Observation Support',
      'primary_code': 'O',
      'secondary_code': 'S',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Scientific / Observation Support',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'OS01',
      'label': 'Meteorological Station / Equipment',
      'primary_code': 'O',
      'secondary_code': 'S',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Scientific / Observation Support',
      'tertiary_desc': 'Meteorological Station / Equipment',
      'quaternary_desc': ''
  }, {
      'code': 'OS02',
      'label': 'Radar / Satellite Infrastructure',
      'primary_code': 'O',
      'secondary_code': 'S',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Scientific / Observation Support',
      'tertiary_desc': 'Radar / Satellite Infrastructure',
      'quaternary_desc': ''
  }, {
      'code': 'OS03',
      'label': 'Telescope / Observation Infrastructure / Astronomy',
      'primary_code': 'O',
      'secondary_code': 'S',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Scientific / Observation Support',
      'tertiary_desc': 'Telescope / Observation Infrastructure / Astronomy',
      'quaternary_desc': ''
  }, {
      'code': 'OT',
      'label': 'Transport Support',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'OT01',
      'label': 'Cattle Grid / Ford',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Cattle Grid / Ford',
      'quaternary_desc': ''
  }, {
      'code': 'OT02',
      'label': 'Elevator / Escalator / Steps',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Elevator / Escalator / Steps',
      'quaternary_desc': ''
  }, {
      'code': 'OT03',
      'label': 'Footbridge / Walkway',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Footbridge / Walkway',
      'quaternary_desc': ''
  }, {
      'code': 'OT04',
      'label': 'Pole / Post / Bollard (Restricting Vehicular Access)',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Pole / Post / Bollard (Restricting Vehicular Access)',
      'quaternary_desc': ''
  }, {
      'code': 'OT05',
      'label': 'Subway / Underpass',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '5',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Subway / Underpass',
      'quaternary_desc': ''
  }, {
      'code': 'OT06',
      'label': 'Customs Inspection Facility',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '6',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Customs Inspection Facility',
      'quaternary_desc': ''
  }, {
      'code': 'OT07',
      'label': 'Lay-By',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '7',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Lay-By',
      'quaternary_desc': ''
  }, {
      'code': 'OT08',
      'label': 'Level Crossing',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '8',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Level Crossing',
      'quaternary_desc': ''
  }, {
      'code': 'OT09',
      'label': 'Mail Pick Up',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '9',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Mail Pick Up',
      'quaternary_desc': ''
  }, {
      'code': 'OT10',
      'label': 'Railway Pedestrian Crossing',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '10',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Railway Pedestrian Crossing',
      'quaternary_desc': ''
  }, {
      'code': 'OT11',
      'label': 'Railway Buffer',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '11',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Railway Buffer',
      'quaternary_desc': ''
  }, {
      'code': 'OT12',
      'label': 'Rail Drag',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '12',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Rail Drag',
      'quaternary_desc': ''
  }, {
      'code': 'OT13',
      'label': 'Rail Infrastructure Services',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '13',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Rail Infrastructure Services',
      'quaternary_desc': ''
  }, {
      'code': 'OT14',
      'label': 'Rail Kilometre Distance Marker',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '14',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Rail Kilometre Distance Marker',
      'quaternary_desc': ''
  }, {
      'code': 'OT15',
      'label': 'Railway Lighting',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '15',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Railway Lighting',
      'quaternary_desc': ''
  }, {
      'code': 'OT16',
      'label': 'Rail Mile Distance Marker',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '16',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Rail Mile Distance Marker',
      'quaternary_desc': ''
  }, {
      'code': 'OT17',
      'label': 'Railway Turntable',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '17',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Railway Turntable',
      'quaternary_desc': ''
  }, {
      'code': 'OT18',
      'label': 'Rail Weighbridge',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '18',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Rail Weighbridge',
      'quaternary_desc': ''
  }, {
      'code': 'OT19',
      'label': 'Rail Signalling',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '19',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Rail Signalling',
      'quaternary_desc': ''
  }, {
      'code': 'OT20',
      'label': 'Railway Traverse',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '20',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Railway Traverse',
      'quaternary_desc': ''
  }, {
      'code': 'OT21',
      'label': 'Goods Tramway',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '21',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Goods Tramway',
      'quaternary_desc': ''
  }, {
      'code': 'OT22',
      'label': 'Road Drag',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '22',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Road Drag',
      'quaternary_desc': ''
  }, {
      'code': 'OT23',
      'label': 'Vehicle Dip',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '23',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Vehicle Dip',
      'quaternary_desc': ''
  }, {
      'code': 'OT24',
      'label': 'Road Turntable',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '24',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Road Turntable',
      'quaternary_desc': ''
  }, {
      'code': 'OT25',
      'label': 'Road Mile Distance Marker',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '25',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Road Mile Distance Marker',
      'quaternary_desc': ''
  }, {
      'code': 'OT26',
      'label': 'Road Kilometre Distance Marker',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '26',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Road Kilometre Distance Marker',
      'quaternary_desc': ''
  }, {
      'code': 'OT27',
      'label': 'Road Infrastructure Services',
      'primary_code': 'O',
      'secondary_code': 'T',
      'tertiary_code': '27',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Transport Support',
      'tertiary_desc': 'Road Infrastructure Services',
      'quaternary_desc': ''
  }, {
      'code': 'OU',
      'label': 'Unsupported Site',
      'primary_code': 'O',
      'secondary_code': 'U',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Unsupported Site',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'OU01',
      'label': 'Cycle Parking Facility',
      'primary_code': 'O',
      'secondary_code': 'U',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Unsupported Site',
      'tertiary_desc': 'Cycle Parking Facility',
      'quaternary_desc': ''
  }, {
      'code': 'OU04',
      'label': 'Picnic / Barbeque Site',
      'primary_code': 'O',
      'secondary_code': 'U',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Unsupported Site',
      'tertiary_desc': 'Picnic / Barbeque Site',
      'quaternary_desc': ''
  }, {
      'code': 'OU05',
      'label': 'Travelling Persons Site',
      'primary_code': 'O',
      'secondary_code': 'U',
      'tertiary_code': '5',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Unsupported Site',
      'tertiary_desc': 'Travelling Persons Site',
      'quaternary_desc': ''
  }, {
      'code': 'OU08',
      'label': 'Shelter (Not Including Bus Shelter)',
      'primary_code': 'O',
      'secondary_code': 'U',
      'tertiary_code': '8',
      'quaternary_code': '',
      'primary_desc': 'Other (Ordnance Survey Only)',
      'secondary_desc': 'Unsupported Site',
      'tertiary_desc': 'Shelter (Not Including Bus Shelter)',
      'quaternary_desc': ''
  }, {
      'code': 'P',
      'label': 'Parent Shell',
      'primary_code': 'P',
      'secondary_code': '',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Parent Shell',
      'secondary_desc': '',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'PP',
      'label': 'Property Shell',
      'primary_code': 'P',
      'secondary_code': 'P',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Parent Shell',
      'secondary_desc': 'Property Shell',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'PS',
      'label': 'Street Record',
      'primary_code': 'P',
      'secondary_code': 'S',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Parent Shell',
      'secondary_desc': 'Street Record',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'R',
      'label': 'Residential',
      'primary_code': 'R',
      'secondary_code': '',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': '',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'RB',
      'label': 'Residential Ancillary Building',
      'primary_code': 'R',
      'secondary_code': 'B',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'Ancillary Building',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'RC',
      'label': 'Car Park Space',
      'primary_code': 'R',
      'secondary_code': 'C',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'Car Park Space',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'RC01',
      'label': 'Allocated Parking',
      'primary_code': 'R',
      'secondary_code': 'C',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'Car Park Space',
      'tertiary_desc': 'Allocated Parking',
      'quaternary_desc': ''
  }, {
      'code': 'RD',
      'label': 'Dwelling',
      'primary_code': 'R',
      'secondary_code': 'D',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'Dwelling',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'RD01',
      'label': 'Caravan',
      'primary_code': 'R',
      'secondary_code': 'D',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'Dwelling',
      'tertiary_desc': 'Caravan',
      'quaternary_desc': ''
  }, {
      'code': 'RD02',
      'label': 'Detached',
      'primary_code': 'R',
      'secondary_code': 'D',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'Dwelling',
      'tertiary_desc': 'Detached',
      'quaternary_desc': ''
  }, {
      'code': 'RD03',
      'label': 'Semi-Detached',
      'primary_code': 'R',
      'secondary_code': 'D',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'Dwelling',
      'tertiary_desc': 'Semi-Detached',
      'quaternary_desc': ''
  }, {
      'code': 'RD04',
      'label': 'Terraced',
      'primary_code': 'R',
      'secondary_code': 'D',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'Dwelling',
      'tertiary_desc': 'Terraced',
      'quaternary_desc': ''
  }, {
      'code': 'RD06',
      'label': 'Self Contained Flat (Includes Maisonette / Apartment)',
      'primary_code': 'R',
      'secondary_code': 'D',
      'tertiary_code': '6',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'Dwelling',
      'tertiary_desc': 'Self Contained Flat (Includes Maisonette / Apartment)',
      'quaternary_desc': ''
  }, {
      'code': 'RD07',
      'label': 'House Boat',
      'primary_code': 'R',
      'secondary_code': 'D',
      'tertiary_code': '7',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'Dwelling',
      'tertiary_desc': 'House Boat',
      'quaternary_desc': ''
  }, {
      'code': 'RD08',
      'label': 'Sheltered Accommodation',
      'primary_code': 'R',
      'secondary_code': 'D',
      'tertiary_code': '8',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'Dwelling',
      'tertiary_desc': 'Sheltered Accommodation',
      'quaternary_desc': ''
  }, {
      'code': 'RD10',
      'label': 'Privately Owned Holiday Caravan / Chalet',
      'primary_code': 'R',
      'secondary_code': 'D',
      'tertiary_code': '10',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'Dwelling',
      'tertiary_desc': 'Privately Owned Holiday Caravan / Chalet',
      'quaternary_desc': ''
  }, {
      'code': 'RG',
      'label': 'Garage',
      'primary_code': 'R',
      'secondary_code': 'G',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'Garage',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'RG02',
      'label': 'Lock-Up Garage / Garage Court',
      'primary_code': 'R',
      'secondary_code': 'G',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'Garage',
      'tertiary_desc': 'Lock-Up Garage / Garage Court',
      'quaternary_desc': ''
  }, {
      'code': 'RH',
      'label': 'House In Multiple Occupation',
      'primary_code': 'R',
      'secondary_code': 'H',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'House In Multiple Occupation',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'RH01',
      'label': 'HMO Parent',
      'primary_code': 'R',
      'secondary_code': 'H',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'House In Multiple Occupation',
      'tertiary_desc': 'HMO Parent',
      'quaternary_desc': ''
  }, {
      'code': 'RH02',
      'label': 'HMO Bedsit / Other Non Self Contained Accommodation',
      'primary_code': 'R',
      'secondary_code': 'H',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'House In Multiple Occupation',
      'tertiary_desc': 'HMO Bedsit / Other Non Self Contained Accommodation',
      'quaternary_desc': ''
  }, {
      'code': 'RH03',
      'label': 'HMO Not Further Divided',
      'primary_code': 'R',
      'secondary_code': 'H',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'House In Multiple Occupation',
      'tertiary_desc': 'HMO Not Further Divided',
      'quaternary_desc': ''
  }, {
      'code': 'RI',
      'label': 'Residential Institution',
      'primary_code': 'R',
      'secondary_code': 'I',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'Residential Institution',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'RI01',
      'label': 'Care / Nursing Home',
      'primary_code': 'R',
      'secondary_code': 'I',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'Residential Institution',
      'tertiary_desc': 'Care / Nursing Home',
      'quaternary_desc': ''
  }, {
      'code': 'RI02',
      'label': 'Communal Residence',
      'primary_code': 'R',
      'secondary_code': 'I',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'Residential Institution',
      'tertiary_desc': 'Communal Residence',
      'quaternary_desc': ''
  }, {
      'code': 'RI02NC',
      'label': 'Non-Commercial Lodgings',
      'primary_code': 'R',
      'secondary_code': 'I',
      'tertiary_code': '2',
      'quaternary_code': 'NC',
      'primary_desc': 'Residential',
      'secondary_desc': 'Residential Institution',
      'tertiary_desc': 'Communal Residence',
      'quaternary_desc': 'Non-Commercial Lodgings'
  }, {
      'code': 'RI02RC',
      'label': 'Religious Community',
      'primary_code': 'R',
      'secondary_code': 'I',
      'tertiary_code': '2',
      'quaternary_code': 'RC',
      'primary_desc': 'Residential',
      'secondary_desc': 'Residential Institution',
      'tertiary_desc': 'Communal Residence',
      'quaternary_desc': 'Religious Community'
  }, {
      'code': 'RI03',
      'label': 'Residential Education',
      'primary_code': 'R',
      'secondary_code': 'I',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Residential',
      'secondary_desc': 'Residential Institution',
      'tertiary_desc': 'Residential Education',
      'quaternary_desc': ''
  }, {
      'code': 'U',
      'label': 'Unclassified',
      'primary_code': 'U',
      'secondary_code': '',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Unclassified',
      'secondary_desc': '',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'UC',
      'label': 'Awaiting Classification',
      'primary_code': 'U',
      'secondary_code': 'C',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Unclassified',
      'secondary_desc': 'Awaiting Classification',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'UP',
      'label': 'Pending Internal Investigation',
      'primary_code': 'U',
      'secondary_code': 'P',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Unclassified',
      'secondary_desc': 'Pending Internal Investigation',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'X',
      'label': 'Dual Use',
      'primary_code': 'X',
      'secondary_code': '',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Dual Use',
      'secondary_desc': '',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'Z',
      'label': 'Object of Interest',
      'primary_code': 'Z',
      'secondary_code': '',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Object of Interest',
      'secondary_desc': '',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'ZA',
      'label': 'Archaeological Dig Site',
      'primary_code': 'Z',
      'secondary_code': 'A',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Archaeological Dig Site',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'ZM',
      'label': 'Monument',
      'primary_code': 'Z',
      'secondary_code': 'M',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Monument',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'ZM01',
      'label': 'Obelisk / Milestone / Standing Stone',
      'primary_code': 'Z',
      'secondary_code': 'M',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Monument',
      'tertiary_desc': 'Obelisk / Milestone / Standing Stone',
      'quaternary_desc': ''
  }, {
      'code': 'ZM01OB',
      'label': 'Obelisk',
      'primary_code': 'Z',
      'secondary_code': 'M',
      'tertiary_code': '1',
      'quaternary_code': 'OB',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Monument',
      'tertiary_desc': 'Obelisk / Milestone / Standing Stone',
      'quaternary_desc': 'Obelisk'
  }, {
      'code': 'ZM01ST',
      'label': 'Standing Stone',
      'primary_code': 'Z',
      'secondary_code': 'M',
      'tertiary_code': '1',
      'quaternary_code': 'ST',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Monument',
      'tertiary_desc': 'Obelisk / Milestone / Standing Stone',
      'quaternary_desc': 'Standing Stone'
  }, {
      'code': 'ZM02',
      'label': 'Memorial / Market Cross',
      'primary_code': 'Z',
      'secondary_code': 'M',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Monument',
      'tertiary_desc': 'Memorial / Market Cross',
      'quaternary_desc': ''
  }, {
      'code': 'ZM03',
      'label': 'Statue',
      'primary_code': 'Z',
      'secondary_code': 'M',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Monument',
      'tertiary_desc': 'Statue',
      'quaternary_desc': ''
  }, {
      'code': 'ZM04',
      'label': 'Castle / Historic Ruin',
      'primary_code': 'Z',
      'secondary_code': 'M',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Monument',
      'tertiary_desc': 'Castle / Historic Ruin',
      'quaternary_desc': ''
  }, {
      'code': 'ZM05',
      'label': 'Other Structure',
      'primary_code': 'Z',
      'secondary_code': 'M',
      'tertiary_code': '5',
      'quaternary_code': '',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Monument',
      'tertiary_desc': 'Other Structure',
      'quaternary_desc': ''
  }, {
      'code': 'ZM05BS',
      'label': 'Boundary Stone',
      'primary_code': 'Z',
      'secondary_code': 'M',
      'tertiary_code': '5',
      'quaternary_code': 'BS',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Monument',
      'tertiary_desc': 'Other Structure',
      'quaternary_desc': 'Boundary Stone'
  }, {
      'code': 'ZM05CE',
      'label': 'Cascade / Fountain',
      'primary_code': 'Z',
      'secondary_code': 'M',
      'tertiary_code': '5',
      'quaternary_code': 'CE',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Monument',
      'tertiary_desc': 'Other Structure',
      'quaternary_desc': 'Cascade / Fountain'
  }, {
      'code': 'ZM05PN',
      'label': 'Permanent Art Display / Sculpture',
      'primary_code': 'Z',
      'secondary_code': 'M',
      'tertiary_code': '5',
      'quaternary_code': 'PN',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Monument',
      'tertiary_desc': 'Other Structure',
      'quaternary_desc': 'Permanent Art Display / Sculpture'
  }, {
      'code': 'ZM05WI',
      'label': 'Windmill (Inactive)',
      'primary_code': 'Z',
      'secondary_code': 'M',
      'tertiary_code': '5',
      'quaternary_code': 'WI',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Monument',
      'tertiary_desc': 'Other Structure',
      'quaternary_desc': 'Windmill (Inactive)'
  }, {
      'code': 'ZS',
      'label': 'Stately Home',
      'primary_code': 'Z',
      'secondary_code': 'S',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Stately Home',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'ZU',
      'label': 'Underground Feature',
      'primary_code': 'Z',
      'secondary_code': 'U',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Underground Feature',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'ZU01',
      'label': 'Cave',
      'primary_code': 'Z',
      'secondary_code': 'U',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Underground Feature',
      'tertiary_desc': 'Cave',
      'quaternary_desc': ''
  }, {
      'code': 'ZU04',
      'label': 'Pothole / Natural Hole',
      'primary_code': 'Z',
      'secondary_code': 'U',
      'tertiary_code': '4',
      'quaternary_code': '',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Underground Feature',
      'tertiary_desc': 'Pothole / Natural Hole',
      'quaternary_desc': ''
  }, {
      'code': 'ZV',
      'label': 'Other Underground Feature',
      'primary_code': 'Z',
      'secondary_code': 'V',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Other Underground Feature',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'ZV01',
      'label': 'Cellar',
      'primary_code': 'Z',
      'secondary_code': 'V',
      'tertiary_code': '1',
      'quaternary_code': '',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Other Underground Feature',
      'tertiary_desc': 'Cellar',
      'quaternary_desc': ''
  }, {
      'code': 'ZV02',
      'label': 'Disused Mine',
      'primary_code': 'Z',
      'secondary_code': 'V',
      'tertiary_code': '2',
      'quaternary_code': '',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Other Underground Feature',
      'tertiary_desc': 'Disused Mine',
      'quaternary_desc': ''
  }, {
      'code': 'ZV02MI',
      'label': 'Mineral Mining / Inactive',
      'primary_code': 'Z',
      'secondary_code': 'V',
      'tertiary_code': '2',
      'quaternary_code': 'MI',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Other Underground Feature',
      'tertiary_desc': 'Disused Mine',
      'quaternary_desc': 'Mineral Mining / Inactive'
  }, {
      'code': 'ZV02OI',
      'label': 'Oil And / Gas Extraction/ Inactive',
      'primary_code': 'Z',
      'secondary_code': 'V',
      'tertiary_code': '2',
      'quaternary_code': 'OI',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Other Underground Feature',
      'tertiary_desc': 'Disused Mine',
      'quaternary_desc': 'Oil And / Gas Extraction/ Inactive'
  }, {
      'code':
      'ZV02QI',
      'label':
      'Mineral Quarrying And / Open Extraction / Inactive',
      'primary_code':
      'Z',
      'secondary_code':
      'V',
      'tertiary_code':
      '2',
      'quaternary_code':
      'QI',
      'primary_desc':
      'Object of Interest',
      'secondary_desc':
      'Other Underground Feature',
      'tertiary_desc':
      'Disused Mine',
      'quaternary_desc':
      'Mineral Quarrying And / Open Extraction / Inactive'
  }, {
      'code': 'ZV03',
      'label': 'Well / Spring',
      'primary_code': 'Z',
      'secondary_code': 'V',
      'tertiary_code': '3',
      'quaternary_code': '',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Other Underground Feature',
      'tertiary_desc': 'Well / Spring',
      'quaternary_desc': ''
  }, {
      'code': 'ZV03SG',
      'label': 'Spring',
      'primary_code': 'Z',
      'secondary_code': 'V',
      'tertiary_code': '3',
      'quaternary_code': 'SG',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Other Underground Feature',
      'tertiary_desc': 'Well / Spring',
      'quaternary_desc': 'Spring'
  }, {
      'code': 'ZV03WL',
      'label': 'Well',
      'primary_code': 'Z',
      'secondary_code': 'V',
      'tertiary_code': '3',
      'quaternary_code': 'WL',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Other Underground Feature',
      'tertiary_desc': 'Well / Spring',
      'quaternary_desc': 'Well'
  }, {
      'code': 'ZW',
      'label': 'Place Of Worship',
      'primary_code': 'Z',
      'secondary_code': 'W',
      'tertiary_code': '',
      'quaternary_code': '',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Place Of Worship',
      'tertiary_desc': '',
      'quaternary_desc': ''
  }, {
      'code': 'ZW99AB',
      'label': 'Abbey',
      'primary_code': 'Z',
      'secondary_code': 'W',
      'tertiary_code': '99',
      'quaternary_code': 'AB',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Place Of Worship',
      'tertiary_desc': '',
      'quaternary_desc': 'Abbey'
  }, {
      'code': 'ZW99CA',
      'label': 'Cathedral',
      'primary_code': 'Z',
      'secondary_code': 'W',
      'tertiary_code': '99',
      'quaternary_code': 'CA',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Place Of Worship',
      'tertiary_desc': '',
      'quaternary_desc': 'Cathedral'
  }, {
      'code': 'ZW99CH',
      'label': 'Church',
      'primary_code': 'Z',
      'secondary_code': 'W',
      'tertiary_code': '99',
      'quaternary_code': 'CH',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Place Of Worship',
      'tertiary_desc': '',
      'quaternary_desc': 'Church'
  }, {
      'code': 'ZW99CP',
      'label': 'Chapel',
      'primary_code': 'Z',
      'secondary_code': 'W',
      'tertiary_code': '99',
      'quaternary_code': 'CP',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Place Of Worship',
      'tertiary_desc': '',
      'quaternary_desc': 'Chapel'
  }, {
      'code': 'ZW99GU',
      'label': 'Gurdwara',
      'primary_code': 'Z',
      'secondary_code': 'W',
      'tertiary_code': '99',
      'quaternary_code': 'GU',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Place Of Worship',
      'tertiary_desc': '',
      'quaternary_desc': 'Gurdwara'
  }, {
      'code': 'ZW99KH',
      'label': 'Kingdom Hall',
      'primary_code': 'Z',
      'secondary_code': 'W',
      'tertiary_code': '99',
      'quaternary_code': 'KH',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Place Of Worship',
      'tertiary_desc': '',
      'quaternary_desc': 'Kingdom Hall'
  }, {
      'code': 'ZW99LG',
      'label': 'Lych Gate',
      'primary_code': 'Z',
      'secondary_code': 'W',
      'tertiary_code': '99',
      'quaternary_code': 'LG',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Place Of Worship',
      'tertiary_desc': '',
      'quaternary_desc': 'Lych Gate'
  }, {
      'code': 'ZW99MQ',
      'label': 'Mosque',
      'primary_code': 'Z',
      'secondary_code': 'W',
      'tertiary_code': '99',
      'quaternary_code': 'MQ',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Place Of Worship',
      'tertiary_desc': '',
      'quaternary_desc': 'Mosque'
  }, {
      'code': 'ZW99MT',
      'label': 'Minster',
      'primary_code': 'Z',
      'secondary_code': 'W',
      'tertiary_code': '99',
      'quaternary_code': 'MT',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Place Of Worship',
      'tertiary_desc': '',
      'quaternary_desc': 'Minster'
  }, {
      'code': 'ZW99SU',
      'label': 'Stupa',
      'primary_code': 'Z',
      'secondary_code': 'W',
      'tertiary_code': '99',
      'quaternary_code': 'SU',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Place Of Worship',
      'tertiary_desc': '',
      'quaternary_desc': 'Stupa'
  }, {
      'code': 'ZW99SY',
      'label': 'Synagogue',
      'primary_code': 'Z',
      'secondary_code': 'W',
      'tertiary_code': '99',
      'quaternary_code': 'SY',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Place Of Worship',
      'tertiary_desc': '',
      'quaternary_desc': 'Synagogue'
  }, {
      'code': 'ZW99TP',
      'label': 'Temple',
      'primary_code': 'Z',
      'secondary_code': 'W',
      'tertiary_code': '99',
      'quaternary_code': 'TP',
      'primary_desc': 'Object of Interest',
      'secondary_desc': 'Place Of Worship',
      'tertiary_desc': '',
      'quaternary_desc': 'Temple'
  }]

  return expected_json


# In the format [{'code': 'ZW99TP', 'class_list_string': '[Object of Interest] [Place Of Worship] [Temple]'}, ...]
def return_classifications_code_and_expected_string_pairs():
  classification_codes_and_string_pairs = [{
      'code': 'C',
      'class_list_string': '[Commercial]'
  }, {
      'code':
      'CA',
      'class_list_string':
      '[Commercial] [Agricultural]'
  }, {
      'code':
      'CA01',
      'class_list_string':
      '[Commercial] [Agricultural] [Farm / Non-Residential Associated Building]'
  }, {
      'code':
      'CA02',
      'class_list_string':
      '[Commercial] [Agricultural] [Fishery]'
  }, {
      'code':
      'CA02FF',
      'class_list_string':
      '[Commercial] [Agricultural] [Fishery] [Fish Farming]'
  }, {
      'code':
      'CA02FH',
      'class_list_string':
      '[Commercial] [Agricultural] [Fishery] [Fish Hatchery]'
  }, {
      'code':
      'CA02FP',
      'class_list_string':
      '[Commercial] [Agricultural] [Fishery] [Fish Processing]'
  }, {
      'code':
      'CA02OY',
      'class_list_string':
      '[Commercial] [Agricultural] [Fishery] [Oyster / Mussel Bed]'
  }, {
      'code':
      'CA03',
      'class_list_string':
      '[Commercial] [Agricultural] [Horticulture]'
  }, {
      'code':
      'CA03SH',
      'class_list_string':
      '[Commercial] [Agricultural] [Horticulture] [Smallholding]'
  }, {
      'code':
      'CA03VY',
      'class_list_string':
      '[Commercial] [Agricultural] [Horticulture] [Vineyard]'
  }, {
      'code':
      'CA03WB',
      'class_list_string':
      '[Commercial] [Agricultural] [Horticulture] [Watercress Bed]'
  }, {
      'code':
      'CA04',
      'class_list_string':
      '[Commercial] [Agricultural] [Slaughter House / Abattoir]'
  }, {
      'code':
      'CB',
      'class_list_string':
      '[Commercial] [Ancillary Building]'
  }, {
      'code':
      'CC',
      'class_list_string':
      '[Commercial] [Community Services]'
  }, {
      'code':
      'CC02',
      'class_list_string':
      '[Commercial] [Community Services] [Law Court]'
  }, {
      'code':
      'CC03',
      'class_list_string':
      '[Commercial] [Community Services] [Prison]'
  }, {
      'code':
      'CC03HD',
      'class_list_string':
      '[Commercial] [Community Services] [Prison] [HM Detention Centre]'
  }, {
      'code':
      'CC03PR',
      'class_list_string':
      '[Commercial] [Community Services] [Prison] [HM Prison Service]'
  }, {
      'code':
      'CC03SC',
      'class_list_string':
      '[Commercial] [Community Services] [Prison] [Secure Residential Accommodation]'
  }, {
      'code':
      'CC04',
      'class_list_string':
      '[Commercial] [Community Services] [Public / Village Hall / Other Community Facility]'
  }, {
      'code':
      'CC04YR',
      'class_list_string':
      '[Commercial] [Community Services] [Public / Village Hall / Other Community Facility] [Youth Recreational / Social Club]'
  }, {
      'code':
      'CC05',
      'class_list_string':
      '[Commercial] [Community Services] [Public Convenience]'
  }, {
      'code':
      'CC06',
      'class_list_string':
      '[Commercial] [Community Services] [Cemetery / Crematorium / Graveyard. In Current Use.]'
  }, {
      'code':
      'CC06CB',
      'class_list_string':
      '[Commercial] [Community Services] [Cemetery / Crematorium / Graveyard. In Current Use.] [Columbarium]'
  }, {
      'code':
      'CC06CN',
      'class_list_string':
      '[Commercial] [Community Services] [Cemetery / Crematorium / Graveyard. In Current Use.] [Crematorium]'
  }, {
      'code':
      'CC06CR',
      'class_list_string':
      '[Commercial] [Community Services] [Cemetery / Crematorium / Graveyard. In Current Use.] [Chapel Of Rest]'
  }, {
      'code':
      'CC06CY',
      'class_list_string':
      '[Commercial] [Community Services] [Cemetery / Crematorium / Graveyard. In Current Use.] [Cemetery]'
  }, {
      'code':
      'CC06MC',
      'class_list_string':
      '[Commercial] [Community Services] [Cemetery / Crematorium / Graveyard. In Current Use.] [Military Cemetery]'
  }, {
      'code':
      'CC06MY',
      'class_list_string':
      '[Commercial] [Community Services] [Cemetery / Crematorium / Graveyard. In Current Use.] [Mortuary]'
  }, {
      'code':
      'CC07',
      'class_list_string':
      '[Commercial] [Community Services] [Church Hall / Religious Meeting Place / Hall]'
  }, {
      'code':
      'CC08',
      'class_list_string':
      '[Commercial] [Community Services] [Community Service Centre / Office]'
  }, {
      'code':
      'CC09',
      'class_list_string':
      '[Commercial] [Community Services] [Public Household Waste Recycling Centre (HWRC)]'
  }, {
      'code':
      'CC10',
      'class_list_string':
      '[Commercial] [Community Services] [Recycling Site]'
  }, {
      'code':
      'CC11',
      'class_list_string':
      '[Commercial] [Community Services] [CCTV]'
  }, {
      'code':
      'CC12',
      'class_list_string':
      '[Commercial] [Community Services] [Job Centre]'
  }, {
      'code':
      'CE',
      'class_list_string':
      '[Commercial] [Education]'
  }, {
      'code':
      'CE01',
      'class_list_string':
      '[Commercial] [Education] [College]'
  }, {
      'code':
      'CE01FE',
      'class_list_string':
      '[Commercial] [Education] [College] [Further Education]'
  }, {
      'code':
      'CE01HE',
      'class_list_string':
      '[Commercial] [Education] [College] [Higher Education]'
  }, {
      'code':
      'CE02',
      'class_list_string':
      '[Commercial] [Education] [Children’s Nursery / Crèche]'
  }, {
      'code':
      'CE03',
      'class_list_string':
      '[Commercial] [Education] [Preparatory / First / Primary / Infant / Junior / Middle School]'
  }, {
      'code':
      'CE03FS',
      'class_list_string':
      '[Commercial] [Education] [Preparatory / First / Primary / Infant / Junior / Middle School] [First School]'
  }, {
      'code':
      'CE03IS',
      'class_list_string':
      '[Commercial] [Education] [Preparatory / First / Primary / Infant / Junior / Middle School] [Infant School]'
  }, {
      'code':
      'CE03JS',
      'class_list_string':
      '[Commercial] [Education] [Preparatory / First / Primary / Infant / Junior / Middle School] [Junior School]'
  }, {
      'code':
      'CE03MS',
      'class_list_string':
      '[Commercial] [Education] [Preparatory / First / Primary / Infant / Junior / Middle School] [Middle School]'
  }, {
      'code':
      'CE03NP',
      'class_list_string':
      '[Commercial] [Education] [Preparatory / First / Primary / Infant / Junior / Middle School] [Non State Primary / Preparatory School]'
  }, {
      'code':
      'CE03PS',
      'class_list_string':
      '[Commercial] [Education] [Preparatory / First / Primary / Infant / Junior / Middle School] [Primary School]'
  }, {
      'code':
      'CE04',
      'class_list_string':
      '[Commercial] [Education] [Secondary / High School]'
  }, {
      'code':
      'CE04NS',
      'class_list_string':
      '[Commercial] [Education] [Secondary / High School] [Non State Secondary School]'
  }, {
      'code':
      'CE04SS',
      'class_list_string':
      '[Commercial] [Education] [Secondary / High School] [Secondary School]'
  }, {
      'code':
      'CE05',
      'class_list_string':
      '[Commercial] [Education] [University]'
  }, {
      'code':
      'CE06',
      'class_list_string':
      '[Commercial] [Education] [Special Needs Establishment.]'
  }, {
      'code':
      'CE07',
      'class_list_string':
      '[Commercial] [Education] [Other Educational Establishment]'
  }, {
      'code':
      'CH',
      'class_list_string':
      '[Commercial] [Hotel / Motel / Boarding / Guest House]'
  }, {
      'code':
      'CH01',
      'class_list_string':
      '[Commercial] [Hotel / Motel / Boarding / Guest House] [Boarding / Guest House / Bed And Breakfast / Youth Hostel]'
  }, {
      'code':
      'CH01YH',
      'class_list_string':
      '[Commercial] [Hotel / Motel / Boarding / Guest House] [Boarding / Guest House / Bed And Breakfast / Youth Hostel] [Youth Hostel]'
  }, {
      'code':
      'CH02',
      'class_list_string':
      '[Commercial] [Hotel / Motel / Boarding / Guest House] [Holiday Let/Accomodation/Short-Term Let Other Than CH01]'
  }, {
      'code':
      'CH03',
      'class_list_string':
      '[Commercial] [Hotel / Motel / Boarding / Guest House] [Hotel/Motel]'
  }, {
      'code':
      'CI',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites]'
  }, {
      'code':
      'CI01',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing]'
  }, {
      'code':
      'CI01AW',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Aircraft Works]'
  }, {
      'code':
      'CI01BB',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Boat Building]'
  }, {
      'code':
      'CI01BR',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Brick Works]'
  }, {
      'code':
      'CI01BW',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Brewery]'
  }, {
      'code':
      'CI01CD',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Cider Manufacture]'
  }, {
      'code':
      'CI01CM',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Chemical Works]'
  }, {
      'code':
      'CI01CW',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Cement Works]'
  }, {
      'code':
      'CI01DA',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Dairy Processing]'
  }, {
      'code':
      'CI01DY',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Distillery]'
  }, {
      'code':
      'CI01FL',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Flour Mill]'
  }, {
      'code':
      'CI01FO',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Food Processing]'
  }, {
      'code':
      'CI01GW',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Glassworks]'
  }, {
      'code':
      'CI01MG',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Manufacturing]'
  }, {
      'code':
      'CI01OH',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Oast House]'
  }, {
      'code':
      'CI01OR',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Oil Refining]'
  }, {
      'code':
      'CI01PG',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Pottery Manufacturing]'
  }, {
      'code':
      'CI01PM',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Paper Mill]'
  }, {
      'code':
      'CI01PW',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Printing Works]'
  }, {
      'code':
      'CI01SR',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Sugar Refinery]'
  }, {
      'code':
      'CI01SW',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Steel Works]'
  }, {
      'code':
      'CI01TL',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Timber Mill]'
  }, {
      'code':
      'CI01WN',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Winery]'
  }, {
      'code':
      'CI01YD',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Factory/Manufacturing] [Shipyard]'
  }, {
      'code':
      'CI02',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Mineral / Ore Working / Quarry / Mine]'
  }, {
      'code':
      'CI02MA',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Mineral / Ore Working / Quarry / Mine] [Mineral Mining / Active]'
  }, {
      'code':
      'CI02MD',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Mineral / Ore Working / Quarry / Mine] [Mineral Distribution / Storage]'
  }, {
      'code':
      'CI02MP',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Mineral / Ore Working / Quarry / Mine] [Mineral Processing]'
  }, {
      'code':
      'CI02OA',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Mineral / Ore Working / Quarry / Mine] [Oil / Gas Extraction / Active]'
  }, {
      'code':
      'CI02QA',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Mineral / Ore Working / Quarry / Mine] [Mineral Quarrying / Open Extraction / Active]'
  }, {
      'code':
      'CI03',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Workshop / Light Industrial]'
  }, {
      'code':
      'CI03GA',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Workshop / Light Industrial] [Servicing Garage]'
  }, {
      'code':
      'CI04',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Warehouse / Store / Storage Depot]'
  }, {
      'code':
      'CI04CS',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Warehouse / Store / Storage Depot] [Crop Handling / Storage]'
  }, {
      'code':
      'CI04PL',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Warehouse / Store / Storage Depot] [Postal Sorting / Distribution]'
  }, {
      'code':
      'CI04SO',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Warehouse / Store / Storage Depot] [Solid Fuel Storage]'
  }, {
      'code':
      'CI04TS',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Warehouse / Store / Storage Depot] [Timber Storage]'
  }, {
      'code':
      'CI05',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Wholesale Distribution]'
  }, {
      'code':
      'CI05SF',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Wholesale Distribution] [Solid Fuel Distribution]'
  }, {
      'code':
      'CI05TD',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Wholesale Distribution] [Timber Distribution]'
  }, {
      'code':
      'CI06',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Recycling Plant]'
  }, {
      'code':
      'CI07',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Incinerator / Waste Transfer Station]'
  }, {
      'code':
      'CI08',
      'class_list_string':
      '[Commercial] [Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites] [Maintenance Depot]'
  }, {
      'code':
      'CL',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises]'
  }, {
      'code':
      'CL01',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Amusements]'
  }, {
      'code':
      'CL01LP',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Amusements] [Leisure Pier]'
  }, {
      'code':
      'CL02',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Holiday / Campsite]'
  }, {
      'code':
      'CL02CG',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Holiday / Campsite] [Camping]'
  }, {
      'code':
      'CL02CV',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Holiday / Campsite] [Caravanning]'
  }, {
      'code':
      'CL02HA',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Holiday / Campsite] [Holiday Accommodation]'
  }, {
      'code':
      'CL02HO',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Holiday / Campsite] [Holiday Centre]'
  }, {
      'code':
      'CL02YC',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Holiday / Campsite] [Youth Organisation Camp]'
  }, {
      'code':
      'CL03',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Library]'
  }, {
      'code':
      'CL03RR',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Library] [Reading Room]'
  }, {
      'code':
      'CL04',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Museum / Gallery]'
  }, {
      'code':
      'CL04AC',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Museum / Gallery] [Art Centre / Gallery]'
  }, {
      'code':
      'CL04AM',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Museum / Gallery] [Aviation Museum]'
  }, {
      'code':
      'CL04HG',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Museum / Gallery] [Heritage Centre]'
  }, {
      'code':
      'CL04IM',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Museum / Gallery] [Industrial Museum]'
  }, {
      'code':
      'CL04MM',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Museum / Gallery] [Military Museum]'
  }, {
      'code':
      'CL04NM',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Museum / Gallery] [Maritime Museum]'
  }, {
      'code':
      'CL04SM',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Museum / Gallery] [Science Museum]'
  }, {
      'code':
      'CL04TM',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Museum / Gallery] [Transport Museum]'
  }, {
      'code':
      'CL06',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre]'
  }, {
      'code':
      'CL06AH',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Athletics Facility]'
  }, {
      'code':
      'CL06BF',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Bowls Facility]'
  }, {
      'code':
      'CL06CK',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Cricket Facility]'
  }, {
      'code':
      'CL06CU',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Curling Facility]'
  }, {
      'code':
      'CL06DS',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Diving / Swimming Facility]'
  }, {
      'code':
      'CL06EQ',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Equestrian Sports Facility]'
  }, {
      'code':
      'CL06FB',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Football Facility]'
  }, {
      'code':
      'CL06FI',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Fishing / Angling Facility]'
  }, {
      'code':
      'CL06GF',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Golf Facility]'
  }, {
      'code':
      'CL06GL',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Gliding Facility]'
  }, {
      'code':
      'CL06GR',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Greyhound Racing Facility]'
  }, {
      'code':
      'CL06HF',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Hockey Facility]'
  }, {
      'code':
      'CL06HR',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Horse Racing Facility]'
  }, {
      'code':
      'CL06HV',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Historic Vessel / Aircraft / Vehicle]'
  }, {
      'code':
      'CL06LS',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Activity / Leisure / Sports Centre]'
  }, {
      'code':
      'CL06ME',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Model Sports Facility]'
  }, {
      'code':
      'CL06MF',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Motor Sports Facility]'
  }, {
      'code':
      'CL06PF',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Playing Field]'
  }, {
      'code':
      'CL06QS',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Racquet Sports Facility]'
  }, {
      'code':
      'CL06RF',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Rugby Facility]'
  }, {
      'code':
      'CL06RG',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Recreation Ground]'
  }, {
      'code':
      'CL06SI',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Shinty Facility]'
  }, {
      'code':
      'CL06SK',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Skateboarding Facility]'
  }, {
      'code':
      'CL06SX',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Civilian Firing Facility]'
  }, {
      'code':
      'CL06TB',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Tenpin Bowling Facility]'
  }, {
      'code':
      'CL06TN',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Public Tennis Court]'
  }, {
      'code':
      'CL06WA',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Water Sports Facility]'
  }, {
      'code':
      'CL06WP',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Winter Sports Facility]'
  }, {
      'code':
      'CL06WY',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Wildlife Sports Facility]'
  }, {
      'code':
      'CL06YF',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Indoor / Outdoor Leisure / Sporting Activity / Centre] [Cycling Sports Facility]'
  }, {
      'code':
      'CL07',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall]'
  }, {
      'code':
      'CL07CI',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall] [Cinema]'
  }, {
      'code':
      'CL07EN',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall] [Entertainment Complex]'
  }, {
      'code':
      'CL07EX',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall] [Conference / Exhibition Centre]'
  }, {
      'code':
      'CL07TH',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall] [Theatre]'
  }, {
      'code':
      'CL08',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Zoo / Theme Park]'
  }, {
      'code':
      'CL08AK',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Zoo / Theme Park] [Amusement Park]'
  }, {
      'code':
      'CL08AQ',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Zoo / Theme Park] [Aquatic Attraction]'
  }, {
      'code':
      'CL08MX',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Zoo / Theme Park] [Model Village Site]'
  }, {
      'code':
      'CL08WZ',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Zoo / Theme Park] [Wildlife / Zoological Park]'
  }, {
      'code':
      'CL09',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Beach Hut (Recreational, Non-Residential Use Only)]'
  }, {
      'code':
      'CL10',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Licensed Private Members’ Club]'
  }, {
      'code':
      'CL10RE',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Licensed Private Members’ Club] [Recreational / Social Club]'
  }, {
      'code':
      'CL11',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Arena / Stadium]'
  }, {
      'code':
      'CL11SD',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Arena / Stadium] [Stadium]'
  }, {
      'code':
      'CL11SJ',
      'class_list_string':
      '[Commercial] [Leisure - Applicable to recreational sites and enterprises] [Arena / Stadium] [Showground]'
  }, {
      'code':
      'CM',
      'class_list_string':
      '[Commercial] [Medical]'
  }, {
      'code':
      'CM01',
      'class_list_string':
      '[Commercial] [Medical] [Dentist]'
  }, {
      'code':
      'CM02',
      'class_list_string':
      '[Commercial] [Medical] [General Practice Surgery / Clinic]'
  }, {
      'code':
      'CM02HC',
      'class_list_string':
      '[Commercial] [Medical] [General Practice Surgery / Clinic] [Health Centre]'
  }, {
      'code':
      'CM02HL',
      'class_list_string':
      '[Commercial] [Medical] [General Practice Surgery / Clinic] [Health Care Services]'
  }, {
      'code':
      'CM03',
      'class_list_string':
      '[Commercial] [Medical] [Hospital / Hospice]'
  }, {
      'code':
      'CM03HI',
      'class_list_string':
      '[Commercial] [Medical] [Hospital / Hospice] [Hospice]'
  }, {
      'code':
      'CM03HP',
      'class_list_string':
      '[Commercial] [Medical] [Hospital / Hospice] [Hospital]'
  }, {
      'code':
      'CM04',
      'class_list_string':
      '[Commercial] [Medical] [Medical / Testing / Research Laboratory]'
  }, {
      'code':
      'CM05',
      'class_list_string':
      '[Commercial] [Medical] [Professional Medical Service]'
  }, {
      'code':
      'CM05ZS',
      'class_list_string':
      '[Commercial] [Medical] [Professional Medical Service] [Assessment / Development Services]'
  }, {
      'code':
      'CM06',
      'class_list_string':
      '[Commercial] [Medical] [Pharmacy]'
  }, {
      'code':
      'CN',
      'class_list_string':
      '[Commercial] [Animal Centre]'
  }, {
      'code':
      'CN01',
      'class_list_string':
      '[Commercial] [Animal Centre] [Cattery / Kennel]'
  }, {
      'code':
      'CN02',
      'class_list_string':
      '[Commercial] [Animal Centre] [Animal Services]'
  }, {
      'code':
      'CN02AX',
      'class_list_string':
      '[Commercial] [Animal Centre] [Animal Services] [Animal Quarantining]'
  }, {
      'code':
      'CN03',
      'class_list_string':
      '[Commercial] [Animal Centre] [Equestrian]'
  }, {
      'code':
      'CN03HB',
      'class_list_string':
      '[Commercial] [Animal Centre] [Equestrian] [Horse Racing / Breeding Stable]'
  }, {
      'code':
      'CN03SB',
      'class_list_string':
      '[Commercial] [Animal Centre] [Equestrian] [Commercial Stabling / Riding]'
  }, {
      'code':
      'CN04',
      'class_list_string':
      '[Commercial] [Animal Centre] [Vet / Animal Medical Treatment]'
  }, {
      'code':
      'CN05',
      'class_list_string':
      '[Commercial] [Animal Centre] [Animal / Bird / Marine Sanctuary]'
  }, {
      'code':
      'CN05AN',
      'class_list_string':
      '[Commercial] [Animal Centre] [Animal / Bird / Marine Sanctuary] [Animal Sanctuary]'
  }, {
      'code':
      'CN05MR',
      'class_list_string':
      '[Commercial] [Animal Centre] [Animal / Bird / Marine Sanctuary] [Marine Sanctuary]'
  }, {
      'code':
      'CO',
      'class_list_string':
      '[Commercial] [Office]'
  }, {
      'code':
      'CO01',
      'class_list_string':
      '[Commercial] [Office] [Office / Work Studio]'
  }, {
      'code':
      'CO01EM',
      'class_list_string':
      '[Commercial] [Office] [Office / Work Studio] [Embassy /, High Commission / Consulate]'
  }, {
      'code':
      'CO01FM',
      'class_list_string':
      '[Commercial] [Office] [Office / Work Studio] [Film Studio]'
  }, {
      'code':
      'CO01GV',
      'class_list_string':
      '[Commercial] [Office] [Office / Work Studio] [Central Government Service]'
  }, {
      'code':
      'CO01LG',
      'class_list_string':
      '[Commercial] [Office] [Office / Work Studio] [Local Government Service]'
  }, {
      'code':
      'CO02',
      'class_list_string':
      '[Commercial] [Office] [Broadcasting (TV / Radio)]'
  }, {
      'code':
      'CR',
      'class_list_string':
      '[Commercial] [Retail]'
  }, {
      'code':
      'CR01',
      'class_list_string':
      '[Commercial] [Retail] [Bank / Financial Service]'
  }, {
      'code':
      'CR02',
      'class_list_string':
      '[Commercial] [Retail] [Retail Service Agent]'
  }, {
      'code':
      'CR02EV',
      'class_list_string':
      '[Commercial] [Retail] [Retail Service Agent] [Electric Car Charging Station]'
  }, {
      'code':
      'CR02PO',
      'class_list_string':
      '[Commercial] [Retail] [Retail Service Agent] [Post Office]'
  }, {
      'code':
      'CR04',
      'class_list_string':
      '[Commercial] [Retail] [Market (Indoor / Outdoor)]'
  }, {
      'code':
      'CR04FK',
      'class_list_string':
      '[Commercial] [Retail] [Market (Indoor / Outdoor)] [Fish Market]'
  }, {
      'code':
      'CR04FV',
      'class_list_string':
      '[Commercial] [Retail] [Market (Indoor / Outdoor)] [Fruit / Vegetable Market]'
  }, {
      'code':
      'CR04LV',
      'class_list_string':
      '[Commercial] [Retail] [Market (Indoor / Outdoor)] [Livestock Market]'
  }, {
      'code':
      'CR05',
      'class_list_string':
      '[Commercial] [Retail] [Petrol Filling Station]'
  }, {
      'code':
      'CR06',
      'class_list_string':
      '[Commercial] [Retail] [Public House / Bar / Nightclub]'
  }, {
      'code':
      'CR06BA',
      'class_list_string':
      '[Commercial] [Retail] [Public House / Bar / Nightclub] [Bar]'
  }, {
      'code':
      'CR06NC',
      'class_list_string':
      '[Commercial] [Retail] [Public House / Bar / Nightclub] [Nightclub]'
  }, {
      'code':
      'CR06PH',
      'class_list_string':
      '[Commercial] [Retail] [Public House / Bar / Nightclub] [Public House]'
  }, {
      'code':
      'CR07',
      'class_list_string':
      '[Commercial] [Retail] [Restaurant / Cafeteria]'
  }, {
      'code':
      'CR08',
      'class_list_string':
      '[Commercial] [Retail] [Shop / Showroom]'
  }, {
      'code':
      'CR08CS',
      'class_list_string':
      '[Commercial] [Retail] [Shop / Showroom] [Convenience Store]'
  }, {
      'code':
      'CR08GC',
      'class_list_string':
      '[Commercial] [Retail] [Shop / Showroom] [Garden Centre]'
  }, {
      'code':
      'CR08SM',
      'class_list_string':
      '[Commercial] [Retail] [Shop / Showroom] [Supermarket]'
  }, {
      'code':
      'CR09',
      'class_list_string':
      '[Commercial] [Retail] [Other Licensed Premise / Vendor]'
  }, {
      'code':
      'CR09BS',
      'class_list_string':
      '[Commercial] [Retail] [Other Licensed Premise / Vendor] [Betting Shop]'
  }, {
      'code':
      'CR09OL',
      'class_list_string':
      '[Commercial] [Retail] [Other Licensed Premise / Vendor] [Off-licence]'
  }, {
      'code':
      'CR10',
      'class_list_string':
      '[Commercial] [Retail] [Fast Food Outlet / Takeaway (Hot / Cold)]'
  }, {
      'code':
      'CR11',
      'class_list_string':
      '[Commercial] [Retail] [Automated Teller Machine (ATM)]'
  }, {
      'code':
      'CS',
      'class_list_string':
      '[Commercial] [Storage Land]'
  }, {
      'code':
      'CS01',
      'class_list_string':
      '[Commercial] [Storage Land] [General Storage Land]'
  }, {
      'code':
      'CS02',
      'class_list_string':
      '[Commercial] [Storage Land] [Builders’ Yard]'
  }, {
      'code':
      'CT',
      'class_list_string':
      '[Commercial] [Transport]'
  }, {
      'code':
      'CT01',
      'class_list_string':
      '[Commercial] [Transport] [Airfield / Airstrip / Airport / Air Transport Infrastructure Facility]'
  }, {
      'code':
      'CT01AF',
      'class_list_string':
      '[Commercial] [Transport] [Airfield / Airstrip / Airport / Air Transport Infrastructure Facility] [Airfield]'
  }, {
      'code':
      'CT01AI',
      'class_list_string':
      '[Commercial] [Transport] [Airfield / Airstrip / Airport / Air Transport Infrastructure Facility] [Air Transport Infrastructure Services]'
  }, {
      'code':
      'CT01AP',
      'class_list_string':
      '[Commercial] [Transport] [Airfield / Airstrip / Airport / Air Transport Infrastructure Facility] [Airport]'
  }, {
      'code':
      'CT01AY',
      'class_list_string':
      '[Commercial] [Transport] [Airfield / Airstrip / Airport / Air Transport Infrastructure Facility] [Air Passenger Terminal]'
  }, {
      'code':
      'CT01HS',
      'class_list_string':
      '[Commercial] [Transport] [Airfield / Airstrip / Airport / Air Transport Infrastructure Facility] [Helicopter Station]'
  }, {
      'code':
      'CT01HT',
      'class_list_string':
      '[Commercial] [Transport] [Airfield / Airstrip / Airport / Air Transport Infrastructure Facility] [Heliport / Helipad]'
  }, {
      'code':
      'CT02',
      'class_list_string':
      '[Commercial] [Transport] [Bus Shelter]'
  }, {
      'code':
      'CT03',
      'class_list_string':
      '[Commercial] [Transport] [Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site]'
  }, {
      'code':
      'CT03PK',
      'class_list_string':
      '[Commercial] [Transport] [Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site] [Public Park And Ride]'
  }, {
      'code':
      'CT03PP',
      'class_list_string':
      '[Commercial] [Transport] [Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site] [Public Car Parking]'
  }, {
      'code':
      'CT03PU',
      'class_list_string':
      '[Commercial] [Transport] [Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site] [Public Coach Parking]'
  }, {
      'code':
      'CT03VP',
      'class_list_string':
      '[Commercial] [Transport] [Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site] [Public Commercial Vehicle Parking]'
  }, {
      'code':
      'CT04',
      'class_list_string':
      '[Commercial] [Transport] [Goods Freight Handling / Terminal]'
  }, {
      'code':
      'CT04AE',
      'class_list_string':
      '[Commercial] [Transport] [Goods Freight Handling / Terminal] [Air Freight Terminal]'
  }, {
      'code':
      'CT04CF',
      'class_list_string':
      '[Commercial] [Transport] [Goods Freight Handling / Terminal] [Container Freight]'
  }, {
      'code':
      'CT04RH',
      'class_list_string':
      '[Commercial] [Transport] [Goods Freight Handling / Terminal] [Road Freight Transport]'
  }, {
      'code':
      'CT04RT',
      'class_list_string':
      '[Commercial] [Transport] [Goods Freight Handling / Terminal] [Rail Freight Transport]'
  }, {
      'code':
      'CT05',
      'class_list_string':
      '[Commercial] [Transport] [Marina]'
  }, {
      'code':
      'CT06',
      'class_list_string':
      '[Commercial] [Transport] [Mooring]'
  }, {
      'code':
      'CT07',
      'class_list_string':
      '[Commercial] [Transport] [Railway Asset]'
  }, {
      'code':
      'CT08',
      'class_list_string':
      '[Commercial] [Transport] [Station / Interchange / Terminal / Halt]'
  }, {
      'code':
      'CT08BC',
      'class_list_string':
      '[Commercial] [Transport] [Station / Interchange / Terminal / Halt] [Bus / Coach Station]'
  }, {
      'code':
      'CT08RS',
      'class_list_string':
      '[Commercial] [Transport] [Station / Interchange / Terminal / Halt] [Railway Station]'
  }, {
      'code':
      'CT08VH',
      'class_list_string':
      '[Commercial] [Transport] [Station / Interchange / Terminal / Halt] [Vehicular Rail Terminal]'
  }, {
      'code':
      'CT09',
      'class_list_string':
      '[Commercial] [Transport] [Transport Track / Way]'
  }, {
      'code':
      'CT09CL',
      'class_list_string':
      '[Commercial] [Transport] [Transport Track / Way] [Cliff Railway]'
  }, {
      'code':
      'CT09CX',
      'class_list_string':
      '[Commercial] [Transport] [Transport Track / Way] [Chair Lift / Cable Car / Ski Tow]'
  }, {
      'code':
      'CT09MO',
      'class_list_string':
      '[Commercial] [Transport] [Transport Track / Way] [Monorail]'
  }, {
      'code':
      'CT10',
      'class_list_string':
      '[Commercial] [Transport] [Vehicle Storage]'
  }, {
      'code':
      'CT10BG',
      'class_list_string':
      '[Commercial] [Transport] [Vehicle Storage] [Boat Storage]'
  }, {
      'code':
      'CT10BU',
      'class_list_string':
      '[Commercial] [Transport] [Vehicle Storage] [Bus / Coach Depot]'
  }, {
      'code':
      'CT11',
      'class_list_string':
      '[Commercial] [Transport] [Transport Related Infrastructure]'
  }, {
      'code':
      'CT11AD',
      'class_list_string':
      '[Commercial] [Transport] [Transport Related Infrastructure] [Aqueduct]'
  }, {
      'code':
      'CT11CA',
      'class_list_string':
      '[Commercial] [Transport] [Transport Related Infrastructure] [Road Bridge Over Canal]'
  }, {
      'code':
      'CT11LK',
      'class_list_string':
      '[Commercial] [Transport] [Transport Related Infrastructure] [Lock]'
  }, {
      'code':
      'CT11MU',
      'class_list_string':
      '[Commercial] [Transport] [Transport Related Infrastructure] [Road Bridge Over Multiple]'
  }, {
      'code':
      'CT11NN',
      'class_list_string':
      '[Commercial] [Transport] [Transport Related Infrastructure] [Road Bridge Over No Network]'
  }, {
      'code':
      'CT11PA',
      'class_list_string':
      '[Commercial] [Transport] [Transport Related Infrastructure] [Road Bridge Over Path]'
  }, {
      'code':
      'CT11RA',
      'class_list_string':
      '[Commercial] [Transport] [Transport Related Infrastructure] [Road Bridge Over Railway]'
  }, {
      'code':
      'CT11RO',
      'class_list_string':
      '[Commercial] [Transport] [Transport Related Infrastructure] [Road Bridge Over Road]'
  }, {
      'code':
      'CT11WA',
      'class_list_string':
      '[Commercial] [Transport] [Transport Related Infrastructure] [Road Bridge Over Water]'
  }, {
      'code':
      'CT11WE',
      'class_list_string':
      '[Commercial] [Transport] [Transport Related Infrastructure] [Weir]'
  }, {
      'code':
      'CT11WG',
      'class_list_string':
      '[Commercial] [Transport] [Transport Related Infrastructure] [Weighbridge / Load Gauge]'
  }, {
      'code':
      'CT12',
      'class_list_string':
      '[Commercial] [Transport] [Overnight Lorry Park]'
  }, {
      'code':
      'CT13',
      'class_list_string':
      '[Commercial] [Transport] [Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay]'
  }, {
      'code':
      'CT13FR',
      'class_list_string':
      '[Commercial] [Transport] [Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay] [Passenger Ferry Terminal]'
  }, {
      'code':
      'CT13NB',
      'class_list_string':
      '[Commercial] [Transport] [Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay] [Non-Tanker Nautical Berthing]'
  }, {
      'code':
      'CT13NF',
      'class_list_string':
      '[Commercial] [Transport] [Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay] [Nautical Refuelling Facility]'
  }, {
      'code':
      'CT13SA',
      'class_list_string':
      '[Commercial] [Transport] [Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay] [Slipway]'
  }, {
      'code':
      'CT13SP',
      'class_list_string':
      '[Commercial] [Transport] [Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay] [Ship Passenger Terminal]'
  }, {
      'code':
      'CT13TK',
      'class_list_string':
      '[Commercial] [Transport] [Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay] [Tanker Berthing]'
  }, {
      'code':
      'CT13VF',
      'class_list_string':
      '[Commercial] [Transport] [Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay] [Vehicular Ferry Terminal]'
  }, {
      'code':
      'CU',
      'class_list_string':
      '[Commercial] [Utility]'
  }, {
      'code':
      'CU01',
      'class_list_string':
      '[Commercial] [Utility] [Electricity Sub-Station]'
  }, {
      'code':
      'CU02',
      'class_list_string':
      '[Commercial] [Utility] [Landfill]'
  }, {
      'code':
      'CU03',
      'class_list_string':
      '[Commercial] [Utility] [Power Station / Energy Production]'
  }, {
      'code':
      'CU03ED',
      'class_list_string':
      '[Commercial] [Utility] [Power Station / Energy Production] [Electricity Distribution Facility]'
  }, {
      'code':
      'CU03EP',
      'class_list_string':
      '[Commercial] [Utility] [Power Station / Energy Production] [Electricity Production Facility]'
  }, {
      'code':
      'CU03WF',
      'class_list_string':
      '[Commercial] [Utility] [Power Station / Energy Production] [Wind Farm]'
  }, {
      'code':
      'CU03WU',
      'class_list_string':
      '[Commercial] [Utility] [Power Station / Energy Production] [Wind Turbine]'
  }, {
      'code':
      'CU04',
      'class_list_string':
      '[Commercial] [Utility] [Pump House / Pumping Station / Water Tower]'
  }, {
      'code':
      'CU04WC',
      'class_list_string':
      '[Commercial] [Utility] [Pump House / Pumping Station / Water Tower] [Water Controlling / Pumping]'
  }, {
      'code':
      'CU04WD',
      'class_list_string':
      '[Commercial] [Utility] [Pump House / Pumping Station / Water Tower] [Water Distribution / Pumping]'
  }, {
      'code':
      'CU04WM',
      'class_list_string':
      '[Commercial] [Utility] [Pump House / Pumping Station / Water Tower] [Water Quality Monitoring]'
  }, {
      'code':
      'CU04WS',
      'class_list_string':
      '[Commercial] [Utility] [Pump House / Pumping Station / Water Tower] [Water Storage]'
  }, {
      'code':
      'CU04WW',
      'class_list_string':
      '[Commercial] [Utility] [Pump House / Pumping Station / Water Tower] [Waste Water Distribution / Pumping]'
  }, {
      'code':
      'CU06',
      'class_list_string':
      '[Commercial] [Utility] [Telecommunication]'
  }, {
      'code':
      'CU06TE',
      'class_list_string':
      '[Commercial] [Utility] [Telecommunication] [Telecommunications Mast]'
  }, {
      'code':
      'CU06TX',
      'class_list_string':
      '[Commercial] [Utility] [Telecommunication] [Telephone Exchange]'
  }, {
      'code':
      'CU07',
      'class_list_string':
      '[Commercial] [Utility] [Water / Waste Water / Sewage Treatment Works]'
  }, {
      'code':
      'CU07WR',
      'class_list_string':
      '[Commercial] [Utility] [Water / Waste Water / Sewage Treatment Works] [Waste Water Treatment]'
  }, {
      'code':
      'CU07WT',
      'class_list_string':
      '[Commercial] [Utility] [Water / Waste Water / Sewage Treatment Works] [Water Treatment]'
  }, {
      'code':
      'CU08',
      'class_list_string':
      '[Commercial] [Utility] [Gas / Oil Storage / Distribution]'
  }, {
      'code':
      'CU08GG',
      'class_list_string':
      '[Commercial] [Utility] [Gas / Oil Storage / Distribution] [Gas Governor]'
  }, {
      'code':
      'CU08GH',
      'class_list_string':
      '[Commercial] [Utility] [Gas / Oil Storage / Distribution] [Gas Holder]'
  }, {
      'code':
      'CU08OT',
      'class_list_string':
      '[Commercial] [Utility] [Gas / Oil Storage / Distribution] [Oil Terminal]'
  }, {
      'code':
      'CU09',
      'class_list_string':
      '[Commercial] [Utility] [Other Utility Use]'
  }, {
      'code':
      'CU09CQ',
      'class_list_string':
      '[Commercial] [Utility] [Other Utility Use] [Cable Terminal Station]'
  }, {
      'code':
      'CU09OV',
      'class_list_string':
      '[Commercial] [Utility] [Other Utility Use] [Observatory]'
  }, {
      'code':
      'CU09RA',
      'class_list_string':
      '[Commercial] [Utility] [Other Utility Use] [Radar Station]'
  }, {
      'code':
      'CU09SE',
      'class_list_string':
      '[Commercial] [Utility] [Other Utility Use] [Satellite Earth Station]'
  }, {
      'code':
      'CU10',
      'class_list_string':
      '[Commercial] [Utility] [Waste Management]'
  }, {
      'code':
      'CU11',
      'class_list_string':
      '[Commercial] [Utility] [Telephone Box]'
  }, {
      'code':
      'CU11OP',
      'class_list_string':
      '[Commercial] [Utility] [Telephone Box] [Other Public Telephones]'
  }, {
      'code':
      'CU12',
      'class_list_string':
      '[Commercial] [Utility] [Dam]'
  }, {
      'code':
      'CX',
      'class_list_string':
      '[Commercial] [Emergency / Rescue Service]'
  }, {
      'code':
      'CX01',
      'class_list_string':
      '[Commercial] [Emergency / Rescue Service] [Police / Transport Police / Station]'
  }, {
      'code':
      'CX01PT',
      'class_list_string':
      '[Commercial] [Emergency / Rescue Service] [Police / Transport Police / Station] [Police Training]'
  }, {
      'code':
      'CX02',
      'class_list_string':
      '[Commercial] [Emergency / Rescue Service] [Fire Station]'
  }, {
      'code':
      'CX02FT',
      'class_list_string':
      '[Commercial] [Emergency / Rescue Service] [Fire Station] [Fire Service Training]'
  }, {
      'code':
      'CX03',
      'class_list_string':
      '[Commercial] [Emergency / Rescue Service] [Ambulance Station]'
  }, {
      'code':
      'CX03AA',
      'class_list_string':
      '[Commercial] [Emergency / Rescue Service] [Ambulance Station] [Air Sea Rescue / Air Ambulance]'
  }, {
      'code':
      'CX04',
      'class_list_string':
      '[Commercial] [Emergency / Rescue Service] [Lifeboat Services / Station]'
  }, {
      'code':
      'CX05',
      'class_list_string':
      '[Commercial] [Emergency / Rescue Service] [Coastguard Rescue / Lookout / Station]'
  }, {
      'code':
      'CX06',
      'class_list_string':
      '[Commercial] [Emergency / Rescue Service] [Mountain Rescue Station]'
  }, {
      'code':
      'CX07',
      'class_list_string':
      '[Commercial] [Emergency / Rescue Service] [Lighthouse]'
  }, {
      'code':
      'CX08',
      'class_list_string':
      '[Commercial] [Emergency / Rescue Service] [Police Box / Kiosk]'
  }, {
      'code':
      'CZ',
      'class_list_string':
      '[Commercial] [Information]'
  }, {
      'code':
      'CZ01',
      'class_list_string':
      '[Commercial] [Information] [Advertising Hoarding]'
  }, {
      'code':
      'CZ02',
      'class_list_string':
      '[Commercial] [Information] [Tourist Information Signage]'
  }, {
      'code':
      'CZ02VI',
      'class_list_string':
      '[Commercial] [Information] [Tourist Information Signage] [Visitor Information]'
  }, {
      'code':
      'CZ03',
      'class_list_string':
      '[Commercial] [Information] [Traffic Information Signage]'
  }, {
      'code': 'L',
      'class_list_string': '[Land]'
  }, {
      'code':
      'LA',
      'class_list_string':
      '[Land] [Agricultural - Applicable to land in farm ownership and not run as a separate business enterprise]'
  }, {
      'code':
      'LA01',
      'class_list_string':
      '[Land] [Agricultural - Applicable to land in farm ownership and not run as a separate business enterprise] [Grazing Land]'
  }, {
      'code':
      'LA02',
      'class_list_string':
      '[Land] [Agricultural - Applicable to land in farm ownership and not run as a separate business enterprise] [Permanent Crop / Crop Rotation]'
  }, {
      'code':
      'LA02OC',
      'class_list_string':
      '[Land] [Agricultural - Applicable to land in farm ownership and not run as a separate business enterprise] [Permanent Crop / Crop Rotation] [Orchard]'
  }, {
      'code':
      'LB',
      'class_list_string':
      '[Land] [Ancillary Building]'
  }, {
      'code':
      'LB99AV',
      'class_list_string':
      '[Land] [Ancillary Building] [Aviary / Dovecot / Cage]'
  }, {
      'code':
      'LB99BD',
      'class_list_string':
      '[Land] [Ancillary Building] [Bandstand]'
  }, {
      'code':
      'LB99PI',
      'class_list_string':
      '[Land] [Ancillary Building] [Pavilion / Changing Room]'
  }, {
      'code':
      'LB99SV',
      'class_list_string':
      '[Land] [Ancillary Building] [Sports Viewing Structure]'
  }, {
      'code':
      'LC',
      'class_list_string':
      '[Land] [Burial Ground]'
  }, {
      'code':
      'LC01',
      'class_list_string':
      '[Land] [Burial Ground] [Historic / Disused Cemetery / Graveyard]'
  }, {
      'code':
      'LD',
      'class_list_string':
      '[Land] [Development]'
  }, {
      'code':
      'LD01',
      'class_list_string':
      '[Land] [Development] [Development Site]'
  }, {
      'code':
      'LD01CC',
      'class_list_string':
      '[Land] [Development] [Development Site] [Commercial Construction Site]'
  }, {
      'code':
      'LD01CO',
      'class_list_string':
      '[Land] [Development] [Development Site] [Community Construction Site]'
  }, {
      'code':
      'LD01RN',
      'class_list_string':
      '[Land] [Development] [Development Site] [Residential Construction Site]'
  }, {
      'code':
      'LD01TC',
      'class_list_string':
      '[Land] [Development] [Development Site] [Transport Construction Site]'
  }, {
      'code':
      'LF',
      'class_list_string':
      '[Land] [Forestry]'
  }, {
      'code':
      'LF02',
      'class_list_string':
      '[Land] [Forestry] [Forest / Arboretum / Pinetum (Managed / Unmanaged)]'
  }, {
      'code':
      'LF02AU',
      'class_list_string':
      '[Land] [Forestry] [Forest / Arboretum / Pinetum (Managed / Unmanaged)] [Arboretum]'
  }, {
      'code':
      'LF03',
      'class_list_string':
      '[Land] [Forestry] [Woodland]'
  }, {
      'code':
      'LL',
      'class_list_string':
      '[Land] [Allotment]'
  }, {
      'code':
      'LM',
      'class_list_string':
      '[Land] [Amenity - Open areas not attracting visitors]'
  }, {
      'code':
      'LM01',
      'class_list_string':
      '[Land] [Amenity - Open areas not attracting visitors] [Landscaped Roundabout]'
  }, {
      'code':
      'LM02',
      'class_list_string':
      '[Land] [Amenity - Open areas not attracting visitors] [Verge / Central Reservation]'
  }, {
      'code':
      'LM02NV',
      'class_list_string':
      '[Land] [Amenity - Open areas not attracting visitors] [Verge / Central Reservation] [Natural Central Reservation]'
  }, {
      'code':
      'LM02VE',
      'class_list_string':
      '[Land] [Amenity - Open areas not attracting visitors] [Verge / Central Reservation] [Natural Verge]'
  }, {
      'code':
      'LM03',
      'class_list_string':
      '[Land] [Amenity - Open areas not attracting visitors] [Maintained Amenity Land]'
  }, {
      'code':
      'LM04',
      'class_list_string':
      '[Land] [Amenity - Open areas not attracting visitors] [Maintained Surfaced Area]'
  }, {
      'code':
      'LM04MV',
      'class_list_string':
      '[Land] [Amenity - Open areas not attracting visitors] [Maintained Surfaced Area] [Made Central Reservation]'
  }, {
      'code':
      'LM04PV',
      'class_list_string':
      '[Land] [Amenity - Open areas not attracting visitors] [Maintained Surfaced Area] [Pavement]'
  }, {
      'code':
      'LO',
      'class_list_string':
      '[Land] [Open Space]'
  }, {
      'code':
      'LO01',
      'class_list_string':
      '[Land] [Open Space] [Heath / Moorland]'
  }, {
      'code': 'LP',
      'class_list_string': '[Land] [Park]'
  }, {
      'code':
      'LP01',
      'class_list_string':
      '[Land] [Park] [Public Park / Garden]'
  }, {
      'code':
      'LP02',
      'class_list_string':
      '[Land] [Park] [Public Open Space / Nature Reserve]'
  }, {
      'code':
      'LP03',
      'class_list_string':
      '[Land] [Park] [Playground]'
  }, {
      'code':
      'LP03PA',
      'class_list_string':
      '[Land] [Park] [Playground] [Play Area]'
  }, {
      'code':
      'LP03PD',
      'class_list_string':
      '[Land] [Park] [Playground] [Paddling Pool]'
  }, {
      'code':
      'LP04',
      'class_list_string':
      '[Land] [Park] [Private Park / Garden]'
  }, {
      'code':
      'LU',
      'class_list_string':
      '[Land] [Unused Land]'
  }, {
      'code':
      'LU01',
      'class_list_string':
      '[Land] [Unused Land] [Vacant / Derelict Land]'
  }, {
      'code':
      'LW',
      'class_list_string':
      '[Land] [Water]'
  }, {
      'code':
      'LW01',
      'class_list_string':
      '[Land] [Water] [Lake / Reservoir]'
  }, {
      'code':
      'LW01BP',
      'class_list_string':
      '[Land] [Water] [Lake / Reservoir] [Balancing Pond]'
  }, {
      'code':
      'LW01BV',
      'class_list_string':
      '[Land] [Water] [Lake / Reservoir] [Buried Reservoir]'
  }, {
      'code':
      'LW02',
      'class_list_string':
      '[Land] [Water] [Named Pond]'
  }, {
      'code':
      'LW02DE',
      'class_list_string':
      '[Land] [Water] [Named Pond] [Dew Pond]'
  }, {
      'code':
      'LW02DP',
      'class_list_string':
      '[Land] [Water] [Named Pond] [Decoy Pond]'
  }, {
      'code':
      'LW02IW',
      'class_list_string':
      '[Land] [Water] [Named Pond] [Static Water]'
  }, {
      'code':
      'LW03',
      'class_list_string':
      '[Land] [Water] [Waterway]'
  }, {
      'code':
      'LW03DR',
      'class_list_string':
      '[Land] [Water] [Waterway] [Drain]'
  }, {
      'code':
      'LW03LR',
      'class_list_string':
      '[Land] [Water] [Waterway] [Leats / Races]'
  }, {
      'code': 'M',
      'class_list_string': '[Military]'
  }, {
      'code':
      'MA',
      'class_list_string':
      '[Military] [Army]'
  }, {
      'code':
      'MA99AG',
      'class_list_string':
      '[Military] [Army] [Army Military Storage]'
  }, {
      'code':
      'MA99AR',
      'class_list_string':
      '[Military] [Army] [Army Military Range]'
  }, {
      'code':
      'MA99AS',
      'class_list_string':
      '[Military] [Army] [Army Site]'
  }, {
      'code':
      'MA99AT',
      'class_list_string':
      '[Military] [Army] [Army Military Training]'
  }, {
      'code':
      'MB',
      'class_list_string':
      '[Military] [Ancillary Building]'
  }, {
      'code':
      'MB99TG',
      'class_list_string':
      '[Military] [Ancillary Building] [Military Target]'
  }, {
      'code':
      'MF',
      'class_list_string':
      '[Military] [Air Force]'
  }, {
      'code':
      'MF99UG',
      'class_list_string':
      '[Military] [Air Force] [Air Force Military Storage]'
  }, {
      'code':
      'MF99UR',
      'class_list_string':
      '[Military] [Air Force] [Air Force Military Range]'
  }, {
      'code':
      'MF99US',
      'class_list_string':
      '[Military] [Air Force] [Air Force Site]'
  }, {
      'code':
      'MF99UT',
      'class_list_string':
      '[Military] [Air Force] [Air Force Military Training]'
  }, {
      'code':
      'MG',
      'class_list_string':
      '[Military] [Defence Estates]'
  }, {
      'code':
      'MN',
      'class_list_string':
      '[Military] [Navy]'
  }, {
      'code':
      'MN99VG',
      'class_list_string':
      '[Military] [Navy] [Naval Military Storage]'
  }, {
      'code':
      'MN99VR',
      'class_list_string':
      '[Military] [Navy] [Naval Military Range]'
  }, {
      'code':
      'MN99VS',
      'class_list_string':
      '[Military] [Navy] [Naval Site]'
  }, {
      'code':
      'MN99VT',
      'class_list_string':
      '[Military] [Navy] [Naval Military Training]'
  }, {
      'code':
      'O',
      'class_list_string':
      '[Other (Ordnance Survey Only)]'
  }, {
      'code':
      'OA',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Aid To Navigation]'
  }, {
      'code':
      'OA01',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Aid To Navigation] [Aid To Aeronautical Navigation]'
  }, {
      'code':
      'OA01AL',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Aid To Navigation] [Aid To Aeronautical Navigation] [Aeronautical Navigation Beacon / Light]'
  }, {
      'code':
      'OA01LL',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Aid To Navigation] [Aid To Aeronautical Navigation] [Landing Light]'
  }, {
      'code':
      'OA01SQ',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Aid To Navigation] [Aid To Aeronautical Navigation] [Signal Square]'
  }, {
      'code':
      'OA01WK',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Aid To Navigation] [Aid To Aeronautical Navigation] [Wind Sock / Wind Tee]'
  }, {
      'code':
      'OA02',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Aid To Navigation] [Aid To Nautical Navigation]'
  }, {
      'code':
      'OA02DM',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Aid To Navigation] [Aid To Nautical Navigation] [Daymark]'
  }, {
      'code':
      'OA02FG',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Aid To Navigation] [Aid To Nautical Navigation] [Fog Horn Warning]'
  }, {
      'code':
      'OA02NL',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Aid To Navigation] [Aid To Nautical Navigation] [Nautical Navigation Beacon / Light]'
  }, {
      'code':
      'OA03',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Aid To Navigation] [Aid To Road Navigation]'
  }, {
      'code':
      'OA03GP',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Aid To Navigation] [Aid To Road Navigation] [Guide Post]'
  }, {
      'code':
      'OC',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Coastal Protection / Flood Prevention]'
  }, {
      'code':
      'OC01',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Coastal Protection / Flood Prevention] [Boulder Wall / Sea Wall]'
  }, {
      'code':
      'OC02',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Coastal Protection / Flood Prevention] [Flood Gate / Flood Sluice Gate / Flood Valve]'
  }, {
      'code':
      'OC03',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Coastal Protection / Flood Prevention] [Groyne]'
  }, {
      'code':
      'OC04',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Coastal Protection / Flood Prevention] [Rip-Rap]'
  }, {
      'code':
      'OE',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Emergency Support]'
  }, {
      'code':
      'OE01',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Emergency Support] [Beach Office / First Aid Facility]'
  }, {
      'code':
      'OE02',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Emergency Support] [Emergency Telephone (Non Motorway)]'
  }, {
      'code':
      'OE03',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Emergency Support] [Fire Alarm Structure / Fire Observation Tower / Fire Beater Facility]'
  }, {
      'code':
      'OE04',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Emergency Support] [Emergency Equipment Point / Emergency Siren / Warning Flag]'
  }, {
      'code':
      'OE05',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Emergency Support] [Lifeguard Facility]'
  }, {
      'code':
      'OE06',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Emergency Support] [LIfe / Belt / Buoy / Float / Jacket / Safety Rope]'
  }, {
      'code':
      'OF',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Street Furniture]'
  }, {
      'code':
      'OG',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Agricultural Support Objects]'
  }, {
      'code':
      'OG01',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Agricultural Support Objects] [Fish Ladder / Lock / Pen / Trap]'
  }, {
      'code':
      'OG02',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Agricultural Support Objects] [Livestock Pen / Dip]'
  }, {
      'code':
      'OG03',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Agricultural Support Objects] [Currick]'
  }, {
      'code':
      'OG04',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Agricultural Support Objects] [Slurry Bed / Pit]'
  }, {
      'code':
      'OH',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Historical Site / Object]'
  }, {
      'code':
      'OH01',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Historical Site / Object] [Historic Structure / Object]'
  }, {
      'code':
      'OI',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Industrial Support]'
  }, {
      'code':
      'OI01',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Industrial Support] [Adit / Incline / Level]'
  }, {
      'code':
      'OI02',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Industrial Support] [Caisson / Dry Dock / Grid]'
  }, {
      'code':
      'OI03',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Industrial Support] [Channel / Conveyor / Conduit / Pipe]'
  }, {
      'code':
      'OI04',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Industrial Support] [Chimney / Flue]'
  }, {
      'code':
      'OI05',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Industrial Support] [Crane / Hoist / Winch / Material Elevator]'
  }, {
      'code':
      'OI06',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Industrial Support] [Flare Stack]'
  }, {
      'code':
      'OI07',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Industrial Support] [Hopper / Silo / Cistern / Tank]'
  }, {
      'code':
      'OI08',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Industrial Support] [Grab / Skip / Other Industrial Waste Machinery / Discharging]'
  }, {
      'code':
      'OI09',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Industrial Support] [Kiln / Oven / Smelter]'
  }, {
      'code':
      'OI10',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Industrial Support] [Manhole / Shaft]'
  }, {
      'code':
      'OI11',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Industrial Support] [Industrial Overflow / Sluice / Valve / Valve Housing]'
  }, {
      'code':
      'OI12',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Industrial Support] [Cooling Tower]'
  }, {
      'code':
      'OI13',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Industrial Support] [Solar Panel / Waterwheel]'
  }, {
      'code':
      'OI14',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Industrial Support] [Telephone Pole / Post]'
  }, {
      'code':
      'OI15',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Industrial Support] [Electricity Distribution Pole / Pylon]'
  }, {
      'code':
      'ON',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Significant Natural Object]'
  }, {
      'code':
      'ON01',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Significant Natural Object] [Boundary / Significant / Historic Tree / Pollard]'
  }, {
      'code':
      'ON02',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Significant Natural Object] [Boundary / Significant Rock / Boulder]'
  }, {
      'code':
      'ON03',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Significant Natural Object] [Natural Hole (Blow / Shake / Swallow)]'
  }, {
      'code':
      'OO',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Ornamental / Cultural Object]'
  }, {
      'code':
      'OO02',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Ornamental / Cultural Object] [Mausoleum / Tomb / Grave]'
  }, {
      'code':
      'OO03',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Ornamental / Cultural Object] [Simple Ornamental Object]'
  }, {
      'code':
      'OO04',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Ornamental / Cultural Object] [Maze]'
  }, {
      'code':
      'OP',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Sport / Leisure Support]'
  }, {
      'code':
      'OP01',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Sport / Leisure Support] [Butt / Hide]'
  }, {
      'code':
      'OP02',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Sport / Leisure Support] [Gallop / Ride]'
  }, {
      'code':
      'OP03',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Sport / Leisure Support] [Miniature Railway]'
  }, {
      'code':
      'OR',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Royal Mail Infrastructure]'
  }, {
      'code':
      'OR01',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Royal Mail Infrastructure] [Postal Box]'
  }, {
      'code':
      'OR02',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Royal Mail Infrastructure] [Postal Delivery Box / Pouch]'
  }, {
      'code':
      'OR03',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Royal Mail Infrastructure] [PO Box]'
  }, {
      'code':
      'OR04',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Royal Mail Infrastructure] [Additional Mail / Packet Addressee]'
  }, {
      'code':
      'OS',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Scientific / Observation Support]'
  }, {
      'code':
      'OS01',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Scientific / Observation Support] [Meteorological Station / Equipment]'
  }, {
      'code':
      'OS02',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Scientific / Observation Support] [Radar / Satellite Infrastructure]'
  }, {
      'code':
      'OS03',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Scientific / Observation Support] [Telescope / Observation Infrastructure / Astronomy]'
  }, {
      'code':
      'OT',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support]'
  }, {
      'code':
      'OT01',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Cattle Grid / Ford]'
  }, {
      'code':
      'OT02',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Elevator / Escalator / Steps]'
  }, {
      'code':
      'OT03',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Footbridge / Walkway]'
  }, {
      'code':
      'OT04',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Pole / Post / Bollard (Restricting Vehicular Access)]'
  }, {
      'code':
      'OT05',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Subway / Underpass]'
  }, {
      'code':
      'OT06',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Customs Inspection Facility]'
  }, {
      'code':
      'OT07',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Lay-By]'
  }, {
      'code':
      'OT08',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Level Crossing]'
  }, {
      'code':
      'OT09',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Mail Pick Up]'
  }, {
      'code':
      'OT10',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Railway Pedestrian Crossing]'
  }, {
      'code':
      'OT11',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Railway Buffer]'
  }, {
      'code':
      'OT12',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Rail Drag]'
  }, {
      'code':
      'OT13',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Rail Infrastructure Services]'
  }, {
      'code':
      'OT14',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Rail Kilometre Distance Marker]'
  }, {
      'code':
      'OT15',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Railway Lighting]'
  }, {
      'code':
      'OT16',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Rail Mile Distance Marker]'
  }, {
      'code':
      'OT17',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Railway Turntable]'
  }, {
      'code':
      'OT18',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Rail Weighbridge]'
  }, {
      'code':
      'OT19',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Rail Signalling]'
  }, {
      'code':
      'OT20',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Railway Traverse]'
  }, {
      'code':
      'OT21',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Goods Tramway]'
  }, {
      'code':
      'OT22',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Road Drag]'
  }, {
      'code':
      'OT23',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Vehicle Dip]'
  }, {
      'code':
      'OT24',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Road Turntable]'
  }, {
      'code':
      'OT25',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Road Mile Distance Marker]'
  }, {
      'code':
      'OT26',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Road Kilometre Distance Marker]'
  }, {
      'code':
      'OT27',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Transport Support] [Road Infrastructure Services]'
  }, {
      'code':
      'OU',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Unsupported Site]'
  }, {
      'code':
      'OU01',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Unsupported Site] [Cycle Parking Facility]'
  }, {
      'code':
      'OU04',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Unsupported Site] [Picnic / Barbeque Site]'
  }, {
      'code':
      'OU05',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Unsupported Site] [Travelling Persons Site]'
  }, {
      'code':
      'OU08',
      'class_list_string':
      '[Other (Ordnance Survey Only)] [Unsupported Site] [Shelter (Not Including Bus Shelter)]'
  }, {
      'code':
      'P',
      'class_list_string':
      '[Parent Shell]'
  }, {
      'code':
      'PP',
      'class_list_string':
      '[Parent Shell] [Property Shell]'
  }, {
      'code':
      'PS',
      'class_list_string':
      '[Parent Shell] [Street Record]'
  }, {
      'code': 'R',
      'class_list_string': '[Residential]'
  }, {
      'code':
      'RB',
      'class_list_string':
      '[Residential] [Ancillary Building]'
  }, {
      'code':
      'RC',
      'class_list_string':
      '[Residential] [Car Park Space]'
  }, {
      'code':
      'RC01',
      'class_list_string':
      '[Residential] [Car Park Space] [Allocated Parking]'
  }, {
      'code':
      'RD',
      'class_list_string':
      '[Residential] [Dwelling]'
  }, {
      'code':
      'RD01',
      'class_list_string':
      '[Residential] [Dwelling] [Caravan]'
  }, {
      'code':
      'RD02',
      'class_list_string':
      '[Residential] [Dwelling] [Detached]'
  }, {
      'code':
      'RD03',
      'class_list_string':
      '[Residential] [Dwelling] [Semi-Detached]'
  }, {
      'code':
      'RD04',
      'class_list_string':
      '[Residential] [Dwelling] [Terraced]'
  }, {
      'code':
      'RD06',
      'class_list_string':
      '[Residential] [Dwelling] [Self Contained Flat (Includes Maisonette / Apartment)]'
  }, {
      'code':
      'RD07',
      'class_list_string':
      '[Residential] [Dwelling] [House Boat]'
  }, {
      'code':
      'RD08',
      'class_list_string':
      '[Residential] [Dwelling] [Sheltered Accommodation]'
  }, {
      'code':
      'RD10',
      'class_list_string':
      '[Residential] [Dwelling] [Privately Owned Holiday Caravan / Chalet]'
  }, {
      'code':
      'RG',
      'class_list_string':
      '[Residential] [Garage]'
  }, {
      'code':
      'RG02',
      'class_list_string':
      '[Residential] [Garage] [Lock-Up Garage / Garage Court]'
  }, {
      'code':
      'RH',
      'class_list_string':
      '[Residential] [House In Multiple Occupation]'
  }, {
      'code':
      'RH01',
      'class_list_string':
      '[Residential] [House In Multiple Occupation] [HMO Parent]'
  }, {
      'code':
      'RH02',
      'class_list_string':
      '[Residential] [House In Multiple Occupation] [HMO Bedsit / Other Non Self Contained Accommodation]'
  }, {
      'code':
      'RH03',
      'class_list_string':
      '[Residential] [House In Multiple Occupation] [HMO Not Further Divided]'
  }, {
      'code':
      'RI',
      'class_list_string':
      '[Residential] [Residential Institution]'
  }, {
      'code':
      'RI01',
      'class_list_string':
      '[Residential] [Residential Institution] [Care / Nursing Home]'
  }, {
      'code':
      'RI02',
      'class_list_string':
      '[Residential] [Residential Institution] [Communal Residence]'
  }, {
      'code':
      'RI02NC',
      'class_list_string':
      '[Residential] [Residential Institution] [Communal Residence] [Non-Commercial Lodgings]'
  }, {
      'code':
      'RI02RC',
      'class_list_string':
      '[Residential] [Residential Institution] [Communal Residence] [Religious Community]'
  }, {
      'code':
      'RI03',
      'class_list_string':
      '[Residential] [Residential Institution] [Residential Education]'
  }, {
      'code':
      'U',
      'class_list_string':
      '[Unclassified]'
  }, {
      'code':
      'UC',
      'class_list_string':
      '[Unclassified] [Awaiting Classification]'
  }, {
      'code':
      'UP',
      'class_list_string':
      '[Unclassified] [Pending Internal Investigation]'
  }, {
      'code': 'X',
      'class_list_string': '[Dual Use]'
  }, {
      'code':
      'Z',
      'class_list_string':
      '[Object of Interest]'
  }, {
      'code':
      'ZA',
      'class_list_string':
      '[Object of Interest] [Archaeological Dig Site]'
  }, {
      'code':
      'ZM',
      'class_list_string':
      '[Object of Interest] [Monument]'
  }, {
      'code':
      'ZM01',
      'class_list_string':
      '[Object of Interest] [Monument] [Obelisk / Milestone / Standing Stone]'
  }, {
      'code':
      'ZM01OB',
      'class_list_string':
      '[Object of Interest] [Monument] [Obelisk / Milestone / Standing Stone] [Obelisk]'
  }, {
      'code':
      'ZM01ST',
      'class_list_string':
      '[Object of Interest] [Monument] [Obelisk / Milestone / Standing Stone] [Standing Stone]'
  }, {
      'code':
      'ZM02',
      'class_list_string':
      '[Object of Interest] [Monument] [Memorial / Market Cross]'
  }, {
      'code':
      'ZM03',
      'class_list_string':
      '[Object of Interest] [Monument] [Statue]'
  }, {
      'code':
      'ZM04',
      'class_list_string':
      '[Object of Interest] [Monument] [Castle / Historic Ruin]'
  }, {
      'code':
      'ZM05',
      'class_list_string':
      '[Object of Interest] [Monument] [Other Structure]'
  }, {
      'code':
      'ZM05BS',
      'class_list_string':
      '[Object of Interest] [Monument] [Other Structure] [Boundary Stone]'
  }, {
      'code':
      'ZM05CE',
      'class_list_string':
      '[Object of Interest] [Monument] [Other Structure] [Cascade / Fountain]'
  }, {
      'code':
      'ZM05PN',
      'class_list_string':
      '[Object of Interest] [Monument] [Other Structure] [Permanent Art Display / Sculpture]'
  }, {
      'code':
      'ZM05WI',
      'class_list_string':
      '[Object of Interest] [Monument] [Other Structure] [Windmill (Inactive)]'
  }, {
      'code':
      'ZS',
      'class_list_string':
      '[Object of Interest] [Stately Home]'
  }, {
      'code':
      'ZU',
      'class_list_string':
      '[Object of Interest] [Underground Feature]'
  }, {
      'code':
      'ZU01',
      'class_list_string':
      '[Object of Interest] [Underground Feature] [Cave]'
  }, {
      'code':
      'ZU04',
      'class_list_string':
      '[Object of Interest] [Underground Feature] [Pothole / Natural Hole]'
  }, {
      'code':
      'ZV',
      'class_list_string':
      '[Object of Interest] [Other Underground Feature]'
  }, {
      'code':
      'ZV01',
      'class_list_string':
      '[Object of Interest] [Other Underground Feature] [Cellar]'
  }, {
      'code':
      'ZV02',
      'class_list_string':
      '[Object of Interest] [Other Underground Feature] [Disused Mine]'
  }, {
      'code':
      'ZV02MI',
      'class_list_string':
      '[Object of Interest] [Other Underground Feature] [Disused Mine] [Mineral Mining / Inactive]'
  }, {
      'code':
      'ZV02OI',
      'class_list_string':
      '[Object of Interest] [Other Underground Feature] [Disused Mine] [Oil And / Gas Extraction/ Inactive]'
  }, {
      'code':
      'ZV02QI',
      'class_list_string':
      '[Object of Interest] [Other Underground Feature] [Disused Mine] [Mineral Quarrying And / Open Extraction / Inactive]'
  }, {
      'code':
      'ZV03',
      'class_list_string':
      '[Object of Interest] [Other Underground Feature] [Well / Spring]'
  }, {
      'code':
      'ZV03SG',
      'class_list_string':
      '[Object of Interest] [Other Underground Feature] [Well / Spring] [Spring]'
  }, {
      'code':
      'ZV03WL',
      'class_list_string':
      '[Object of Interest] [Other Underground Feature] [Well / Spring] [Well]'
  }, {
      'code':
      'ZW',
      'class_list_string':
      '[Object of Interest] [Place Of Worship]'
  }, {
      'code':
      'ZW99AB',
      'class_list_string':
      '[Object of Interest] [Place Of Worship] [Abbey]'
  }, {
      'code':
      'ZW99CA',
      'class_list_string':
      '[Object of Interest] [Place Of Worship] [Cathedral]'
  }, {
      'code':
      'ZW99CH',
      'class_list_string':
      '[Object of Interest] [Place Of Worship] [Church]'
  }, {
      'code':
      'ZW99CP',
      'class_list_string':
      '[Object of Interest] [Place Of Worship] [Chapel]'
  }, {
      'code':
      'ZW99GU',
      'class_list_string':
      '[Object of Interest] [Place Of Worship] [Gurdwara]'
  }, {
      'code':
      'ZW99KH',
      'class_list_string':
      '[Object of Interest] [Place Of Worship] [Kingdom Hall]'
  }, {
      'code':
      'ZW99LG',
      'class_list_string':
      '[Object of Interest] [Place Of Worship] [Lych Gate]'
  }, {
      'code':
      'ZW99MQ',
      'class_list_string':
      '[Object of Interest] [Place Of Worship] [Mosque]'
  }, {
      'code':
      'ZW99MT',
      'class_list_string':
      '[Object of Interest] [Place Of Worship] [Minster]'
  }, {
      'code':
      'ZW99SU',
      'class_list_string':
      '[Object of Interest] [Place Of Worship] [Stupa]'
  }, {
      'code':
      'ZW99SY',
      'class_list_string':
      '[Object of Interest] [Place Of Worship] [Synagogue]'
  }, {
      'code':
      'ZW99TP',
      'class_list_string':
      '[Object of Interest] [Place Of Worship] [Temple]'
  }]

  return classification_codes_and_string_pairs
