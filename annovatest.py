import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.stats.multicomp as mc
import statsmodels.api as sm


#here chatbot_ratings_Most_Likable.csv contains data responses from participant
#format -> participant , task , chatbot1_rank , chatbot2_rank ,chatbot3_rank ,chatbot4_rank , chatbot5_rank

data_array = np.genfromtxt('chatbot_ratings_Most_Likable.csv',delimiter=',', skip_header=1)

chatbots = [[],[],[],[],[]]

for j in range(2,7):
    for i in range(0,53):
        chatbots[j-2].append(data_array[i,j])
        #data[j-1][5-int(data_array[i,j])] = data[j-1][5-int(data_array[i,j])]+1

f_stat, p_value = stats.f_oneway(chatbots[0], chatbots[1], chatbots[2],chatbots[3],chatbots[4])


print("F-Statistic:", f_stat)
print("P-Value:", p_value)

data = {
    'ChatBot': ['Openness'] * 53 + ['Conscientiousness'] * 53 + ['ExtraVersion'] * 53 + ['Agreeableness'] * 53 +['Neutral'] * 53,
    'Scores': []
}
for j in range(2,7):
    for i in range(0,53):
        data['Scores'].append(data_array[i,j])

df = pd.DataFrame(data)

tukey = mc.MultiComparison(df['Scores'], df['ChatBot'])
tukey_results = tukey.tukeyhsd()

# Print the results
print("\nTukey's HSD Results:\n")
print(tukey_results.summary())


