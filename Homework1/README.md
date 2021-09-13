# Readme for homework1
## Instruction
This readme file contains:

1)instructions that are necessary for running scripts under this folder

2)answers to each question asked in the exercises 1-4

3)how I proved my code was correct using different tests

4)any other relevant information. 

## Support
If you have any question, please feel free to [contact me].(https://github.com/QingyangYu0529/BIS-634-QingyangYu#Maintainer)

Any comments or insights would be greatly appreciated.

## Exercise 1

### Question
Write a function temp_tester that takes a definition of normal body temperature and returns a function that returns True if its argument is within 1 degree of normal temperature (i.e. the value is a healthy temperature), and False if not (10 points). 

Test your code with the following (include a copy of your tests in [your GitHub](https://github.com/QingyangYu0529/BIS-634-QingyangYu) repository) (10 points):

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework1/Figures-in-homework-question/exercise1.jpg" style="zoom:150%;" />

### Solution

#### >> Code explanation: 

Using the concept of "closure(it is allowed to return a function)" so that every time we run the function temp_tester, function set_temp_tester also runs, which is designed to decide whether a given temperature temp is beyond normal temperature normal_temp by using if/else, if the temperature is normal, print 'TRUE', otherwise print 'False'.

#### >> Tesing process:

During tesing process, at first the normal temperatures of human and chicken are set as 37 ℃ and 41.1℃ separately.
After different temperatures are given to human or chicken, the code could successfully decide whether the given temperature is normal (consider as within 1 degree of the normal temperature).

## Exercise 2

### Question:

Download the sqlite3 database from [hw1-population.db] (https://yale.instructure.com/courses/70314/files/5320045?wrap=1). (Note: this is a link to a page where you can download the database; it is not the database.)
Use the following code to load it into Python as a pandas DataFrame:
<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework1/Figures-in-homework-question/exercise2.jpg" style="zoom:150%;" />

Examine data. What columns does it have? (2 points) How many rows (think: people) does it have? (2 points)
Examine the distribution of the ages in the dataset. In particular, be sure to have your code report the mean, standard deviation, minimum, maximum. Plot a histogram of the distribution with an appropriate number of bins for the size of the dataset (describe in your readme the role of the number of bins). Comment on any outliers or patterns you notice in the distribution of ages. (3 points)
Repeat the above for the distribution of weights. (3 points)
Make a scatterplot of the weights vs the ages. (3 points) Describe the general relationship between the two variables (3 points). You should notice at least one outlier that does not follow the general relationship. What is the name of the person? (3 points) Be sure to explain your process for identifying the person whose values don't follow the usual relationship in the readme. (3 points)

### Solution

#### >> Code explanation: 
1)Using .columns to see how many columns are in this dataframe.

2)Using .groupby to see how many people(not repetitive rows) in this dataframe.


3)Using .describe to generate statistical description on the dataframe. Using .loc to locate the data in the 'age' column. 

4&5)Import matplotlib to draw the histogram and scatterplot in order to visualize the distribution of ages and weights. Using .xlabel, .ylabel, .title to set the x axis label, y axis label and figure title.

6)From the scatterplot, I have noticed an outlier whose age is among 40-50, and weight is among 20-30. 

First, the dataframe was transposed for further use since pandas dataframe is hard to process directly. Then in the function I defined find_outlier(), I created a list called name_list(at first is empty). Then I used for loop to go through all the elements in transposed dataframe(also use range() and len() to achieve this). I used if as conditional statements. 

According to the above scatterplot, the filter condition refers to when age is among 40-50, and weight is among 20-30. Then the name of that person was added to the name_list.

#### >> Question answer: 
1)The dataframe has four columns: 'name', 'age', 'weight', 'eyecolor', and the datatype is 'object'.

2)There are 137592 people(non-repetitive rows) in this dataframe.

3)For 'age' data, the count is 152361, the mean is 39.51, the standard deviation is 24.15, the minimum is 0.00074, the maximum is 99.99.

4)The number of bins indicates the size of statistical interval. If the number of bins is large, the statistical interval is quite small. While on the contrary, the interval is large.

> Patterns noticed in the distribution of ages:

> Noticed that for people in the dataset, their ages follow uniform distribution in two ranges: either in the range [0,70], or in the range [70,100].

> For people whose ages range [0,70], the amount of people in every age is almost the same(~10000). And for people whose ages range [70,100], the amount of people in every age is almost the same(~2000).

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework1/Figures-in-running-result/histogram-of-age-distribution.jpg" style="zoom:150%;" />

> Patterns noticed in the distribution of weights:

> Noticed that for people in the dataset, for most of the people(~20%), their weights are around 68-70 kg.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework1/Figures-in-running-result/histogram-of-weight-distribution.jpg" style="zoom:150%;" />

5)The general relationship between ages and weights:

Noticed that for people in the dataset, the weights of young people(aged from 0 to ~20) increase with ages, and the increase rate is steady, indicating a proportional increase. 

As people grow older (aged from 20 to 100), their weights remain stable. 

Also noticed that for people aged over 60, their weights slightly decrease.

6)The name of that person(outlier) is Anthony Freeman.

#### >> Tesing process:
Function test_find_outlier() is defined for testing if the outlier I found is a real outlier. 

I use for loop to travase the whole dataframe, use if as conditional statement: if the name is 'Anthony Freeman', print his age and weight.

In total I found two records from Anthony Freeman: first record showed his age is 41.3, and his weight is 21.7. Second record showed his age is 33.3, and his weight is 74.0. According to the scatterplot of ages vs weights, the mean of ages or weights, the first record is a real outlier.

## Exercise 3

### Question

Download historical data for COVID-19 cases by state from The New York Times's GitHub at [link](https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv (Links to an external site.). 
As this is an ongoing public health crisis, include in your readme the date you downloaded the data (2 points). Since you are using data from an external source, be sure to credit The New York Times as your data source in your readme as well (2 points).
Load the data into Python in any way you wish. Here's one way that gives you a DataFrame assuming you've put the data in your working directory:
<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework1/Figures-in-homework-question/exercise3.jpg" style="zoom:150%;" />

Make a function that takes a list of state names and plots their cases vs date using overlaid line graphs, one for each selected state. (Edit 2021-09-03: You can plot either the number of new cases, a smoothed average of the last n days, or the running total; just be clear what you're doing.) Be sure to provide a way to tell which line corresponds to what state (one possibility: using colors and a legend). If your approach has any specific limitations, explain them in your readme. (4 points)
Test the above function and provide examples of it in use. (4 points)
Make a function that takes the name of a state and returns the date of its highest number of new cases. (4 points)
Make a function that takes the names of two states and reports which one had its highest number of cases first and how many days separate that one's peak from the other one's peak. (e.g. Connecticut had its highest number of cases in mid-January, whereas Colorado's peak number of cases was in November 2020, so Colorado had its highest number of cases about 2 months before Connecticut.) (5 points)
Test the above function and provide examples of it in use. (4 points)

### Solution

#### >> Code explanation: 

1)
#### >> Question answer:

#### >> Testing process: 

## Exercise 4

### Question

### Solution

#### >> Code explanation: 

#### >> Question answer: 

#### >> Testing process: 

## Maintainer
@QingyangYu0529
| Name        | Email                | Organization                                                 |
| :---------: | ---------------------| ------------------------------------------------------------ |
| Qingyang Yu | qingyang.yu@yale.edu | Graduate student, Yale School of Public Health, Yale University |
