## Exercises

### For each of the following questions, formulate a null and alternative hypothesis (be as specific as you can be), then give an example of what a true positive, true negative, type I and type II errors would look like. Note that some of the questions are intentionally phrased in a vague way. It is your job to reword these as more precise questions that could be tested.

#### 1. Has the network latency gone up since we switched internet service providers?
# - ISP 1 vs ISP 2 (discrete, boolean, isp_switch)
# - Network latency (continuous, net_latency)
# - Comparison of means of two groups (t-test)

# H{0} : latency (mean a) is less than or equal latency b(mean)

# H{a}: latency (mean a) is greater than latency (mean b)

# True Positive: Reject H{0} when H{0} is false (latency went up and we said it did)

# True Negative: Accept H{0} when H{0} is true (fail to reject H{0} (latency didnt go up and we said it didnt)

# Type 1 error: Latency did not go up with ISP switch, but we said it did

# Type 2 error: Latency did go up with ISP switch, but we said it didnt

#### 2. Is the website redesign any good?

# - Question: Are we getting more traffic on the website since the website redesign?
# - Variables: Website redesign (web_redesign),discrete, boolean ('True' or 'False) AND web traffic hits (traffic_rate), continuous variable
# - H{0}: There is no difference in website traffic since the website redesign
# - H{a}: There is a significant difference in website trafic since the redesign

# True Positive: Reject H{0} when H{0} is false (Traffic is greater than before and after website redesign and we said it would be greater)

# True Negative: Accept H{0} when H{0} is true (fail to reject H{0}) (Traffic is less than or equal to the rate when website was redesigned, and we said it would be less than or equal)

# Type 1 Error: There is no significant increase in website traffic since the redesign, but we conclude that there is a significant increase in website traffic with website redesign (we reject the null)

# Type 2 Error: There is a significant increase in website traffic since the redesign, but we conclude that the traffic level is less than or the same as before (we accept the null)




#### 3.  Is our television ad driving more sales?
# Question: Did the television add increase sales for the company?

# Variables: TV_ad (discrete/categorical), boolean (True, False); Sales figures ('sales'), continuous variable

# H{0}: The introduction of a TV add had no significant impact on sales (sales2 <= sales 1)
# H{a}: The introduction of a TV add had a significant impact on sales (sales 2 > sales 1)

# True Positive: Reject H{0} when H{0} is false (The TV add drove more sales, and we said the TV add drove more sales)

# True Negative: Accept H{0} when H{0} is true (The TV add did not drive more sales, and we agreed with (H0) that there was no signficant increase in sales with the new TV add)

# Type 1 error: There was no increase in sales with the new TV ad, but we conclude there is a significant increase in sales from the TV ad (we rejected the null)

# Type 2 error: There was a significant increase in sales with the new TV ad, but we conclude that there is no significant increase in sales (we accepted the null)

## Exercises

import numpy as np
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt

### For each of the following questions, formulate a null and alternative hypothesis (be as specific as you can be), then give an example of what a true positive, true negative, type I and type II errors would look like. Note that some of the questions are intentionally phrased in a vague way. It is your job to reword these as more precise questions that could be tested.

#### 1. Has the network latency gone up since we switched internet service providers?
- ISP 1 vs ISP 2 (discrete, boolean, isp_switch)
- Network latency (continuous, net_latency)
- Comparison of means of two groups (t-test)

H{0} : latency (mean a) is less than or equal latency b(mean)

H{a}: latency (mean a) is greater than latency (mean b)

True Positive: Reject H{0} when H{0} is false (latency went up and we said it did)

