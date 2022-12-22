import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style

class Article:

    def __init__(self, url, title):
        self.url = url
        self.title = title
        if self.url is None:
            return None
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        title = soup.find('h1', attrs={'data-cy': 'story-headline'})
        header = title.parent
        body = Article.get_body(header)
        if body is None:
            return None
        self.chunks = Article.get_chunks(body)

    def __str__(self) -> str:
        retString = ""
        retString += Fore.GREEN + "[" + self.title + ", " + self.url + "]" + Style.RESET_ALL +"\n"
        for chunk in self.chunks:
            main = chunk['main']
            bullets = chunk['bullets']
            retString += Fore.CYAN + main + Style.RESET_ALL + '\n'
            for bullet in bullets:
                retString += Fore.BLUE + bullet + Style.RESET_ALL + '\n'
            # retString += str(chunk) + '\n'
        return retString

    @staticmethod
    def get_body(header):
        for sibbling in header.next_siblings:
            if sibbling.name == 'div':
                return sibbling

    # Chunks: [Chunk]
    # Chunk:
    #  main: string
    #  bullets: [string]
    @staticmethod
    def get_chunks(body):
        chunks = []
        bullets = ""

        lastChunk = {}
        for sibbling in body.findChildren():
            if sibbling.name == 'p':
                if 'Go deeper' in sibbling.text or "Editor's note" in sibbling.text in sibbling.text:
                    continue
                lastChunk = {
                    'main': Article.clean_chunk(sibbling),
                    'bullets': []
                }
                chunks.append(lastChunk)
                continue
            elif sibbling.name == 'ul':
                lastChunk['bullets'].append(Article.clean_chunk(sibbling))
                continue
        return chunks

    @staticmethod 
    def clean_chunk(chunk):
        chunk_content = []
        for content in chunk.contents:
            if content.name == 'strong':
                # Keep text if it doesn't end with : to deal with case beginning of sentence is just bold
                clean_content = content.text.strip()
                if content.text.strip()[-1] != ':':
                    chunk_content.append(clean_content)
            if content.name != 'strong':
                clean_content = content.text.strip().strip(':').strip().lstrip(',').lstrip()
                chunk_content.append(clean_content)
        return ' '.join(chunk_content)
