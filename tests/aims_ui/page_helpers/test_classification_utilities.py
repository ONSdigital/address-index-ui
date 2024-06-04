from flask import Flask

from src import aims_ui
from aims_ui.page_helpers.classification_utilities import check_reverse_classification

def test_check_reverse_classification():
    """ Check that the classification can be obtained from the string value """
    
    result = check_reverse_classification('C')
    assert result == 'Commercial'
    
    result = check_reverse_classification('CA')
    assert result == 'Agricultural'
    
    result = check_reverse_classification('CA01')
    assert result == 'Farm / Non-Residential Associated Building'
    
    result = check_reverse_classification('CA02')
    assert result == 'Fishery'
    
    result = check_reverse_classification('CA02FF')
    assert result == 'Fish Farming'
    
    result = check_reverse_classification('CA02FH')
    assert result == 'Fish Hatchery'
    
    result = check_reverse_classification('CA02FP')
    assert result == 'Fish Processing'
    
    result = check_reverse_classification('CA02OY')
    assert result == 'Oyster / Mussel Bed'
    
    result = check_reverse_classification('CA03')
    assert result == 'Horticulture'
    
    result = check_reverse_classification('CA03SH')
    assert result == 'Smallholding'
    
    result = check_reverse_classification('CA03VY')
    assert result == 'Vineyard'
    
    result = check_reverse_classification('CA03WB')
    assert result == 'Watercress Bed'
    
    result = check_reverse_classification('CA04')
    assert result == 'Slaughter House / Abattoir'
    
    result = check_reverse_classification('CB')
    assert result == 'Ancillary Building'
    
    result = check_reverse_classification('CC')
    assert result == 'Community Services'
    
    result = check_reverse_classification('CC02')
    assert result == 'Law Court'
    
    result = check_reverse_classification('CC03')
    assert result == 'Prison'
    
    result = check_reverse_classification('CC03HD')
    assert result == 'HM Detention Centre'
    
    result = check_reverse_classification('CC03PR')
    assert result == 'HM Prison Service'
    
    result = check_reverse_classification('CC03SC')
    assert result == 'Secure Residential Accommodation'
    
    result = check_reverse_classification('CC04')
    assert result == 'Public / Village Hall / Other Community Facility'
    
    result = check_reverse_classification('CC04YR')
    assert result == 'Youth Recreational / Social Club'
    
    result = check_reverse_classification('CC05')
    assert result == 'Public Convenience'
    
    result = check_reverse_classification('CC06')
    assert result == 'Cemetery / Crematorium / Graveyard. In Current Use.'
    
    result = check_reverse_classification('CC06CB')
    assert result == 'Columbarium'
    
    result = check_reverse_classification('CC06CR')
    assert result == 'Chapel Of Rest'
    
    result = check_reverse_classification('CC06CN')
    assert result == 'Crematorium'
    
    result = check_reverse_classification('CC06CY')
    assert result == 'Cemetery'
    
    result = check_reverse_classification('CC06MC')
    assert result == 'Military Cemetery'
    
    result = check_reverse_classification('CC06MY')
    assert result == 'Mortuary'
    
    result = check_reverse_classification('CC07')
    assert result == 'Church Hall / Religious Meeting Place / Hall'
    
    result = check_reverse_classification('CC08')
    assert result == 'Community Service Centre / Office'
    
    result = check_reverse_classification('CC09')
    assert result == 'Public Household Waste Recycling Centre (HWRC)'
    
    result = check_reverse_classification('CC10')
    assert result == 'Recycling Site'
    
    result = check_reverse_classification('CC11')
    assert result == 'CCTV'
    
    result = check_reverse_classification('CC12')
    assert result == 'Job Centre'
    
    result = check_reverse_classification('CE')
    assert result == 'Education'
    
    result = check_reverse_classification('CE01')
    assert result == 'College'
    
    result = check_reverse_classification('CE01FE')
    assert result == 'Further Education'
    
    result = check_reverse_classification('CE01HE')
    assert result == 'Higher Education'
    
    result = check_reverse_classification('CE02')
    assert result == "Children''s Nursery / Crèche"
    
    result = check_reverse_classification('CE03')
    assert result == 'Preparatory / First / Primary / Infant / Junior / Middle School'
    
    result = check_reverse_classification('CE03FS')
    assert result == 'First School'
    
    result = check_reverse_classification('CE03IS')
    assert result == 'Infant School'
    
    result = check_reverse_classification('CE03JS')
    assert result == 'Junior School'
    
    result = check_reverse_classification('CE03MS')
    assert result == 'Middle School'
    
    result = check_reverse_classification('CE03NP')
    assert result == 'Non State Primary / Preparatory School'
    
    result = check_reverse_classification('CE03PS')
    assert result == 'Primary School'
    
    result = check_reverse_classification('CE04')
    assert result == 'Secondary / High School'
    
    result = check_reverse_classification('CE04NS')
    assert result == 'Non State Secondary School'
    
    result = check_reverse_classification('CE04SS')
    assert result == 'Secondary School'
    
    result = check_reverse_classification('CE05')
    assert result == 'University'
    
    result = check_reverse_classification('CE06')
    assert result == 'Special Needs Establishment.'
    
    result = check_reverse_classification('CE07')
    assert result == 'Other Educational Establishment'
    
    result = check_reverse_classification('CH')
    assert result == 'Hotel / Motel / Boarding / Guest House'
    
    result = check_reverse_classification('CH01')
    assert result == 'Boarding / Guest House / Bed And Breakfast / Youth Hostel'
    
    result = check_reverse_classification('CH01YH')
    assert result == 'Youth Hostel'
    
    result = check_reverse_classification('CH02')
    assert result == 'Holiday Let/Accomodation/Short-Term Let Other Than CH01'
    
    result = check_reverse_classification('CH03')
    assert result == 'Hotel/Motel'
    
    result = check_reverse_classification('CI')
    assert result == 'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites'
    
    result = check_reverse_classification('CI01')
    assert result == 'Factory/Manufacturing'
    
    result = check_reverse_classification('CI01AW')
    assert result == 'Aircraft Works'
    
    result = check_reverse_classification('CI01BB')
    assert result == 'Boat Building'
    
    result = check_reverse_classification('CI01BR')
    assert result == 'Brick Works'
    
    result = check_reverse_classification('CI01BW')
    assert result == 'Brewery'
    
    result = check_reverse_classification('CI01CD')
    assert result == 'Cider Manufacture'
    
    result = check_reverse_classification('CI01CM')
    assert result == 'Chemical Works'
    
    result = check_reverse_classification('CI01CW')
    assert result == 'Cement Works'
    
    result = check_reverse_classification('CI01DA')
    assert result == 'Dairy Processing'
    
    result = check_reverse_classification('CI01DY')
    assert result == 'Distillery'
    
    result = check_reverse_classification('CI01FL')
    assert result == 'Flour Mill'
    
    result = check_reverse_classification('CI01FO')
    assert result == 'Food Processing'
    
    result = check_reverse_classification('CI01GW')
    assert result == 'Glassworks'
    
    result = check_reverse_classification('CI01MG')
    assert result == 'Manufacturing'
    
    result = check_reverse_classification('CI01OH')
    assert result == 'Oast House'
    
    result = check_reverse_classification('CI01OR')
    assert result == 'Oil Refining'
    
    result = check_reverse_classification('CI01PG')
    assert result == 'Pottery Manufacturing'
    
    result = check_reverse_classification('CI01PM')
    assert result == 'Paper Mill'
    
    result = check_reverse_classification('CI01PW')
    assert result == 'Printing Works'
    
    result = check_reverse_classification('CI01YD')
    assert result == 'Shipyard'
    
    result = check_reverse_classification('CI01SR')
    assert result == 'Sugar Refinery'
    
    result = check_reverse_classification('CI01SW')
    assert result == 'Steel Works'
    
    result = check_reverse_classification('CI01TL')
    assert result == 'Timber Mill'
    
    result = check_reverse_classification('CI01WN')
    assert result == 'Winery'
    
    result = check_reverse_classification('CI02')
    assert result == 'Mineral / Ore Working / Quarry / Mine'
    
    result = check_reverse_classification('CI02MA')
    assert result == 'Mineral Mining / Active'
    
    result = check_reverse_classification('CI02MD')
    assert result == 'Mineral Distribution / Storage'
    
    result = check_reverse_classification('CI02MP')
    assert result == 'Mineral Processing'
    
    result = check_reverse_classification('CI02OA')
    assert result == 'Oil / Gas Extraction / Active'
    
    result = check_reverse_classification('CI02QA')
    assert result == 'Mineral Quarrying / Open Extraction / Active'
    
    result = check_reverse_classification('CI03')
    assert result == 'Workshop / Light Industrial'
    
    result = check_reverse_classification('CI03GA')
    assert result == 'Servicing Garage'
    
    result = check_reverse_classification('CI04')
    assert result == 'Warehouse / Store / Storage Depot'
    
    result = check_reverse_classification('CI04CS')
    assert result == 'Crop Handling / Storage'
    
    result = check_reverse_classification('CI04PL')
    assert result == 'Postal Sorting / Distribution'
    
    result = check_reverse_classification('CI04SO')
    assert result == 'Solid Fuel Storage'
    
    result = check_reverse_classification('CI04TS')
    assert result == 'Timber Storage'
    
    result = check_reverse_classification('CI05')
    assert result == 'Wholesale Distribution'
    
    result = check_reverse_classification('CI05SF')
    assert result == 'Solid Fuel Distribution'
    
    result = check_reverse_classification('CI05TD')
    assert result == 'Timber Distribution'
    
    result = check_reverse_classification('CI06')
    assert result == 'Recycling Plant'
    
    result = check_reverse_classification('CI07')
    assert result == 'Incinerator / Waste Transfer Station'
    
    result = check_reverse_classification('CI08')
    assert result == 'Maintenance Depot'
    
    result = check_reverse_classification('CL')
    assert result == 'Leisure - Applicable to recreational sites and enterprises'
    
    result = check_reverse_classification('CL01')
    assert result == 'Amusements'
    
    result = check_reverse_classification('CL01LP')
    assert result == 'Leisure Pier'
    
    result = check_reverse_classification('CL02')
    assert result == 'Holiday / Campsite'
    
    result = check_reverse_classification('CL02CG')
    assert result == 'Camping'
    
    result = check_reverse_classification('CL02CV')
    assert result == 'Caravanning'
    
    result = check_reverse_classification('CL02HA')
    assert result == 'Holiday Accommodation'
    
    result = check_reverse_classification('CL02HO')
    assert result == 'Holiday Centre'
    
    result = check_reverse_classification('CL02YC')
    assert result == 'Youth Organisation Camp'
    
    result = check_reverse_classification('CL03')
    assert result == 'Library'
    
    result = check_reverse_classification('CL03RR')
    assert result == 'Reading Room'
    
    result = check_reverse_classification('CL04')
    assert result == 'Museum / Gallery'
    
    result = check_reverse_classification('CL04AC')
    assert result == 'Art Centre / Gallery'
    
    result = check_reverse_classification('CL04AM')
    assert result == 'Aviation Museum'
    
    result = check_reverse_classification('CL04HG')
    assert result == 'Heritage Centre'
    
    result = check_reverse_classification('CL04IM')
    assert result == 'Industrial Museum'
    
    result = check_reverse_classification('CL04MM')
    assert result == 'Military Museum'
    
    result = check_reverse_classification('CL04SM')
    assert result == 'Science Museum'
    
    result = check_reverse_classification('CL04TM')
    assert result == 'Transport Museum'
    
    result = check_reverse_classification('CL04NM')
    assert result == 'Maritime Museum'
    
    result = check_reverse_classification('CL06')
    assert result == 'Indoor / Outdoor Leisure / Sporting Activity / Centre'
    
    result = check_reverse_classification('CL06AH')
    assert result == 'Athletics Facility'
    
    result = check_reverse_classification('CL06BF')
    assert result == 'Bowls Facility'
    
    result = check_reverse_classification('CL06CK')
    assert result == 'Cricket Facility'
    
    result = check_reverse_classification('CL06CU')
    assert result == 'Curling Facility'
    
    result = check_reverse_classification('CL06YF')
    assert result == 'Cycling Sports Facility'
    
    result = check_reverse_classification('CL06DS')
    assert result == 'Diving / Swimming Facility'
    
    result = check_reverse_classification('CL06EQ')
    assert result == 'Equestrian Sports Facility'
    
    result = check_reverse_classification('CL06FB')
    assert result == 'Football Facility'
    
    result = check_reverse_classification('CL06FI')
    assert result == 'Fishing / Angling Facility'
    
    result = check_reverse_classification('CL06GF')
    assert result == 'Golf Facility'
    
    result = check_reverse_classification('CL06GL')
    assert result == 'Gliding Facility'
    
    result = check_reverse_classification('CL06GR')
    assert result == 'Greyhound Racing Facility'
    
    result = check_reverse_classification('CL06HF')
    assert result == 'Hockey Facility'
    
    result = check_reverse_classification('CL06HR')
    assert result == 'Horse Racing Facility'
    
    result = check_reverse_classification('CL06HV')
    assert result == 'Historic Vessel / Aircraft / Vehicle'
    
    result = check_reverse_classification('CL06LS')
    assert result == 'Activity / Leisure / Sports Centre'
    
    result = check_reverse_classification('CL06ME')
    assert result == 'Model Sports Facility'
    
    result = check_reverse_classification('CL06MF')
    assert result == 'Motor Sports Facility'
    
    result = check_reverse_classification('CL06PF')
    assert result == 'Playing Field'
    
    result = check_reverse_classification('CL06QS')
    assert result == 'Racquet Sports Facility'
    
    result = check_reverse_classification('CL06RF')
    assert result == 'Rugby Facility'
    
    result = check_reverse_classification('CL06RG')
    assert result == 'Recreation Ground'
    
    result = check_reverse_classification('CL06SI')
    assert result == 'Shinty Facility'
    
    result = check_reverse_classification('CL06SK')
    assert result == 'Skateboarding Facility'
    
    result = check_reverse_classification('CL06SX')
    assert result == 'Civilian Firing Facility'
    
    result = check_reverse_classification('CL06TB')
    assert result == 'Tenpin Bowling Facility'
    
    result = check_reverse_classification('CL06TN')
    assert result == 'Public Tennis Court'
    
    result = check_reverse_classification('CL06WA')
    assert result == 'Water Sports Facility'
    
    result = check_reverse_classification('CL06WP')
    assert result == 'Winter Sports Facility'
    
    result = check_reverse_classification('CL06WY')
    assert result == 'Wildlife Sports Facility'
    
    result = check_reverse_classification('CL07')
    assert result == 'Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall'
    
    result = check_reverse_classification('CL07TH')
    assert result == 'Theatre'
    
    result = check_reverse_classification('CL07CI')
    assert result == 'Cinema'
    
    result = check_reverse_classification('CL07EN')
    assert result == 'Entertainment Complex'
    
    result = check_reverse_classification('CL07EX')
    assert result == 'Conference / Exhibition Centre'
    
    result = check_reverse_classification('CL08')
    assert result == 'Zoo / Theme Park'
    
    result = check_reverse_classification('CL08AK')
    assert result == 'Amusement Park'
    
    result = check_reverse_classification('CL08MX')
    assert result == 'Model Village Site'
    
    result = check_reverse_classification('CL08WZ')
    assert result == 'Wildlife / Zoological Park'
    
    result = check_reverse_classification('CL08AQ')
    assert result == 'Aquatic Attraction'
    
    result = check_reverse_classification('CL09')
    assert result == 'Beach Hut (Recreational, Non-Residential Use Only)'
    
    result = check_reverse_classification('CL10')
    assert result == 'Licensed Private Members Club'
    
    result = check_reverse_classification('CL10RE')
    assert result == 'Recreational / Social Club'
    
    result = check_reverse_classification('CL11')
    assert result == 'Arena / Stadium'
    
    result = check_reverse_classification('CL11SD')
    assert result == 'Stadium'
    
    result = check_reverse_classification('CL11SJ')
    assert result == 'Showground'
    
    result = check_reverse_classification('CM')
    assert result == 'Medical'
    
    result = check_reverse_classification('CM01')
    assert result == 'Dentist'
    
    result = check_reverse_classification('CM02')
    assert result == 'General Practice Surgery / Clinic'
    
    result = check_reverse_classification('CM02HL')
    assert result == 'Health Care Services'
    
    result = check_reverse_classification('CM02HC')
    assert result == 'Health Centre'
    
    result = check_reverse_classification('CM03')
    assert result == 'Hospital / Hospice'
    
    result = check_reverse_classification('CM03HI')
    assert result == 'Hospice'
    
    result = check_reverse_classification('CM03HP')
    assert result == 'Hospital'
    
    result = check_reverse_classification('CM04')
    assert result == 'Medical / Testing / Research Laboratory'
    
    result = check_reverse_classification('CM05')
    assert result == 'Professional Medical Service'
    
    result = check_reverse_classification('CM05ZS')
    assert result == 'Assessment / Development Services'
    
    result = check_reverse_classification('CN')
    assert result == 'Animal Centre'
    
    result = check_reverse_classification('CN01')
    assert result == 'Cattery / Kennel'
    
    result = check_reverse_classification('CN02')
    assert result == 'Animal Services'
    
    result = check_reverse_classification('CN02AX')
    assert result == 'Animal Quarantining'
    
    result = check_reverse_classification('CN03')
    assert result == 'Equestrian'
    
    result = check_reverse_classification('CN03HB')
    assert result == 'Horse Racing / Breeding Stable'
    
    result = check_reverse_classification('CN03SB')
    assert result == 'Commercial Stabling / Riding'
    
    result = check_reverse_classification('CN04')
    assert result == 'Vet / Animal Medical Treatment'
    
    result = check_reverse_classification('CN05')
    assert result == 'Animal / Bird / Marine Sanctuary'
    
    result = check_reverse_classification('CN05AN')
    assert result == 'Animal Sanctuary'
    
    result = check_reverse_classification('CN05MR')
    assert result == 'Marine Sanctuary'
    
    result = check_reverse_classification('CO')
    assert result == 'Office'
    
    result = check_reverse_classification('CO01')
    assert result == 'Office / Work Studio'
    
    result = check_reverse_classification('CO01EM')
    assert result == 'Embassy / High Commission / Consulate'
    
    result = check_reverse_classification('CO01FM')
    assert result == 'Film Studio'
    
    result = check_reverse_classification('CO01GV')
    assert result == 'Central Government Service'
    
    result = check_reverse_classification('CO01LG')
    assert result == 'Local Government Service'
    
    result = check_reverse_classification('CO02')
    assert result == 'Broadcasting (TV / Radio)'
    
    result = check_reverse_classification('CR')
    assert result == 'Retail'
    
    result = check_reverse_classification('CR01')
    assert result == 'Bank / Financial Service'
    
    result = check_reverse_classification('CR02')
    assert result == 'Retail Service Agent'
    
    result = check_reverse_classification('CR02PO')
    assert result == 'Post Office'
    
    result = check_reverse_classification('CR04')
    assert result == 'Market (Indoor / Outdoor)'
    
    result = check_reverse_classification('CR04FK')
    assert result == 'Fish Market'
    
    result = check_reverse_classification('CR04FV')
    assert result == 'Fruit / Vegetable Market'
    
    result = check_reverse_classification('CR04LV')
    assert result == 'Livestock Market'
    
    result = check_reverse_classification('CR05')
    assert result == 'Petrol Filling Station'
    
    result = check_reverse_classification('CR06')
    assert result == 'Public House / Bar / Nightclub'
    
    result = check_reverse_classification('CR07')
    assert result == 'Restaurant / Cafeteria'
    
    result = check_reverse_classification('CR08')
    assert result == 'Shop / Showroom'
    
    result = check_reverse_classification('CR08GC')
    assert result == 'Garden Centre'
    
    result = check_reverse_classification('CR09')
    assert result == 'Other Licensed Premise / Vendor'
    
    result = check_reverse_classification('CR10')
    assert result == 'Fast Food Outlet / Takeaway (Hot / Cold)'
    
    result = check_reverse_classification('CR11')
    assert result == 'Automated Teller Machine (ATM)'
    
    result = check_reverse_classification('CS')
    assert result == 'Storage Land'
    
    result = check_reverse_classification('CS01')
    assert result == 'General Storage Land'
    
    result = check_reverse_classification('CS02')
    assert result == 'Builders Yard'
    
    result = check_reverse_classification('CT')
    assert result == 'Transport'
    
    result = check_reverse_classification('CT01')
    assert result == 'Airfield / Airstrip / Airport / Air Transport Infrastructure Facility'
    
    result = check_reverse_classification('CT01AF')
    assert result == 'Airfield'
    
    result = check_reverse_classification('CT01AY')
    assert result == 'Air Passenger Terminal'
    
    result = check_reverse_classification('CT01AI')
    assert result == 'Air Transport Infrastructure Services'
    
    result = check_reverse_classification('CT01AP')
    assert result == 'Airport'
    
    result = check_reverse_classification('CT01HS')
    assert result == 'Helicopter Station'
    
    result = check_reverse_classification('CT01HT')
    assert result == 'Heliport / Helipad'
    
    result = check_reverse_classification('CT02')
    assert result == 'Bus Shelter'
    
    result = check_reverse_classification('CT03')
    assert result == 'Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site'
    
    result = check_reverse_classification('CT03PK')
    assert result == 'Public Park And Ride'
    
    result = check_reverse_classification('CT03PP')
    assert result == 'Public Car Parking'
    
    result = check_reverse_classification('CT03PU')
    assert result == 'Public Coach Parking'
    
    result = check_reverse_classification('CT03VP')
    assert result == 'Public Commercial Vehicle Parking'
    
    result = check_reverse_classification('CT04')
    assert result == 'Goods Freight Handling / Terminal'
    
    result = check_reverse_classification('CT04AE')
    assert result == 'Air Freight Terminal'
    
    result = check_reverse_classification('CT04CF')
    assert result == 'Container Freight'
    
    result = check_reverse_classification('CT04RH')
    assert result == 'Road Freight Transport'
    
    result = check_reverse_classification('CT04RT')
    assert result == 'Rail Freight Transport'
    
    result = check_reverse_classification('CT05')
    assert result == 'Marina'
    
    result = check_reverse_classification('CT06')
    assert result == 'Mooring'
    
    result = check_reverse_classification('CT07')
    assert result == 'Railway Asset'
    
    result = check_reverse_classification('CT08')
    assert result == 'Station / Interchange / Terminal / Halt'
    
    result = check_reverse_classification('CT08BC')
    assert result == 'Bus / Coach Station'
    
    result = check_reverse_classification('CT08RS')
    assert result == 'Railway Station'
    
    result = check_reverse_classification('CT08VH')
    assert result == 'Vehicular Rail Terminal'
    
    result = check_reverse_classification('CT09')
    assert result == 'Transport Track / Way'
    
    result = check_reverse_classification('CT09CL')
    assert result == 'Cliff Railway'
    
    result = check_reverse_classification('CT09CX')
    assert result == 'Chair Lift / Cable Car / Ski Tow'
    
    result = check_reverse_classification('CT09MO')
    assert result == 'Monorail'
    
    result = check_reverse_classification('CT10')
    assert result == 'Vehicle Storage'
    
    result = check_reverse_classification('CT10BG')
    assert result == 'Boat Storage'
    
    result = check_reverse_classification('CT10BU')
    assert result == 'Bus / Coach Depot'
    
    result = check_reverse_classification('CT11')
    assert result == 'Transport Related Infrastructure'
    
    result = check_reverse_classification('CT11AD')
    assert result == 'Aqueduct'
    
    result = check_reverse_classification('CT11LK')
    assert result == 'Lock'
    
    result = check_reverse_classification('CT11WE')
    assert result == 'Weir'
    
    result = check_reverse_classification('CT11WG')
    assert result == 'Weighbridge / Load Gauge'
    
    result = check_reverse_classification('CT12')
    assert result == 'Overnight Lorry Park'
    
    result = check_reverse_classification('CT13')
    assert result == 'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay'
    
    result = check_reverse_classification('CT13FR')
    assert result == 'Passenger Ferry Terminal'
    
    result = check_reverse_classification('CT13NB')
    assert result == 'Non-Tanker Nautical Berthing'
    
    result = check_reverse_classification('CT13NF')
    assert result == 'Nautical Refuelling Facility'
    
    result = check_reverse_classification('CT13SA')
    assert result == 'Slipway'
    
    result = check_reverse_classification('CT13SP')
    assert result == 'Ship Passenger Terminal'
    
    result = check_reverse_classification('CT13TK')
    assert result == 'Tanker Berthing'
    
    result = check_reverse_classification('CT13VF')
    assert result == 'Vehicular Ferry Terminal'
    
    result = check_reverse_classification('CU')
    assert result == 'Utility'
    
    result = check_reverse_classification('CU01')
    assert result == 'Electricity Sub-Station'
    
    result = check_reverse_classification('CU02')
    assert result == 'Landfill'
    
    result = check_reverse_classification('CU03')
    assert result == 'Power Station / Energy Production'
    
    result = check_reverse_classification('CU03ED')
    assert result == 'Electricity Distribution Facility'
    
    result = check_reverse_classification('CU03EP')
    assert result == 'Electricity Production Facility'
    
    result = check_reverse_classification('CU03WF')
    assert result == 'Wind Farm'
    
    result = check_reverse_classification('CU03WU')
    assert result == 'Wind Turbine'
    
    result = check_reverse_classification('CU04')
    assert result == 'Pump House / Pumping Station / Water Tower'
    
    result = check_reverse_classification('CU04WC')
    assert result == 'Water Controlling / Pumping'
    
    result = check_reverse_classification('CU04WD')
    assert result == 'Water Distribution / Pumping'
    
    result = check_reverse_classification('CU04WM')
    assert result == 'Water Quality Monitoring'
    
    result = check_reverse_classification('CU04WS')
    assert result == 'Water Storage'
    
    result = check_reverse_classification('CU04WW')
    assert result == 'Waste Water Distribution / Pumping'
    
    result = check_reverse_classification('CU06')
    assert result == 'Telecommunication'
    
    result = check_reverse_classification('CU06TE')
    assert result == 'Telecommunications Mast'
    
    result = check_reverse_classification('CU06TX')
    assert result == 'Telephone Exchange'
    
    result = check_reverse_classification('CU07')
    assert result == 'Water / Waste Water / Sewage Treatment Works'
    
    result = check_reverse_classification('CU07WR')
    assert result == 'Waste Water Treatment'
    
    result = check_reverse_classification('CU07WT')
    assert result == 'Water Treatment'
    
    result = check_reverse_classification('CU08')
    assert result == 'Gas / Oil Storage / Distribution'
    
    result = check_reverse_classification('CU08GG')
    assert result == 'Gas Governor'
    
    result = check_reverse_classification('CU08GH')
    assert result == 'Gas Holder'
    
    result = check_reverse_classification('CU08OT')
    assert result == 'Oil Terminal'
    
    result = check_reverse_classification('CU09')
    assert result == 'Other Utility Use'
    
    result = check_reverse_classification('CU09OV')
    assert result == 'Observatory'
    
    result = check_reverse_classification('CU09RA')
    assert result == 'Radar Station'
    
    result = check_reverse_classification('CU09SE')
    assert result == 'Satellite Earth Station'
    
    result = check_reverse_classification('CU09CQ')
    assert result == 'Cable Terminal Station'
    
    result = check_reverse_classification('CU10')
    assert result == 'Waste Management'
    
    result = check_reverse_classification('CU11')
    assert result == 'Telephone Box'
    
    result = check_reverse_classification('CU11OP')
    assert result == 'Other Public Telephones'
    
    result = check_reverse_classification('CU12')
    assert result == 'Dam'
    
    result = check_reverse_classification('CX')
    assert result == 'Emergency / Rescue Service'
    
    result = check_reverse_classification('CX01')
    assert result == 'Police / Transport Police / Station'
    
    result = check_reverse_classification('CX01PT')
    assert result == 'Police Training'
    
    result = check_reverse_classification('CX02')
    assert result == 'Fire Station'
    
    result = check_reverse_classification('CX02FT')
    assert result == 'Fire Service Training'
    
    result = check_reverse_classification('CX03')
    assert result == 'Ambulance Station'
    
    result = check_reverse_classification('CX03AA')
    assert result == 'Air Sea Rescue / Air Ambulance'
    
    result = check_reverse_classification('CX04')
    assert result == 'Lifeboat Services / Station'
    
    result = check_reverse_classification('CX05')
    assert result == 'Coastguard Rescue / Lookout / Station'
    
    result = check_reverse_classification('CX06')
    assert result == 'Mountain Rescue Station'
    
    result = check_reverse_classification('CX07')
    assert result == 'Lighthouse'
    
    result = check_reverse_classification('CX08')
    assert result == 'Police Box / Kiosk'
    
    result = check_reverse_classification('CZ')
    assert result == 'Information'
    
    result = check_reverse_classification('CZ01')
    assert result == 'Advertising Hoarding'
    
    result = check_reverse_classification('CZ02')
    assert result == 'Tourist Information Signage'
    
    result = check_reverse_classification('CZ02VI')
    assert result == 'Visitor Information'
    
    result = check_reverse_classification('CZ03')
    assert result == 'Traffic Information Signage'
    
    result = check_reverse_classification('L')
    assert result == 'Land'
    
    result = check_reverse_classification('LA')
    assert result == 'Agricultural - Applicable to land in farm ownership and not run as a separate business enterprise'
    
    result = check_reverse_classification('LA01')
    assert result == 'Grazing Land'
    
    result = check_reverse_classification('LA02')
    assert result == 'Permanent Crop / Crop Rotation'
    
    result = check_reverse_classification('LA02OC')
    assert result == 'Orchard'
    
    result = check_reverse_classification('LB')
    assert result == 'Ancillary Building'
    
    result = check_reverse_classification('LB99AV')
    assert result == 'Aviary / Dovecot / Cage'
    
    result = check_reverse_classification('LB99BD')
    assert result == 'Bandstand'
    
    result = check_reverse_classification('LB99PI')
    assert result == 'Pavilion / Changing Room'
    
    result = check_reverse_classification('LB99SV')
    assert result == 'Sports Viewing Structure'
    
    result = check_reverse_classification('LC')
    assert result == 'Burial Ground'
    
    result = check_reverse_classification('LC01')
    assert result == 'Historic / Disused Cemetery / Graveyard'
    
    result = check_reverse_classification('LD')
    assert result == 'Development'
    
    result = check_reverse_classification('LD01')
    assert result == 'Development Site'
    
    result = check_reverse_classification('LD01CC')
    assert result == 'Commercial Construction Site'
    
    result = check_reverse_classification('LD01CO')
    assert result == 'Community Construction Site'
    
    result = check_reverse_classification('LD01RN')
    assert result == 'Residential Construction Site'
    
    result = check_reverse_classification('LD01TC')
    assert result == 'Transport Construction Site'
    
    result = check_reverse_classification('LF')
    assert result == 'Forestry'
    
    result = check_reverse_classification('LF02')
    assert result == 'Forest / Arboretum / Pinetum (Managed / Unmanaged)'
    
    result = check_reverse_classification('LF02AU')
    assert result == 'Arboretum'
    
    result = check_reverse_classification('LF03')
    assert result == 'Woodland'
    
    result = check_reverse_classification('LL')
    assert result == 'Allotment'
    
    result = check_reverse_classification('LM')
    assert result == 'Amenity - Open areas not attracting visitors'
    
    result = check_reverse_classification('LM01')
    assert result == 'Landscaped Roundabout'
    
    result = check_reverse_classification('LM02')
    assert result == 'Verge / Central Reservation'
    
    result = check_reverse_classification('LM02NV')
    assert result == 'Natural Central Reservation'
    
    result = check_reverse_classification('LM02VE')
    assert result == 'Natural Verge'
    
    result = check_reverse_classification('LM03')
    assert result == 'Maintained Amenity Land'
    
    result = check_reverse_classification('LM04')
    assert result == 'Maintained Surfaced Area'
    
    result = check_reverse_classification('LM04MV')
    assert result == 'Made Central Reservation'
    
    result = check_reverse_classification('LM04PV')
    assert result == 'Pavement'
    
    result = check_reverse_classification('LO')
    assert result == 'Open Space'
    
    result = check_reverse_classification('LO01')
    assert result == 'Heath / Moorland'
    
    result = check_reverse_classification('LP')
    assert result == 'Park'
    
    result = check_reverse_classification('LP01')
    assert result == 'Public Park / Garden'
    
    result = check_reverse_classification('LP02')
    assert result == 'Public Open Space / Nature Reserve'
    
    result = check_reverse_classification('LP03')
    assert result == 'Playground'
    
    result = check_reverse_classification('LP03PA')
    assert result == 'Play Area'
    
    result = check_reverse_classification('LP03PD')
    assert result == 'Paddling Pool'
    
    result = check_reverse_classification('LP04')
    assert result == 'Private Park / Garden'
    
    result = check_reverse_classification('LU')
    assert result == 'Unused Land'
    
    result = check_reverse_classification('LU01')
    assert result == 'Vacant / Derelict Land'
    
    result = check_reverse_classification('LW')
    assert result == 'Water'
    
    result = check_reverse_classification('LW01')
    assert result == 'Lake / Reservoir'
    
    result = check_reverse_classification('LW01BP')
    assert result == 'Balancing Pond'
    
    result = check_reverse_classification('LW01BV')
    assert result == 'Buried Reservoir'
    
    result = check_reverse_classification('LW02')
    assert result == 'Named Pond'
    
    result = check_reverse_classification('LW02DE')
    assert result == 'Dew Pond'
    
    result = check_reverse_classification('LW02DP')
    assert result == 'Decoy Pond'
    
    result = check_reverse_classification('LW02IW')
    assert result == 'Static Water'
    
    result = check_reverse_classification('LW03')
    assert result == 'Waterway'
    
    result = check_reverse_classification('LW03LR')
    assert result == 'Leats / Races'
    
    result = check_reverse_classification('LW03DR')
    assert result == 'Drain'
    
    result = check_reverse_classification('M')
    assert result == 'Military'
    
    result = check_reverse_classification('MA')
    assert result == 'Army'
    
    result = check_reverse_classification('MA99AR')
    assert result == 'Army Military Range'
    
    result = check_reverse_classification('MA99AS')
    assert result == 'Army Site'
    
    result = check_reverse_classification('MA99AT')
    assert result == 'Army Military Training'
    
    result = check_reverse_classification('MA99AG')
    assert result == 'Army Military Storage'
    
    result = check_reverse_classification('MB')
    assert result == 'Ancillary Building'
    
    result = check_reverse_classification('MB99TG')
    assert result == 'Military Target'
    
    result = check_reverse_classification('MF')
    assert result == 'Air Force'
    
    result = check_reverse_classification('MF99UG')
    assert result == 'Air Force Military Storage'
    
    result = check_reverse_classification('MF99UR')
    assert result == 'Air Force Military Range'
    
    result = check_reverse_classification('MF99US')
    assert result == 'Air Force Site'
    
    result = check_reverse_classification('MF99UT')
    assert result == 'Air Force Military Training'
    
    result = check_reverse_classification('MG')
    assert result == 'Defence Estates'
    
    result = check_reverse_classification('MN')
    assert result == 'Navy'
    
    result = check_reverse_classification('MN99VG')
    assert result == 'Naval Military Storage'
    
    result = check_reverse_classification('MN99VR')
    assert result == 'Naval Military Range'
    
    result = check_reverse_classification('MN99VS')
    assert result == 'Naval Site'
    
    result = check_reverse_classification('MN99VT')
    assert result == 'Naval Military Training'
    
    result = check_reverse_classification('O')
    assert result == 'Other (Ordnance Survey Only)'
    
    result = check_reverse_classification('OA')
    assert result == 'Aid To Navigation'
    
    result = check_reverse_classification('OA01')
    assert result == 'Aid To Aeronautical Navigation'
    
    result = check_reverse_classification('OA01AL')
    assert result == 'Aeronautical Navigation Beacon / Light'
    
    result = check_reverse_classification('OA01LL')
    assert result == 'Landing Light'
    
    result = check_reverse_classification('OA01SQ')
    assert result == 'Signal Square'
    
    result = check_reverse_classification('OA01WK')
    assert result == 'Wind Sock / Wind Tee'
    
    result = check_reverse_classification('OA02')
    assert result == 'Aid To Nautical Navigation'
    
    result = check_reverse_classification('OA02DM')
    assert result == 'Daymark'
    
    result = check_reverse_classification('OA02FG')
    assert result == 'Fog Horn Warning'
    
    result = check_reverse_classification('OA02NL')
    assert result == 'Nautical Navigation Beacon / Light'
    
    result = check_reverse_classification('OA03')
    assert result == 'Aid To Road Navigation'
    
    result = check_reverse_classification('OA03GP')
    assert result == 'Guide Post'
    
    result = check_reverse_classification('OC')
    assert result == 'Coastal Protection / Flood Prevention'
    
    result = check_reverse_classification('OC01')
    assert result == 'Boulder Wall / Sea Wall'
    
    result = check_reverse_classification('OC02')
    assert result == 'Flood Gate / Flood Sluice Gate / Flood Valve'
    
    result = check_reverse_classification('OC03')
    assert result == 'Groyne'
    
    result = check_reverse_classification('OC04')
    assert result == 'Rip-Rap'
    
    result = check_reverse_classification('OE')
    assert result == 'Emergency Support'
    
    result = check_reverse_classification('OE01')
    assert result == 'Beach Office / First Aid Facility'
    
    result = check_reverse_classification('OE02')
    assert result == 'Emergency Telephone (Non Motorway)'
    
    result = check_reverse_classification('OE03')
    assert result == 'Fire Alarm Structure / Fire Observation Tower / Fire Beater Facility'
    
    result = check_reverse_classification('OE04')
    assert result == 'Emergency Equipment Point / Emergency Siren / Warning Flag'
    
    result = check_reverse_classification('OE05')
    assert result == 'Lifeguard Facility'
    
    result = check_reverse_classification('OE06')
    assert result == 'Life / Belt / Buoy / Float / Jacket / Safety Rope'
    
    result = check_reverse_classification('OF')
    assert result == 'Street Furniture'
    
    result = check_reverse_classification('OG')
    assert result == 'Agricultural Support Objects'
    
    result = check_reverse_classification('OG01')
    assert result == 'Fish Ladder / Lock / Pen / Trap'
    
    result = check_reverse_classification('OG02')
    assert result == 'Livestock Pen / Dip'
    
    result = check_reverse_classification('OG03')
    assert result == 'Currick'
    
    result = check_reverse_classification('OG04')
    assert result == 'Slurry Bed / Pit'
    
    result = check_reverse_classification('OH')
    assert result == 'Historical Site / Object'
    
    result = check_reverse_classification('OH01')
    assert result == 'Historic Structure / Object'
    
    result = check_reverse_classification('OI')
    assert result == 'Industrial Support'
    
    result = check_reverse_classification('OI01')
    assert result == 'Adit / Incline / Level'
    
    result = check_reverse_classification('OI02')
    assert result == 'Caisson / Dry Dock / Grid'
    
    result = check_reverse_classification('OI03')
    assert result == 'Channel / Conveyor / Conduit / Pipe'
    
    result = check_reverse_classification('OI04')
    assert result == 'Chimney / Flue'
    
    result = check_reverse_classification('OI05')
    assert result == 'Crane / Hoist / Winch / Material Elevator'
    
    result = check_reverse_classification('OI06')
    assert result == 'Flare Stack'
    
    result = check_reverse_classification('OI07')
    assert result == 'Hopper / Silo / Cistern / Tank'
    
    result = check_reverse_classification('OI08')
    assert result == 'Grab / Skip / Other Industrial Waste Machinery / Discharging'
    
    result = check_reverse_classification('OI09')
    assert result == 'Kiln / Oven / Smelter'
    
    result = check_reverse_classification('OI10')
    assert result == 'Manhole / Shaft'
    
    result = check_reverse_classification('OI11')
    assert result == 'Industrial Overflow / Sluice / Valve / Valve Housing'
    
    result = check_reverse_classification('OI12')
    assert result == 'Cooling Tower'
    
    result = check_reverse_classification('OI13')
    assert result == 'Solar Panel / Waterwheel'
    
    result = check_reverse_classification('OI14')
    assert result == 'Telephone Pole / Post'
    
    result = check_reverse_classification('OI15')
    assert result == 'Electricity Distribution Pole / Pylon'
    
    result = check_reverse_classification('ON')
    assert result == 'Significant Natural Object'
    
    result = check_reverse_classification('ON01')
    assert result == 'Boundary / Significant / Historic Tree / Pollard'
    
    result = check_reverse_classification('ON02')
    assert result == 'Boundary / Significant Rock / Boulder'
    
    result = check_reverse_classification('ON03')
    assert result == 'Natural Hole (Blow / Shake / Swallow)'
    
    result = check_reverse_classification('OO')
    assert result == 'Ornamental / Cultural Object'
    
    result = check_reverse_classification('OO02')
    assert result == 'Mausoleum / Tomb / Grave'
    
    result = check_reverse_classification('OO03')
    assert result == 'Simple Ornamental Object'
    
    result = check_reverse_classification('OO04')
    assert result == 'Maze'
    
    result = check_reverse_classification('OP')
    assert result == 'Sport / Leisure Support'
    
    result = check_reverse_classification('OP01')
    assert result == 'Butt / Hide'
    
    result = check_reverse_classification('OP02')
    assert result == 'Gallop / Ride'
    
    result = check_reverse_classification('OP03')
    assert result == 'Miniature Railway'
    
    result = check_reverse_classification('OR')
    assert result == 'Royal Mail Infrastructure'
    
    result = check_reverse_classification('OR01')
    assert result == 'Postal Box'
    
    result = check_reverse_classification('OR02')
    assert result == 'Postal Delivery Box / Pouch'
    
    result = check_reverse_classification('OR03')
    assert result == 'PO Box'
    
    result = check_reverse_classification('OR04')
    assert result == 'Additional Mail / Packet Addressee'
    
    result = check_reverse_classification('OS')
    assert result == 'Scientific / Observation Support'
    
    result = check_reverse_classification('OS01')
    assert result == 'Meteorological Station / Equipment'
    
    result = check_reverse_classification('OS02')
    assert result == 'Radar / Satellite Infrastructure'
    
    result = check_reverse_classification('OS03')
    assert result == 'Telescope / Observation Infrastructure / Astronomy'
    
    result = check_reverse_classification('OT')
    assert result == 'Transport Support'
    
    result = check_reverse_classification('OT01')
    assert result == 'Cattle Grid / Ford'
    
    result = check_reverse_classification('OT02')
    assert result == 'Elevator / Escalator / Steps'
    
    result = check_reverse_classification('OT03')
    assert result == 'Footbridge / Walkway'
    
    result = check_reverse_classification('OT04')
    assert result == 'Pole / Post / Bollard (Restricting Vehicular Access)'
    
    result = check_reverse_classification('OT05')
    assert result == 'Subway / Underpass'
    
    result = check_reverse_classification('OT06')
    assert result == 'Customs Inspection Facility'
    
    result = check_reverse_classification('OT07')
    assert result == 'Lay-By'
    
    result = check_reverse_classification('OT08')
    assert result == 'Level Crossing'
    
    result = check_reverse_classification('OT09')
    assert result == 'Mail Pick Up'
    
    result = check_reverse_classification('OT10')
    assert result == 'Railway Pedestrian Crossing'
    
    result = check_reverse_classification('OT11')
    assert result == 'Railway Buffer'
    
    result = check_reverse_classification('OT12')
    assert result == 'Rail Drag'
    
    result = check_reverse_classification('OT13')
    assert result == 'Rail Infrastructure Services'
    
    result = check_reverse_classification('OT14')
    assert result == 'Rail Kilometre Distance Marker'
    
    result = check_reverse_classification('OT15')
    assert result == 'Railway Lighting'
    
    result = check_reverse_classification('OT16')
    assert result == 'Rail Mile Distance Marker'
    
    result = check_reverse_classification('OT17')
    assert result == 'Railway Turntable'
    
    result = check_reverse_classification('OT18')
    assert result == 'Rail Weighbridge'
    
    result = check_reverse_classification('OT19')
    assert result == 'Rail Signalling'
    
    result = check_reverse_classification('OT20')
    assert result == 'Railway Traverse'
    
    result = check_reverse_classification('OT21')
    assert result == 'Goods Tramway'
    
    result = check_reverse_classification('OT22')
    assert result == 'Road Drag'
    
    result = check_reverse_classification('OT23')
    assert result == 'Vehicle Dip'
    
    result = check_reverse_classification('OT24')
    assert result == 'Road Turntable'
    
    result = check_reverse_classification('OT25')
    assert result == 'Road Mile Distance Marker'
    
    result = check_reverse_classification('OT26')
    assert result == 'Road Kilometre Distance Marker'
    
    result = check_reverse_classification('OT27')
    assert result == 'Road Infrastructure Services'
    
    result = check_reverse_classification('OU')
    assert result == 'Unsupported Site'
    
    result = check_reverse_classification('OU01')
    assert result == 'Cycle Parking Facility'
    
    result = check_reverse_classification('OU04')
    assert result == 'Picnic / Barbeque Site'
    
    result = check_reverse_classification('OU05')
    assert result == 'Travelling Persons Site'
    
    result = check_reverse_classification('OU08')
    assert result == 'Shelter (Not Including Bus Shelter)'
    
    result = check_reverse_classification('P')
    assert result == 'Parent Shell'
    
    result = check_reverse_classification('PP')
    assert result == 'Property Shell'
    
    result = check_reverse_classification('PS')
    assert result == 'Street Record'
    
    result = check_reverse_classification('R')
    assert result == 'Residential'
    
    result = check_reverse_classification('RB')
    assert result == 'Ancillary Building'
    
    result = check_reverse_classification('RC')
    assert result == 'Car Park Space'
    
    result = check_reverse_classification('RC01')
    assert result == 'Allocated Parking'
    
    result = check_reverse_classification('RD')
    assert result == 'Dwelling'
    
    result = check_reverse_classification('RD01')
    assert result == 'Caravan'
    
    result = check_reverse_classification('RD02')
    assert result == 'Detached'
    
    result = check_reverse_classification('RD03')
    assert result == 'Semi-Detached'
    
    result = check_reverse_classification('RD04')
    assert result == 'Terraced'
    
    result = check_reverse_classification('RD06')
    assert result == 'Self Contained Flat (Includes Maisonette / Apartment)'
    
    result = check_reverse_classification('RD07')
    assert result == 'House Boat'
    
    result = check_reverse_classification('RD08')
    assert result == 'Sheltered Accommodation'
    
    result = check_reverse_classification('RD10')
    assert result == 'Privately Owned Holiday Caravan / Chalet'
    
    result = check_reverse_classification('RG')
    assert result == 'Garage'
    
    result = check_reverse_classification('RG02')
    assert result == 'Lock-Up Garage / Garage Court'
    
    result = check_reverse_classification('RH')
    assert result == 'House In Multiple Occupation'
    
    result = check_reverse_classification('RH01')
    assert result == 'HMO Parent'
    
    result = check_reverse_classification('RH02')
    assert result == 'HMO Bedsit / Other Non Self Contained Accommodation'
    
    result = check_reverse_classification('RH03')
    assert result == 'HMO Not Further Divided'
    
    result = check_reverse_classification('RI')
    assert result == 'Residential Institution'
    
    result = check_reverse_classification('RI01')
    assert result == 'Care / Nursing Home'
    
    result = check_reverse_classification('RI02')
    assert result == 'Communal Residence'
    
    result = check_reverse_classification('RI02NC')
    assert result == 'Non-Commercial Lodgings'
    
    result = check_reverse_classification('RI02RC')
    assert result == 'Religious Community'
    
    result = check_reverse_classification('RI03')
    assert result == 'Residential Education'
    
    result = check_reverse_classification('U')
    assert result == 'Unclassified'
    
    result = check_reverse_classification('UC')
    assert result == 'Awaiting Classification'
    
    result = check_reverse_classification('UP')
    assert result == 'Pending Internal Investigation'
    
    result = check_reverse_classification('X')
    assert result == 'Dual Use'
    
    result = check_reverse_classification('Z')
    assert result == 'Object of Interest'
    
    result = check_reverse_classification('ZA')
    assert result == 'Archaeological Dig Site'
    
    result = check_reverse_classification('ZM')
    assert result == 'Monument'
    
    result = check_reverse_classification('ZM01')
    assert result == 'Obelisk / Milestone / Standing Stone'
    
    result = check_reverse_classification('ZM01OB')
    assert result == 'Obelisk'
    
    result = check_reverse_classification('ZM01ST')
    assert result == 'Standing Stone'
    
    result = check_reverse_classification('ZM02')
    assert result == 'Memorial / Market Cross'
    
    result = check_reverse_classification('ZM03')
    assert result == 'Statue'
    
    result = check_reverse_classification('ZM04')
    assert result == 'Castle / Historic Ruin'
    
    result = check_reverse_classification('ZM05')
    assert result == 'Other Structure'
    
    result = check_reverse_classification('ZM05BS')
    assert result == 'Boundary Stone'
    
    result = check_reverse_classification('ZM05PN')
    assert result == 'Permanent Art Display / Sculpture'
    
    result = check_reverse_classification('ZM05CE')
    assert result == 'Cascade / Fountain'
    
    result = check_reverse_classification('ZM05WI')
    assert result == 'Windmill (Inactive)'
    
    result = check_reverse_classification('ZS')
    assert result == 'Stately Home'
    
    result = check_reverse_classification('ZU')
    assert result == 'Underground Feature'
    
    result = check_reverse_classification('ZU01')
    assert result == 'Cave'
    
    result = check_reverse_classification('ZU04')
    assert result == 'Pothole / Natural Hole'
    
    result = check_reverse_classification('ZV')
    assert result == 'Other Underground Feature'
    
    result = check_reverse_classification('ZV01')
    assert result == 'Cellar'
    
    result = check_reverse_classification('ZV02')
    assert result == 'Disused Mine'
    
    result = check_reverse_classification('ZV02MI')
    assert result == 'Mineral Mining / Inactive'
    
    result = check_reverse_classification('ZV02OI')
    assert result == 'Oil And / Gas Extraction/ Inactive'
    
    result = check_reverse_classification('ZV02QI')
    assert result == 'Mineral Quarrying And / Open Extraction / Inactive'
    
    result = check_reverse_classification('ZV03')
    assert result == 'Well / Spring'
    
    result = check_reverse_classification('ZV03SG')
    assert result == 'Spring'
    
    result = check_reverse_classification('ZV03WL')
    assert result == 'Well'
    
    result = check_reverse_classification('ZW')
    assert result == 'Place Of Worship'
    
    result = check_reverse_classification('ZW99AB')
    assert result == 'Abbey'
    
    result = check_reverse_classification('ZW99CA')
    assert result == 'Cathedral'
    
    result = check_reverse_classification('ZW99CH')
    assert result == 'Church'
    
    result = check_reverse_classification('ZW99CP')
    assert result == 'Chapel'
    
    result = check_reverse_classification('ZW99GU')
    assert result == 'Gurdwara'
    
    result = check_reverse_classification('ZW99KH')
    assert result == 'Kingdom Hall'
    
    result = check_reverse_classification('ZW99MQ')
    assert result == 'Mosque'
    
    result = check_reverse_classification('ZW99MT')
    assert result == 'Minster'
    
    result = check_reverse_classification('ZW99SU')
    assert result == 'Stupa'
    
    result = check_reverse_classification('ZW99SY')
    assert result == 'Synagogue'
    
    result = check_reverse_classification('ZW99TP')
    assert result == 'Temple'
    
    result = check_reverse_classification('ZW99LG')
    assert result == 'Lych Gate'