True Negative: Accept H{0} when H{0} is true (fail to reject H{0} (latency didnt go up and we said it didnt)

Type 1 error: Latency did not go up with ISP switch, but we said it did

Type 2 error: Latency did go up with ISP switch, but we said it didnt

#### 2. Is the website redesign any good?

- Question: Are we getting more traffic on the website since the website redesign?
- Variables: Website redesign (web_redesign),discrete, boolean ('True' or 'False) AND web traffic hits (traffic_rate), continuous variable
- H{0}: There is no difference in website traffic since the website redesign
- H{a}: There is a significant difference in website trafic since the redesign

True Positive: Reject H{0} when H{0} is false (Traffic is greater than before and after website redesign and we said it would be greater)

True Negative: Accept H{0} when H{0} is true (fail to reject H{0}) (Traffic is less than or equal to the rate when website was redesigned, and we said it would be less than or equal)

Type 1 Error: There is no significant increase in website traffic since the redesign, but we conclude that there is a significant increase in website traffic with website redesign (we reject the null)

Type 2 Error: There is a significant increase in website traffic since the redesign, but we conclude that the traffic level is less than or the same as before (we accept the null)




#### 3.  Is our television ad driving more sales?
Question: Did the television add increase sales for the company?

Variables: TV_ad (discrete/categorical), boolean (True, False); Sales figures ('sales'), continuous variable

H{0}: The introduction of a TV add had no significant impact on sales (sales2 <= sales 1)
H{a}: The introduction of a TV add had a significant impact on sales (sales 2 > sales 1)

True Positive: Reject H{0} when H{0} is false (The TV add drove more sales, and we said the TV add drove more sales)

True Negative: Accept H{0} when H{0} is true (The TV add did not drive more sales, and we agreed with (H0) that there was no signficant increase in sales with the new TV add)

Type 1 error: There was no increase in sales with the new TV ad, but we conclude there is a significant increase in sales from the TV ad (we rejected the null)

Type 2 error: There was a significant increase in sales with the new TV ad, but we conclude that there is no significant increase in sales (we accepted the null)



#### T-Test Exercises

### 1.  Answer with the type of test you would use (assume normal distribution):

# - Is there a difference in grades of students on the second floor compared to grades of all students?
#     - One sample T-Test

# 2. Are adults who drink milk taller than adults who dont drink milk?
#     - Two sample T-test (Independent T-Test), one tail
    

# 3. Is the the price of gas higher in texas or in new mexico?
#     - Two sample T-Test (Independent T-Test), one tail
    
    
# 4. Are there differences in stress levels between students who take data science vs students who take web development vs students who take cloud academy?
#     - ANOVA


### 2. Ace Realty wants to determine whether the average time it takes to sell homes is different for its two offices. A sample of 40 sales from office #1 revealed a mean of 90 days and a standard deviation of 15 days. A sample of 50 sales from office #2 revealed a mean of 100 days and a standard deviation of 20 days. Use a .05 level of significance.

# H0: means are equal between groups (average time to sell at office 1 = office 2)
# Ha: means are not equal between groups (average time to sell at office != office 2)
# alpha: 0.05
# Simulation to generate dataset ##This could have been solved using rvs
office_1 = np.random.normal(90, 15, 40)
office_2 = np.random.normal(100, 20, 50)

#Need to ensure variances are equal
stat, pval = stats.levene(office_1, office_2)
if pval < 0.05:
    print('We can reject H0 ==> inequal variance')
pval
# pval over 0.05 so we assume variances are equal

#Compute test statistic
alpha = 0.05
t, p = stats.ttest_ind(office_1, office_2)
t, p

#verify significance
if p < alpha:
    print('We can reject the null hypothesis, there is a significant difference in mean between office 1 and office 2')
else:
    print('we fail to reject the null hypothesis, there is no difference in mean sales between office 1 and office 2')

### 3. Load the mpg dataset and use it to answer the following questions:
Is there a difference in fuel-efficiency in cars from 2008 vs 1999?

from pydataset import data
mpg = data('mpg')
mpg.head()

#Set Hypothesis

#H0: There is no significant difference in fuel economy between 99 and 08 car models
#Ha: There is a significant difference between the mean of fuel economy in 99 and 08 car models

# Create another column for fuel efficiency
#Use Harmonic mean because it is a rate
mpg['total_mpg'] = 2/(1/mpg.cty + 1/mpg.hwy)

#place each car year into their own variable
cars_99 = mpg[mpg.year == 1999].total_mpg
cars_08 = mpg[mpg.year == 2008].total_mpg

#reset index
cars_99.reset_index(inplace = True, drop = True)
cars_08.reset_index(inplace = True, drop = True)

# n of 99 model year cars
len(cars_99)

#Visualize Data
cars_99.hist()
cars_08.hist()

# n of each car df
len(cars_08)
len(cars_99)

#check variance equality
alpha = .05
stat, pval = stats.levene(cars_99, cars_08)
print(pval)
# Variances are equal, we can continue

# Compute test statistic
tstat, pval = stats.ttest_ind(cars_99, cars_08)
tstat, pval

if (pval < alpha) and (tstat > 0):
    print("we can reject the null hypothesis")
else:
    print('We fail to reject the null hypothesis: There is no significant difference in fuel economy between 99 and 08 car models')

### Are compact cars more fuel-efficient than the average car?

# One sample test (vs population)
# One tailed test
mpg.head()

#Set Hypothesis

#H0: Compact car fuel efficiency is less than or equal to the average car fuel efficiency (mean cc < mean avg)
#Ha: Compact cars fuel efficiency is greater than the average car (mean of compact car fuel efficiency > 
# average car fuel efficiency)

compact_cars = mpg[mpg['class'] == 'compact'].total_mpg

#Visualize problem
compact_cars.hist()

#Get test statistic values
average_cars = mpg.total_mpg.mean()
average_cars

#Compute test statistic
alpha = 0.05
tstat, pval = stats.ttest_1samp(compact_cars, average_cars)

tstat, pval

#Conclusion
#verify significance
if (pval / 2 < alpha) and (tstat > 0):
    print("we can reject the null hypothesis: compact cars are more fuel efficient than the average car")
else:
    print('We fail to reject the null hypothesis')

### Do manual cars get better gas mileage than automatic cars?

#Hypotheses:

$H0$: Manual cars gas mileage <= automatic car gas mileage

$Ha$: Manual cars gas mileage > automatic car gas mileage

#Type of test selection?
One-tailed, two sample t-test

#Use value_counts
mpg.trans.value_counts()

man_cars = mpg[mpg.trans.str.contains('manual')].total_mpg
auto_cars = mpg[mpg.trans.str.contains('auto')].total_mpg

#Visualize the data
man_cars.hist()

auto_cars.hist()

#Check n size
man_cars.count()
auto_cars.count()

#check variance equality
alpha = .05
stat, pval = stats.levene(man_cars, auto_cars)
print(pval)
#Variances are equal, we can continue

# Compute test statistic
tstat, pval = stats.ttest_ind(man_cars, auto_cars)
tstat, pval

#Conclusion
#verify significance
if (pval / 2 < alpha) and (tstat > 0):
    print("we can reject the null hypothesis: gas mileage of manual cars is greater than gas mileage of auto cars")
else:
    print('We fail to reject the null hypothesis, gas mileage of manual cars is less than or equal to gas mileage of auto cars')