import abc
from threading import Timer
from mongodb.mongo_client import MongoClientSingleton
from colorama import Fore, Back, Style

class ArticleSummarizer(Timer, metaclass=abc.ABCMeta):
    
    def __init__(self):
        self.is_running = False
        self.interval = 10 # seconds
        self.articles_collection = MongoClientSingleton().get_collection("news", "articles")
        self.summarized_collection_str = "invalid_collection"
        # Enable this eventually
        # self.start()

    def summarize(self):
        # Get a reference to the target collection to save summarized articles
        summarized_collection = MongoClientSingleton().get_collection("news", self.summarized_collection_str)

        articles = self.articles_collection.find()

        for article in articles:
            # Check if a summarized article with the same url exists in summarized_collection
            summarized_lookup = summarized_collection.find_one({"url": article["url"]})
            if summarized_lookup is None:
                summarized_text = self.summarize_text(article["text"])
                summarized_article = {
                    "url": article["url"],
                    "title": article["title"],
                    "text": summarized_text
                }
                summarized_collection.insert_one(summarized_article)
                print("Added summarized article" + article["url"] + f"to {self.summarized_collection_str}")
            else:
                print(Fore.RED + "Article already summarized: " + article["url"] + Style.RESET_ALL)

    @abc.abstractmethod
    def summarize_text(self, text):
        pass

    def _run(self):
        self.is_running = False
        # Collect the site
        self.summarize()
        self.start()
        print(f"Running summarizer on {self.summarized_collection_str}...")

    # Start scheduled task in thread
    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False