
def setup_logging(PLATFORM):
  from logging.config import dictConfig

  dictConfig({
      'version': 1,
      'formatters': {'default': {
          'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
      }},
      'handlers': {'wsgi': {
          'class': 'logging.StreamHandler',
          'stream': 'sys.stdout',
          'formatter': 'default'
      }},
      'root': {
          'level': 'INFO',
          'handlers': ['wsgi']
      }
  })

  if PLATFORM == 'GCP':
    import google.cloud.logging

    client = google.cloud.logging.Client()

    client.get_default_handler()
    client.setup_logging()  

