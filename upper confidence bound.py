# %% [markdown]
# Upper Confidence Bound (UCB)

# %% [markdown]
# Importing the Libraries

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# %% [markdown]
# Importing the Data Set

# %%
df=pd.read_csv("Ads_CTR_Optimisation.csv")
df.head()

# %% [markdown]
# Implementing the UBC algorithm

# %%
import math
# total number of user 
N=10000
#! no of ads
d=10
#! no of ads selected upto 10000
Ads_Selected=[]
# list of 10 0s
number_of_selection=[0]*d
# ! sums of rewards
Sum_of_Reward=[0]*d
Total_Reward=0
for j in range(N):
    ad=0
    max_upper_bound=0
    for i in range(d):
        if (number_of_selection[i]>0):
            Average_Reward=Sum_of_Reward[i]/number_of_selection[i]
            delta_i=math.sqrt((3/2)*(math.log(j+1)/number_of_selection[i]))
            upper_bound=Average_Reward+delta_i
        else:
            upper_bound=1e400
            # make its value to max value
        if (upper_bound>max_upper_bound):
            max_upper_bound=upper_bound
            ad=i
    Ads_Selected.append(ad)
    number_of_selection[ad]+=1
    reward=df.values[j,ad]
    Sum_of_Reward[ad]+=reward
    Total_Reward+=reward            
# print(Sum_of_Reward)
# print(number_of_selection)
# print(reward)
# print(Total_Reward)
# print(Ads_Selected)


# %% [markdown]
# Visualizing the Results

# %%
plt.hist(Ads_Selected)
plt.title("Histogram of ads selected")
plt.xlabel("Ads ")
plt.ylabel("No fo time each Ad is selected")
plt.savefig("Histogram of UPPER CONFIDENCE BOUND.png")
plt.show()


