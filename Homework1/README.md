# Readme for homework1

## Instruction

This readme file contains:

1)Instructions that are necessary for running scripts under this folder.

2)Answers to each question asked in the exercises 1-4.

3)How I proved my code was correct using different tests.

4)Any other relevant information. 

## Support
If you have any question, please feel free to [contact me](https://github.com/QingyangYu0529/BIS-634-QingyangYu#Maintainer).

Any comments or insights would be greatly appreciated.



## Exercise 1

### Question
Write a function temp_tester that takes a definition of normal body temperature and returns a function that returns True if its argument is within 1 degree of normal temperature (i.e. the value is a healthy temperature), and False if not (10 points). 

Test your code with the following (include a copy of your tests in [your GitHub](https://github.com/QingyangYu0529/BIS-634-QingyangYu) repository) (10 points):

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework1/Figures-in-homework-question/exercise1.jpg" style="zoom:120%;" />

### Solution

#### >> Code explanation: 

Using the concept of "closure(it is allowed to return a function)" so that every time we run the function temp_tester, function set_temp_tester also runs, which is designed to decide whether a given temperature temp is beyond normal temperature normal_temp by using if/else, if the temperature is normal, print 'TRUE', otherwise print 'False'.

#### >> Testing process:

During testing process, at first the normal temperatures of human and chicken are set as 37 ℃ and 41.1℃ separately.
After different temperatures are given to human or chicken, the code could successfully decide whether the given temperature is normal (consider as within 1 degree of the normal temperature).



## Exercise 2

### Question:

Download the sqlite3 database from [hw1-population.db](https://yale.instructure.com/courses/70314/files/5320045?wrap=1). 
(Note: this is a link to a page where you can download the database; it is not the database.)
Use the following code to load it into Python as a pandas DataFrame:
<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework1/Figures-in-homework-question/exercise2.jpg" style="zoom:120%;" />

Examine data. What columns does it have? (2 points) How many rows (think: people) does it have? (2 points)
Examine the distribution of the ages in the dataset. In particular, be sure to have your code report the mean, standard deviation, minimum, maximum. Plot a histogram of the distribution with an appropriate number of bins for the size of the dataset (describe in your readme the role of the number of bins). Comment on any outliers or patterns you notice in the distribution of ages. (3 points)
Repeat the above for the distribution of weights. (3 points)
Make a scatterplot of the weights vs the ages. (3 points) Describe the general relationship between the two variables (3 points). You should notice at least one outlier that does not follow the general relationship. What is the name of the person? (3 points) Be sure to explain your process for identifying the person whose values don't follow the usual relationship in the readme. (3 points)

### Solution

#### >> Code explanation: 
1)Using .columns to see how many columns are in this dataframe.

2)Using .groupby to see how many people(not repetitive rows) in this dataframe.

3)Using .describe to generate statistical description on the dataframe. Using .loc to locate the data in the 'age' column. 

4&5)Imported matplotlib to draw the histogram and scatterplot in order to visualize the distribution of ages and weights. Using .xlabel, .ylabel, .title to set the x-axis label, y-axis label and figure title.

6)From the scatterplot, I have noticed an outlier whose age is among 40-50, and weight is among 20-30. 

First, the dataframe was transposed for further use since pandas dataframe is hard to process directly. Then in the defined function find_outlier(), I created a list called name_list(at first is empty), to store the names in the dataframe. Then I used for loop to go through all the elements in transposed dataframe(also use range() and len() to achieve this). I used if/else as conditional statements:

According to the above scatterplot, the filter condition refers to when age is among 40-50, and weight is among 20-30. Then the name of that person was added to the name_list.

#### >> Question answer: 

1)The dataframe has four columns: 'name', 'age', 'weight', 'eyecolor', and the datatype is 'object'.

2)There are 137592 people(non-repetitive rows) in this dataframe.

3)For 'age' data, the count is 152361, the mean is 39.51, the standard deviation is 24.15, the minimum is 0.00074, the maximum is 99.99.

4)The number of bins indicates the size of statistical interval. If the number of bins is large, the statistical interval is quite small. While on the contrary, the interval is large.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework1/Figures-in-running-result/exercise2/histogram-of-age-distribution.jpg" style="zoom:200%;" />

> Patterns noticed in the distribution of ages:

> Noticed that for people in the dataset, their ages follow uniform distribution in two ranges: either in the range [0,70], or in the range [70,100].

> For people whose ages range [0,70], the amount of people in every age is almost the same(~10000). And for people whose ages range [70,100], the amount of people in every age is almost the same(~2000).

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework1/Figures-in-running-result/exercise2/histogram-of-weight-distribution.jpg" style="zoom:200%;" />

