import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Manually set data for each chatbot and parameter
# Each inner list represents the values for a single chatbot (Chatbot 1 to Chatbot 5)
# Columns represent values for parameters A, B, C, D, and E


data_array = np.genfromtxt('chatbot_ratings_Most_Likable.csv',delimiter=',', skip_header=1)


data = [[0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]
#                      range of responses for that task                 
#task-1  -   1-11         0,11
#task-2  -   12-23        11,22
#task-3    - 24-34         22,33
#task-4   -  35-44          33,43
#task-5  -   45-53          43,53


for j in range(2,7):
    for i in range(0,11):           #change range of i according to task
        data[j-2][5-int(data_array[i,j])] = data[j-2][5-int(data_array[i,j])]+1


# Labels for chatbots and parameters
groups = ['Openness to experience', 'Conscientiousness ', 'ExtraVersion ', 'Agreeableness ', 'Neutral ']
parameters = ['Rank 5', 'Rank 4', 'Rank 3', 'Rank 2', 'Rank 1']

data = np.array(data)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate cumulative data for stacked plotting
cumulative_data = np.cumsum(data, axis=1)

# Colors for each parameter
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Plot each parameter as a part of the horizontal bar and add labels
for i, param in enumerate(parameters):
    if i == 0:
        bars = ax.barh(groups, data[:, i], color=colors[i], label=param)
    else:
        bars = ax.barh(groups, data[:, i], left=cumulative_data[:, i-1], color=colors[i], label=param)
    
    # Add text labels in the center of each segment
    for bar, value in zip(bars, data[:, i]):
        ax.text(bar.get_x() + bar.get_width() / 2, 
                bar.get_y() + bar.get_height() / 2,
                str(value),
                ha='center', va='center', color='black', fontsize=9)

# Add labels, title, and legend
ax.set_xlabel("Values")
ax.set_title("Most Likable chatbot")
ax.legend(title="Parameters", bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout to fit the legend and avoid overlap
plt.tight_layout()
plt.show()