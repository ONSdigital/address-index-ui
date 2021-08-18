# address-index-ui

To run this project:

Pre-requisites: 
* Python 3.9.x
* https://github.com/ONSdigital/address-index-api
(Clone then run `docker-compose up` to start local Elastic Search including test data)


*Setup Environment Variables*
`export FLASK_APP="aims_ui"`
`export FLASK_ENV="development"`	

*Install Python Packages*
Run
`pip install -r requirements.txt`

*Install project as a python package*
`pip install -e .`

*To run*
python3 -m flask run




