from summarizer import Summarizer
from news.summarize.article_summarizer import ArticleSummarizer

class BertSummarizer(ArticleSummarizer):

    def __init__(self):
        super().__init__()
        self.summarized_collection_str = "bert"
    
    def summarize_text(self, text):
        bert_model = Summarizer()
        result = bert_model(text, num_sentences=4)
        return result