> Patterns noticed in the distribution of weights:

> Noticed that for people in the dataset, for most of the people(~20%), their weights are around 68-70 kg.

5)The general relationship between ages and weights:

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework1/Figures-in-running-result/exercise2/scatterplot-weights-vs-ages.jpg" style="zoom:200%;" />

> Noticed that for people in the dataset, the weights of young people(aged from 0 to ~20) increase with ages, and the increase rate is steady, indicating a proportional increase. 

> As people grow older (aged from 20 to 100), their weights remain stable. 

> Also noticed that for people aged over 60, their weights slightly decrease.

6)The name of that person(outlier) is Anthony Freeman.

#### >> Testing process:

Function test_find_outlier() was defined for testing if the outlier I found is a real outlier. 

I used for loop to traverse the whole dataframe, use if as conditional statement: if the name is 'Anthony Freeman', print his age and weight.

In total I found two records from Anthony Freeman: first record showed his age is 41.3, and his weight is 21.7. Second record showed his age is 33.3, and his weight is 74.0. According to the scatterplot of ages vs weights, the mean of ages or weights, the first record is a real outlier.



## Exercise 3

### Question

Download historical data for COVID-19 cases by state from The New York Times's GitHub at [link](https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv.
(Links to an external site.). 
As this is an ongoing public health crisis, include in your readme the date you downloaded the data (2 points). Since you are using data from an external source, be sure to credit The New York Times as your data source in your readme as well (2 points).
Load the data into Python in any way you wish. Here's one way that gives you a DataFrame assuming you've put the data in your working directory:
<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework1/Figures-in-homework-question/exercise3.jpg" style="zoom:120%;" />

Make a function that takes a list of state names and plots their cases vs date using overlaid line graphs, one for each selected state. (Edit 2021-09-03: You can plot either the number of new cases, a smoothed average of the last n days, or the running total; just be clear what you're doing.) Be sure to provide a way to tell which line corresponds to what state (one possibility: using colors and a legend). If your approach has any specific limitations, explain them in your readme. (4 points)
Test the above function and provide examples of it in use. (4 points)
Make a function that takes the name of a state and returns the date of its highest number of new cases. (4 points)
Make a function that takes the names of two states and reports which one had its highest number of cases first and how many days separate that one's peak from the other one's peak. (e.g. Connecticut had its highest number of cases in mid-January, whereas Colorado's peak number of cases was in November 2020, so Colorado had its highest number of cases about 2 months before Connecticut.) (5 points)
Test the above function and provide examples of it in use. (4 points)

### Solution

#### >> Code explanation: 

1)Using np.random.choice to randomly select five states in the dataset. The names of these five states are saved in the list data_state0.

2)First, the dataframe was transposed for further use. The function cases_vs_date_of_states() was defined, which is used to plot cases vs. dates of selected states in the list data_state0.

In the function cases_vs_date_of_states(), I created two lists DataDate_list and DataCases_list, in order to store the dates and cases of selected states. Then I used DataDate_list, DataCases_list, in order to store the dates and cases of selected states. I used if/else as conditional statement, traverse the whole dataframe: If the state of element is in the data_state0, save the date and cases of this state into two lists DataDate_list and DataCases_list. Finally, I used matplotlib.pyplot to draw the overlaid line graphs, one for each selected state. Also used .xlabel, .ylabel, .title, .legend to set the x-axis label, y-axis label, figure title and upper left lengend.

3)The function return_highest_date() was defined, which is used to take the name of a state, and return the date of its highest number of new cases. then I created lists sel_state_cases, sel_state_date, daily_cases to save the cases, date and number of daily cases of selected state. I used for loop three times to solve the problem:

The first one was coupled with if/else to traverse the whole dataframe: If the state of element is the selected state, save the date and cases of selected state into lists sel_state_cases, sel_state_date.

The second one was used to calculate daily cases by latter substract former. results are saved into list daily_cases.

The final one was used to find the largest element in the list daily_cases, and save into the variable highest_cases. The corresponding date was saved into the variable highest_cases_date.

4)The function compare_states_highest_cases() was defined, which takes the names of two states and reports which one had its highest number of cases first and how many days separate that one's peak from the others. 

First I used the above function return_highest_date to get the highest cases number of two states, marked as date1 and date2. Then used parse_date to parse date/time of string type into date type, and calculated for how many days/months between these two dates, saved in the variable separate_days, separate_months. Then used if/else as conditional statement, to report which one had its highest number of cases first: If separate_days is bigger than zero, state1 had its highest number of cases first, otherwise state2 had first.

#### >> Question answer:

1)The date I downloaded the data is 2021/09/07.

