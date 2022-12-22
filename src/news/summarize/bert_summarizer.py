from summarizer import Summarizer
from news.summarize.article_summarizer import ArticleSummarizer
from colorama import Fore, Style

class BertSummarizer(ArticleSummarizer):

    def __init__(self):
        super().__init__()
        self.summarized_collection_str = "bert"
        self.bert_model = Summarizer()
    
    def summarize_text(self, text):
        try:
            result = self.bert_model(text, num_sentences=4)
            return result
        except Exception as e:
            print(Fore.RED + e + Style.RESET_ALL)
            return ""
