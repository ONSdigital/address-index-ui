from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os
import signal
import subprocess
import time
import atexit

class RestartServerHandler(PatternMatchingEventHandler):
    def __init__(self, patterns):
        super().__init__(patterns=patterns)
        self.process = None
        self.start_server()

    def start_server(self):
        if self.process:
            os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
        self.process = subprocess.Popen(
            ["python3", "-m", "flask", "run", "--host=0.0.0.0"],
            preexec_fn=os.setsid)

    def stop_server(self):
        if self.process:
            print("Stopping Flask server.")
            os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
            self.process = None

    def on_any_event(self, event):
        print(f"Detected change in {event.src_path}. Restarting server.")
        self.start_server()

def cleanup(observer, handler):
    observer.stop()
    observer.join()
    handler.stop_server()

if __name__ == "__main__":
    patterns = ["*.py", "*.nunjucks", "*.mjs", '*.css', '*.html']
    event_handler = RestartServerHandler(patterns)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()

    atexit.register(cleanup, observer, event_handler)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
