
from aims_ui.page_helpers.classification_utilities import check_reverse_classification


def test_check_reverse_classification():
  """ Check that the classification can be obtained from the string value """

  result = check_reverse_classification('Commercial')
  assert result == 'C*'

  result = check_reverse_classification('Agricultural')
  assert result == 'CA*'

  result = check_reverse_classification(
      'Farm / Non-Residential Associated Building')
  assert result == 'CA01*'

  result = check_reverse_classification('Fishery')
  assert result == 'CA02*'

  result = check_reverse_classification('Fish Farming')
  assert result == 'CA02FF*'

  result = check_reverse_classification('Fish Hatchery')
  assert result == 'CA02FH*'

  result = check_reverse_classification('Fish Processing')
  assert result == 'CA02FP*'

  result = check_reverse_classification('Oyster / Mussel Bed')
  assert result == 'CA02OY*'

  result = check_reverse_classification('Horticulture')
  assert result == 'CA03*'

  result = check_reverse_classification('Smallholding')
  assert result == 'CA03SH*'

  result = check_reverse_classification('Vineyard')
  assert result == 'CA03VY*'

  result = check_reverse_classification('Watercress Bed')
  assert result == 'CA03WB*'

  result = check_reverse_classification('Slaughter House / Abattoir')
  assert result == 'CA04*'

  result = check_reverse_classification('Community Services')
  assert result == 'CC*'

  result = check_reverse_classification('Law Court')
  assert result == 'CC02*'

  result = check_reverse_classification('Prison')
  assert result == 'CC03*'

  result = check_reverse_classification('HM Detention Centre')
  assert result == 'CC03HD*'

  result = check_reverse_classification('HM Prison Service')
  assert result == 'CC03PR*'

  result = check_reverse_classification('Secure Residential Accommodation')
  assert result == 'CC03SC*'

  result = check_reverse_classification(
      'Public / Village Hall / Other Community Facility')
  assert result == 'CC04*'

  result = check_reverse_classification('Youth Recreational / Social Club')
  assert result == 'CC04YR*'

  result = check_reverse_classification('Public Convenience')
  assert result == 'CC05*'

  result = check_reverse_classification(
      'Cemetery / Crematorium / Graveyard. In Current Use.')
  assert result == 'CC06*'

  result = check_reverse_classification('Columbarium')
  assert result == 'CC06CB*'

  result = check_reverse_classification('Chapel Of Rest')
  assert result == 'CC06CR*'

  result = check_reverse_classification('Crematorium')
  assert result == 'CC06CN*'

  result = check_reverse_classification('Cemetery')
  assert result == 'CC06CY*'

  result = check_reverse_classification('Military Cemetery')
  assert result == 'CC06MC*'

  result = check_reverse_classification('Mortuary')
  assert result == 'CC06MY*'

  result = check_reverse_classification(
      'Church Hall / Religious Meeting Place / Hall')
  assert result == 'CC07*'

  result = check_reverse_classification('Community Service Centre / Office')
  assert result == 'CC08*'

  result = check_reverse_classification(
      'Public Household Waste Recycling Centre (HWRC)')
  assert result == 'CC09*'

  result = check_reverse_classification('Recycling Site')
  assert result == 'CC10*'

  result = check_reverse_classification('CCTV')
  assert result == 'CC11*'

  result = check_reverse_classification('Job Centre')
  assert result == 'CC12*'

  result = check_reverse_classification('Education')
  assert result == 'CE*'

  result = check_reverse_classification('College')
  assert result == 'CE01*'

  result = check_reverse_classification('Further Education')
  assert result == 'CE01FE*'

  result = check_reverse_classification('Higher Education')
  assert result == 'CE01HE*'

  result = check_reverse_classification("Children''s Nursery / Crèche")
  assert result == 'CE02*'

  result = check_reverse_classification(
      'Preparatory / First / Primary / Infant / Junior / Middle School')
  assert result == 'CE03*'

  result = check_reverse_classification('First School')
  assert result == 'CE03FS*'

  result = check_reverse_classification('Infant School')
  assert result == 'CE03IS*'

  result = check_reverse_classification('Junior School')
  assert result == 'CE03JS*'

  result = check_reverse_classification('Middle School')
  assert result == 'CE03MS*'

  result = check_reverse_classification(
      'Non State Primary / Preparatory School')
  assert result == 'CE03NP*'

  result = check_reverse_classification('Primary School')
  assert result == 'CE03PS*'

  result = check_reverse_classification('Secondary / High School')
  assert result == 'CE04*'

  result = check_reverse_classification('Non State Secondary School')
  assert result == 'CE04NS*'

  result = check_reverse_classification('Secondary School')
  assert result == 'CE04SS*'

  result = check_reverse_classification('University')
  assert result == 'CE05*'

  result = check_reverse_classification('Special Needs Establishment.')
  assert result == 'CE06*'

  result = check_reverse_classification('Other Educational Establishment')
  assert result == 'CE07*'

  result = check_reverse_classification(
      'Hotel / Motel / Boarding / Guest House')
  assert result == 'CH*'

  result = check_reverse_classification(
      'Boarding / Guest House / Bed And Breakfast / Youth Hostel')
  assert result == 'CH01*'

  result = check_reverse_classification('Youth Hostel')
  assert result == 'CH01YH*'

  result = check_reverse_classification(
      'Holiday Let/Accomodation/Short-Term Let Other Than CH01')
  assert result == 'CH02*'

  result = check_reverse_classification('Hotel/Motel')
  assert result == 'CH03*'

  result = check_reverse_classification(
      'Industrial Applicable to manufacturing, engineering, maintenance, storage / wholesale distribution and extraction sites'
  )
  assert result == 'CI*'

  result = check_reverse_classification('Factory/Manufacturing')
  assert result == 'CI01*'

  result = check_reverse_classification('Aircraft Works')
  assert result == 'CI01AW*'

  result = check_reverse_classification('Boat Building')
  assert result == 'CI01BB*'

  result = check_reverse_classification('Brick Works')
  assert result == 'CI01BR*'

  result = check_reverse_classification('Brewery')
  assert result == 'CI01BW*'

  result = check_reverse_classification('Cider Manufacture')
  assert result == 'CI01CD*'

  result = check_reverse_classification('Chemical Works')
  assert result == 'CI01CM*'

  result = check_reverse_classification('Cement Works')
  assert result == 'CI01CW*'

  result = check_reverse_classification('Dairy Processing')
  assert result == 'CI01DA*'

  result = check_reverse_classification('Distillery')
  assert result == 'CI01DY*'

  result = check_reverse_classification('Flour Mill')
  assert result == 'CI01FL*'

  result = check_reverse_classification('Food Processing')
  assert result == 'CI01FO*'

  result = check_reverse_classification('Glassworks')
  assert result == 'CI01GW*'

  result = check_reverse_classification('Manufacturing')
  assert result == 'CI01MG*'

  result = check_reverse_classification('Oast House')
  assert result == 'CI01OH*'

  result = check_reverse_classification('Oil Refining')
  assert result == 'CI01OR*'

  result = check_reverse_classification('Pottery Manufacturing')
  assert result == 'CI01PG*'

  result = check_reverse_classification('Paper Mill')
  assert result == 'CI01PM*'

  result = check_reverse_classification('Printing Works')
  assert result == 'CI01PW*'

  result = check_reverse_classification('Shipyard')
  assert result == 'CI01YD*'

  result = check_reverse_classification('Sugar Refinery')
  assert result == 'CI01SR*'

  result = check_reverse_classification('Steel Works')
  assert result == 'CI01SW*'

  result = check_reverse_classification('Timber Mill')
  assert result == 'CI01TL*'

  result = check_reverse_classification('Winery')
  assert result == 'CI01WN*'

  result = check_reverse_classification(
      'Mineral / Ore Working / Quarry / Mine')
  assert result == 'CI02*'

  result = check_reverse_classification('Mineral Mining / Active')
  assert result == 'CI02MA*'

  result = check_reverse_classification('Mineral Distribution / Storage')
  assert result == 'CI02MD*'

  result = check_reverse_classification('Mineral Processing')
  assert result == 'CI02MP*'

  result = check_reverse_classification('Oil / Gas Extraction / Active')
  assert result == 'CI02OA*'

  result = check_reverse_classification(
      'Mineral Quarrying / Open Extraction / Active')
  assert result == 'CI02QA*'

  result = check_reverse_classification('Workshop / Light Industrial')
  assert result == 'CI03*'

  result = check_reverse_classification('Servicing Garage')
  assert result == 'CI03GA*'

  result = check_reverse_classification('Warehouse / Store / Storage Depot')
  assert result == 'CI04*'

  result = check_reverse_classification('Crop Handling / Storage')
  assert result == 'CI04CS*'

  result = check_reverse_classification('Postal Sorting / Distribution')
  assert result == 'CI04PL*'

  result = check_reverse_classification('Solid Fuel Storage')
  assert result == 'CI04SO*'

  result = check_reverse_classification('Timber Storage')
  assert result == 'CI04TS*'

  result = check_reverse_classification('Wholesale Distribution')
  assert result == 'CI05*'

  result = check_reverse_classification('Solid Fuel Distribution')
  assert result == 'CI05SF*'

  result = check_reverse_classification('Timber Distribution')
  assert result == 'CI05TD*'

  result = check_reverse_classification('Recycling Plant')
  assert result == 'CI06*'

  result = check_reverse_classification('Incinerator / Waste Transfer Station')
  assert result == 'CI07*'

  result = check_reverse_classification('Maintenance Depot')
  assert result == 'CI08*'

  result = check_reverse_classification(
      'Leisure - Applicable to recreational sites and enterprises')
  assert result == 'CL*'

  result = check_reverse_classification('Amusements')
  assert result == 'CL01*'

  result = check_reverse_classification('Leisure Pier')
  assert result == 'CL01LP*'

  result = check_reverse_classification('Holiday / Campsite')
  assert result == 'CL02*'

  result = check_reverse_classification('Camping')
  assert result == 'CL02CG*'

  result = check_reverse_classification('Caravanning')
  assert result == 'CL02CV*'

  result = check_reverse_classification('Holiday Accommodation')
  assert result == 'CL02HA*'

  result = check_reverse_classification('Holiday Centre')
  assert result == 'CL02HO*'

  result = check_reverse_classification('Youth Organisation Camp')
  assert result == 'CL02YC*'

  result = check_reverse_classification('Library')
  assert result == 'CL03*'

  result = check_reverse_classification('Reading Room')
  assert result == 'CL03RR*'

  result = check_reverse_classification('Museum / Gallery')
  assert result == 'CL04*'

  result = check_reverse_classification('Art Centre / Gallery')
  assert result == 'CL04AC*'

  result = check_reverse_classification('Aviation Museum')
  assert result == 'CL04AM*'

  result = check_reverse_classification('Heritage Centre')
  assert result == 'CL04HG*'

  result = check_reverse_classification('Industrial Museum')
  assert result == 'CL04IM*'

  result = check_reverse_classification('Military Museum')
  assert result == 'CL04MM*'

  result = check_reverse_classification('Science Museum')
  assert result == 'CL04SM*'

  result = check_reverse_classification('Transport Museum')
  assert result == 'CL04TM*'

  result = check_reverse_classification('Maritime Museum')
  assert result == 'CL04NM*'

  result = check_reverse_classification(
      'Indoor / Outdoor Leisure / Sporting Activity / Centre')
  assert result == 'CL06*'

  result = check_reverse_classification('Athletics Facility')
  assert result == 'CL06AH*'

  result = check_reverse_classification('Bowls Facility')
  assert result == 'CL06BF*'

  result = check_reverse_classification('Cricket Facility')
  assert result == 'CL06CK*'

  result = check_reverse_classification('Curling Facility')
  assert result == 'CL06CU*'

  result = check_reverse_classification('Cycling Sports Facility')
  assert result == 'CL06YF*'

  result = check_reverse_classification('Diving / Swimming Facility')
  assert result == 'CL06DS*'

  result = check_reverse_classification('Equestrian Sports Facility')
  assert result == 'CL06EQ*'

  result = check_reverse_classification('Football Facility')
  assert result == 'CL06FB*'

  result = check_reverse_classification('Fishing / Angling Facility')
  assert result == 'CL06FI*'

  result = check_reverse_classification('Golf Facility')
  assert result == 'CL06GF*'

  result = check_reverse_classification('Gliding Facility')
  assert result == 'CL06GL*'

  result = check_reverse_classification('Greyhound Racing Facility')
  assert result == 'CL06GR*'

  result = check_reverse_classification('Hockey Facility')
  assert result == 'CL06HF*'

  result = check_reverse_classification('Horse Racing Facility')
  assert result == 'CL06HR*'

  result = check_reverse_classification('Historic Vessel / Aircraft / Vehicle')
  assert result == 'CL06HV*'

  result = check_reverse_classification('Activity / Leisure / Sports Centre')
  assert result == 'CL06LS*'

  result = check_reverse_classification('Model Sports Facility')
  assert result == 'CL06ME*'

  result = check_reverse_classification('Motor Sports Facility')
  assert result == 'CL06MF*'

  result = check_reverse_classification('Playing Field')
  assert result == 'CL06PF*'

  result = check_reverse_classification('Racquet Sports Facility')
  assert result == 'CL06QS*'

  result = check_reverse_classification('Rugby Facility')
  assert result == 'CL06RF*'

  result = check_reverse_classification('Recreation Ground')
  assert result == 'CL06RG*'

  result = check_reverse_classification('Shinty Facility')
  assert result == 'CL06SI*'

  result = check_reverse_classification('Skateboarding Facility')
  assert result == 'CL06SK*'

  result = check_reverse_classification('Civilian Firing Facility')
  assert result == 'CL06SX*'

  result = check_reverse_classification('Tenpin Bowling Facility')
  assert result == 'CL06TB*'

  result = check_reverse_classification('Public Tennis Court')
  assert result == 'CL06TN*'

  result = check_reverse_classification('Water Sports Facility')
  assert result == 'CL06WA*'

  result = check_reverse_classification('Winter Sports Facility')
  assert result == 'CL06WP*'

  result = check_reverse_classification('Wildlife Sports Facility')
  assert result == 'CL06WY*'

  result = check_reverse_classification(
      'Bingo Hall / Cinema / Conference / Exhibition Centre / Theatre / Concert Hall'
  )
  assert result == 'CL07*'

  result = check_reverse_classification('Theatre')
  assert result == 'CL07TH*'

  result = check_reverse_classification('Cinema')
  assert result == 'CL07CI*'

  result = check_reverse_classification('Entertainment Complex')
  assert result == 'CL07EN*'

  result = check_reverse_classification('Conference / Exhibition Centre')
  assert result == 'CL07EX*'

  result = check_reverse_classification('Zoo / Theme Park')
  assert result == 'CL08*'

  result = check_reverse_classification('Amusement Park')
  assert result == 'CL08AK*'

  result = check_reverse_classification('Model Village Site')
  assert result == 'CL08MX*'

  result = check_reverse_classification('Wildlife / Zoological Park')
  assert result == 'CL08WZ*'

  result = check_reverse_classification('Aquatic Attraction')
  assert result == 'CL08AQ*'

  result = check_reverse_classification(
      'Beach Hut (Recreational, Non-Residential Use Only)')
  assert result == 'CL09*'

  result = check_reverse_classification('Licensed Private Members Club')
  assert result == 'CL10*'

  result = check_reverse_classification('Recreational / Social Club')
  assert result == 'CL10RE*'

  result = check_reverse_classification('Arena / Stadium')
  assert result == 'CL11*'

  result = check_reverse_classification('Stadium')
  assert result == 'CL11SD*'

  result = check_reverse_classification('Showground')
  assert result == 'CL11SJ*'

  result = check_reverse_classification('Medical')
  assert result == 'CM*'

  result = check_reverse_classification('Dentist')
  assert result == 'CM01*'

  result = check_reverse_classification('General Practice Surgery / Clinic')
  assert result == 'CM02*'

  result = check_reverse_classification('Health Care Services')
  assert result == 'CM02HL*'

  result = check_reverse_classification('Health Centre')
  assert result == 'CM02HC*'

  result = check_reverse_classification('Hospital / Hospice')
  assert result == 'CM03*'

  result = check_reverse_classification('Hospice')
  assert result == 'CM03HI*'

  result = check_reverse_classification('Hospital')
  assert result == 'CM03HP*'

  result = check_reverse_classification(
      'Medical / Testing / Research Laboratory')
  assert result == 'CM04*'

  result = check_reverse_classification('Professional Medical Service')
  assert result == 'CM05*'

  result = check_reverse_classification('Assessment / Development Services')
  assert result == 'CM05ZS*'

  result = check_reverse_classification('Animal Centre')
  assert result == 'CN*'

  result = check_reverse_classification('Cattery / Kennel')
  assert result == 'CN01*'

  result = check_reverse_classification('Animal Services')
  assert result == 'CN02*'

  result = check_reverse_classification('Animal Quarantining')
  assert result == 'CN02AX*'

  result = check_reverse_classification('Equestrian')
  assert result == 'CN03*'

  result = check_reverse_classification('Horse Racing / Breeding Stable')
  assert result == 'CN03HB*'

  result = check_reverse_classification('Commercial Stabling / Riding')
  assert result == 'CN03SB*'

  result = check_reverse_classification('Vet / Animal Medical Treatment')
  assert result == 'CN04*'

  result = check_reverse_classification('Animal / Bird / Marine Sanctuary')
  assert result == 'CN05*'

  result = check_reverse_classification('Animal Sanctuary')
  assert result == 'CN05AN*'

  result = check_reverse_classification('Marine Sanctuary')
  assert result == 'CN05MR*'

  result = check_reverse_classification('Office')
  assert result == 'CO*'

  result = check_reverse_classification('Office / Work Studio')
  assert result == 'CO01*'

  result = check_reverse_classification(
      'Embassy / High Commission / Consulate')
  assert result == 'CO01EM*'

  result = check_reverse_classification('Film Studio')
  assert result == 'CO01FM*'

  result = check_reverse_classification('Central Government Service')
  assert result == 'CO01GV*'

  result = check_reverse_classification('Local Government Service')
  assert result == 'CO01LG*'

  result = check_reverse_classification('Broadcasting (TV / Radio)')
  assert result == 'CO02*'

  result = check_reverse_classification('Retail')
  assert result == 'CR*'

  result = check_reverse_classification('Bank / Financial Service')
  assert result == 'CR01*'

  result = check_reverse_classification('Retail Service Agent')
  assert result == 'CR02*'

  result = check_reverse_classification('Post Office')
  assert result == 'CR02PO*'

  result = check_reverse_classification('Market (Indoor / Outdoor)')
  assert result == 'CR04*'

  result = check_reverse_classification('Fish Market')
  assert result == 'CR04FK*'

  result = check_reverse_classification('Fruit / Vegetable Market')
  assert result == 'CR04FV*'

  result = check_reverse_classification('Livestock Market')
  assert result == 'CR04LV*'

  result = check_reverse_classification('Petrol Filling Station')
  assert result == 'CR05*'

  result = check_reverse_classification('Public House / Bar / Nightclub')
  assert result == 'CR06*'

  result = check_reverse_classification('Restaurant / Cafeteria')
  assert result == 'CR07*'

  result = check_reverse_classification('Shop / Showroom')
  assert result == 'CR08*'

  result = check_reverse_classification('Garden Centre')
  assert result == 'CR08GC*'

  result = check_reverse_classification('Other Licensed Premise / Vendor')
  assert result == 'CR09*'

  result = check_reverse_classification(
      'Fast Food Outlet / Takeaway (Hot / Cold)')
  assert result == 'CR10*'

  result = check_reverse_classification('Automated Teller Machine (ATM)')
  assert result == 'CR11*'

  result = check_reverse_classification('Storage Land')
  assert result == 'CS*'

  result = check_reverse_classification('General Storage Land')
  assert result == 'CS01*'

  result = check_reverse_classification('Builders Yard')
  assert result == 'CS02*'

  result = check_reverse_classification('Transport')
  assert result == 'CT*'

  result = check_reverse_classification(
      'Airfield / Airstrip / Airport / Air Transport Infrastructure Facility')
  assert result == 'CT01*'

  result = check_reverse_classification('Airfield')
  assert result == 'CT01AF*'

  result = check_reverse_classification('Air Passenger Terminal')
  assert result == 'CT01AY*'

  result = check_reverse_classification(
      'Air Transport Infrastructure Services')
  assert result == 'CT01AI*'

  result = check_reverse_classification('Airport')
  assert result == 'CT01AP*'

  result = check_reverse_classification('Helicopter Station')
  assert result == 'CT01HS*'

  result = check_reverse_classification('Heliport / Helipad')
  assert result == 'CT01HT*'

  result = check_reverse_classification('Bus Shelter')
  assert result == 'CT02*'

  result = check_reverse_classification(
      'Car / Coach / Commercial Vehicle / Taxi Parking / Park And Ride Site')
  assert result == 'CT03*'

  result = check_reverse_classification('Public Park And Ride')
  assert result == 'CT03PK*'

  result = check_reverse_classification('Public Car Parking')
  assert result == 'CT03PP*'

  result = check_reverse_classification('Public Coach Parking')
  assert result == 'CT03PU*'

  result = check_reverse_classification('Public Commercial Vehicle Parking')
  assert result == 'CT03VP*'

  result = check_reverse_classification('Goods Freight Handling / Terminal')
  assert result == 'CT04*'

  result = check_reverse_classification('Air Freight Terminal')
  assert result == 'CT04AE*'

  result = check_reverse_classification('Container Freight')
  assert result == 'CT04CF*'

  result = check_reverse_classification('Road Freight Transport')
  assert result == 'CT04RH*'

  result = check_reverse_classification('Rail Freight Transport')
  assert result == 'CT04RT*'

  result = check_reverse_classification('Marina')
  assert result == 'CT05*'

  result = check_reverse_classification('Mooring')
  assert result == 'CT06*'

  result = check_reverse_classification('Railway Asset')
  assert result == 'CT07*'

  result = check_reverse_classification(
      'Station / Interchange / Terminal / Halt')
  assert result == 'CT08*'

  result = check_reverse_classification('Bus / Coach Station')
  assert result == 'CT08BC*'

  result = check_reverse_classification('Railway Station')
  assert result == 'CT08RS*'

  result = check_reverse_classification('Vehicular Rail Terminal')
  assert result == 'CT08VH*'

  result = check_reverse_classification('Transport Track / Way')
  assert result == 'CT09*'

  result = check_reverse_classification('Cliff Railway')
  assert result == 'CT09CL*'

  result = check_reverse_classification('Chair Lift / Cable Car / Ski Tow')
  assert result == 'CT09CX*'

  result = check_reverse_classification('Monorail')
  assert result == 'CT09MO*'

  result = check_reverse_classification('Vehicle Storage')
  assert result == 'CT10*'

  result = check_reverse_classification('Boat Storage')
  assert result == 'CT10BG*'

  result = check_reverse_classification('Bus / Coach Depot')
  assert result == 'CT10BU*'

  result = check_reverse_classification('Transport Related Infrastructure')
  assert result == 'CT11*'

  result = check_reverse_classification('Aqueduct')
  assert result == 'CT11AD*'

  result = check_reverse_classification('Lock')
  assert result == 'CT11LK*'

  result = check_reverse_classification('Weir')
  assert result == 'CT11WE*'

  result = check_reverse_classification('Weighbridge / Load Gauge')
  assert result == 'CT11WG*'

  result = check_reverse_classification('Overnight Lorry Park')
  assert result == 'CT12*'

  result = check_reverse_classification(
      'Harbour / Port / Dock / Dockyard / Slipway / Landing Stage / Pier / Jetty / Pontoon / Terminal / Berthing / Quay'
  )
  assert result == 'CT13*'

  result = check_reverse_classification('Passenger Ferry Terminal')
  assert result == 'CT13FR*'

  result = check_reverse_classification('Non-Tanker Nautical Berthing')
  assert result == 'CT13NB*'

  result = check_reverse_classification('Nautical Refuelling Facility')
  assert result == 'CT13NF*'

  result = check_reverse_classification('Slipway')
  assert result == 'CT13SA*'

  result = check_reverse_classification('Ship Passenger Terminal')
  assert result == 'CT13SP*'

  result = check_reverse_classification('Tanker Berthing')
  assert result == 'CT13TK*'

  result = check_reverse_classification('Vehicular Ferry Terminal')
  assert result == 'CT13VF*'

  result = check_reverse_classification('Utility')
  assert result == 'CU*'

  result = check_reverse_classification('Electricity Sub-Station')
  assert result == 'CU01*'

  result = check_reverse_classification('Landfill')
  assert result == 'CU02*'

  result = check_reverse_classification('Power Station / Energy Production')
  assert result == 'CU03*'

  result = check_reverse_classification('Electricity Distribution Facility')
  assert result == 'CU03ED*'

  result = check_reverse_classification('Electricity Production Facility')
  assert result == 'CU03EP*'

  result = check_reverse_classification('Wind Farm')
  assert result == 'CU03WF*'

  result = check_reverse_classification('Wind Turbine')
  assert result == 'CU03WU*'

  result = check_reverse_classification(
      'Pump House / Pumping Station / Water Tower')
  assert result == 'CU04*'

  result = check_reverse_classification('Water Controlling / Pumping')
  assert result == 'CU04WC*'

  result = check_reverse_classification('Water Distribution / Pumping')
  assert result == 'CU04WD*'

  result = check_reverse_classification('Water Quality Monitoring')
  assert result == 'CU04WM*'

  result = check_reverse_classification('Water Storage')
  assert result == 'CU04WS*'

  result = check_reverse_classification('Waste Water Distribution / Pumping')
  assert result == 'CU04WW*'

  result = check_reverse_classification('Telecommunication')
  assert result == 'CU06*'

  result = check_reverse_classification('Telecommunications Mast')
  assert result == 'CU06TE*'

  result = check_reverse_classification('Telephone Exchange')
  assert result == 'CU06TX*'

  result = check_reverse_classification(
      'Water / Waste Water / Sewage Treatment Works')
  assert result == 'CU07*'

  result = check_reverse_classification('Waste Water Treatment')
  assert result == 'CU07WR*'

  result = check_reverse_classification('Water Treatment')
  assert result == 'CU07WT*'

  result = check_reverse_classification('Gas / Oil Storage / Distribution')
  assert result == 'CU08*'

  result = check_reverse_classification('Gas Governor')
  assert result == 'CU08GG*'

  result = check_reverse_classification('Gas Holder')
  assert result == 'CU08GH*'

  result = check_reverse_classification('Oil Terminal')
  assert result == 'CU08OT*'

  result = check_reverse_classification('Other Utility Use')
  assert result == 'CU09*'

  result = check_reverse_classification('Observatory')
  assert result == 'CU09OV*'

  result = check_reverse_classification('Radar Station')
  assert result == 'CU09RA*'

  result = check_reverse_classification('Satellite Earth Station')
  assert result == 'CU09SE*'

  result = check_reverse_classification('Cable Terminal Station')
  assert result == 'CU09CQ*'

  result = check_reverse_classification('Waste Management')
  assert result == 'CU10*'

  result = check_reverse_classification('Telephone Box')
  assert result == 'CU11*'

  result = check_reverse_classification('Other Public Telephones')
  assert result == 'CU11OP*'

  result = check_reverse_classification('Dam')
  assert result == 'CU12*'

  result = check_reverse_classification('Emergency / Rescue Service')
  assert result == 'CX*'

  result = check_reverse_classification('Police / Transport Police / Station')
  assert result == 'CX01*'

  result = check_reverse_classification('Police Training')
  assert result == 'CX01PT*'

  result = check_reverse_classification('Fire Station')
  assert result == 'CX02*'

  result = check_reverse_classification('Fire Service Training')
  assert result == 'CX02FT*'

  result = check_reverse_classification('Ambulance Station')
  assert result == 'CX03*'

  result = check_reverse_classification('Air Sea Rescue / Air Ambulance')
  assert result == 'CX03AA*'

  result = check_reverse_classification('Lifeboat Services / Station')
  assert result == 'CX04*'

  result = check_reverse_classification(
      'Coastguard Rescue / Lookout / Station')
  assert result == 'CX05*'

  result = check_reverse_classification('Mountain Rescue Station')
  assert result == 'CX06*'

  result = check_reverse_classification('Lighthouse')
  assert result == 'CX07*'

  result = check_reverse_classification('Police Box / Kiosk')
  assert result == 'CX08*'

  result = check_reverse_classification('Information')
  assert result == 'CZ*'

  result = check_reverse_classification('Advertising Hoarding')
  assert result == 'CZ01*'

  result = check_reverse_classification('Tourist Information Signage')
  assert result == 'CZ02*'

  result = check_reverse_classification('Visitor Information')
  assert result == 'CZ02VI*'

  result = check_reverse_classification('Traffic Information Signage')
  assert result == 'CZ03*'

  result = check_reverse_classification('Land')
  assert result == 'L*'

  result = check_reverse_classification(
      'Agricultural - Applicable to land in farm ownership and not run as a separate business enterprise'
  )
  assert result == 'LA*'

  result = check_reverse_classification('Grazing Land')
  assert result == 'LA01*'

  result = check_reverse_classification('Permanent Crop / Crop Rotation')
  assert result == 'LA02*'

  result = check_reverse_classification('Orchard')
  assert result == 'LA02OC*'

  result = check_reverse_classification('Aviary / Dovecot / Cage')
  assert result == 'LB99AV*'

  result = check_reverse_classification('Bandstand')
  assert result == 'LB99BD*'

  result = check_reverse_classification('Pavilion / Changing Room')
  assert result == 'LB99PI*'

  result = check_reverse_classification('Sports Viewing Structure')
  assert result == 'LB99SV*'

  result = check_reverse_classification('Burial Ground')
  assert result == 'LC*'

  result = check_reverse_classification(
      'Historic / Disused Cemetery / Graveyard')
  assert result == 'LC01*'

  result = check_reverse_classification('Development')
  assert result == 'LD*'

  result = check_reverse_classification('Development Site')
  assert result == 'LD01*'

  result = check_reverse_classification('Commercial Construction Site')
  assert result == 'LD01CC*'

  result = check_reverse_classification('Community Construction Site')
  assert result == 'LD01CO*'

  result = check_reverse_classification('Residential Construction Site')
  assert result == 'LD01RN*'

  result = check_reverse_classification('Transport Construction Site')
  assert result == 'LD01TC*'

  result = check_reverse_classification('Forestry')
  assert result == 'LF*'

  result = check_reverse_classification(
      'Forest / Arboretum / Pinetum (Managed / Unmanaged)')
  assert result == 'LF02*'

  result = check_reverse_classification('Arboretum')
  assert result == 'LF02AU*'

  result = check_reverse_classification('Woodland')
  assert result == 'LF03*'

  result = check_reverse_classification('Allotment')
  assert result == 'LL*'

  result = check_reverse_classification(
      'Amenity - Open areas not attracting visitors')
  assert result == 'LM*'

  result = check_reverse_classification('Landscaped Roundabout')
  assert result == 'LM01*'

  result = check_reverse_classification('Verge / Central Reservation')
  assert result == 'LM02*'

  result = check_reverse_classification('Natural Central Reservation')
  assert result == 'LM02NV*'

  result = check_reverse_classification('Natural Verge')
  assert result == 'LM02VE*'

  result = check_reverse_classification('Maintained Amenity Land')
  assert result == 'LM03*'

  result = check_reverse_classification('Maintained Surfaced Area')
  assert result == 'LM04*'

  result = check_reverse_classification('Made Central Reservation')
  assert result == 'LM04MV*'

  result = check_reverse_classification('Pavement')
  assert result == 'LM04PV*'

  result = check_reverse_classification('Open Space')
  assert result == 'LO*'

  result = check_reverse_classification('Heath / Moorland')
  assert result == 'LO01*'

  result = check_reverse_classification('Park')
  assert result == 'LP*'

  result = check_reverse_classification('Public Park / Garden')
  assert result == 'LP01*'

  result = check_reverse_classification('Public Open Space / Nature Reserve')
  assert result == 'LP02*'

  result = check_reverse_classification('Playground')
  assert result == 'LP03*'

  result = check_reverse_classification('Play Area')
  assert result == 'LP03PA*'

  result = check_reverse_classification('Paddling Pool')
  assert result == 'LP03PD*'

  result = check_reverse_classification('Private Park / Garden')
  assert result == 'LP04*'

  result = check_reverse_classification('Unused Land')
  assert result == 'LU*'

  result = check_reverse_classification('Vacant / Derelict Land')
  assert result == 'LU01*'

  result = check_reverse_classification('Water')
  assert result == 'LW*'

  result = check_reverse_classification('Lake / Reservoir')
  assert result == 'LW01*'

  result = check_reverse_classification('Balancing Pond')
  assert result == 'LW01BP*'

  result = check_reverse_classification('Buried Reservoir')
  assert result == 'LW01BV*'

  result = check_reverse_classification('Named Pond')
  assert result == 'LW02*'

  result = check_reverse_classification('Dew Pond')
  assert result == 'LW02DE*'

  result = check_reverse_classification('Decoy Pond')
  assert result == 'LW02DP*'

  result = check_reverse_classification('Static Water')
  assert result == 'LW02IW*'

  result = check_reverse_classification('Waterway')
  assert result == 'LW03*'

  result = check_reverse_classification('Leats / Races')
  assert result == 'LW03LR*'

  result = check_reverse_classification('Drain')
  assert result == 'LW03DR*'

  result = check_reverse_classification('Military')
  assert result == 'M*'

  result = check_reverse_classification('Army')
  assert result == 'MA*'

  result = check_reverse_classification('Army Military Range')
  assert result == 'MA99AR*'

  result = check_reverse_classification('Army Site')
  assert result == 'MA99AS*'

  result = check_reverse_classification('Army Military Training')
  assert result == 'MA99AT*'

  result = check_reverse_classification('Army Military Storage')
  assert result == 'MA99AG*'

  result = check_reverse_classification('Military Target')
  assert result == 'MB99TG*'

  result = check_reverse_classification('Air Force')
  assert result == 'MF*'

  result = check_reverse_classification('Air Force Military Storage')
  assert result == 'MF99UG*'

  result = check_reverse_classification('Air Force Military Range')
  assert result == 'MF99UR*'

  result = check_reverse_classification('Air Force Site')
  assert result == 'MF99US*'

  result = check_reverse_classification('Air Force Military Training')
  assert result == 'MF99UT*'

  result = check_reverse_classification('Defence Estates')
  assert result == 'MG*'

  result = check_reverse_classification('Navy')
  assert result == 'MN*'

  result = check_reverse_classification('Naval Military Storage')
  assert result == 'MN99VG*'

  result = check_reverse_classification('Naval Military Range')
  assert result == 'MN99VR*'

  result = check_reverse_classification('Naval Site')
  assert result == 'MN99VS*'

  result = check_reverse_classification('Naval Military Training')
  assert result == 'MN99VT*'

  result = check_reverse_classification('Other (Ordnance Survey Only)')
  assert result == 'O*'

  result = check_reverse_classification('Aid To Navigation')
  assert result == 'OA*'

  result = check_reverse_classification('Aid To Aeronautical Navigation')
  assert result == 'OA01*'

  result = check_reverse_classification(
      'Aeronautical Navigation Beacon / Light')
  assert result == 'OA01AL*'

  result = check_reverse_classification('Landing Light')
  assert result == 'OA01LL*'

  result = check_reverse_classification('Signal Square')
  assert result == 'OA01SQ*'

  result = check_reverse_classification('Wind Sock / Wind Tee')
  assert result == 'OA01WK*'

  result = check_reverse_classification('Aid To Nautical Navigation')
  assert result == 'OA02*'

  result = check_reverse_classification('Daymark')
  assert result == 'OA02DM*'

  result = check_reverse_classification('Fog Horn Warning')
  assert result == 'OA02FG*'

  result = check_reverse_classification('Nautical Navigation Beacon / Light')
  assert result == 'OA02NL*'

  result = check_reverse_classification('Aid To Road Navigation')
  assert result == 'OA03*'

  result = check_reverse_classification('Guide Post')
  assert result == 'OA03GP*'

  result = check_reverse_classification(
      'Coastal Protection / Flood Prevention')
  assert result == 'OC*'

  result = check_reverse_classification('Boulder Wall / Sea Wall')
  assert result == 'OC01*'

  result = check_reverse_classification(
      'Flood Gate / Flood Sluice Gate / Flood Valve')
  assert result == 'OC02*'

  result = check_reverse_classification('Groyne')
  assert result == 'OC03*'

  result = check_reverse_classification('Rip-Rap')
  assert result == 'OC04*'

  result = check_reverse_classification('Emergency Support')
  assert result == 'OE*'

  result = check_reverse_classification('Beach Office / First Aid Facility')
  assert result == 'OE01*'

  result = check_reverse_classification('Emergency Telephone (Non Motorway)')
  assert result == 'OE02*'

  result = check_reverse_classification(
      'Fire Alarm Structure / Fire Observation Tower / Fire Beater Facility')
  assert result == 'OE03*'

  result = check_reverse_classification(
      'Emergency Equipment Point / Emergency Siren / Warning Flag')
  assert result == 'OE04*'

  result = check_reverse_classification('Lifeguard Facility')
  assert result == 'OE05*'

  result = check_reverse_classification(
      'Life / Belt / Buoy / Float / Jacket / Safety Rope')
  assert result == 'OE06*'

  result = check_reverse_classification('Street Furniture')
  assert result == 'OF*'

  result = check_reverse_classification('Agricultural Support Objects')
  assert result == 'OG*'

  result = check_reverse_classification('Fish Ladder / Lock / Pen / Trap')
  assert result == 'OG01*'

  result = check_reverse_classification('Livestock Pen / Dip')
  assert result == 'OG02*'

  result = check_reverse_classification('Currick')
  assert result == 'OG03*'

  result = check_reverse_classification('Slurry Bed / Pit')
  assert result == 'OG04*'

  result = check_reverse_classification('Historical Site / Object')
  assert result == 'OH*'

  result = check_reverse_classification('Historic Structure / Object')
  assert result == 'OH01*'

  result = check_reverse_classification('Industrial Support')
  assert result == 'OI*'

  result = check_reverse_classification('Adit / Incline / Level')
  assert result == 'OI01*'

  result = check_reverse_classification('Caisson / Dry Dock / Grid')
  assert result == 'OI02*'

  result = check_reverse_classification('Channel / Conveyor / Conduit / Pipe')
  assert result == 'OI03*'

  result = check_reverse_classification('Chimney / Flue')
  assert result == 'OI04*'

  result = check_reverse_classification(
      'Crane / Hoist / Winch / Material Elevator')
  assert result == 'OI05*'

  result = check_reverse_classification('Flare Stack')
  assert result == 'OI06*'

  result = check_reverse_classification('Hopper / Silo / Cistern / Tank')
  assert result == 'OI07*'

  result = check_reverse_classification(
      'Grab / Skip / Other Industrial Waste Machinery / Discharging')
  assert result == 'OI08*'

  result = check_reverse_classification('Kiln / Oven / Smelter')
  assert result == 'OI09*'

  result = check_reverse_classification('Manhole / Shaft')
  assert result == 'OI10*'

  result = check_reverse_classification(
      'Industrial Overflow / Sluice / Valve / Valve Housing')
  assert result == 'OI11*'

  result = check_reverse_classification('Cooling Tower')
  assert result == 'OI12*'

  result = check_reverse_classification('Solar Panel / Waterwheel')
  assert result == 'OI13*'

  result = check_reverse_classification('Telephone Pole / Post')
  assert result == 'OI14*'

  result = check_reverse_classification(
      'Electricity Distribution Pole / Pylon')
  assert result == 'OI15*'

  result = check_reverse_classification('Significant Natural Object')
  assert result == 'ON*'

  result = check_reverse_classification(
      'Boundary / Significant / Historic Tree / Pollard')
  assert result == 'ON01*'

  result = check_reverse_classification(
      'Boundary / Significant Rock / Boulder')
  assert result == 'ON02*'

  result = check_reverse_classification(
      'Natural Hole (Blow / Shake / Swallow)')
  assert result == 'ON03*'

  result = check_reverse_classification('Ornamental / Cultural Object')
  assert result == 'OO*'

  result = check_reverse_classification('Mausoleum / Tomb / Grave')
  assert result == 'OO02*'

  result = check_reverse_classification('Simple Ornamental Object')
  assert result == 'OO03*'

  result = check_reverse_classification('Maze')
  assert result == 'OO04*'

  result = check_reverse_classification('Sport / Leisure Support')
  assert result == 'OP*'

  result = check_reverse_classification('Butt / Hide')
  assert result == 'OP01*'

  result = check_reverse_classification('Gallop / Ride')
  assert result == 'OP02*'

  result = check_reverse_classification('Miniature Railway')
  assert result == 'OP03*'

  result = check_reverse_classification('Royal Mail Infrastructure')
  assert result == 'OR*'

  result = check_reverse_classification('Postal Box')
  assert result == 'OR01*'

  result = check_reverse_classification('Postal Delivery Box / Pouch')
  assert result == 'OR02*'

  result = check_reverse_classification('PO Box')
  assert result == 'OR03*'

  result = check_reverse_classification('Additional Mail / Packet Addressee')
  assert result == 'OR04*'

  result = check_reverse_classification('Scientific / Observation Support')
  assert result == 'OS*'

  result = check_reverse_classification('Meteorological Station / Equipment')
  assert result == 'OS01*'

  result = check_reverse_classification('Radar / Satellite Infrastructure')
  assert result == 'OS02*'

  result = check_reverse_classification(
      'Telescope / Observation Infrastructure / Astronomy')
  assert result == 'OS03*'

  result = check_reverse_classification('Transport Support')
  assert result == 'OT*'

  result = check_reverse_classification('Cattle Grid / Ford')
  assert result == 'OT01*'

  result = check_reverse_classification('Elevator / Escalator / Steps')
  assert result == 'OT02*'

  result = check_reverse_classification('Footbridge / Walkway')
  assert result == 'OT03*'

  result = check_reverse_classification(
      'Pole / Post / Bollard (Restricting Vehicular Access)')
  assert result == 'OT04*'

  result = check_reverse_classification('Subway / Underpass')
  assert result == 'OT05*'

  result = check_reverse_classification('Customs Inspection Facility')
  assert result == 'OT06*'

  result = check_reverse_classification('Lay-By')
  assert result == 'OT07*'

  result = check_reverse_classification('Level Crossing')
  assert result == 'OT08*'

  result = check_reverse_classification('Mail Pick Up')
  assert result == 'OT09*'

  result = check_reverse_classification('Railway Pedestrian Crossing')
  assert result == 'OT10*'

  result = check_reverse_classification('Railway Buffer')
  assert result == 'OT11*'

  result = check_reverse_classification('Rail Drag')
  assert result == 'OT12*'

  result = check_reverse_classification('Rail Infrastructure Services')
  assert result == 'OT13*'

  result = check_reverse_classification('Rail Kilometre Distance Marker')
  assert result == 'OT14*'

  result = check_reverse_classification('Railway Lighting')
  assert result == 'OT15*'

  result = check_reverse_classification('Rail Mile Distance Marker')
  assert result == 'OT16*'

  result = check_reverse_classification('Railway Turntable')
  assert result == 'OT17*'

  result = check_reverse_classification('Rail Weighbridge')
  assert result == 'OT18*'

  result = check_reverse_classification('Rail Signalling')
  assert result == 'OT19*'

  result = check_reverse_classification('Railway Traverse')
  assert result == 'OT20*'

  result = check_reverse_classification('Goods Tramway')
  assert result == 'OT21*'

  result = check_reverse_classification('Road Drag')
  assert result == 'OT22*'

  result = check_reverse_classification('Vehicle Dip')
  assert result == 'OT23*'

  result = check_reverse_classification('Road Turntable')
  assert result == 'OT24*'

  result = check_reverse_classification('Road Mile Distance Marker')
  assert result == 'OT25*'

  result = check_reverse_classification('Road Kilometre Distance Marker')
  assert result == 'OT26*'

  result = check_reverse_classification('Road Infrastructure Services')
  assert result == 'OT27*'

  result = check_reverse_classification('Unsupported Site')
  assert result == 'OU*'

  result = check_reverse_classification('Cycle Parking Facility')
  assert result == 'OU01*'

  result = check_reverse_classification('Picnic / Barbeque Site')
  assert result == 'OU04*'

  result = check_reverse_classification('Travelling Persons Site')
  assert result == 'OU05*'

  result = check_reverse_classification('Shelter (Not Including Bus Shelter)')
  assert result == 'OU08*'

  result = check_reverse_classification('Parent Shell')
  assert result == 'P*'

  result = check_reverse_classification('Property Shell')
  assert result == 'PP*'

  result = check_reverse_classification('Street Record')
  assert result == 'PS*'

  result = check_reverse_classification('Residential')
  assert result == 'R*'

  result = check_reverse_classification('Car Park Space')
  assert result == 'RC*'

  result = check_reverse_classification('Allocated Parking')
  assert result == 'RC01*'

  result = check_reverse_classification('Dwelling')
  assert result == 'RD*'

  result = check_reverse_classification('Caravan')
  assert result == 'RD01*'

  result = check_reverse_classification('Detached')
  assert result == 'RD02*'

  result = check_reverse_classification('Semi-Detached')
  assert result == 'RD03*'

  result = check_reverse_classification('Terraced')
  assert result == 'RD04*'

  result = check_reverse_classification(
      'Self Contained Flat (Includes Maisonette / Apartment)')
  assert result == 'RD06*'

  result = check_reverse_classification('House Boat')
  assert result == 'RD07*'

  result = check_reverse_classification('Sheltered Accommodation')
  assert result == 'RD08*'

  result = check_reverse_classification(
      'Privately Owned Holiday Caravan / Chalet')
  assert result == 'RD10*'

  result = check_reverse_classification('Garage')
  assert result == 'RG*'

  result = check_reverse_classification('Lock-Up Garage / Garage Court')
  assert result == 'RG02*'

  result = check_reverse_classification('House In Multiple Occupation')
  assert result == 'RH*'

  result = check_reverse_classification('HMO Parent')
  assert result == 'RH01*'

  result = check_reverse_classification(
      'HMO Bedsit / Other Non Self Contained Accommodation')
  assert result == 'RH02*'

  result = check_reverse_classification('HMO Not Further Divided')
  assert result == 'RH03*'

  result = check_reverse_classification('Residential Institution')
  assert result == 'RI*'

  result = check_reverse_classification('Care / Nursing Home')
  assert result == 'RI01*'

  result = check_reverse_classification('Communal Residence')
  assert result == 'RI02*'

  result = check_reverse_classification('Non-Commercial Lodgings')
  assert result == 'RI02NC*'

  result = check_reverse_classification('Religious Community')
  assert result == 'RI02RC*'

  result = check_reverse_classification('Residential Education')
  assert result == 'RI03*'

  result = check_reverse_classification('Unclassified')
  assert result == 'U*'

  result = check_reverse_classification('Awaiting Classification')
  assert result == 'UC*'

  result = check_reverse_classification('Pending Internal Investigation')
  assert result == 'UP*'

  result = check_reverse_classification('Dual Use')
  assert result == 'X*'

  result = check_reverse_classification('Object of Interest')
  assert result == 'Z*'

  result = check_reverse_classification('Archaeological Dig Site')
  assert result == 'ZA*'

  result = check_reverse_classification('Monument')
  assert result == 'ZM*'

  result = check_reverse_classification('Obelisk / Milestone / Standing Stone')
  assert result == 'ZM01*'

  result = check_reverse_classification('Obelisk')
  assert result == 'ZM01OB*'

  result = check_reverse_classification('Standing Stone')
  assert result == 'ZM01ST*'

  result = check_reverse_classification('Memorial / Market Cross')
  assert result == 'ZM02*'

  result = check_reverse_classification('Statue')
  assert result == 'ZM03*'

  result = check_reverse_classification('Castle / Historic Ruin')
  assert result == 'ZM04*'

  result = check_reverse_classification('Other Structure')
  assert result == 'ZM05*'

  result = check_reverse_classification('Boundary Stone')
  assert result == 'ZM05BS*'

  result = check_reverse_classification('Permanent Art Display / Sculpture')
  assert result == 'ZM05PN*'

  result = check_reverse_classification('Cascade / Fountain')
  assert result == 'ZM05CE*'

  result = check_reverse_classification('Windmill (Inactive)')
  assert result == 'ZM05WI*'

  result = check_reverse_classification('Stately Home')
  assert result == 'ZS*'

  result = check_reverse_classification('Underground Feature')
  assert result == 'ZU*'

  result = check_reverse_classification('Cave')
  assert result == 'ZU01*'

  result = check_reverse_classification('Pothole / Natural Hole')
  assert result == 'ZU04*'

  result = check_reverse_classification('Other Underground Feature')
  assert result == 'ZV*'

  result = check_reverse_classification('Cellar')
  assert result == 'ZV01*'

  result = check_reverse_classification('Disused Mine')
  assert result == 'ZV02*'

  result = check_reverse_classification('Mineral Mining / Inactive')
  assert result == 'ZV02MI*'

  result = check_reverse_classification('Oil And / Gas Extraction/ Inactive')
  assert result == 'ZV02OI*'

  result = check_reverse_classification(
      'Mineral Quarrying And / Open Extraction / Inactive')
  assert result == 'ZV02QI*'

  result = check_reverse_classification('Well / Spring')
  assert result == 'ZV03*'

  result = check_reverse_classification('Spring')
  assert result == 'ZV03SG*'

  result = check_reverse_classification('Well')
  assert result == 'ZV03WL*'

  result = check_reverse_classification('Place Of Worship')
  assert result == 'ZW*'

  result = check_reverse_classification('Abbey')
  assert result == 'ZW99AB*'

  result = check_reverse_classification('Cathedral')
  assert result == 'ZW99CA*'

  result = check_reverse_classification('Church')
  assert result == 'ZW99CH*'

  result = check_reverse_classification('Chapel')
  assert result == 'ZW99CP*'

  result = check_reverse_classification('Gurdwara')
  assert result == 'ZW99GU*'

  result = check_reverse_classification('Kingdom Hall')
  assert result == 'ZW99KH*'

  result = check_reverse_classification('Mosque')
  assert result == 'ZW99MQ*'

  result = check_reverse_classification('Minster')
  assert result == 'ZW99MT*'

  result = check_reverse_classification('Stupa')
  assert result == 'ZW99SU*'

  result = check_reverse_classification('Synagogue')
  assert result == 'ZW99SY*'

  result = check_reverse_classification('Temple')
  assert result == 'ZW99TP*'

  result = check_reverse_classification('Lych Gate')
  assert result == 'ZW99LG*'

  # Ancillary tests - Noteable because these need to be replaced with a more specific label

  result = check_reverse_classification('Residential Ancillary Building')
  assert result == 'RB*'

  result = check_reverse_classification('Land Ancillary Building')
  assert result == 'LB*'

  result = check_reverse_classification('Military Ancillary Building')
  assert result == 'MB*'

  result = check_reverse_classification('Commercial Ancillary Building')
  assert result == 'CB*'
