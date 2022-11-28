import requests
from bs4 import BeautifulSoup
from news.collect.article import Article


class Site:

    def __init__(self, url):
        self.url = "https://www.axios.com"
        self.articles = Site.get_articles(self.url)

    def __str__(self) -> str:
        retString = ""
        retString += "Site: [" + self.url + "]"
        for article in self.articles:
            retString += str(article) + '\n\n'
        return retString

    @staticmethod
    def get_articles(url):
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
                articles.append(Article(article_url, article_title))
            except:
                pass
        return articles
