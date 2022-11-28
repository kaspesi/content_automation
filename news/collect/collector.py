from news.collect.site import Site
from threading import Timer
from mongodb.mongo_client import MongoClientSingleton
from colorama import Fore, Back, Style

class Collector(Timer):

    def __init__(self, url):
        self.url = url
        self.site = Site(self.url)
        print(self.site)
        self.save(self.site)

        # Enable this eventually
        # self.start()

    def save(self, site):
        # Get the URLs of the articles in the site
        # Check if we have the article in the database
        # If not, add it to the database
        # If so, do nothing
        articles_collection = MongoClientSingleton().get_collection("news", "articles")
        for article in site.articles:
            if article is None:
                continue
            article_lookup = articles_collection.find_one({"url": article.url})
            if article_lookup is None:
                articles_collection.insert_one(article.__dict__)
                print("Added article to database: " + str(article))
            else:
                print(Fore.RED + "Article already exists in database: " + str(article.url) + Style.RESET_ALL)

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