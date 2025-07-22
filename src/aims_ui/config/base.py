"""FLASK BASE CONFIG"""
import base64
import json
import os

# Port that the Flask server will run on
UI_EXPOSED_PORT = 5000

JSONIFY_PRETTYPRINT_REGULAR = True
MAX_CONTENT_LENGTH = 10 * 1024 * 1024
API_AUTH_TYPE = os.getenv('API_AUTH_TYPE')

API_JWT_TOKEN = os.getenv('API_JWT_TOKEN')
API_JWT_TOKEN_BEARER = 'Bearer ' + str(API_JWT_TOKEN if API_JWT_TOKEN else '')

BM_JWT_TOKEN = os.getenv('BM_JWT_TOKEN')
BM_JWT_TOKEN_BEARER = 'Bearer ' + str(BM_JWT_TOKEN if BM_JWT_TOKEN else '')
BM_JOB_NAME_CHAR_LIMIT = int(os.getenv('BM_JOB_NAME_CHAR_LIMIT', '20'))

PROJECT_DOMAIN = os.getenv('PROJECT_DOMAIN')
BM_API_URL = os.getenv('BM_API_URL')
BM_MAX_JOBS = int(os.getenv('BM_MAX_JOBS', '7'))

SESSION_COOKIE_SECURE = True
AIMS_UI_PAGES_LOCATION = 'aims_ui_pages'

API_BSC_AUTH_USERNAME = os.getenv('API_BSC_AUTH_USERNAME')
API_BSC_AUTH_PASSWORD = os.getenv('API_BSC_AUTH_PASSWORD')

API_JWT_K_VALUE = str(os.getenv('API_JWT_K_VALUE'))
API_JWT_K_VALUE = base64.b64decode(API_JWT_K_VALUE)

FLASK_ENV = str(os.getenv('FLASK_ENV')).upper()

# Default usernames for paywall
USER_AUTHS = json.loads(os.getenv('USER_AUTHS', '{}'))

# Define order of pages on header and Paywall Limitations
ALL_PAGE_NAMES = [
    'singlesearch', 'uprn', 'postcode', 'typeahead',
    'multiple_address_original', 'multiple_address_results', 'multiple_address_attributes',
    'multiple_address', 'uprn_multiple_match', 'custom_response', 'help',
    'settings'
]

DEFAULT_BULK_LIMITS = {
    'limit_mini_bulk': 5000,
    'limit_vast_bulk': 100000,
    'limit_uprn_match': 5000,
}

# yapf: disable
USER_GROUPS = [
    {
        'name': 'default',  # UNSPECIFIED USERS WILL BE IN THIS GROUP
        'description': 'Users that do not fall into another group will be part of this group',
        'usernames': USER_AUTHS.get('default', []),
        'pages_to_remove': ['custom_response'],
        'bulk_limits': DEFAULT_BULK_LIMITS,
    },
    {
        'name': 'developers',
        'description': 'Developer users who might need more granular access to the API and are comfortable dealing with errors and less guard rails',
        'usernames': USER_AUTHS.get('developers', []),
        'pages_to_remove': [],
        'bulk_limits': DEFAULT_BULK_LIMITS,
    },
    {
        'name': 'bulk_removed',
        'description': 'Completely remove access to the bulk match pages',
        'usernames': USER_AUTHS.get('bulk_removed', []),
        'pages_to_remove': [
            'multiple_address_original', 'uprn_multiple_match',
            'multiple_address', 'multiple_address_results', 'multiple_address_attributes'
        ],
        'bulk_limits': DEFAULT_BULK_LIMITS,
    },
    {
        'name': 'limited_bulk',
        'description': 'Limit the matching capacity but leave access to the pages',
        'usernames': USER_AUTHS.get('limited_bulk', []),
        'pages_to_remove': [],
        'bulk_limits': {
            'limit_mini_bulk': 10,
            'limit_vast_bulk': 550,
            'limit_uprn_match': 50,
        }
    },
]
# yapf: enable

# For each group, create a list of "allowed pages"
for group in USER_GROUPS:
  allowed_pages = []
  for page_name in ALL_PAGE_NAMES:
    if page_name not in group.get('pages_to_remove'):
      allowed_pages.append(page_name)
  group['allowed_pages'] = allowed_pages

# Default Classification and Epoch options, should the initial server response be incorrect (or the endpoint doesn't exist)

DEFAULT_EPOCH_SELECTED = '89'
DEFAULT_EPOCH_OPTIONS = [{
    'id': '39',
    'text': '39',
    'value': '39',
    'description': 'Exeter Sample'
}, {
    'id': '80',
    'text': '80',
    'value': '80',
    'description': 'Census no extras'
}, {
    'id': '87',
    'text': '87',
    'value': '87',
    'description': 'September 2021'
}, {
    'id': '89',
    'text': '89',
    'value': '89',
    'description': 'December 2021'
}]

