import pandas as pd

# Generate question without quote and space, remember to clean the output file to avoid duplication every time you run it

# infile = open("C:\SentStrength_Data\data\question_tab.txt", 'r', encoding='utf-8') # open file for appending
# outfile = open("C:\SentStrength_Data\data\question_tab_withquote.txt","a", encoding='utf-8') # open file for appending
#
# for line in infile.readlines():
#     outfile.write("\"" + line.strip("\n")+" \"\n")
#     print("\"" + line.strip("\n")+" \"\n")
#
# infile = open("C:\SentStrength_Data\data\question_tab_withquote.txt", 'r', encoding='utf-8') # open file for appending
# outfile = open("C:\SentStrength_Data\data\question_tab_withquote_noSpace.txt","a", encoding='utf-8') # open file for appending
#
# for line in infile.readlines():
#     outfile.write(line.replace(" \"", "\""))
#     print(line.replace(" \"", "\""))
#
# infile.close()
# outfile.close()


# Appending question after sentiment rating
# a = pd.read_csv("C:\SentStrength_Data\data\Report\Cleaned_result\question_sentiment_result_strongest.csv")
# b = pd.read_csv("C:\SentStrength_Data\data\question_tab_withquote_noSpace.txt")
# # merged = a.merge(b, how='outer')
# merged = pd.concat([a, b], axis=1)
# merged.to_csv("C:\SentStrength_Data\data\Report\Cleaned_result\question_sentiment_result_strongest_withQuestions.csv", index=False)

