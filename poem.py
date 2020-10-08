#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapers import get_poem_detail

class Poem:
    def __init__(self,author,title,link):
        self.author = author
        self.title = title
        self.link = link
    
    def get_poem(self):
        text = get_poem_detail(self.link)
        return text

    def get_tweet(self):
        return f"\"{self.get_poem()['text'][1:121]}...\" -- Lisez ma choix de poème du jour \"{self.get_poem()['title']}\", de {self.get_poem()['author'].upper()}: {self.link}"



