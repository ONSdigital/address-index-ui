@echo off
setlocal

REM ----------------------------------------------------------------------------
REM  Step 1: Identify script location and move to parent directory
REM ----------------------------------------------------------------------------
echo [INFO] Determining script directory...
SET SCRIPT_DIR=%~dp0
echo [INFO] SCRIPT_DIR=%SCRIPT_DIR%

echo [INFO] Changing to parent folder of script directory...
cd /d "%SCRIPT_DIR%.."
echo [INFO] Current working directory is now: %CD%
echo.
PAUSE
REM ----------------------------------------------------------------------------
REM  Step 2: Prepare variables and temp folder
REM ----------------------------------------------------------------------------
SET DESIGN_SYSTEM_VERSION=70.0.2
echo [INFO] DESIGN_SYSTEM_VERSION=%DESIGN_SYSTEM_VERSION%

SET TEMP_DIR=%TEMP%\templates%RANDOM%
echo [INFO] Creating temporary directory: "%TEMP_DIR%"
mkdir "%TEMP_DIR%"
echo.
PAUSE
REM ----------------------------------------------------------------------------
REM  Step 3: Download the templates zip
REM ----------------------------------------------------------------------------
echo [INFO] Downloading templates.zip from:
echo        https://github.com/ONSdigital/design-system/releases/download/%DESIGN_SYSTEM_VERSION%/templates.zip
echo [INFO] Saving to: "%TEMP_DIR%\templates.zip"
curl -L --url "https://github.com/ONSdigital/design-system/releases/download/%DESIGN_SYSTEM_VERSION%/templates.zip" ^
     --output "%TEMP_DIR%\templates.zip"
echo.
PAUSE
REM ----------------------------------------------------------------------------
REM  Step 4: Unzip using PowerShell
REM ----------------------------------------------------------------------------
echo [INFO] Unzipping %TEMP_DIR%\templates.zip into "%TEMP_DIR%\templates"
powershell -Command "Expand-Archive -Path '%TEMP_DIR%\templates.zip' -DestinationPath '%TEMP_DIR%\templates' -Force"
echo.
PAUSE
REM ----------------------------------------------------------------------------
REM  Step 6: Remove old directories (components, layout) and recreate components
REM ----------------------------------------------------------------------------
echo [INFO] Removing old 'components' and 'layout' folders under src\aims_ui\templates
rmdir /s /q src\aims_ui\templates\components 2>nul
rmdir /s /q src\aims_ui\templates\layout 2>nul
PAUSE
echo [INFO] Recreating src\aims_ui\templates\components
mkdir src\aims_ui\templates\components
echo.
PAUSE
REM ----------------------------------------------------------------------------
REM  Step 7: Move the newly downloaded templates into components
REM          (mirroring your original shell script approach)
REM ----------------------------------------------------------------------------
echo [INFO] Moving from "%TEMP_DIR%\templates\templates\*" to "%CD%\src\aims_ui\templates\components\"
move "%TEMP_DIR%\templates\templates\*" "%CD%\src\aims_ui\templates\components\"
echo.
PAUSE
REM ----------------------------------------------------------------------------
REM  Step 8: Remove the temp directory
REM ----------------------------------------------------------------------------
echo [INFO] Removing temporary directory "%TEMP_DIR%"
rmdir /s /q "%TEMP_DIR%"
echo.
PAUSE
REM ----------------------------------------------------------------------------
REM  Step 9: Robocopy from components -> templates (similar to rsync -a)
REM ----------------------------------------------------------------------------
echo [INFO] Copying all files from src\aims_ui\templates\components -> src\aims_ui\templates
robocopy src\aims_ui\templates\components src\aims_ui\templates /E
PAUSE
echo.
echo [INFO] Final structure under src\aims_ui\templates:
dir /s src\aims_ui\templates
PAUSE
echo.
echo [INFO] Done. Exiting...
exit /b 0