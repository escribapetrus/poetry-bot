import pandas as pd

from csv_manage import read_csv, write_csv
from poem import Poem
from tweeter import api as tweeter

df = pd.read_csv('poem_list.csv')
(author,title,link) = tuple(df.sample(1).iloc[0])

poem = Poem(author,title,link)
tweet = poem.get_tweet()
tweeter.update_status(tweet)
print("Twitter update\n{}".format(tweet))