DEFAULT_CLASSIFICATION_CLASS_LIST = [{
    'code': 'C',
    'label': 'Commercial'
}, {
    'code': 'CA',
    'label': 'Agricultural'
}, {
    'code':
    'CA01',
    'label':
    'Farm / Non-Residential Associated Building'
}, {
    'code': 'CA02',
    'label': 'Fishery'
}, {
    'code': 'CA02FF',
    'label': 'Fish Farming'
}, {
    'code': 'CA02FH',
    'label': 'Fish Hatchery'
}, {
    'code': 'CA02FP',
    'label': 'Fish Processing'
}, {
    'code': 'CA02OY',
    'label': 'Oyster / Mussel Bed'
}, {
    'code': 'CA03',
    'label': 'Horticulture'
}, {
    'code': 'CA03SH',
    'label': 'Smallholding'
}, {
    'code': 'CA03VY',
    'label': 'Vineyard'
}, {
    'code': 'CA03WB',
    'label': 'Watercress Bed'
}, {
    'code': 'CA04',
    'label': 'Slaughter House / Abattoir'
}, {
    'code': 'CB',
    'label': 'Ancillary Building'
}, {
    'code': 'CC',
    'label': 'Community Services'
}, {
    'code': 'CC02',
    'label': 'Law Court'
}, {
    'code': 'CC03',
    'label': 'Prison'
}, {
    'code': 'CC03HD',
    'label': 'HM Detention Centre'
}, {
    'code': 'CC03PR',
    'label': 'HM Prison Service'
}, {
    'code':
    'CC03SC',
    'label':
    'Secure Residential Accommodation'
}, {
    'code':
    'CC04',
    'label':
    'Public / Village Hall / Other Community Facility'
}, {
    'code':
    'CC04YR',
    'label':
    'Youth Recreational / Social Club'
}, {
    'code': 'CC05',
    'label': 'Public Convenience'
}, {
    'code':
    'CC06',
    'label':
    'Cemetery / Crematorium / Graveyard. In Current Use.'
}, {
    'code': 'CC06CB',
    'label': 'Columbarium'
}, {
    'code': 'CC06CR',
    'label': 'Chapel Of Rest'
}, {
    'code': 'CC06CN',
    'label': 'Crematorium'
}, {
    'code': 'CC06CY',
    'label': 'Cemetery'
}, {
    'code': 'CC06MC',
    'label': 'Military Cemetery'
}, {
    'code': 'CC06MY',
    'label': 'Mortuary'
}, {
    'code':
    'CC07',
    'label':
    'Church Hall / Religious Meeting Place / Hall'
}, {
    'code':
    'CC08',
    'label':
    'Community Service Centre / Office'
}, {
    'code':
    'CC09',
    'label':
    'Public Household Waste Recycling Centre (HWRC)'
}, {
    'code': 'CC10',
    'label': 'Recycling Site'
}, {
    'code': 'CC11',
    'label': 'CCTV'
}, {
    'code': 'CC12',
    'label': 'Job Centre'
}, {
    'code': 'CE',
    'label': 'Education'
}, {
    'code': 'CE01',
    'label': 'College'
}, {
    'code': 'CE01FE',
    'label': 'Further Education'
}, {
    'code': 'CE01HE',
    'label': 'Higher Education'
}, {
    'code': 'CE02',
    'label': "Children''s Nursery / Crèche"
}, {
    'code':
    'CE03',
    'label':
    'Preparatory / First / Primary / Infant / Junior / Middle School'
}, {
    'code': 'CE03FS',
    'label': 'First School'
}, {
    'code': 'CE03IS',
    'label': 'Infant School'
}, {
    'code': 'CE03JS',
    'label': 'Junior School'
}, {
    'code': 'CE03MS',
    'label': 'Middle School'
}, {
    'code':
    'CE03NP',
    'label':
    'Non State Primary / Preparatory School'
}, {
    'code': 'CE03PS',
    'label': 'Primary School'
}, {
    'code': 'CE04',
    'label': 'Secondary / High School'
}, {
    'code': 'CE04NS',
    'label': 'Non State Secondary School'
}, {
    'code': 'CE04SS',
    'label': 'Secondary School'
}, {
    'code': 'CE05',
    'label': 'University'
}, {
    'code': 'CE06',
    'label': 'Special Needs Establishment.'
}, {
    'code': 'CE07',
    'label': 'Other Educational Establishment'
}, {
    'code':
    'CH',
    'label':
    'Hotel / Motel / Boarding / Guest House'
}, {
    'code':
    'CH01',
    'label':
    'Boarding / Guest House / Bed And Breakfast / Youth Hostel'
}, {
    'code': 'CH01YH',
    'label': 'Youth Hostel'
}, {
    'code':
    'CH02',
    'label':
    'Holiday Let/Accomodation/Short-Term Let Other Than CH01'
}, {
    'code': 'CH03',
    'label': 'Hotel/Motel'
}, {
    'code':
    'CI',
    'label':
    'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites'
}, {
    'code': 'CI01',
    'label': 'Factory/Manufacturing'
}, {
    'code': 'CI01AW',
    'label': 'Aircraft Works'
}, {
    'code': 'CI01BB',
    'label': 'Boat Building'
}, {
    'code': 'CI01BR',
    'label': 'Brick Works'
}, {
    'code': 'CI01BW',
    'label': 'Brewery'
}, {
    'code': 'CI01CD',
    'label': 'Cider Manufacture'
}, {
    'code': 'CI01CM',
    'label': 'Chemical Works'
}, {
    'code': 'CI01CW',
    'label': 'Cement Works'
}, {
    'code': 'CI01DA',
    'label': 'Dairy Processing'
}, {
    'code': 'CI01DY',
    'label': 'Distillery'
}, {
    'code': 'CI01FL',
    'label': 'Flour Mill'
}, {
    'code': 'CI01FO',
    'label': 'Food Processing'
}, {
    'code': 'CI01GW',
    'label': 'Glassworks'
}, {
    'code': 'CI01MG',
    'label': 'Manufacturing'
}, {
    'code': 'CI01OH',
    'label': 'Oast House'
}, {
    'code': 'CI01OR',
    'label': 'Oil Refining'
}, {
    'code': 'CI01PG',
    'label': 'Pottery Manufacturing'
}, {
    'code': 'CI01PM',
    'label': 'Paper Mill'
}, {
    'code': 'CI01PW',
    'label': 'Printing Works'
}, {
    'code': 'CI01YD',
    'label': 'Shipyard'
}, {
    'code': 'CI01SR',
    'label': 'Sugar Refinery'
}, {
    'code': 'CI01SW',
    'label': 'Steel Works'
}, {
    'code': 'CI01TL',
    'label': 'Timber Mill'
}, {
    'code': 'CI01WN',
    'label': 'Winery'
}, {
    'code':
    'CI02',
    'label':
    'Mineral / Ore Working / Quarry / Mine'
}, {
    'code': 'CI02MA',
    'label': 'Mineral Mining / Active'
}, {
    'code': 'CI02MD',
    'label': 'Mineral Distribution / Storage'
}, {
    'code': 'CI02MP',
    'label': 'Mineral Processing'
}, {
    'code': 'CI02OA',
    'label': 'Oil / Gas Extraction / Active'
}, {
    'code':
    'CI02QA',
    'label':
    'Mineral Quarrying / Open Extraction / Active'
}, {
    'code': 'CI03',
    'label': 'Workshop / Light Industrial'
}, {
    'code': 'CI03GA',
    'label': 'Servicing Garage'
}, {
    'code':
    'CI04',
    'label':
    'Warehouse / Store / Storage Depot'
}, {
    'code': 'CI04CS',
    'label': 'Crop Handling / Storage'
}, {
    'code': 'CI04PL',
    'label': 'Postal Sorting / Distribution'
}, {
    'code': 'CI04SO',
    'label': 'Solid Fuel Storage'
}, {
    'code': 'CI04TS',
    'label': 'Timber Storage'
}, {
    'code': 'CI05',
    'label': 'Wholesale Distribution'
}, {
    'code': 'CI05SF',
    'label': 'Solid Fuel Distribution'
}, {
    'code': 'CI05TD',
    'label': 'Timber Distribution'
}, {
    'code': 'CI06',
    'label': 'Recycling Plant'
}, {
    'code':
    'CI07',
    'label':
    'Incinerator / Waste Transfer Station'
}, {
    'code': 'CI08',
    'label': 'Maintenance Depot'
}, {
    'code':
    'CL',
    'label':
    'Leisure - Applicable to recreational sites and enterprises'
}, {
    'code': 'CL01',
    'label': 'Amusements'
}, {
    'code': 'CL01LP',
    'label': 'Leisure Pier'
}, {
    'code': 'CL02',
    'label': 'Holiday / Campsite'
}, {
    'code': 'CL02CG',
    'label': 'Camping'
}, {
    'code': 'CL02CV',
    'label': 'Caravanning'
}, {
    'code': 'CL02HA',
    'label': 'Holiday Accommodation'
}, {
    'code': 'CL02HO',
    'label': 'Holiday Centre'
}, {
    'code': 'CL02YC',
    'label': 'Youth Organisation Camp'
}, {
    'code': 'CL03',
    'label': 'Library'
}, {
    'code': 'CL03RR',
    'label': 'Reading Room'
}, {
    'code': 'CL04',
    'label': 'Museum / Gallery'
}, {
    'code': 'CL04AC',
    'label': 'Art Centre / Gallery'
}, {
    'code': 'CL04AM',
    'label': 'Aviation Museum'
}, {
    'code': 'CL04HG',
    'label': 'Heritage Centre'
}, {
    'code': 'CL04IM',
    'label': 'Industrial Museum'
}, {
    'code': 'CL04MM',
    'label': 'Military Museum'
}, {
    'code': 'CL04SM',
    'label': 'Science Museum'
}, {
    'code': 'CL04TM',
    'label': 'Transport Museum'
}, {
    'code': 'CL04NM',
    'label': 'Maritime Museum'
}, {
    'code':
    'CL06',
    'label':
    'Indoor / Outdoor Leisure / Sporting Activity / Centre'
}, {
    'code': 'CL06AH',
    'label': 'Athletics Facility'
}, {
    'code': 'CL06BF',
    'label': 'Bowls Facility'
}, {
    'code': 'CL06CK',
    'label': 'Cricket Facility'
}, {
    'code': 'CL06CU',
    'label': 'Curling Facility'
}, {
    'code': 'CL06YF',
    'label': 'Cycling Sports Facility'
}, {
    'code': 'CL06DS',
    'label': 'Diving / Swimming Facility'
}, {
    'code': 'CL06EQ',
    'label': 'Equestrian Sports Facility'
}, {
    'code': 'CL06FB',
    'label': 'Football Facility'
}, {
    'code': 'CL06FI',
    'label': 'Fishing / Angling Facility'
}, {
    'code': 'CL06GF',
    'label': 'Golf Facility'
}, {
    'code': 'CL06GL',
    'label': 'Gliding Facility'
}, {
    'code': 'CL06GR',
    'label': 'Greyhound Racing Facility'
}, {
    'code': 'CL06HF',
    'label': 'Hockey Facility'
}, {
    'code': 'CL06HR',
    'label': 'Horse Racing Facility'
}, {
    'code':
    'CL06HV',
    'label':
    'Historic Vessel / Aircraft / Vehicle'
}, {
    'code':
    'CL06LS',
    'label':
    'Activity / Leisure / Sports Centre'
}, {
    'code': 'CL06ME',
    'label': 'Model Sports Facility'
}, {
    'code': 'CL06MF',
    'label': 'Motor Sports Facility'
}, {
    'code': 'CL06PF',
    'label': 'Playing Field'
}, {
    'code': 'CL06QS',
    'label': 'Racquet Sports Facility'
}, {
    'code': 'CL06RF',
    'label': 'Rugby Facility'
}, {
    'code': 'CL06RG',
    'label': 'Recreation Ground'
}, {
    'code': 'CL06SI',
    'label': 'Shinty Facility'
}, {
    'code': 'CL06SK',
    'label': 'Skateboarding Facility'
}, {
    'code': 'CL06SX',
    'label': 'Civilian Firing Facility'
}, {
    'code': 'CL06TB',
    'label': 'Tenpin Bowling Facility'
}, {
    'code': 'CL06TN',
    'label': 'Public Tennis Court'
}, {
    'code': 'CL06WA',
    'label': 'Water Sports Facility'
}, {
    'code': 'CL06WP',
    'label': 'Winter Sports Facility'
}, {
    'code': 'CL06WY',
    'label': 'Wildlife Sports Facility'
}, {
    'code':
    'CL07',
    'label':
    'Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall'
}, {
    'code': 'CL07TH',
    'label': 'Theatre'
}, {
    'code': 'CL07CI',
    'label': 'Cinema'
}, {
    'code': 'CL07EN',
    'label': 'Entertainment Complex'
}, {
    'code': 'CL07EX',
    'label': 'Conference / Exhibition Centre'
}, {
    'code': 'CL08',
    'label': 'Zoo / Theme Park'
}, {
    'code': 'CL08AK',
    'label': 'Amusement Park'
}, {
    'code': 'CL08MX',
    'label': 'Model Village Site'
}, {
    'code': 'CL08WZ',
    'label': 'Wildlife / Zoological Park'
}, {
    'code': 'CL08AQ',
    'label': 'Aquatic Attraction'
}, {
    'code':
    'CL09',
    'label':
    'Beach Hut (Recreational, Non-Residential Use Only)'
}, {
    'code': 'CL10',
    'label': 'Licensed Private Members Club'
}, {
    'code': 'CL10RE',
    'label': 'Recreational / Social Club'
}, {
    'code': 'CL11',
    'label': 'Arena / Stadium'
}, {
    'code': 'CL11SD',
    'label': 'Stadium'
}, {
    'code': 'CL11SJ',
    'label': 'Showground'
}, {
    'code': 'CM',
    'label': 'Medical'
}, {
    'code': 'CM01',
    'label': 'Dentist'
}, {
    'code':
    'CM02',
    'label':
    'General Practice Surgery / Clinic'
}, {
    'code': 'CM02HL',
    'label': 'Health Care Services'
}, {
    'code': 'CM02HC',
    'label': 'Health Centre'
}, {
    'code': 'CM03',
    'label': 'Hospital / Hospice'
}, {
    'code': 'CM03HI',
    'label': 'Hospice'
}, {
    'code': 'CM03HP',
    'label': 'Hospital'
}, {
    'code':
    'CM04',
    'label':
    'Medical / Testing / Research Laboratory'
}, {
    'code': 'CM05',
    'label': 'Professional Medical Service'
}, {
    'code':
    'CM05ZS',
    'label':
    'Assessment / Development Services'
}, {
    'code': 'CN',
    'label': 'Animal Centre'
}, {
    'code': 'CN01',
    'label': 'Cattery / Kennel'
}, {
    'code': 'CN02',
    'label': 'Animal Services'
}, {
    'code': 'CN02AX',
    'label': 'Animal Quarantining'
}, {
    'code': 'CN03',
    'label': 'Equestrian'
}, {
    'code': 'CN03HB',
    'label': 'Horse Racing / Breeding Stable'
}, {
    'code': 'CN03SB',
    'label': 'Commercial Stabling / Riding'
}, {
    'code': 'CN04',
    'label': 'Vet / Animal Medical Treatment'
}, {
    'code':
    'CN05',
    'label':
    'Animal / Bird / Marine Sanctuary'
}, {
    'code': 'CN05AN',
    'label': 'Animal Sanctuary'
}, {
    'code': 'CN05MR',
    'label': 'Marine Sanctuary'
}, {
    'code': 'CO',
    'label': 'Office'
}, {
    'code': 'CO01',
    'label': 'Office / Work Studio'
}, {
    'code':
    'CO01EM',
    'label':
    'Embassy / High Commission / Consulate'
}, {
    'code': 'CO01FM',
    'label': 'Film Studio'
}, {
    'code': 'CO01GV',
    'label': 'Central Government Service'
}, {
    'code': 'CO01LG',
    'label': 'Local Government Service'
}, {
    'code': 'CO02',
    'label': 'Broadcasting (TV / Radio)'
}, {
    'code': 'CR',
    'label': 'Retail'
}, {
    'code': 'CR01',
    'label': 'Bank / Financial Service'
}, {
    'code': 'CR02',
    'label': 'Retail Service Agent'
}, {
    'code': 'CR02PO',
    'label': 'Post Office'
}, {
    'code': 'CR04',
    'label': 'Market (Indoor / Outdoor)'
}, {
    'code': 'CR04FK',
    'label': 'Fish Market'
}, {
    'code': 'CR04FV',
    'label': 'Fruit / Vegetable Market'
}, {
    'code': 'CR04LV',
    'label': 'Livestock Market'
}, {
    'code': 'CR05',
    'label': 'Petrol Filling Station'
}, {
    'code': 'CR06',
    'label': 'Public House / Bar / Nightclub'
}, {
    'code': 'CR07',
    'label': 'Restaurant / Cafeteria'
}, {
    'code': 'CR08',
    'label': 'Shop / Showroom'
}, {
    'code': 'CR08GC',
    'label': 'Garden Centre'
}, {
    'code': 'CR09',
    'label': 'Other Licensed Premise / Vendor'
}, {
    'code':
    'CR10',
    'label':
    'Fast Food Outlet / Takeaway (Hot / Cold)'
}, {
    'code': 'CR11',
    'label': 'Automated Teller Machine (ATM)'
}, {
    'code': 'CS',
    'label': 'Storage Land'
}, {
    'code': 'CS01',
    'label': 'General Storage Land'
}, {
    'code': 'CS02',
    'label': 'Builders Yard'
}, {
    'code': 'CT',
    'label': 'Transport'
}, {
    'code':
    'CT01',
    'label':
    'Airfield / Airstrip / Airport / Air Transport Infrastructure Facility'
}, {
    'code': 'CT01AF',
    'label': 'Airfield'
}, {
    'code': 'CT01AY',
    'label': 'Air Passenger Terminal'
}, {
    'code':
    'CT01AI',
    'label':
    'Air Transport Infrastructure Services'
}, {
    'code': 'CT01AP',
    'label': 'Airport'
}, {
    'code': 'CT01HS',
    'label': 'Helicopter Station'
}, {
    'code': 'CT01HT',
    'label': 'Heliport / Helipad'
}, {
    'code': 'CT02',
    'label': 'Bus Shelter'
}, {
    'code':
    'CT03',
    'label':
    'Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site'
}, {
    'code': 'CT03PK',
    'label': 'Public Park And Ride'
}, {
    'code': 'CT03PP',
    'label': 'Public Car Parking'
}, {
    'code': 'CT03PU',
    'label': 'Public Coach Parking'
}, {
    'code':
    'CT03VP',
    'label':
    'Public Commercial Vehicle Parking'
}, {
    'code':
    'CT04',
    'label':
    'Goods Freight Handling / Terminal'
}, {
    'code': 'CT04AE',
    'label': 'Air Freight Terminal'
}, {
    'code': 'CT04CF',
    'label': 'Container Freight'
}, {
    'code': 'CT04RH',
    'label': 'Road Freight Transport'
}, {
    'code': 'CT04RT',
    'label': 'Rail Freight Transport'
}, {
    'code': 'CT05',
    'label': 'Marina'
}, {
    'code': 'CT06',
    'label': 'Mooring'
}, {
    'code': 'CT07',
    'label': 'Railway Asset'
}, {
    'code':
    'CT08',
    'label':
    'Station / Interchange / Terminal / Halt'
}, {
    'code': 'CT08BC',
    'label': 'Bus / Coach Station'
}, {
    'code': 'CT08RS',
    'label': 'Railway Station'
}, {
    'code': 'CT08VH',
    'label': 'Vehicular Rail Terminal'
}, {
    'code': 'CT09',
    'label': 'Transport Track / Way'
}, {
    'code': 'CT09CL',
    'label': 'Cliff Railway'
}, {
    'code':
    'CT09CX',
    'label':
    'Chair Lift / Cable Car / Ski Tow'
}, {
    'code': 'CT09MO',
    'label': 'Monorail'
}, {
    'code': 'CT10',
    'label': 'Vehicle Storage'
}, {
    'code': 'CT10BG',
    'label': 'Boat Storage'
}, {
    'code': 'CT10BU',
    'label': 'Bus / Coach Depot'
}, {
    'code':
    'CT11',
    'label':
    'Transport Related Infrastructure'
}, {
    'code': 'CT11AD',
    'label': 'Aqueduct'
}, {
    'code': 'CT11LK',
    'label': 'Lock'
}, {
    'code': 'CT11WE',
    'label': 'Weir'
}, {
    'code': 'CT11WG',
    'label': 'Weighbridge / Load Gauge'
}, {
    'code': 'CT12',
    'label': 'Overnight Lorry Park'
}, {
    'code':
    'CT13',
    'label':
    'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay'
}, {
    'code': 'CT13FR',
    'label': 'Passenger Ferry Terminal'
}, {
    'code': 'CT13NB',
    'label': 'Non-Tanker Nautical Berthing'
}, {
    'code': 'CT13NF',
    'label': 'Nautical Refuelling Facility'
}, {
    'code': 'CT13SA',
    'label': 'Slipway'
}, {
    'code': 'CT13SP',
    'label': 'Ship Passenger Terminal'
}, {
    'code': 'CT13TK',
    'label': 'Tanker Berthing'
}, {
    'code': 'CT13VF',
    'label': 'Vehicular Ferry Terminal'
}, {
    'code': 'CU',
    'label': 'Utility'
}, {
    'code': 'CU01',
    'label': 'Electricity Sub-Station'
}, {
    'code': 'CU02',
    'label': 'Landfill'
}, {
    'code':
    'CU03',
    'label':
    'Power Station / Energy Production'
}, {
    'code':
    'CU03ED',
    'label':
    'Electricity Distribution Facility'
}, {
    'code': 'CU03EP',
    'label': 'Electricity Production Facility'
}, {
    'code': 'CU03WF',
    'label': 'Wind Farm'
}, {
    'code': 'CU03WU',
    'label': 'Wind Turbine'
}, {
    'code':
    'CU04',
    'label':
    'Pump House / Pumping Station / Water Tower'
}, {
    'code': 'CU04WC',
    'label': 'Water Controlling / Pumping'
}, {
    'code': 'CU04WD',
    'label': 'Water Distribution / Pumping'
}, {
    'code': 'CU04WM',
    'label': 'Water Quality Monitoring'
}, {
    'code': 'CU04WS',
    'label': 'Water Storage'
}, {
    'code':
    'CU04WW',
    'label':
    'Waste Water Distribution / Pumping'
}, {
    'code': 'CU06',
    'label': 'Telecommunication'
}, {
    'code': 'CU06TE',
    'label': 'Telecommunications Mast'
}, {
    'code': 'CU06TX',
    'label': 'Telephone Exchange'
}, {
    'code':
    'CU07',
    'label':
    'Water / Waste Water / Sewage Treatment Works'
}, {
    'code': 'CU07WR',
    'label': 'Waste Water Treatment'
}, {
    'code': 'CU07WT',
    'label': 'Water Treatment'
}, {
    'code':
    'CU08',
    'label':
    'Gas / Oil Storage / Distribution'
}, {
    'code': 'CU08GG',
    'label': 'Gas Governor'
}, {
    'code': 'CU08GH',
    'label': 'Gas Holder'
}, {
    'code': 'CU08OT',
    'label': 'Oil Terminal'
}, {
    'code': 'CU09',
    'label': 'Other Utility Use'
}, {
    'code': 'CU09OV',
    'label': 'Observatory'
}, {
    'code': 'CU09RA',
    'label': 'Radar Station'
}, {
    'code': 'CU09SE',
    'label': 'Satellite Earth Station'
}, {
    'code': 'CU09CQ',
    'label': 'Cable Terminal Station'
}, {
    'code': 'CU10',
    'label': 'Waste Management'
}, {
    'code': 'CU11',
    'label': 'Telephone Box'
}, {
    'code': 'CU11OP',
    'label': 'Other Public Telephones'
}, {
    'code': 'CU12',
    'label': 'Dam'
}, {
    'code': 'CX',
    'label': 'Emergency / Rescue Service'
}, {
    'code':
    'CX01',
    'label':
    'Police / Transport Police / Station'
}, {
    'code': 'CX01PT',
    'label': 'Police Training'
}, {
    'code': 'CX02',
    'label': 'Fire Station'
}, {
    'code': 'CX02FT',
    'label': 'Fire Service Training'
}, {
    'code': 'CX03',
    'label': 'Ambulance Station'
}, {
    'code': 'CX03AA',
    'label': 'Air Sea Rescue / Air Ambulance'
}, {
    'code': 'CX04',
    'label': 'Lifeboat Services / Station'
}, {
    'code':
    'CX05',
    'label':
    'Coastguard Rescue / Lookout / Station'
}, {
    'code': 'CX06',
    'label': 'Mountain Rescue Station'
}, {
    'code': 'CX07',
    'label': 'Lighthouse'
}, {
    'code': 'CX08',
    'label': 'Police Box / Kiosk'
}, {
    'code': 'CZ',
    'label': 'Information'
}, {
    'code': 'CZ01',
    'label': 'Advertising Hoarding'
}, {
    'code': 'CZ02',
    'label': 'Tourist Information Signage'
}, {
    'code': 'CZ02VI',
    'label': 'Visitor Information'
}, {
    'code': 'CZ03',
    'label': 'Traffic Information Signage'
}, {
    'code': 'L',
    'label': 'Land'
}, {
    'code':
    'LA',
    'label':
    'Agricultural - Applicable to land in farm ownership and not run as a separate business enterprise'
}, {
    'code': 'LA01',
    'label': 'Grazing Land'
}, {
    'code': 'LA02',
    'label': 'Permanent Crop / Crop Rotation'
}, {
    'code': 'LA02OC',
    'label': 'Orchard'
}, {
    'code': 'LB',
    'label': 'Ancillary Building'
}, {
    'code': 'LB99AV',
    'label': 'Aviary / Dovecot / Cage'
}, {
    'code': 'LB99BD',
    'label': 'Bandstand'
}, {
    'code': 'LB99PI',
    'label': 'Pavilion / Changing Room'
}, {
    'code': 'LB99SV',
    'label': 'Sports Viewing Structure'
}, {
    'code': 'LC',
    'label': 'Burial Ground'
}, {
    'code':
    'LC01',
    'label':
    'Historic / Disused Cemetery / Graveyard'
}, {
    'code': 'LD',
    'label': 'Development'
}, {
    'code': 'LD01',
    'label': 'Development Site'
}, {
    'code': 'LD01CC',
    'label': 'Commercial Construction Site'
}, {
    'code': 'LD01CO',
    'label': 'Community Construction Site'
}, {
    'code': 'LD01RN',
    'label': 'Residential Construction Site'
}, {
    'code': 'LD01TC',
    'label': 'Transport Construction Site'
}, {
    'code': 'LF',
    'label': 'Forestry'
}, {
    'code':
    'LF02',
    'label':
    'Forest / Arboretum / Pinetum (Managed / Unmanaged)'
}, {
    'code': 'LF02AU',
    'label': 'Arboretum'
}, {
    'code': 'LF03',
    'label': 'Woodland'
}, {
    'code': 'LL',
    'label': 'Allotment'
}, {
    'code':
    'LM',
    'label':
    'Amenity - Open areas not attracting visitors'
}, {
    'code': 'LM01',
    'label': 'Landscaped Roundabout'
}, {
    'code': 'LM02',
    'label': 'Verge / Central Reservation'
}, {
    'code': 'LM02NV',
    'label': 'Natural Central Reservation'
}, {
    'code': 'LM02VE',
    'label': 'Natural Verge'
}, {
    'code': 'LM03',
    'label': 'Maintained Amenity Land'
}, {
    'code': 'LM04',
    'label': 'Maintained Surfaced Area'
}, {
    'code': 'LM04MV',
    'label': 'Made Central Reservation'
}, {
    'code': 'LM04PV',
    'label': 'Pavement'
}, {
    'code': 'LO',
    'label': 'Open Space'
}, {
    'code': 'LO01',
    'label': 'Heath / Moorland'
}, {
    'code': 'LP',
    'label': 'Park'
}, {
    'code': 'LP01',
    'label': 'Public Park / Garden'
}, {
    'code':
    'LP02',
    'label':
    'Public Open Space / Nature Reserve'
}, {
    'code': 'LP03',
    'label': 'Playground'
}, {
    'code': 'LP03PA',
    'label': 'Play Area'
}, {
    'code': 'LP03PD',
    'label': 'Paddling Pool'
}, {
    'code': 'LP04',
    'label': 'Private Park / Garden'
}, {
    'code': 'LU',
    'label': 'Unused Land'
}, {
    'code': 'LU01',
    'label': 'Vacant / Derelict Land'
}, {
    'code': 'LW',
    'label': 'Water'
}, {
    'code': 'LW01',
    'label': 'Lake / Reservoir'
}, {
    'code': 'LW01BP',
    'label': 'Balancing Pond'
}, {
    'code': 'LW01BV',
    'label': 'Buried Reservoir'
}, {
    'code': 'LW02',
    'label': 'Named Pond'
}, {
    'code': 'LW02DE',
    'label': 'Dew Pond'
}, {
    'code': 'LW02DP',
    'label': 'Decoy Pond'
}, {
    'code': 'LW02IW',
    'label': 'Static Water'
}, {
    'code': 'LW03',
    'label': 'Waterway'
}, {
    'code': 'LW03LR',
    'label': 'Leats / Races'
}, {
    'code': 'LW03DR',
    'label': 'Drain'
}, {
    'code': 'M',
    'label': 'Military'
}, {
    'code': 'MA',
    'label': 'Army'
}, {
    'code': 'MA99AR',
    'label': 'Army Military Range'
}, {
    'code': 'MA99AS',
    'label': 'Army Site'
}, {
    'code': 'MA99AT',
    'label': 'Army Military Training'
}, {
    'code': 'MA99AG',
    'label': 'Army Military Storage'
}, {
    'code': 'MB',
    'label': 'Ancillary Building'
}, {
    'code': 'MB99TG',
    'label': 'Military Target'
}, {
    'code': 'MF',
    'label': 'Air Force'
}, {
    'code': 'MF99UG',
    'label': 'Air Force Military Storage'
}, {
    'code': 'MF99UR',
    'label': 'Air Force Military Range'
}, {
    'code': 'MF99US',
    'label': 'Air Force Site'
}, {
    'code': 'MF99UT',
    'label': 'Air Force Military Training'
}, {
    'code': 'MG',
    'label': 'Defence Estates'
}, {
    'code': 'MN',
    'label': 'Navy'
}, {
    'code': 'MN99VG',
    'label': 'Naval Military Storage'
}, {
    'code': 'MN99VR',
    'label': 'Naval Military Range'
}, {
    'code': 'MN99VS',
    'label': 'Naval Site'
}, {
    'code': 'MN99VT',
    'label': 'Naval Military Training'
}, {
    'code': 'O',
    'label': 'Other (Ordnance Survey Only)'
}, {
    'code': 'OA',
    'label': 'Aid To Navigation'
}, {
    'code': 'OA01',
    'label': 'Aid To Aeronautical Navigation'
}, {
    'code':
    'OA01AL',
    'label':
    'Aeronautical Navigation Beacon / Light'
}, {
    'code': 'OA01LL',
    'label': 'Landing Light'
}, {
    'code': 'OA01SQ',
    'label': 'Signal Square'
}, {
    'code': 'OA01WK',
    'label': 'Wind Sock / Wind Tee'
}, {
    'code': 'OA02',
    'label': 'Aid To Nautical Navigation'
}, {
    'code': 'OA02DM',
    'label': 'Daymark'
}, {
    'code': 'OA02FG',
    'label': 'Fog Horn Warning'
}, {
    'code':
    'OA02NL',
    'label':
    'Nautical Navigation Beacon / Light'
}, {
    'code': 'OA03',
    'label': 'Aid To Road Navigation'
}, {
    'code': 'OA03GP',
    'label': 'Guide Post'
}, {
    'code':
    'OC',
    'label':
    'Coastal Protection / Flood Prevention'
}, {
    'code': 'OC01',
    'label': 'Boulder Wall / Sea Wall'
}, {
    'code':
    'OC02',
    'label':
    'Flood Gate / Flood Sluice Gate / Flood Valve'
}, {
    'code': 'OC03',
    'label': 'Groyne'
}, {
    'code': 'OC04',
    'label': 'Rip-Rap'
}, {
    'code': 'OE',
    'label': 'Emergency Support'
}, {
    'code':
    'OE01',
    'label':
    'Beach Office / First Aid Facility'
}, {
    'code':
    'OE02',
    'label':
    'Emergency Telephone (Non Motorway)'
}, {
    'code':
    'OE03',
    'label':
    'Fire Alarm Structure / Fire Observation Tower / Fire Beater Facility'
}, {
    'code':
    'OE04',
    'label':
    'Emergency Equipment Point / Emergency Siren / Warning Flag'
}, {
    'code': 'OE05',
    'label': 'Lifeguard Facility'
}, {
    'code':
    'OE06',
    'label':
    'Life / Belt / Buoy / Float / Jacket / Safety Rope'
}, {
    'code': 'OF',
    'label': 'Street Furniture'
}, {
    'code': 'OG',
    'label': 'Agricultural Support Objects'
}, {
    'code': 'OG01',
    'label': 'Fish Ladder / Lock / Pen / Trap'
}, {
    'code': 'OG02',
    'label': 'Livestock Pen / Dip'
}, {
    'code': 'OG03',
    'label': 'Currick'
}, {
    'code': 'OG04',
    'label': 'Slurry Bed / Pit'
}, {
    'code': 'OH',
    'label': 'Historical Site / Object'
}, {
    'code': 'OH01',
    'label': 'Historic Structure / Object'
}, {
    'code': 'OI',
    'label': 'Industrial Support'
}, {
    'code': 'OI01',
    'label': 'Adit / Incline / Level'
}, {
    'code': 'OI02',
    'label': 'Caisson / Dry Dock / Grid'
}, {
    'code':
    'OI03',
    'label':
    'Channel / Conveyor / Conduit / Pipe'
}, {
    'code': 'OI04',
    'label': 'Chimney / Flue'
}, {
    'code':
    'OI05',
    'label':
    'Crane / Hoist / Winch / Material Elevator'
}, {
    'code': 'OI06',
    'label': 'Flare Stack'
}, {
    'code': 'OI07',
    'label': 'Hopper / Silo / Cistern / Tank'
}, {
    'code':
    'OI08',
    'label':
    'Grab / Skip / Other Industrial Waste Machinery / Discharging'
}, {
    'code': 'OI09',
    'label': 'Kiln / Oven / Smelter'
}, {
    'code': 'OI10',
    'label': 'Manhole / Shaft'
}, {
    'code':
    'OI11',
    'label':
    'Industrial Overflow / Sluice / Valve / Valve Housing'
}, {
    'code': 'OI12',
    'label': 'Cooling Tower'
}, {
    'code': 'OI13',
    'label': 'Solar Panel / Waterwheel'
}, {
    'code': 'OI14',
    'label': 'Telephone Pole / Post'
}, {
    'code':
    'OI15',
    'label':
    'Electricity Distribution Pole / Pylon'
}, {
    'code': 'ON',
    'label': 'Significant Natural Object'
}, {
    'code':
    'ON01',
    'label':
    'Boundary / Significant / Historic Tree / Pollard'
}, {
    'code':
    'ON02',
    'label':
    'Boundary / Significant Rock / Boulder'
}, {
    'code':
    'ON03',
    'label':
    'Natural Hole (Blow / Shake / Swallow)'
}, {
    'code': 'OO',
    'label': 'Ornamental / Cultural Object'
}, {
    'code': 'OO02',
    'label': 'Mausoleum / Tomb / Grave'
}, {
    'code': 'OO03',
    'label': 'Simple Ornamental Object'
}, {
    'code': 'OO04',
    'label': 'Maze'
}, {
    'code': 'OP',
    'label': 'Sport / Leisure Support'
}, {
    'code': 'OP01',
    'label': 'Butt / Hide'
}, {
    'code': 'OP02',
    'label': 'Gallop / Ride'
}, {
    'code': 'OP03',
    'label': 'Miniature Railway'
}, {
    'code': 'OR',
    'label': 'Royal Mail Infrastructure'
}, {
    'code': 'OR01',
    'label': 'Postal Box'
}, {
    'code': 'OR02',
    'label': 'Postal Delivery Box / Pouch'
}, {
    'code': 'OR03',
    'label': 'PO Box'
}, {
    'code':
    'OR04',
    'label':
    'Additional Mail / Packet Addressee'
}, {
    'code':
    'OS',
    'label':
    'Scientific / Observation Support'
}, {
    'code':
    'OS01',
    'label':
    'Meteorological Station / Equipment'
}, {
    'code':
    'OS02',
    'label':
    'Radar / Satellite Infrastructure'
}, {
    'code':
    'OS03',
    'label':
    'Telescope / Observation Infrastructure / Astronomy'
}, {
    'code': 'OT',
    'label': 'Transport Support'
}, {
    'code': 'OT01',
    'label': 'Cattle Grid / Ford'
}, {
    'code': 'OT02',
    'label': 'Elevator / Escalator / Steps'
}, {
    'code': 'OT03',
    'label': 'Footbridge / Walkway'
}, {
    'code':
    'OT04',
    'label':
    'Pole / Post / Bollard (Restricting Vehicular Access)'
}, {
    'code': 'OT05',
    'label': 'Subway / Underpass'
}, {
    'code': 'OT06',
    'label': 'Customs Inspection Facility'
}, {
    'code': 'OT07',
    'label': 'Lay-By'
}, {
    'code': 'OT08',
    'label': 'Level Crossing'
}, {
    'code': 'OT09',
    'label': 'Mail Pick Up'
}, {
    'code': 'OT10',
    'label': 'Railway Pedestrian Crossing'
}, {
    'code': 'OT11',
    'label': 'Railway Buffer'
}, {
    'code': 'OT12',
    'label': 'Rail Drag'
}, {
    'code': 'OT13',
    'label': 'Rail Infrastructure Services'
}, {
    'code': 'OT14',
    'label': 'Rail Kilometre Distance Marker'
}, {
    'code': 'OT15',
    'label': 'Railway Lighting'
}, {
    'code': 'OT16',
    'label': 'Rail Mile Distance Marker'
}, {
    'code': 'OT17',
    'label': 'Railway Turntable'
}, {
    'code': 'OT18',
    'label': 'Rail Weighbridge'
}, {
    'code': 'OT19',
    'label': 'Rail Signalling'
}, {
    'code': 'OT20',
    'label': 'Railway Traverse'
}, {
    'code': 'OT21',
    'label': 'Goods Tramway'
}, {
    'code': 'OT22',
    'label': 'Road Drag'
}, {
    'code': 'OT23',
    'label': 'Vehicle Dip'
}, {
    'code': 'OT24',
    'label': 'Road Turntable'
}, {
    'code': 'OT25',
    'label': 'Road Mile Distance Marker'
}, {
    'code': 'OT26',
    'label': 'Road Kilometre Distance Marker'
}, {
    'code': 'OT27',
    'label': 'Road Infrastructure Services'
}, {
    'code': 'OU',
    'label': 'Unsupported Site'
}, {
    'code': 'OU01',
    'label': 'Cycle Parking Facility'
}, {
    'code': 'OU04',
    'label': 'Picnic / Barbeque Site'
}, {
    'code': 'OU05',
    'label': 'Travelling Persons Site'
}, {
    'code':
    'OU08',
    'label':
    'Shelter (Not Including Bus Shelter)'
}, {
    'code': 'P',
    'label': 'Parent Shell'
}, {
    'code': 'PP',
    'label': 'Property Shell'
}, {
    'code': 'PS',
    'label': 'Street Record'
}, {
    'code': 'R',
    'label': 'Residential'
}, {
    'code': 'RB',
    'label': 'Ancillary Building'
}, {
    'code': 'RC',
    'label': 'Car Park Space'
}, {
    'code': 'RC01',
    'label': 'Allocated Parking'
}, {
    'code': 'RD',
    'label': 'Dwelling'
}, {
    'code': 'RD01',
    'label': 'Caravan'
}, {
    'code': 'RD02',
    'label': 'Detached'
}, {
    'code': 'RD03',
    'label': 'Semi-Detached'
}, {
    'code': 'RD04',
    'label': 'Terraced'
}, {
    'code':
    'RD06',
    'label':
    'Self Contained Flat (Includes Maisonette / Apartment)'
}, {
    'code': 'RD07',
    'label': 'House Boat'
}, {
    'code': 'RD08',
    'label': 'Sheltered Accommodation'
}, {
    'code':
    'RD10',
    'label':
    'Privately Owned Holiday Caravan / Chalet'
}, {
    'code': 'RG',
    'label': 'Garage'
}, {
    'code': 'RG02',
    'label': 'Lock-Up Garage / Garage Court'
}, {
    'code': 'RH',
    'label': 'House In Multiple Occupation'
}, {
    'code': 'RH01',
    'label': 'HMO Parent'
}, {
    'code':
    'RH02',
    'label':
    'HMO Bedsit / Other Non Self Contained Accommodation'
}, {
    'code': 'RH03',
    'label': 'HMO Not Further Divided'
}, {
    'code': 'RI',
    'label': 'Residential Institution'
}, {
    'code': 'RI01',
    'label': 'Care / Nursing Home'
}, {
    'code': 'RI02',
    'label': 'Communal Residence'
}, {
    'code': 'RI02NC',
    'label': 'Non-Commercial Lodgings'
}, {
    'code': 'RI02RC',
    'label': 'Religious Community'
}, {
    'code': 'RI03',
    'label': 'Residential Education'
}, {
    'code': 'U',
    'label': 'Unclassified'
}, {
    'code': 'UC',
    'label': 'Awaiting Classification'
}, {
    'code': 'UP',
    'label': 'Pending Internal Investigation'
}, {
    'code': 'X',
    'label': 'Dual Use'
}, {
    'code': 'Z',
    'label': 'Object of Interest'
}, {
    'code': 'ZA',
    'label': 'Archaeological Dig Site'
}, {
    'code': 'ZM',
    'label': 'Monument'
}, {
    'code':
    'ZM01',
    'label':
    'Obelisk / Milestone / Standing Stone'
}, {
    'code': 'ZM01OB',
    'label': 'Obelisk'
}, {
    'code': 'ZM01ST',
    'label': 'Standing Stone'
}, {
    'code': 'ZM02',
    'label': 'Memorial / Market Cross'
}, {
    'code': 'ZM03',
    'label': 'Statue'
}, {
    'code': 'ZM04',
    'label': 'Castle / Historic Ruin'
}, {
    'code': 'ZM05',
    'label': 'Other Structure'
}, {
    'code': 'ZM05BS',
    'label': 'Boundary Stone'
}, {
    'code':
    'ZM05PN',
    'label':
    'Permanent Art Display / Sculpture'
}, {
    'code': 'ZM05CE',
    'label': 'Cascade / Fountain'
}, {
    'code': 'ZM05WI',
    'label': 'Windmill (Inactive)'
}, {
    'code': 'ZS',
    'label': 'Stately Home'
}, {
    'code': 'ZU',
    'label': 'Underground Feature'
}, {
    'code': 'ZU01',
    'label': 'Cave'
}, {
    'code': 'ZU04',
    'label': 'Pothole / Natural Hole'
}, {
    'code': 'ZV',
    'label': 'Other Underground Feature'
}, {
    'code': 'ZV01',
    'label': 'Cellar'
}, {
    'code': 'ZV02',
    'label': 'Disused Mine'
}, {
    'code': 'ZV02MI',
    'label': 'Mineral Mining / Inactive'
}, {
    'code':
    'ZV02OI',
    'label':
    'Oil And / Gas Extraction/ Inactive'
}, {
    'code':
    'ZV02QI',
    'label':
    'Mineral Quarrying And / Open Extraction / Inactive'
}, {
    'code': 'ZV03',
    'label': 'Well / Spring'
}, {
    'code': 'ZV03SG',
    'label': 'Spring'
}, {
    'code': 'ZV03WL',
    'label': 'Well'
}, {
    'code': 'ZW',
    'label': 'Place Of Worship'
}, {
    'code': 'ZW99AB',
    'label': 'Abbey'
}, {
    'code': 'ZW99CA',
    'label': 'Cathedral'
}, {
    'code': 'ZW99CH',
    'label': 'Church'
}, {
    'code': 'ZW99CP',
    'label': 'Chapel'
}, {
    'code': 'ZW99GU',
    'label': 'Gurdwara'
}, {
    'code': 'ZW99KH',
    'label': 'Kingdom Hall'
}, {
    'code': 'ZW99MQ',
    'label': 'Mosque'
}, {
    'code': 'ZW99MT',
    'label': 'Minster'
}, {
    'code': 'ZW99SU',
    'label': 'Stupa'
}, {
    'code': 'ZW99SY',
    'label': 'Synagogue'
}, {
    'code': 'ZW99TP',
    'label': 'Temple'
}, {
    'code': 'ZW99LG',
    'label': 'Lych Gate'
}]
