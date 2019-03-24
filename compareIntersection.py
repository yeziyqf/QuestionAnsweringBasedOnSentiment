import csv

NLTK = set()
with open ('C:\SentStrength_Data\data\Report\Intersection data\selectedQuestion_NLTK_threshold0.4.txt', encoding= 'utf-8') as f:
    for row in csv.reader(f):
        portion = row[0]
        NLTK.add(portion)
        # print(portion)

sentiStrength = set()
with open ('C:\SentStrength_Data\data\Report\Intersection data\selectedQuestion_sentiStrength_threshold_3.txt', encoding= 'utf-8') as g:
    for row in csv.reader(g):
        portion = row[0]
        sentiStrength.add(portion)
        # print(portion)

standfordCoreNLP = set()
with open ('C:\SentStrength_Data\data\Report\Intersection data\standfordCoreNLP_withSentiment.txt', encoding= 'utf-8') as g:
    for row in csv.reader(g):
        portion = row[0]
        standfordCoreNLP.add(portion)
        # print(portion)

# results = NLTK & sentiStrength
# results = NLTK & sentiStrength & standfordCoreNLP
results = sentiStrength & standfordCoreNLP

print('There are', len(results), 'matching addresses between the two csv files')

# for result in sorted(results):
#     print(result)