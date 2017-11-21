# Script for getting tweets from JBS event (May 17th of 2017)
# You shall execute "chcp 65001" before "py jbs.py"

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
