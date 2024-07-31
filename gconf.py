import os
import multiprocessing

# port defaults to 5000 (not currently overridden)
PORT = int(os.getenv("PORT", 5000))

# Gunicorn config
bind = ":" + str(PORT)
# Disable TLSv1.0 and TLSv1.1
ssl_context = 'TLSv1_2'
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()
timeout = 420
