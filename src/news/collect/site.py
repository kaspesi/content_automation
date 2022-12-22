import requests
from bs4 import BeautifulSoup
from news.collect.article import Article


class Site:

    def __init__(self, articles_collection, url):
        self.url = url
        self.articles_collection = articles_collection
        self.articles = self.get_articles(self.url)

    def __str__(self) -> str:
        retString = ""
        retString += "Site: [" + self.url + "]"
        for article in self.articles:
            retString += str(article) + '\n\n'
        return retString

    def get_articles(self, url):
        if url is None:
            return None

        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        articles_html = soup.find_all("div", class_=["gtmView", "grid-layout"])
        articles = []
        for article_html in articles_html:
            try:
                article_url = url + article_html.h2.a['href']
                article_title = article_html.h2.a['aria-label']
                article_lookup = self.articles_collection.find_one({"url": article_url})
                # print("article_lookup: " + str(article_url))
                if article_lookup is None:
                    articles.append(Article(article_url, article_title))
                else:
                    print("Article already exists: " + article_url)
            except:
                pass
        return articles
