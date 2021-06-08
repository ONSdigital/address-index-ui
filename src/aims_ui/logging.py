from logging.config import dictConfig


def setup_logging(platform):

  dictConfig({
      'version': 1,
      'formatters': {
          'default': {
              'format':
              '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
          }
      },
      'handlers': {
          'wsgi': {
              'class': 'logging.StreamHandler',
              'stream': 'ext://sys.stdout',
              'formatter': 'default'
          }
      },
      'root': {
          'level': 'INFO',
          'handlers': ['wsgi']
      }
  })

  if platform == 'GCP':
    import google.cloud.logging

    client = google.cloud.logging.Client()

    client.get_default_handler()
    client.setup_logging()
