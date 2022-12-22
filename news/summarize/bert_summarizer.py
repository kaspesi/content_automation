from summarizer import Summarizer
from article_summarizer import ArticleSummarizer

class BertSummarizer(ArticleSummarizer):

    def __init__(self):
        super().__init__()
        self.summarized_collection_str = "bert"
    
    def transform_text(self, text):
        bert_model = Summarizer()
        result = bert_model(text, num_sentences=4)
        return result
