# README #

### What is this repository for? ###

This repository contains the Flask web app that is used to interact with the [Address Index API ](https://github.com/ONSdigital/aims-api/).

A functioning version of the API is required to use this application, which can be setup using the Address Index API instructions.

### How do I run the UI? ###

It is now recomended users download the entire AIMS stack including the UI and API bundled together with pre-loaded example address data from [aims-diy](https://github.com/ONSdigital/aims-diy) as it's the easiest way to see the UI in action.

The UI can be run without an API, however many features that require the API will not work as intended. 

If users want to run the UI and API seperately, it is recomended you use the bundled version of the API from the [aims-diy repositroy](https://github.com/ONSdigital/aims-diy), while commenting out the "UI" portion of the docker-compose.

### How do I get set up for development? ###

1) Required Installations
   * Access to an API as described above
   * Python 3.12.1

2) Create Project from GitHub (IntelliJ shown as example)
   * File, New, Project from Version Control, GitHub
   * Git Repository URL - select "https://github.com/ONSdigital/address-index-ui"
   * Clone

3) Setup Environment Variables

Required Variables (the UI will not run without these being set) ✅

| Environment Variable    | Value                          | Bash Command                                          | PowerShell Command                                    |
| ----------------------- | ------------------------------ | ----------------------------------------------------- | ----------------------------------------------------- |
| `FLASK_APP`             | `"aims_ui"`                    | `export FLASK_APP="aims_ui"`                          | `$Env:FLASK_APP = "aims_ui"`                          |
| `FLASK_ENV`             | `"development"`                | `export FLASK_ENV="development"`                      | `$Env:FLASK_ENV = "development"`                      |


Optional Variables (set them according to your setup)

| Environment Variable    | Value                          | Bash Command                                          | PowerShell Command                                    |
| ----------------------- | ------------------------------ | ----------------------------------------------------- | ----------------------------------------------------- |
| `API_AUTH_TYPE`         | `"JWT"`                        | `export API_AUTH_TYPE="JWT"`                          | `$Env:API_AUTH_TYPE = "JWT"`                          |
| `API_JWT_TOKEN`*        | `[enter_jwt_token_here]`       | `export API_JWT_TOKEN="[enter_jwt_token_here]"`       | `$Env:API_JWT_TOKEN = "[enter_jwt_token_here]"`       |
| `BM_API_URL`            | `[enter_bulk_match_url]`       | `export BM_API_URL="[enter_bulk_match_url]"`          | `$Env:BM_API_URL = "[enter_bulk_match_url]"`          |
| `BM_JWT_TOKEN`*         | `[enter_jwt_token_here]`       | `export BM_JWT_TOKEN="[enter_jwt_token_here]"`        | `$Env:BM_JWT_TOKEN = "[enter_jwt_token_here]"`        |
| `API_JWT_K_VALUE`*      | `[enter_API_JWT_K_VALUE_here]` | `export API_JWT_K_VALUE="NA"`                         | `$Env:API_JWT_K_VALUE = "NA"`                         |
| `API_BSC_AUTH_USERNAME` | `[enter_bsc_username]`         | `export API_BSC_AUTH_USERNAME="[enter_bsc_username]"` | `$Env:API_BSC_AUTH_USERNAME = "[enter_bsc_username]"` |
| `API_BSC_AUTH_PASSWORD` | `[enter_bsc_password]`         | `export API_BSC_AUTH_PASSWORD="[enter_bsc_password]"` | `$Env:API_BSC_AUTH_PASSWORD = "[enter_bsc_password]"` |
| `PROJECT_DOMAIN`        | `[enter_project_domain]`       | `export PROJECT_DOMAIN="[enter_project_domain]"`      | `$Env:PROJECT_DOMAIN = "[enter_project_domain]"`      |
| `USER_AUTHS`            | `{"developers":["NotLoggedinUser"]}`| `export USER_AUTHS='{"developers":["NotLoggedinUser"]}'`| `$Env:USER_AUTHS='{"developers":["NotLoggedinUser"]}'`|

*Note: JWT token is exported WITHOUT 'Bearer ' before it*


| Environment Variable    | Options | Notes |
| ----------------------- | ------------------------------ | ----------------------------------------------------- | 
| `FLASK_ENV`             | `"development", "testing", "production"`| Use development when actively developing, testing for running tests and production in production |

