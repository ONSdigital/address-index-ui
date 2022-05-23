# address-index-ui

To run this project:

Pre-requisites:
* Python 3.9.x
* https://github.com/ONSdigital/address-index-api
(Clone then run `docker-compose up` to start local Elastic Search including test data)


## Setup Environment Variables

`export FLASK_APP="aims_ui"`

`export FLASK_ENV="development"`

`export API_AUTH_TYPE="JWT"`

`export JWT_TOKEN=[enter_jwt_token_here]`

`export API_BSC_AUTH_USERNAME=[enter_bsc_username]`

`export API_BSC_AUTH_PASSWORD=[enter_bsc_password]`

`export PROJECT_DOMAIN=[enter_project_domain]`

*Note: JWT token is exported WITHOUT 'Bearer ' before it*

## Install Python Packages
Run

`pip install -r requirements.txt`

## Install project as a python package*
`pip install -e .`

# To run Flask Project
python3 -m flask run

## To reformat code
yapf --style='{based_on_style: pep8, indent_width: 2}' -ir .

FOR WINDOWS USERS ONLY:

*Ensure you have python 3.9 installed*

*Run a command window as an administrator and cd to the project root*
`pip install -r requirements.txt`

*Download the design system templates from https://github.com/ONSdigital/design-system/releases*

*Unzip the components and layout directories into the project's templates folder*

*Set environment variables and run (on localhost:5000)*
`set FLASK_ENV=development`
`set FLASK_APP=src/aims_ui`
`python -m flask run`
