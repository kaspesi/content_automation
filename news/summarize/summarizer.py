import abc
from threading import Timer
from mongodb.mongo_client import MongoClientSingleton

class Summarizer(Timer):

    def __init__(self, url):
        self.url = url
        self.is_running = False
        self.interval = 10 # seconds
        self.articles_collection = MongoClientSingleton().get_collection("news", "articles")
        # self.site = Site(self.url)
        # print(self.site)
        # self.save(self.site)

        # Enable this eventually
        # self.start()

    def summarize(self):
        # Get references to the articles

    def _run(self):
        self.is_running = False
        # Collect the site
        self.collect()
        # Clean the site
        # Save the site to database
        self.save(self.site)
        self.start()
        print("Running collector...")

    # Start scheduled task in thread
    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False