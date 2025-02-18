# README

It is now recomended users download the entire AIMS stack including the UI and API bundled together with pre-loaded example address data from [https://github.com/ONSdigital/aims-diy](https://github.com/ONSdigital/aims-diy) as it's the easiest way to see the UI in action.

The UI can be run without an API, however many features that require the API will not work as intended. 

Therefore if you want to run the UI locally you will need to connect it to an instance of AIMS. It is recomended you use the bundled version of the API from [https://github.com/ONSdigital/aims-diy](https://github.com/ONSdigital/aims-diy) while commenting out the "UI" portion of the docker-compose.

Pre-requisites:
* Access to an API as described above
* Python 3.12.1

## Setup Environment Variables

| Environment Variable         | Value                      | Command                                     |
|-----------------------------|----------------------------|---------------------------------------------|
| `export FLASK_APP`          | `"aims_ui"`                | `export FLASK_APP="aims_ui"`                 |
| `export FLASK_ENV`          | `"development"`            | `export FLASK_ENV="development"`             |
| `export API_AUTH_TYPE`      | `"JWT"`                    | `export API_AUTH_TYPE="JWT"`                 |
| `export API_JWT_TOKEN`      | `[enter_jwt_token_here]`   | `export API_JWT_TOKEN="[enter_jwt_token_here]"` |
| `export BM_API_URL`         | `[enter_bulk_match_url]`   | `export BM_API_URL="[enter_bulk_match_url]"` |
| `export BM_JWT_TOKEN`       | `[enter_jwt_token_here]`   | `export BM_JWT_TOKEN="[enter_jwt_token_here]"` |
| `export API_JWT_K_VALUE` | `[enter_API_JWT_K_VALUE_here] | `export API_JWT_K_VALUE="NA"` |
| `export API_BSC_AUTH_USERNAME` | `[enter_bsc_username]`  | `export API_BSC_AUTH_USERNAME="[enter_bsc_username]"` |
| `export API_BSC_AUTH_PASSWORD` | `[enter_bsc_password]`  | `export API_BSC_AUTH_PASSWORD="[enter_bsc_password]"` |
| `export PROJECT_DOMAIN`     | `[enter_project_domain]`   | `export PROJECT_DOMAIN="[enter_project_domain]"` |
*Note: JWT token is exported WITHOUT 'Bearer ' before it*

Set the "groups" of users (by default all users including the "NotLoggedInUser" are in the "default" group
`export USER_AUTHS='{"developers":["NotLoggedinUer"]}'`


## Install Python Packages

`pip install -r requirements.txt`

If running tests as well
`pip install -r requirements_test.txt`

## Install project as a python package*

`pip install -e .`

# To run Flask Project

`python3 -m flask run`

# To run as a developer (Any file-saves restart server)
`python3 run_ui_developer.py`

## To lint code

### For python:
`yapf --style='{based_on_style: pep8, indent_width: 2}' -ir .`
### For python imports:
   - Pre-requisites: `pip install isort`
                     `pip install autoflake`
`autoflake --in-place --remove-all-unused-imports --remove-unused-variables \"${file}\"`
`isort \"${file}\`
This will remove unused imoports and organise imports consistantly

### For js/mjs:
`npm run lint`  

### To Test

#### Python
1. Ensure the API is up and running on port 9001
2. Run the UI with the wsgi.py script `python wsgi.py`
3. Headless: `python3 -m pytest tests/pytest_tests -n 4`
4. Visible: `python3 -m pytest tests/pytest_tests --browser chromium --slowmo 2000 --headed`

### Javascript 
`npm run test:jest`

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

* Note that the above is for Command Prompt not Powershell - use `$Env:<variable-name>`for powershell launch
