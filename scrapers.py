from bs4 import BeautifulSoup as soup
import requests

BASE_URL = "BASE URL" # USE CORRECT URL
flatten = lambda l: [item for sublist in l for item in sublist]

def get_authors(lis):
	jackie = map(lambda x: x.string, lis)
	return list(jackie)

def get_urls(lis):
	jackie = map(lambda x: x.a['href'], lis)
	return list(jackie)

def get_poem_list(url):
	author_html = requests.get(url).text
	author_soup = soup(author_html, "html.parser")
	author_articles = author_soup.findAll("article")
	author_poems = map(lambda x: {"title": x.header.a.text, "link": x.header.a['href']} ,author_articles)
	return list(author_poems)

def get_poem_detail(url):
	poem_html = requests.get(url).text
	poem_soup = soup(poem_html, "html.parser")
	text = poem_soup.find("div",{'class':'entry-content'}).text.replace("\xa0", "").replace('\n',' ')
	header = poem_soup.find('header',{'class':'entry-header'})
	return {'author': header.div.text,'title':header.h1.text,'text':text}

#get each author as {'name': name, 'poems': get_poem_list(idx)}
# example: apollinaire = [{'author':library[3][0],'poems': get_poem_list(library[3][1])}]

def scrape_site():
	base_html = requests.get(BASE_URL).text
	base_soup = soup(base_html, "html.parser")
	author_menu = base_soup.find("ul",{"id":"MENU SELECTOR"}) #USE CORRECT SELECTOR
	author_list = author_menu.findAll('li')
	authors = get_authors(author_list)
	urls = get_urls(author_list)
	library = list(zip(authors,urls))[:-1]
	all_authors = list(map(lambda x: {'author':x[0],'poems': get_poem_list(x[1])},library))
	return flatten(all_authors)

