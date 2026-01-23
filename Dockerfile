# syntax=docker/dockerfile:1
FROM python:3.9-alpine
WORKDIR /code
ENV FLASK_APP=aims_ui
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN ls -la && chmod +x scripts/load_templates.sh && ./scripts/load_templates.sh && ls -la && ls -la src/aims_ui/templates/
EXPOSE 5000
COPY . .
RUN pip install -e .
CMD ["gunicorn", "wsgi:app", "--preload", "--timeout=420", "--config=gconf.py"]
