from csvwriter import read_csv
from scrapers import get_poem_detail
import pandas as pd
import random
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
        return f"\"{self.get_poem()['text'][1:101]}...\" -- Read the featured poem \"{self.get_poem()['title']}\", by {self.get_poem()['author']}"

df = pd.read_csv('FILENAME.csv')
(author,title,link) = tuple(df.sample(1).iloc[0])

auth = Poem(author,title,link)

