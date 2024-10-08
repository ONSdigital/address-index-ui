#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "${DIR}"/.. || exit

DESIGN_SYSTEM_VERSION="70.0.2"

TEMP_DIR=$(mktemp -d)

curl -L --url "https://github.com/ONSdigital/design-system/releases/download/$DESIGN_SYSTEM_VERSION/templates.zip" --output ${TEMP_DIR}/templates.zip
unzip ${TEMP_DIR}/templates.zip -d ${TEMP_DIR}/templates
rm -r -f src/aims_ui/templates/components
rm -r -f src/aims_ui/templates/layout
mkdir -p src/aims_ui/templates/components/
mv ${TEMP_DIR}/templates/templates/* src/aims_ui/templates/components/
rm -rf ${TEMP_DIR}
rsync -a  src/aims_ui/templates/components/  src/aims_ui/templates/
