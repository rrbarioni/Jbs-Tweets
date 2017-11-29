import re
import csv

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

RE_NUMBERS = re.compile(r'[0-9]+')
RE_NOT_LETTERS = re.compile(r'[^a-zA-Z]+')
RE_SPACES = re.compile(r'[^\S\f\t\n\r]+')

targets = [
    'No', # Not related to JBS delations
    'Yes' # Related to JBS delations
]

def clean_text(text):
    text = RE_NUMBERS.sub(' NUM ', text)
    text = RE_NOT_LETTERS.sub(' ', text)
    text = RE_SPACES.sub(' ', text)
    return text.lower()

def main():
    rows = []
    with open('tweets_1000_day/all_tweets_labeled_2.csv', newline='', encoding='utf-8') as csvfile:
        for row in csvfile.readlines():
            rows += [row.split(';')]

    # Cleaning tweets
    tweets = [[row[0], clean_text(row[1]), row[2]] for row in rows]
    tweets_text = [tweet[1] for tweet in tweets]
    print('Tweets\' set size: ' + str(len(tweets)))

    # Tweet takes part on training set if it is labeled (third column)
    tweets_training_set = [tweet for tweet in tweets if tweet[2] != '\r\n']
    tweets_text_training_set = [tweet[1] for tweet in tweets_training_set]
    print('Training set size: ' + str(len(tweets_training_set)))
    
    # Bag of words
    count_vect = CountVectorizer()
    x_train_counts = count_vect.fit_transform(tweets_text_training_set)
    print(x_train_counts.shape)

    # Machine Learning
    # Training Naive Bayes (NB) classifier on training data.
    # print('Starting Naive Bayes classifier training')
    # clf = MultinomialNB().fit(x_train_counts, targets)
    # print('ended')

if __name__ == '__main__':
    main()