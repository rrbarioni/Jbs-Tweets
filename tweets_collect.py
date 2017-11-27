'''
Script for getting tweets from JBS event (May 17th of 2017)
You shall execute "chcp 65001" before "py jbs.py"

Plano:
    pegar tweets a partir de 17/11/2016 e até 17/11/2017
    5000 tweets por mês? 1000 tweets por dia?
    verificar palavras-chave de tweets relacionados ao evento da delação da JBS ("Temer", "Cunha", "delação", etc)
        procurar nos tweets de perto do acontecido, pra considerar que o tweet está relacionado à delação
    usar conjunto de palavras-chave obtido pra filtar todos os tweets obtidos, a fim de ver se o tweet está relacionado à delação (ou não)
'''

import get_old_tweets as got
from date_util import *

jbs_keywords = []

unicode_encode_error_not_covered = [
    "\u200b"
]

def get_tweets(query_search, start_date, end_date, tweets_amount):
    file = open("tweets/" + str(query_search) + "_" + str(start_date) + "_" + str(end_date) + "_" + str(tweets_amount) + ".txt", "w", encoding="utf8")
    
    tweetCriteria = got.manager.TweetCriteria()\
        .setQuerySearch(query_search)\
        .setSince(start_date)\
        .setUntil(end_date)\
        .setMaxTweets(tweets_amount)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    tweets_text = [tweet.text for tweet in tweets]
    for char in unicode_encode_error_not_covered:
        tweets_text = [text.replace(char, " ") for text in tweets_text]

    for tweet in tweets_text:
        file.write(tweet)
        file.write("\n")

    file.close()

# pegar tweets a partir de 17/11/2016 e até 17/11/2017
# 5000 tweets por mês
def tweets_5000_month():
    query_search = "jbs"
    start_date = "2016-11-17"
    end_date = "2017-11-17"
    tweets_amount = 5000

    current_date = start_date
    while month_after(current_date) != end_date:
        get_tweets(
            query_search=query_search,
            start_date=current_date,
            end_date=month_after(current_date),
            tweets_amount=tweets_amount
        )
        current_date = month_after(current_date)

# pegar tweets a partir de 17/11/2016 e até 17/11/2017
# 1000 tweets por dia
def tweets_1000_day():
    query_search = "jbs"
    start_date = "2016-11-17"
    end_date = "2017-11-17"
    tweets_amount = 1000

    current_date = start_date
    while current_date != end_date:
        print("current_date: " + current_date)

        get_tweets(
            query_search=query_search,
            start_date=current_date,
            end_date=day_after(current_date),
            tweets_amount=tweets_amount
        )
        current_date = day_after(current_date)

if __name__ == '__main__':
    tweets_1000_day()