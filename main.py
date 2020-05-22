from csvwriter import read_csv, write_csv
from scrapers import folha_horoscope, metropole_horoscopes 
flatten = lambda l: [item for sublist in l for item in sublist]

pkmn = [
    [{'num': 1,'name':'bulbasaur'},
    {'num': 2,'name':'venusaur'},
    {'num': 3,'name':'ivysaur'}],
    [{'num': 4,'name':'charmander'},
    {'num': 5,'name':'charmeleon'},
    {'num': 6,'name':'charizard'}],
    [{'num':7,'name':'squirtle'},
    {'num':8,'name':'wartortle'},
    {'num':9,'name':'blastoise'}]
]

write_csv("horoscopes.csv",'w',flatten(metropole_horoscopes()))