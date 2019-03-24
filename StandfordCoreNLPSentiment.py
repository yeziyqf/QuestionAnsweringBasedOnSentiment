# Please run the stadford server using
# java -mx5g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 10000 first
# notice because we write in append mode, remember to delete previous file when run writing script

from pycorenlp import StanfordCoreNLP
import pandas as pd
import pickle

# file = pd.read_csv('C:\SentStrength_Data\data\question_tab_withquote_noSpace_withouSharpColumn.txt',
#             delimiter=',', encoding='utf-8', names=['question'])

data_set = pickle.load(open("C:/Thesis_work/Question-Answer-Selection/data/myData/QAs_sent.pickle",'rb'))
print('training set')
print(data_set['q'])

sentences = data_set['q'].tolist()
sentences = sentences[29951:]

# print(file)
# sentences = file.iloc[:, 0].tolist()

nlp = StanfordCoreNLP('http://localhost:9000')

positive_count = 0
negative_count = 0
neutral_count = 0
count = 29951
pos_list = []
neu_list = []
neg_list = []

print()
df_neu = pd.DataFrame([])
df_pos = pd.DataFrame([])
df_neg = pd.DataFrame([])

# res = nlp.annotate("how do you solve:  (2x^-2y^3)^2(-4x^2y^-6)/6x^9y^3   thanks?",
#                    properties={
#                        'annotators': 'sentiment',
#                        'outputFormat': 'json',
#                        'timeout': 1000,
#                        'encoding': 'utf-8'
#                    })
#
# for s in res["sentences"]:
#     print("%d: '%s': %s %s" % (
#         s["index"],
#         " ".join([t["word"] for t in s["tokens"]]),
#         s["sentimentValue"], s["sentiment"]))

for sentence in sentences:
    try:
        res = nlp.annotate(sentence,
                           properties={
                               'annotators': 'sentiment',
                               'outputFormat': 'json',
                               'timeout': 1000,
                           })
        # print(res)
        # print(sentence + ' ' + res['sentences'][0]['sentiment'] + ' ' + res['sentences'][0]['sentimentValue'])
        if res['sentences'][0]['sentiment'] == 'Neutral':
            neutral_count += 1
            neu_list.append(count)
            # print(count)
            # print('Neu: ' + sentence)
            # df_tmp = pd.DataFrame([[sentence]])
            # df_neu = pd.concat([df_neu, df_tmp])
            # df_tmp.to_csv("C:\SentStrength_Data\data\Report\StandfordCoreNLP\standfordCoreNLP_neutral.txt", mode='a',
            #               header=False, index=False)
        if res['sentences'][0]['sentiment'] == 'Negative':
            negative_count += 1
            neg_list.append(count)
            # print(count)
            # print('Neg: ' + sentence)
            # df_tmp = pd.DataFrame([[sentence]])
            # df_neg = pd.concat([df_neg, df_tmp])
            # df_tmp.to_csv("C:\SentStrength_Data\data\Report\StandfordCoreNLP\standfordCoreNLP_negative.txt", mode='a',
            #               header=False, index=False)
        if res['sentences'][0]['sentiment'] == 'Positive':
            positive_count += 1
            pos_list.append(count)
            # print(count)
            # print('Pos: ' + sentence)
            # df_tmp = pd.DataFrame([[sentence]])
            # df_pos = pd.concat([df_pos, df_tmp])
            # df_tmp.to_csv("C:\SentStrength_Data\data\Report\StandfordCoreNLP\standfordCoreNLP_positive.txt", mode='a',
            #               header=False, index=False)

        count += 1
        # if count%100 == 0:
        #     print(df_neg)
        print('positive_count: ' + str(positive_count))
        print('negative_count: ' + str(negative_count))
        print('neutral_count: ' + str(neutral_count))
        print('Total count: ' + str(count))
        if neutral_count == 4000:
            with open("C:/Thesis_work/Question-Answer-Selection/data/myData/neu_list.txt", "w") as output:
                for s in neu_list:
                    output.write("%s\n" % s)
    except Exception:
        pass  # or you could use 'continue'
    if (positive_count + negative_count) >= 4000:
        break


# print('positive_count: ' +  str(positive_count))
# print('negative_count: ' +  str(negative_count))
# print('neutral_count: ' +  str(neutral_count))
# print('Total count: ' + str(total))

# print(df_pos)
# df_neu.to_csv("C:\SentStrength_Data\data\Report\StandfordCoreNLP\standfordCoreNLP_neutral.txt", index=False)
# df_pos.to_csv("C:\SentStrength_Data\data\Report\StandfordCoreNLP\standfordCoreNLP_positive.txt", index=False)
# df_neg.to_csv("C:\SentStrength_Data\data\Report\StandfordCoreNLP\standfordCoreNLP_negative.txt", index=False)

# Write row number to file
with open("C:/Thesis_work/Question-Answer-Selection/data/myData/pos_list.txt", "w") as output:
    for s in pos_list:
        output.write("%s\n" % s)

with open("C:/Thesis_work/Question-Answer-Selection/data/myData/neg_list.txt", "w") as output:
    for s in neg_list:
        output.write("%s\n" % s)

with open("C:/Thesis_work/Question-Answer-Selection/data/myData/sent_list.txt", "w") as output:
    for s in neg_list:
        output.write("%s\n" % s)
    for s in pos_list:
        output.write("%s\n" % s)