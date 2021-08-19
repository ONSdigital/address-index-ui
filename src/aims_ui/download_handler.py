import os
from . import app
import json
import csv
from io import StringIO, BytesIO
from flask import render_template, request, session, send_file
from flask_login import login_required
import requests


@login_required
@app.route(f'/downloads/example_csv', methods=['GET', 'POST'])
def download_handler():
  # Create example_csv

  proxy = StringIO()
  writer = csv.writer(proxy)
  # Header Row
  writer.writerow(['id', 'searchAddress'])

  # Sample test data
  sample_body = [
      ['100316', '33 GRASSLANDS DRIVE PINHOE EXETER DEVON EX1 3QR'],
      ['100319', '135 CHESTNUT AVENUE EXETER DEVON EX2 6DN'],
      ['100322', '71 VICTORIA STREET EXETER DEVON EX4 6JQ'],
      ['101158', 'FLAT 1 3 BLACKALL ROAD EXETER EX4 4HD'],
      ['101159', '120 FLAT 1 OLD TIVERTON ROAD EXETER EX4 6LD'],
      ['101286', '10 EXETER ROAD NEWPORT NP19 8DB'],
      [
          '101625',
          'STUDIO 1.2 BLOCK J BIRKS HALLS NEW NORTH ROAD EXETER EX4 4ZZ'
      ],
      ['101801', '5 EXETER ROAD OKEHAMPTON EX11 1ZZ'],
      ['101802', '59 EXETER ROAD OKEHAMPTON EX11 1ZZ'],
      ['101931', '1 EXETER ROAD NEWPORT EX2 7EE'],
      ['102122', '238 EXETER ROAD RAYNERS LANE HARROW HA2 9ZZ'],
      ['102260', '7 RYDON LANE EXETER EX2 7ZZ'],
      ['102414', '2 SYLVAN ROAD EXETER EX4 6EW'],
      ['102565', '7 ALPHA STREET EXETER EX1 2SP'],
      ['103163', '1 DIAMOND COTTAGES SANDYGATE EXETER EX2 7JN'],
      ['103164', '5 SOWTON VILLAGE SOWTON EXETER EX5 2AD'],
      ['103169', '2 HIGH STREET STOKE CANON EXETER EX5 4AR'],
      ['103443', '2 RICHMOND COURT ST. DAVIDS HILL EXETER EX4 3RA'],
      ['103565', 'WOODLANDS HALDON HILL KENNFORD EXETER EX6 7XX'],
      ['103567', '6 MORETON TERRACE BRIDFORD EXETER EX6 7JG'],
      ['103568', '2 ORCHARD TERRACE TEDBURN ST. MARY EXETER EX6 6AU'],
      ['103569', '3 ORCHARD TERRACE TEDBURN ST. MARY EXETER EX6 6AU'],
      ['104299', '47 REGENTS PARK 47 REGENTS PARK HEAVITREE EXETER EX1 2NZ'],
      ['104301', 'HONITON MANOR NURSING HOME EXETER ROAD HONITON EX14 1AL'],
      ['104305', 'ARTHUR ROBERTS HOUSE 121 BURNTHOUSE LANE EXETER EX2 6NB'],
      ['104314', 'PENNSYLVANIA HOUSE 7-9 POWDERHAM CRESCENT EXETER EX4 6DA'],
      [
          '104315',
          'SPURFIELD HOUSE RESIDENTIAL HOME MAIN ROAD EXMINSTER, EXETER DEVON EX6 8BU'
      ],
      [
          '104896',
          'ROSEMOUNT 48 OLD EXETER STREET CHUDLEIGH NEWTON ABBOT TQ13 0JX'
      ],
  ]

  for row in sample_body:
    writer.writerow(row)

  # Creating the byteIO object from the StringIO Object
  mem = BytesIO()
  mem.write(proxy.getvalue().encode())
  mem.seek(0)
  proxy.close()

  return send_file(mem,
                   mimetype='text/csv',
                   attachment_filename=f'example_upload.csv',
                   as_attachment=True)
