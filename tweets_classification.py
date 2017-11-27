import re
import os
import csv

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

RE_NUMBERS = re.compile(r'[0-9]+')
RE_NOT_LETTERS = re.compile(r'[^a-zA-Z]+')
RE_SPACES = re.compile(r'[^\S\f\t\n\r]+')

def clean_tweet(tweet):
    tweet = RE_NUMBERS.sub(' NUM ', tweet)
    tweet = RE_NOT_LETTERS.sub(' ', tweet)
    tweet = RE_SPACES.sub(' ', tweet)
    return tweet.lower()
    # return re.sub('[^a-zA-Z]+', ' ', tweet).lower()

def write_to_csv():
    '''
    Converts all txt tweets files into one single csv file
    '''
    tweets = []
    tweets_files_folder = 'tweets_1000_day/raw'
    tweets_file_list = os.listdir(tweets_files_folder)

    with open("tweets_1000_day/all_clean_tweets.csv", "w", newline="") as tweets_csv:
        spamwriter = csv.writer(tweets_csv, delimiter=';')
        for file_name in tweets_file_list:
            print(file_name)
            with open(tweets_files_folder + '/' + file_name, encoding='utf-8') as txt_file:
                current_file_date = file_name[4:14]
                tweets = [clean_tweet(line.strip()) for line in txt_file]
                for tweet in tweets:
                    spamwriter.writerow([str(current_file_date), tweet.replace(';', ',')])

def main():
    with open('tweets_1000_day/all_clean_tweets_labeled.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        rows = [row for row in spamreader]

    # Eliminating empty tweets
    tweets = [row for row in rows if not row[1] == " "]
    tweets_text = [tweet[1] for tweet in tweets]

    # Tweet takes part on training set if it is labeled (third column)
    tweets_training_set = [tweet for tweet in tweets if len(tweet) == 3]
    tweets_text_training_set = [tweet[1] for tweet in tweets_training_set]
    print(tweets_text_training_set)
    
    # Bag of words
    count_vect = CountVectorizer()
    x_train_counts = count_vect.fit_transform(tweets_text_training_set)
    print(x_train_counts.shape)

    # Machine Learning
    # Training Naive Bayes (NB) classifier on training data.
    # clf = MultinomialNB().fit(x_train_counts, twenty_train.target)

if __name__ == '__main__':
    # main()
    write_to_csv()