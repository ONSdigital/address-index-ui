# syntax=docker/dockerfile:1
FROM python:3.9-alpine
WORKDIR /code
ENV FLASK_APP=aims_ui
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
ENV API_AUTH_TYPE=JWT
ENV JWT_TOKEN=needed_for_typeahead
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
RUN pip install -e .
# put a local copy of this in your root directory https://github.com/ONSdigital/design-system/releases/download/42.0.0/templates.zip
RUN mkdir -p temp
RUN unzip templates.zip -d temp/templates
RUN rm -r -f src/aims_ui/templates/components
RUN rm -r -f src/aims_ui/templates/layout
RUN mkdir -p src/aims_ui/templates/components/
RUN mkdir -p src/aims_ui/templates/layout
RUN mv temp/templates/templates/components/* src/aims_ui/templates/components/
RUN mv temp/templates/templates/layout/* src/aims_ui/templates/layout/
RUN rm -rf temp
CMD ["flask","run"]
#docker build -t testui .
#docker run -d -p 5000:5000 testui
