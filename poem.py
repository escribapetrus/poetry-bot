from scrapers import get_poem_detail
import pandas as pd
import requests

class Poem:
    def __init__(self,author,title,link):
        self.author = author
        self.title = title
        self.link = link
    
    def get_poem(self):
        text = get_poem_detail(self.link)
        return text

    def get_tweet(self):
        return f"\"{self.get_poem()['text'][1:121]}...\" -- Read the featured poem \"{self.get_poem()['title']}\", by {self.get_poem()['author'].upper()}: {self.link}"



