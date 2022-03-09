# address-index-ui

To run this project:

Pre-requisites: 
* Python 3.9.x
* https://github.com/ONSdigital/address-index-api
(Clone then run `docker-compose up` to start local Elastic Search including test data)


*Setup Environment Variables*
`export FLASK_APP="aims_ui"`
`export FLASK_ENV="development"`	
`export API_AUTH_TYPE="JWT"`	
`export JWT_TOKEN=[enter_jwt_token_here]`
`export API_BSC_AUTH_USERNAME=[enter_bsc_username]`
`export API_BSC_AUTH_PASSWORD=[enter_bsc_password]`

*Install Python Packages*
Run
`pip install -r requirements.txt`

*Install project as a python package*
`pip install -e .`

*To run*
python3 -m flask run

*To format*
yapf --style='{based_on_style: pep8, indent_width: 2}' -ir .