#### Required Variables (the UI will not run without these being set)

**FLASK_APP**  
Value: `"aims_ui"`

```sh
export FLASK_APP="aims_ui"
```

```powershell
$Env:FLASK_APP = "aims_ui"
```

**FLASK_ENV**  
Value: `"development"`

```sh
export FLASK_ENV="development"
```

```powershell
$Env:FLASK_ENV = "development"
```

---

#### Optional Variables (set them according to your setup)

**API_AUTH_TYPE**  
Value: `"JWT"`

```sh
export API_AUTH_TYPE="JWT"
```

```powershell
$Env:API_AUTH_TYPE = "JWT"
```

**API_JWT_TOKEN***  
Value: `[enter_jwt_token_here]`

```sh
export API_JWT_TOKEN="[enter_jwt_token_here]"
```

```powershell
$Env:API_JWT_TOKEN = "[enter_jwt_token_here]"
```

**BM_API_URL**  
Value: `[enter_bulk_match_url]`

```sh
export BM_API_URL="[enter_bulk_match_url]"
```

```powershell
$Env:BM_API_URL = "[enter_bulk_match_url]"
```

**BM_JWT_TOKEN***  
Value: `[enter_jwt_token_here]`

```sh
export BM_JWT_TOKEN="[enter_jwt_token_here]"
```

```powershell
$Env:BM_JWT_TOKEN = "[enter_jwt_token_here]"
```

**API_JWT_K_VALUE***  
Value: `[enter_API_JWT_K_VALUE_here]`

```sh
export API_JWT_K_VALUE="NA"
```

```powershell
$Env:API_JWT_K_VALUE = "NA"
```

**API_BSC_AUTH_USERNAME**  
Value: `[enter_bsc_username]`

```sh
export API_BSC_AUTH_USERNAME="[enter_bsc_username]"
```

```powershell
$Env:API_BSC_AUTH_USERNAME = "[enter_bsc_username]"
```

**API_BSC_AUTH_PASSWORD**  
Value: `[enter_bsc_password]`

```sh
export API_BSC_AUTH_PASSWORD="[enter_bsc_password]"
```

```powershell
$Env:API_BSC_AUTH_PASSWORD = "[enter_bsc_password]"
```

**PROJECT_DOMAIN**  
Value: `[enter_project_domain]`

```sh
export PROJECT_DOMAIN="[enter_project_domain]"
```

```powershell
$Env:PROJECT_DOMAIN = "[enter_project_domain]"
```

**USER_AUTHS**  
Value: `{"developers":["NotLoggedinUser"]}`

```sh
export USER_AUTHS='{"developers":["NotLoggedinUser"]}'
```

```powershell
$Env:USER_AUTHS = '{"developers":["NotLoggedinUser"]}'
```


4) Install Python Prerequisites

```sh
pip install -r requirements.txt
```

If also running tests:

```sh
pip install -r requirements_test.txt
```

5) Install Project as Python Package

Run in the root directory

```sh
pip install -e .
```

6) Install Design System Components

Run the script located in this project at

```sh
scripts/load_templates.sh
```

7) Running the UI

```sh
python3 -m flask run
```

Or to run as a developer (auto-restarts on file save):

```sh
python3 run_ui_developer.py
```

### Tools ###

#### Python

1) Python Linters

To lint Python code using [YAPF](https://github.com/google/yapf)

```sh
yapf --style='{based_on_style: pep8, indent_width: 2}' -ir .
```

2) To Lint Imports Specifically

Pre-requisites: 

```sh
pip install isort
pip install autoflake
```

```sh
autoflake --in-place --remove-all-unused-imports --remove-unused-variables "${file}"
```

```sh
isort "${file}"
```

#### JS/MJS ####

1) Linting JS files

```sh
npm run lint
```

### Tests ###

To test the full application with [Playwright](https://github.com/microsoft/playwright)

1. Ensure the API is up and running on port 9001  
2. Run the UI with the wsgi.py script

```sh
python wsgi.py
```

3. Headless:

```sh
python3 -m pytest tests/pytest_tests -n 4
```

4. Visible:

```sh
python3 -m pytest tests/pytest_tests --browser chromium --slowmo 2000 --headed
```

To run the standalone JS tests:

```sh
npm run test:jest
```