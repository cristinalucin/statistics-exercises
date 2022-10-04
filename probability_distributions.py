# Exercises

### For the following problems, use python to simulate the problem and calculate an experimental probability, then compare that to the theoretical probability.

# pyplot for plotting
import matplotlib.pyplot as plt
# numpy for vectorized array operations
import numpy as np
# pandas for proper tabular manipulation
import pandas as pd
# scipy stats for our subversions
from scipy import stats

### 1. A bank found that the average number of cars waiting during the noon hour at a drive-up window follows a Poisson distribution with a mean of 2 cars. Make a chart of this distribution and answer these questions concerning the probability of cars waiting at the drive-up window.

λ = 2
μ = 2
drive_thru = stats.poisson(λ)

# Visualization


#What is the probability that no cars drive up in the noon hour?
drive_thru
drive_thru.pmf(0)

#What is the probability that 3 or more cars come through the drive through?
drive_thru.sf(2) #greater than 2 encompasses 3

#How likely is it that the drive through gets at least 1 car?
drive_thru.sf(0) # greater than 0

### 2. Grades of State University graduates are normally distributed with a mean of 3.0 and a standard deviation of .3. Calculate the following:

μ = 3.0
σ = .3
gpa = stats.norm(μ, σ)

# What grade point average is required to be in the top 5% of the graduating class?
gpa.isf(0.05)

# What GPA constitutes the bottom 15% of the class?
gpa.ppf(0.15)

# An eccentric alumnus left scholarship money for students in the third decile from the bottom of their class.
# Determine the range of the third decile. Would a student with a 2.8 grade point average qualify for this scholarship?

gpa.ppf(.30)
gpa.ppf(.20)
# They would qualify
range_of_gpas = gpa.ppf([0.2,0.3])
range_of_gpas

# If I have a GPA of 3.5, what percentile am I in?
gpa.cdf(3.5) #less than or equal to, use cdf

### 3. A marketing website has an average click-through rate of 2%. One day they observe 4326 visitors and 97 click-throughs. How likely is it that this many people or more click through?

click_rate = 0.02
visitors = 4326
click throughs = 97

#Using scipy stats module
# Binomial Parameters:

# trials: 4326
# probability of success: 0.5

trials = 4326
prob = 0.02

coin_flips = stats.binom(trials, prob)
coin_flips

coin_flips.sf(96) #we need more than 96 (97)

### 4. You are working on some statistics homework consisting of 100 questions where all of the answers are a probability rounded to the hundreths place. Looking to save time, you put down random probabilities as the answer to each question. What is the probability that at least one of your first 60 answers is correct?

#Using scipy stats module
# Binomial Parameters:

# trials: 100
# probability of success: 0.01

trials = 60 #n
prob = 0.01

stats_hw = stats.binom(trials,prob)
stats_hw

stats_hw.sf(0)

### 5. The codeup staff tends to get upset when the student break area is not cleaned up. Suppose that there's a 3% chance that any one student cleans the break area when they visit it, and, on any given day, about 90% of the 3 active cohorts of 22 students visit the break area. How likely is it that the break area gets cleaned up each day? How likely is it that it goes two days without getting cleaned up? All week?

#Using scipy stats module
# Binomial Parameters:

# trials: 100
# probability of success: 0.03

trials = 59
prob = 0.03

cleanup = stats.binom(trials,prob)
cleanup

# How likely is it that the break area gets cleaned up each day?
cleanup.sf(0)

# How likely is it that it goes two days without getting cleaned up?
stats.binom(trials*2, prob).pmf(0)

# All week?
stats.binom(trials*5, prob).pmf(0)

### 6. You want to get lunch at La Panaderia, but notice that the line is usually very long at lunchtime. After several weeks of careful observation, you notice that the average number of people in line when your lunch break starts is normally distributed with a mean of 15 and standard deviation of 3. If it takes 2 minutes for each person to order, and 10 minutes from ordering to getting your food, what is the likelihood that you have at least 15 minutes left to eat your food before you have to go back to class? Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.

#Assume normal distribution, mean is in minutes
μ = 15
σ = 3
lunch = stats.norm(μ*2, σ*2)
lunch.cdf(33)

###  7. Connect to the employees database and find the average salary of current employees, along with the standard deviation. For the following questions, calculate the answer based on modeling the employees salaries with a normal distribution defined by the calculated mean and standard deviation then compare this answer to the actual values present in the salaries dataset.
What percent of employees earn between 65,000 and 80,000?
What do the top 5% of employees make?

from env import get_db_url

url = get_db_url('employees')

sql = '''
SELECT
    salary,
    to_date
FROM salaries
WHERE salaries.to_date == '9999-01-01'
'''

salaries = pd.read_sql(sql, url)
salaries.head()

#make a dataframe
salaries = pd.DataFrame(salaries)
salaries.head()

#lets get some statistics
salaries.salary.mean()
salaries.salary.std()
salaries.count()

# What percent of employees earn between 65,000 and 80,000?
μ = 63810.75
σ = 16904.83
salary = stats.norm(μ, σ)
np.diff(stats.norm(μ, σ).cdf([65000, 80000]))

#What percent of employees earn less than 60,000?
salary.cdf(60000)
# calculating from dataset
len(salaries[salaries.salary < 60000]) / len(salaries)

# What percent of employees earn more than 95,000?
salary.sf(95000)
# old way taking from dataset
#len(salaries[salaries.salary > 95000]) / len(salaries)

#What do the top 5 percent of employees make?
salary.isf(0.05)

