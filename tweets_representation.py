import re
import os
import csv

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

def clean_tweet(tweet):
	'''
	Keep only letters on tweets
	Lower case letters
	'''
	return re.sub('[^a-zA-Z]+', ' ', tweet).lower()

def train():
	tweets = []

	with open('miranda/caveira.txt', encoding='utf-8') as txt_file:
		tweets = [clean_tweet(line.strip()) for line in txt_file]
		print(tweets[0])

def write_to_csv():
	tweets = []
	tweets_files_folder = 'tweets_1000_day/raw'
	tweets_file_list = os.listdir(tweets_files_folder)

	with open("all_clean_tweets.csv", "w", newline="") as tweets_csv:
		spamwriter = csv.writer(tweets_csv, delimiter=';')
		for file_name in tweets_file_list:
			with open(tweets_files_folder + '/' + file_name, encoding='utf-8') as txt_file:
				current_file_date = file_name[4:14]
				tweets = [clean_tweet(line.strip()) for line in txt_file]
				for tweet in tweets:
					spamwriter.writerow([str(current_file_date), tweet.replace(';', ',')])

def main_2():
	with open('tweets_1000_day/all_clean_tweets.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
		for row in spamreader:
			print(row)

def main():
	tweets = []
	tweets_files_folder = 'tweets_1000_day/raw'
	tweets_file_list = os.listdir(tweets_files_folder)

	'''
	Read tweets from txt file
	'''
	for file_name in tweets_file_list:
		with open(tweets_files_folder + '/' + file_name, encoding='utf-8') as txt_file:
			tweets += [clean_tweet(line.strip()) for line in txt_file]
			print(str(file_name) + ", " + str(len(tweets)))

	# Bag of words
	count_vect = CountVectorizer()
	x_train_counts = count_vect.fit_transform(tweets)
	print(x_train_counts.shape)

	# TF-IDF stuff
	tfidf_transformer = TfidfTransformer()
	x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)
	print(x_train_tfidf.shape)

	# Machine Learning
	# Training Naive Bayes (NB) classifier on training data.
	# clf = MultinomialNB().fit(x_train_tfidf, twenty_train.target)

if __name__ == '__main__':
	main_2()
	# write_to_csv()