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

query_search = "jbs"
start_date = "2017-05-16"
end_date = "2017-05-18"
max_tweets = 100

jbs_keywords = [

]

unicode_encode_error_not_covered = [
	"\u200b"
]

file = open("tweets/" + str(query_search) + "_" + str(start_date) + "_" + str(end_date) + "_" + str(max_tweets) + ".txt", "w")

tweetCriteria = got.manager.TweetCriteria()\
	.setQuerySearch(query_search)\
	.setSince(start_date)\
	.setUntil(end_date)\
	.setMaxTweets(max_tweets)
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
tweets_text = [tweet.text for tweet in tweets]
for char in unicode_encode_error_not_covered:
	tweets_text = [text.replace(char, " ") for text in tweets_text]

for tweet in tweets_text:
	file.write(tweet)
	file.write("\n")

file.close()
