from collect.site import Site
from threading import Timer

class Collector:

    def __init__(self, url):
        self.url = url
        self.site = Site(self.url)
        print(self.site)
