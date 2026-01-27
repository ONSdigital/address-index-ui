import os
import multiprocessing

# port defaults to 5000 (not currently overridden)
PORT = int(os.getenv("PORT", 5000))

# Gunicorn config
bind = ":" + str(PORT)
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()
timeout = 600


# Disable TLSv1.0 and TLSv1.1
def ssl_context(conf, default_ssl_context_factory):
  import ssl
  context = default_ssl_context_factory()
  context.minimum_version = ssl.TLSVersion.TLSv1_2
  return context
