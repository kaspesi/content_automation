from collect.site import Site
from threading import Timer
from mongodb.mongo_client import MongoClient

db = MongoClient().db()

class Collector(Timer):

    def __init__(self, url):
        self.url = url
        self.site = Site(self.url)
        print(self.site)

        # Enable this eventually
        # self.start()

    def save(self):
        # Get the URLs of the articles in the site
        # Check if we have the article in the database
        # If not, add it to the database
        # If so, do nothing
        
        print("Saving... (not implemented)")

    def _run(self):
        self.is_running = False
        self.start()
        self.save

    # Start scheduled task in thread
    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False