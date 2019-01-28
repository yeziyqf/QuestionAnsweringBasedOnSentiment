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
sentences = file.iloc[:, 0].tolist()
# print(sentences)
# print(len(sentences))

sid = SentimentIntensityAnalyzer()
total = 0
positive = 0
negative = 0
significance = 0
threshold = 0.4
df = pd.DataFrame([])
for sentence in sentences:
    ss = sid.polarity_scores(sentence)
    # print(ss['compound'], ss['neg'], ss['neu'], ss['pos'])
    if (ss['compound'] > threshold) or (ss['compound'] < -1 * threshold):
        # print(sentence)
        df_new = pd.DataFrame([[sentence]])
        df = pd.concat([df, df_new])
        # for k in sorted(ss):
        #     print('{0}: {1}, '.format(k, ss[k]), end='')
        # print()
        # print()
        significance += 1
        if ss['compound'] > 0.1:
            positive += 1
        if ss['compound'] < -0.1:
            negative += 1
    total += 1

print(df)
print(df_new)
# df.to_csv("C:\SentStrength_Data\data\Report\Intersection data\selectedQuestion_NLTK.txt", index=False)

print('total: ' + str(total))
print('significance: ' + str(significance))
print('positive: ' + str(positive))
print('negative: ' + str(negative))
print('significance percent: ' + str(significance/total))