2)Note: Data used in this exercise came from [The New York Times's GitHub](https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv).

3)Noted that in the overlaid line graphs, x-axis indicates dates developed over time, y-axis indicates the cumulative (total)cases of each selected state. Colors of lines indicate different states.

This function could be used to monitor the total COVID-19 cases or disease increase rate in every state of US. Federal or state officials could indicate the trand showed in the figure, then adjust public health actions in different states.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework1/Figures-in-running-result/exercise3/overlaid_line_graph_5_states.jpg" style="zoom:200%;" />

4)For the function compare_states_highest_cases() (takes the names of two states and reports which one had its highest number of cases first and how many days separate that one's peak from the others), it could be used to see the pattern of covid-19 transmission between adjacent states. If one state has reached the highest number of new cases, when will the state nearby also reach its peak? 

Also it could be used to map the route of covid-19 transmission. In terms of states that reach their peak really fast, what are the possible factors that may contribute to this result? This could urge state or local officials to take public health actions.

#### >> Testing process: 

1)Function cases_vs_date_of_states() was defined for plotting cases vs. dates of selected states.

I run the function to see whether it is able to draw a figure based on the given background, also tested the above function by drawing another overlaid line graph of ten different states that were randomly selected.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework1/Figures-in-running-result/exercise3/overlaid_line_graph_10_states.jpg" style="zoom:200%;" />

2)Function return_highest_date() was defined, which is used to take the name of a state, and return the date of its highest number of new cases.

i.I test the function by giving a state name 'Washington', to see whether it could return the date of its highest number of new cases.

I also defined two functions to test the function return_highest_date():

ii.Since I used state 'Washington' to test the function return_highest_date(), I defined function test_for_return_highest_date1(), in which a list two_cases was created to save the dates(when highest cases occur and the day before that day) of state Washington. Then I calculated the number of highest cases by substracting the two elements in two_cases. The result 8346 is same as that in the function return_highest_date(). 

iii.I defined another testing function test_for_return_highest_date2(), to see if function return_highest_date() could print the result regardless of which state it is. First I saved all the state names into list unique_state, then used for loop to traverse the list unique_state. For each state, run function return_highest_date(). Results indicate that return_highest_date() works for each state.

3)Function test_for_compare_states_highest_cases() was defined, to see if function compare_states_highest_cases() could make comparison between each two states. Results indicate that compare_states_highest_cases() works for each two states.



## Exercise 4

### Question

In class on September 2, we discussed a randomized response protocol. Let's simulate it and see what insights we can gain about the relationship between sample size, population size, and predicted accuracy. In particular:
4a. Make a function that takes a population size n and a number of drug users d and returns a list of size n with d True values and n - d False values. The Trues represent drug users, the Falses represent non-drug users. (2 points)

4b. Make a function that selects a sample of size s (think: study participants) from such a population and returns that sample's responses to the protocol from the slides. In particular, for each study participant, they flip a coin (choose one of two paths randomly with equal probability). If they flip "heads", they flip a coin and either report True or False (with equal probability). If instead, they flip "tails", they report their drug use status (True or False). (Hint: You can select a sample of a population using random.sample) (3 points)

4c. Make a function that takes parameters for the total population, the true number of drug users in the population, the sample size, and returns the estimated number of drug users in the population that would be predicted using such a sample and the randomized response protocol. (Hint: recall from class that the E[yes] = 0.25 + 0.5p, where p is the fraction of drug users; use the measured yes rate to predict the fraction p. EDIT 2021-09-07: if the predicted rate is less than 0, assume 0.) (3 points) (EDIT 2021-09-07: for 3 extra-credit points, analyze the going negative issue in some way that is interesting to you and provide a brief written discussion and either a figure or a statistical analysis.)

4d. Suppose that we have a population of 1000 people, 100 of whom are drug users and we do a survey using this protocol that samples 50 people from the total population. What is the estimated number of drug users you get from such an approach? (3 points)

4e. Your results in part d will obviously depend on which 50 people you surveyed and how their coin-flips worked out. To get a sense of the distribution, repeat the experiment many times (justify how you decided how many was enough in your readme; 2 points) and plot a histogram showing the predictions (4 points).

4f. Repeat parts d and e but with a population of 100_000 people, 10_000 drug users and sampling 5_000 people; i.e. with everything scaled up by a factor of 100. (5 points) How do your results compare? (3 points)

4g. Repeat parts d and e but with 500 drug users in a population of 1_000 and sampling 50 people. i.e. with the smaller population but with higher drug usage rates. (5 points) How do your results compare? (3 points)

### Solution

#### >> Code explanation: 

