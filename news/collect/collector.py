from news.collect.site import Site
from threading import Timer
from mongodb.mongo_client import MongoClientSingleton
from colorama import Fore, Back, Style
import functools

class Collector(Timer):

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

    def save(self, site):
        print(site.articles)
        if(site.articles is None):
            print (Fore.RED + "No articles to save" + Style.RESET_ALL)
            return

        print("Saving articles to database..." + str(site.articles))
        for article in site.articles:
            if article is None:
                continue
            article_lookup = self.articles_collection.find_one({"url": article.url})
            if article_lookup is None:
                self.articles_collection.insert_one(article.__dict__)
                print("Added article to database: " + str(article))
            else:
                print(Fore.RED + "Article already exists in database: " + str(article.url) + Style.RESET_ALL)

    def collect(self):
        if self.url is None:
            raise Exception("Collector: Cannot collect URL is None")
        self.site = Site(self.articles_collection, self.url)
        print(self.site)


    banned_phrases = [
        "Go deeper",
        "Editor's note"
    ]

    def clean_chunk(self, chunk):
        # TODO: Implement chunk cleaning here
        return chunk

    def clean(self):
        articles = self.site.articles
        for article in articles:
            clean_chunks = []
            text_chunk = article.chunks
            if functools.reduce(lambda a, b: b in text_chunk and a, self.banned_phrases):
                print("Banned phrase found in article: " + str(article.url))
            clean_chunks.append(self.clean_chunk(text_chunk))
            

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