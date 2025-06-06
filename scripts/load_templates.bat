@echo off

pushd "%~dp0\.."
set "BASE_DIR=%CD%"

REM Design system version
set "DESIGN_SYSTEM_VERSION=70.0.2"

REM Create a temporary directory
for /f "usebackq delims=" %%G in (`powershell -NoProfile -Command ^
    "[System.IO.Path]::Combine([System.IO.Path]::GetTempPath(), [System.Guid]::NewGuid().ToString())"`) do (
    set "TEMP_DIR=%%G"
)
powershell -NoProfile -Command "New-Item -ItemType Directory -Path '%TEMP_DIR%' | Out-Null"

REM Download templates.zip from GitHub Releases into temp folder
powershell -NoProfile -Command ^
    "Invoke-WebRequest -Uri 'https://github.com/ONSdigital/design-system/releases/download/%DESIGN_SYSTEM_VERSION%/templates.zip' -OutFile '%TEMP_DIR%\templates.zip'"

REM Unzip into a subfolder named "templates"
powershell -NoProfile -Command ^
    "Expand-Archive -LiteralPath '%TEMP_DIR%\templates.zip' -DestinationPath '%TEMP_DIR%\templates'"

REM Remove any existing components/ and layout/ directories under src\aims_ui\templates
if exist "%BASE_DIR%\src\aims_ui\templates\components" (
    rd /s /q "%BASE_DIR%\src\aims_ui\templates\components"
)
if exist "%BASE_DIR%\src\aims_ui\templates\layout" (
    rd /s /q "%BASE_DIR%\src\aims_ui\templates\layout"
)

REM Recreate the components/ and layout/ directories
mkdir "%BASE_DIR%\src\aims_ui\templates\components"
mkdir "%BASE_DIR%\src\aims_ui\templates\layout"

REM Copy layout and components into "templates" folder
xcopy /E /I "%TEMP_DIR%\templates\templates\components\*" "%BASE_DIR%\src\aims_ui\templates\components\" > nul
xcopy /E /I "%TEMP_DIR%\templates\templates\layout\*" "%BASE_DIR%\src\aims_ui\templates\layout\" > nul

REM Clean up the temporary directory
rd /s /q "%TEMP_DIR%"

REM Return to the original working directory
popd

echo.
echo Design system v%DESIGN_SYSTEM_VERSION% templates have been installed.
exit /b 0