1)The function report_druguse_state0() was defined in order to take a population size n and a number of drug users d, and return a list of size n with d True values and n - d False values. First I created the list druguse_results, to print the results of drug use in the population. Also I created variable rest, to save the number of non-drug users. Then I used two while loop: for each drug user, print 'True', and for each non-drug user, print 'False'.

2)The function report_druguse_states1() was defined, which could return samples' responses to the randomized response protocol from the slides. 

First I created several lists including: pop_result to save the results of drug use in the population, flip_choice1, flip_choice2 to list the possible results of flip coins for two times, flip_result1, final_result to save the results after the first coin flip and the samples' reponses.

Then I used two for loop to save the results of drug use in the population into pop_result. I used random.sample to select a sample of size s from such population, save into sample_result. I used for loop to save the result of first coin flip into flip_result1. Then I used zip function to store sample_result and flip_result1 in a list samp_and_flip_result1 in order.

Finally I traversed each element in the list samp_and_flip_result1, use if/else to simulate the process of second coin flip: If the result of first coin flip is 'Head', flip a coin again as the sample's response; if the result of first coin flip is 'Tail' and the sampled person is a drug user, 'True' is the sample's response, otherwise 'False' is the response. And I used for loop to print the result of samples' reponses.

3)The function report_druguse_states2() was defined, which could return the estimated number of drug users in the population that would be predicted using such a sample and the randomized response protocol. 

The function is developed based on report_druguse_states1(). I used for loop to calculate the number of sampled people that reported 'True', save in the variable yes. Also the measured yes rate measured_yes_rate, the fraction of drug users in the population p, the estimated number of drug users in the population that could be predicted using such a sample estimated_druguser_in_pop were calculated.

4)The function repeat_function() was defined to repeat the experiment many times. I created list estimated_druguser to save all the results of estimated number of drug users, and used for loop to repeat the function report_druguse_states2() and saved results in the list estimated_druguser.

To visualize the results, I used matplotlib.hist to draw the histagram of numbers of estimated drug users.


#### >> Question answer: 

1)Discussion of E[yes] negative issue:
If estimated number of drug users in the population is negative, then the fraction of drug users in the population p is negative. 

According to the given fomula, E[yes]<0.25, which means in the sampled population, less than 25% people said they are drug users(said 'True'). 

This makes sense if there are few drug users in the whole population, or the sampled population can not present the whole population.


2)According to the question 4d, n = 1000, d = 100, s = 50. And The estimated number of drug users is 60.
Note: Every time you run the code, the estimated number of drug users would change due to randomly sample.

3)According to the question 4e, in order to decide how many running times was enough, I set different running times to see if running time increases, the distribution of estimated_druguser(estimated number of drug users in the population) will be stable, and the estimated number of drug user in the population with highest frequency is similar to the given number of drug users.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework1/Figures-in-running-result/exercise4/exercise4e.jpg" style="zoom:200%;" />

> Noted that when running time reaches 100000, the distribution remain quite stable. Also the estimated number of drug user in the population with highest frequency is similar to the given background(~100 people).

4)

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework1/Figures-in-running-result/exercise4/exercise4f.jpg" style="zoom:200%;" />

> Compared the figure with the former one, with everything scaled up by a factor of 100(n=100000, d=10000, s=5000), the figure become very compact. The distribution intervel is much bigger as well(5000-15000) Also the estimated number of drug user in the population with highest frequency has become much bigger(~10000 people). This is due to scaled up of the whole population.

5)

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework1/Figures-in-running-result/exercise4/exercise4g.jpg" style="zoom:200%;" />

> Compared the figure with the first one, with the smaller population but with higher drug usage rates(n=1000, d=500, s=50), the estimated number of drug user in the population with highest frequency has become much bigger(~500 people). This is because I increased the number of total drug users. The distribution intervel is slightly bigger(0-1000). I assume that if the total population has much higher drug usage rates, the estimated number of drug user in the population is more likely to be a positive number.



#### >> Testing process: 

1)I tested the function report_druguse_state0() by randomly set population size n and number of drug users d.

2)I tested the function report_druguse_state1() by randomly set population size n, number of drug users d and sample size s.

3)I tested the function report_druguse_state2() by randomly set population size n, number of drug users d and sample size s.



## Data source

Data of exercise2 comes from [hw1-population.db](https://yale.instructure.com/courses/70314/files/5320045?wrap=1).

Data of exercise3 comes from [The New York Times's GitHub](https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv).



## Maintainer
@QingyangYu0529
| Name        | Email                | Organization                                                 |
| :---------: | ---------------------| ------------------------------------------------------------ |
| Qingyang Yu | qingyang.yu@yale.edu | Graduate student, Yale School of Public Health, Yale University |
