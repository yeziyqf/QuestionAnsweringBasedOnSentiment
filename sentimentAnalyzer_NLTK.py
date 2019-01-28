import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk import tokenize
import pandas as pd
nltk.download('punkt')
nltk.download('vader_lexicon')

file = pd.read_csv('C:\SentStrength_Data\data\question_tab_withquote_noSpace.txt',
            delimiter=',', encoding='utf-8', names=['question'])
print(file)
file.iloc[:, 0].tolist()


sentences = ["I want to lose weight.",  # positive sentence example
             "VADER is smart, handsome, and funny!",
             # punctuation emphasis handled correctly (sentiment intensity adjusted)
             "VADER is very smart, handsome, and funny.",
             # booster words handled correctly (sentiment intensity adjusted)
             "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
             "VADER is VERY SMART, handsome, and FUNNY!!!",
             # combination of signals - VADER appropriately adjusts intensity
             "VADER is VERY SMART, really handsome, and INCREDIBLY FUNNY!!!",
             # booster words & punctuation make this close to ceiling for score
             "The book was good.",  # positive sentence
             "The book was kind of good.",  # qualified positive sentence is handled correctly (intensity adjusted)
             "The plot was good, but the characters are uncompelling and the dialog is not great.",
             # mixed negation sentence
             "A really bad, horrible book.",  # negative sentence with booster words
             "At least it isn't a horrible book.",  # negated negative sentence with contraction
             ":) and :D",  # emoticons handled
             "",  # an empty string is correctly handled
             "Today sux",  # negative slang handled
             "Today sux!",  # negative slang with punctuation emphasis handled
             "Today SUX!",  # negative slang with capitalization emphasis
             "Today kinda sux! But I'll get by, lol"
             # mixed sentiment example with slang and constrastive conjunction "but"
             ]

sid = SentimentIntensityAnalyzer()
total = 0
positive = 0
negative = 0
significance = 0
threshold = 0.1
for sentence in sentences:
    ss = sid.polarity_scores(sentence)
    # print(ss['compound'], ss['neg'], ss['neu'], ss['pos'])
    if (ss['compound'] > threshold) or (ss['compound'] < -1 * threshold):
        print(sentence)
        for k in sorted(ss):
            print('{0}: {1}, '.format(k, ss[k]), end='')
        print()
        print()
        significance += 1
        if ss['compound'] > 0.1:
            positive +=1
        if ss['compound'] < -0.1:
            negative += 1
    total += 1

print('total: ' + str(total))
print('significance: ' + str(significance))
print('positive: ' + str(positive))
print('negative: ' + str(negative))
print('significance percent: ' + str(significance/total))
