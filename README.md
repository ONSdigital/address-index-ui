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

`export API_URL=[enter_api_url]`
`export API_JWT_TOKEN=[enter_jwt_token_here]`

`export BM_API_URL=[enter_bulk_match_url]`
`export BM_JWT_TOKEN=[enter_jwt_token_here]`

`export API_BSC_AUTH_USERNAME=[enter_bsc_username]`
`export API_BSC_AUTH_PASSWORD=[enter_bsc_password]`

`export PROJECT_DOMAIN=[enter_project_domain]`

Optional:

Set the "groups" of users (by default all users including the "NotLoggedInUser" are in the "default" group

`export USER_AUTHS='{"developers":["NotLoggedinUer"]}'`

*Note: JWT token is exported WITHOUT 'Bearer ' before it*

## Install Python Packages

`pip install -r requirements.txt`

## Install project as a python package*

`pip install -e .`

# To run Flask Project

`python3 -m flask run`

## To lint code

### For python:
`yapf --style='{based_on_style: pep8, indent_width: 2}' -ir .`

### For js/mjs:
`npx prettier --write "**/*.mjs"`

### To Test
`python3 -m pytest`

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

