#imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%config InlineBackend.figure_format = 'retina'
import viz # curriculum example visualizations

np.random.seed(29)

## Exercise # 1

# How likely is it that you roll doubles when rolling two dice? give two variables to two separate rolls

# my solution
n_trials = nrows = 10_000 # reminder of rows and columns when putting into function
n_dice = ncols = 1
roll_1 = np.random.choice([1, 2, 3, 4, 5, 6], size = (n_trials, n_dice)) 
roll_2 = np.random.choice([1, 2, 3, 4, 5, 6], size = (n_trials, n_dice))
roll_test = roll_1 == roll_2
roll_test.mean()

#Class Solution
n_trials = nrows = 10_000 # reminder of rows and columns when putting into function
n_dice = ncols = 2
rolls = np.random.choice([1, 2, 3, 4, 5, 6], size = (n_trials, n_dice))
rolls[:,0] == rolls[:,1].sum() / 10000

## Exercise 2

#If you flip 8 coins, what is the probability of getting exactly 3 heads? 
# What is the  probability of getting more than 3 heads?

n_trials = nrows = 10_000 # reminder of rows and columns when putting into function
n_coin = ncols = 8
#Using random.choice()
coin_flip = np.random.choice([True, False], size = (n_trials, n_coin))
coin_flip
sums_by_trial = coin_flip.sum(axis=1)

coin_flip = pd.DataFrame(coin_flip)
coin_flip

sums_by_trial = pd.Series(sums_by_trial)

coin_flip['sums_by_trial'] = sums_by_trial

coin_flip.head()

#Probability of getting exactly three heads
len(coin_flip[sums_by_trial == 3]) / n_trials

# Class Solution
flips = np.random.choice([0,1], size = (100_000, 8))
flips.sum(axis = 1)
(flips.sum(axis = 1) == 3).mean()

#Probability of getting more than three heads
len(coin_flip[sums_by_trial > 3]) / n_trials

# Class Solution
(flips.sum(axis = 1) > 3).mean()

## Exercise 3

# There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. 
# Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that
# the two billboards I drive past both have data science students on them?

p_ds = .25
ncols = 2
n_simulated_billboards = nrows = 10**5

billboards = np.random.choice([0,1], size =(nrows, ncols), p =[0.75, 0.25])
p = (billboards.sum(axis =1) == 2).mean()

# Convert from probability to odds:
1-p

odds = p/(1-p)
odds
##approximately 1/14 odds

## Exercise 4

# Codeup students buy, on average, 3 poptart packages with a standard deviation of 1.5 a day from
# the snack vending machine. If on monday the machine is restocked with 17 poptart packages, how likely 
# is it that I will be able to buy some poptarts on Friday afternoon? 
# (Remember, if you have mean and standard deviation, use the np.random.normal) You'll need 
# to make a judgement call on how to handle some of your values

n_simulations = nrows = 10**5 # number of trials
n_days = ncols = 5 # number of elements in each trial

poptarts = np.random.normal(loc = 3.0, scale = 1.5, size = (nrows, n_days))
poptarts

# Turn into a dataframe
poptarts_df = pd.DataFrame(poptarts, columns=['day_1', 'day_2', 'day_3', 'day_4', 'day_5'])
poptarts_df.head()
weekly_poptarts = poptarts_df.sum(axis=1) # axis = 1 means by row
len(poptarts_df[weekly_poptarts <= 16]) / len(poptarts_df)
poptarts_df['weekly_poptarts'] = weekly_poptarts # append poptarts df with new row of total weekly poptarts

# chances you can get a poptart friday afternoon
friday_poptart = len(poptarts_df[weekly_poptarts <= 16]) / len(poptarts_df) # used boolean
friday_poptart

## Exercise 5

#Compare Heights

# Men have an average height of 178 cm and standard deviation of 8cm.
# Women have a mean of 170, sd = 6cm.
# Since you have means and standard deviations, you can use np.random.normal to generate observations. 
# If a man and woman are chosen at random, what is the likelihood the woman is taller than the man?

# Creating simulated height sample n 10_000
w_height = np.random.normal(170, 6, size = 10000)
m_height = np.random.normal(178, 8, size = 10000)
#Turning arrays into series
w_height = pd.Series(w_height) # turning array into series
m_height = pd.Series(m_height)

#turning series into dataframe
w_height_df = pd.DataFrame(w_height)
m_height_df = pd.DataFrame(m_height)
height_df = pd.concat([w_height_df, m_height_df], axis=1)

#Make it presentable
height_df.columns =['womens_height', 'mens_height']

#Find out the likelihood that women are taller then men
height_df.womens_height > height_df.mens_height # generates number of rows where this is the case
height_df[height_df.womens_height > height_df.mens_height] # takes this list and applies to entire dataframe
len(height_df[height_df.womens_height > height_df.mens_height]) # gets number of rows where this is true
len(height_df[height_df.womens_height > height_df.mens_height]) / len(height_df) # probability where this is true

## Exercise 6

# When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted 
# and the installation fails. What are the odds that after having 50 students download anaconda, 
# no one has an installation issue? 100 students?
# What is the probability that we observe an installation issue within the first 150 students that download anaconda?
# How likely is it that 450 students all download anaconda without an issue?

anaconda_sim_50 = np.random.choice([True, False], size = 50)
anaconda_sim_100 = np.random.choice([True, False], size = 100)

#
#0 = no issues, 1 = issue
install = np.random.choice([0,1], size = [10000, 50], p = [249/250, 1/250])
install

#probability of 0 issues for 50 installations
(install.sum(axis=1) == 0).mean()

#Probability of 0 issues for 150 installations
install_150 = np.random.choice([0,1], size = (10000, 150), p = [249/250, 1/250] )
install_150
(install_150.sum(axis=1) ==0).mean()

#Probability of 0 issues for 450 students
install_450 = np.random.choice([0,1], size = (10000, 150), p = [249/250, 1/250] )
(install_450.sum(axis = 1) ==0).mean()

## Exercise 7

# There's a 70% chance on any given day that there will be at least one food truck at Travis Park. 
# However, you haven't seen a food truck there in 3 days. How unlikely is this?
# How likely is it that a food truck will show up sometime this week?
trucks = np.random.choice( [0,1], size = (10000, 3), p= [0.3, 0.7] )
trucks

# However, you haven't seen a food truck there in 3 days. How unlikely is this?
#probability that no truck shows up in 3 days
(trucks.sum(axis=1) == 0).mean()

## How likely is it that a food truck will show up sometime this week?
trucks_wk = np.random.choice( [0,1], size = (10000, 5), p= [0.3, 0.7] )
trucks_wk
(trucks_wk.sum(axis=1) >= 1).mean() # 1 boolean means they will come

## Exercise 8

# If 23 people are in the same room, what are the odds that two of them share a birthday? 
# What if it's 20 people? 40?
#simulation of 10000 rooms with 23 people
bd = np.random.choice(range(1,366), size = (10000, 23))
bd
#making dataframe
pd.DataFrame(bd).nunique(axis = 1)

#Which percentage of simulated rooms with a shared birthday
(pd.DataFrame(bd).nunique(axis = 1) < 23).mean()

# What about 20 people in the room?
bd_20 = np.random.choice(range(1,366), size = (10000, 20))
pd.DataFrame(bd_20).nunique(axis = 1)
(pd.DataFrame(bd_20).nunique(axis = 1) < 20).mean()

# What about 40 people in the room?
bd_40 = np.random.choice(range(1,366), size = (10000, 40))
pd.DataFrame(bd_40).nunique(axis = 1)
(pd.DataFrame(bd_40).nunique(axis = 1) < 40).mean()