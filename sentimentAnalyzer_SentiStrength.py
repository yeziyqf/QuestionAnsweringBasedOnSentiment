import pandas as pd

file = pd.read_csv('C:\SentStrength_Data\data\Report\Cleaned_result\question_sentiment_result_strongest_withQuestions.csv',
            delimiter=',', encoding='utf-8', names=['positive', 'negative', 'question'])
print(file)

positive_count = 0
negative_count = 0
emotionSignificance = 0
total = 0

thresholdPositive = 3
thresholdNegative = 3
TotalEmotionThreshold = 3

print('PositiveThreshold: ' + str(thresholdPositive))
print('NegativeThreshold: ' + str(thresholdNegative))
print('TotalEmotionThreshold: ' + str(TotalEmotionThreshold))
print()
df = pd.DataFrame([])

for index, row in file.iterrows():
    # print(row["positive"], row["negative"])
    if abs(row['positive']) >= thresholdPositive:
        positive_count += 1
    if abs(row['negative']) >= thresholdNegative:
        negative_count += 1
    if (abs(row['positive'])+abs(row['negative'])) >= TotalEmotionThreshold:
        emotionSignificance += 1
        # print(row["question"] + ', pos: ' + str(row["positive"]) + ' ,neg: ' + str(row["negative"]))
        df_new = pd.DataFrame([[row["question"]]])
        df = pd.concat([df, df_new])
    total += 1

print('Positive: ' + str(positive_count))
print('Negative: ' + str(negative_count))
print('Total Records Count: ' + str(total))
print('Positive significance percent: ' + str(positive_count/total))
print('Negative significance percent: ' + str(negative_count/total))

# ones satisfied emotion significance threshold
print('Total emotion significance count: ' + str(emotionSignificance))
print('Total emotion significance percent: ' + str(emotionSignificance/total))

df.to_csv("C:\SentStrength_Data\data\Report\Cleaned_result\selectedSentiStrengththresholdData\selectedQuestion_sentiStrength_threshold_" + str(TotalEmotionThreshold) + ".txt", index=False)