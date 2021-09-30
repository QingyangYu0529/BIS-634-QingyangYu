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

Examine the contents of [hw2-patients.xml](https://yale.instructure.com/courses/70314/files/5401025?wrap=1).  Download [hw2-patients.xmlin](https://yale.instructure.com/courses/70314/files/5401025/download?download_frd=1) a text-editor to see its structure, but in brief, there are a handful of fields you can ignore for this exercise and then several <patient> entries, all contained inside <patients>. Each <patient> has several attributes that we will want, namely name, age, and gender. Some patients have other associated data (e.g. diagnoses), but we won't need that here.

Load the data. Plot a histogram showing the distribution of ages (2 points). Do any of the patients share the same exact age? (2 points) How do you know? (2 points).
(For an extra 2 points: explain how the answer to the question about multiple patients having the same age affects the solution to the rest of the problem.)

Plot the distribution of genders. (2 points). In particular, how did this provider encode gender? What categories did they use? (2 points)
Sort the patients by age and store the result in a list (use the "sorted" function with the appropriate key, or implement sort yourself by modifying one of the algorithms from the slides or in some other way). (2 points) Who is the oldest patient? (2 points).

Identifying the oldest person from a list sorted by age should be an O(1) task... but sorting is an O(n log n) process (assuming we're using an efficient algorithm), so the total time for the above is O(n log n). Describe how (you don't need to implement this, unless that's easier than writing it out) you could find the second oldest person's name in O(n) time. (2 points). Discuss when it might be advantageous to sort and when it is better to just use the O(n) solution. (2 points).

Recall from our discussion of the motivating problem for September 9th that we can search within a sorted list in O(log n) time via bisection. Use bisection on your sorted list (implement this yourself; don't trivialize the problem by using Python's bisect module) to identify the patient who is 41.5 years old. (2 points)
Once you have identified the above, use arithmetic to find the number of patients who are at least 41.5 years old. (2 points)

Generalizing the above, write a function that in O(log n) time returns the number of patients who are at least low_age years old but are strictly less than high_age years old. (2 points) Test this function (show your tests) and convince me that this function works. (2 points). (A suggestion: sometimes when you're writing high efficiency algorithms, it helps to make a slower, more obviously correct implementation to compare with for your tests. Be sure your function works both for ages that are and are not in the dataset.)
Modify the above, including possibly the data structure you're using, to provide a function that returns both the total number of patients in an age range AND the number of males in the age range, all in O(log n) time as measured after any initial data setup. (2 points). Test it (show your tests) and justify that your algorithm works. (2 points)

### Solution


#### >> Code explanation: 

1) Imported module minidom to read xml files, imported library matplotlib to draw the figures.

Created a list age, to save ages(float type) of all patients.
Using matplotlib.pyplot to draw the histagram of ages. Using .xlabel, .ylabel, .title to set the x-axis label, y-axis label and figure title.

The function share_same_age() was defined to determine if any of the patients share the same exact age. Using if/else statement to determine whether the length of list age equals to that of set age: If the length are the same, there are no patients share the same age. Otherwise there are at least two patients share the same age.

2) Created a list gender, to save gender(string type) of all patients.

Using matplotlib.pyplot to draw the histagram of genders. use .xlabel, .ylabel, .title to set the x-axis label, y-axis label and figure title.

3) Created a list name, to save name(string type) of all patients.Using zip function to store age and name of in a list age_name_tuple. Using sorted function to sort the patients by age, and store the sorted result into the list age_sorted_result.

To find the name of the oldest patient, I used for loop to traverse all the attribute age. And used if/else statement: If the value of this element's attribute age equals to the last element in the sorted age list age_sorted_result(the oldest age), print this element's attribute name.

Sorted the list age_name_tuple by ages, and saved into the list tuple_sorted_by_age1.

4) The function bisection() was defined, which is used to identify the patient with known age using the concept of bisection.

I set mid as global variable, so that it could be used in other funcitons. Variables low and high are used to define the search range of ages.








#### >> Question answer: 

1) <img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework2/Figures-in-running-result/exercise1/histogram-of-age-distribution.jpg" style="zoom:200%;" />

No patients share the same exact age. Since set do not have duplicates, if the length of age as a set is not the length of age as a list, there must be at least one duplicate(two patients has the same age).

*Extra points：* If multiple patients share the same age, the bisection function need to be modified: Instead of searching for the index of the single target value, the bisection is asked to search for the leftmost/rightmost target value(since there are multiple target values.)

When value in the list bigger than target value(found_age), high = mid, since the high value might be the leftmost target value; when value in the list smaller than target value, low = mid + 1, to avoid endless loop.

2) <img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework2/Figures-in-running-result/exercise1/histogram-of-gender-distribution.jpg" style="zoom:200%;" />

> According to the distribution of genders, this provider encode gender by using 3 categories: female, male and unknown.

3) Monica Caponera is the oldest person.

4) In order to find the second oldest people, first I use zip() to form a list including age and name, called age_name_tuple. Then I use the max() function on the list age_name_tuple, to find the age and name of the oldest people. The time complexity is O(n). 
Then I use remove() function to remove the element that contained age and name of the oldest people, the time complexity is O(1). 
Finally I use max() on the list age_name_tuple again, to find the age and name of the second oldest people. The time complexity is O(n).
In general, the total time complexity is O(n).

Codes: age_name_tuple = zip(age,name) max(age_name_tuple) age.remove(84.99855742449432) max(age_name_tuple)

Sorting is an O(nlogn) process, but identifying one single element from a sorted list is an O(1) process.
While traversing a not sorted list is an O(n) process.

Therefore if you need to find a single element from a not sorted list many times, it is a good choice to use sorted function. The total time complexity is O(nlogn). If you only need to find a single element from a list for one time, it is better to use traverse. The total time complexity is O(n).

5) The patient who is 41.5 years old is John Braswell.

6) The number of patients who are at least 41.5 years old is 150471.

#### >> Tesing process:

1) Last two question 1+2.

2)


## Exercise 2

### Question:

Download and uncompress the latest Human Reference Genome(GRCh38.p13) from (https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/405/GCA_000001405.28_GRCh38.p13/GCA_000001405.28_GRCh38.p13_genomic.fna.gz) (Links to an external site.)
The above should create the file GCA_000001405.28_GRCh38.p13_genomic.fna. This is a FASTA file a little over 3 GB in size, representing the about 3 billion bases in the human genome.
(The Human Reference Genome is a product of the Genome Reference Consortium. It is a composite sequence representing no individual human but primarily derived from 11 individual humans. Other projects are trying to characterize the diversity possible across the species.)

Write code to loop through all 15-mers, subsequences of 15 bases within chromosome 2 (CM000664.2).  (5 points)

Hint: Remember, it's generally best not to try to parse files yourself. If you have BioPython installed, you can do something like the following:

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework2/Figures-in-homework-question/homework2_question2_1.jpg" style="zoom:200%;" />

(If you don't, consider installing BioPython.)
If you would like to learn more about BioPython's SeqIO module, its documentation is at https://biopython.org/wiki/SeqIO (Links to an external site.)
In the above, sequence is a byte string of lower-cased letters. I suggest doing this to simplify our call to the hashing function later, but you could leave it as a regular string instead.

Naively, you would expect 4^15 ≈ 1 billion potentially unique distinct subsequences, so by the pigeon hole principle, at least one subsequence must occur more than once in the genome. Things are a little more complicated because these FASTA files also include N for places where any nucleotides might occur. Ignore all subsequences containing more than 2 Ns.

(Recall that N can stand for any nucleotide, but for the purposes of this question consider two 15-mers the same if and only if they have the same sequence of A, C, T, G, and Ns... i.e. if two 15-mers are the same except the 3rd position is an N in one and an A in the other, then they are different.)
How many total subsequences are there (counting duplicates) that do not contain more than 2 Ns? (5 points)

Using 100 hash functions from the family below and a single pass through the sequences, estimate the number of distinct 15-mers in the reference genome's chromosome 2 using the big data method for estimating distinct counts discussed in class. (5 points) (Here I mean distinct in the sense that if we have the list 1, 1, 2, 3, 4, 5, 4, there are 5 distinct values that appear.) How does your estimate change for different-sized subsets of these hash functions, e.g. the one with a=1 only, or a=1, 2, .., 10, or a=1, 2, ...100, etc? (5 points) (I suggest combining the hashes by taking the median of the minimum values and then turning that into an estimate for distinct elements, but you may want to experiment with other strategies. I further suggest that to get a feel for this, you may want to vary the number of hash functions used more smoothly, e.g. 1, 2, 3, 4, ... 100.)

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework2/Figures-in-homework-question/homework2_question2_2.jpg" style="zoom:200%;" />

For any byte string, this returns an integer between 0 and scale. For example,

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework2/Figures-in-homework-question/homework2_question2_3.jpg" style="zoom:200%;" />

To get a number between 0 and 1 from this, you'll want to divide the returned value by scale. Note: you probably don't want to literally use this code as the sha256 return value is the same for all hashes in our family, so feel free to factor that out rather than calling it over and over again.

(For those curious about the mathematics, this is an approximately universal hash family, and this result depends in part on the fact that this p is prime. This particular large prime p belongs to the family of Wieferich primes base 23.)

This will take a while to run. Test your code on some medium sized fake data before trying it on chromosome 2. Explain your tests and why they convinced you that your code works (5 points).


### Solution

#### >> Code explanation: 

1)

#### >> Question answer: 

1)



#### >> Tesing process:





## Exercise 3

### Question

Your friend says to you, "you have to help me! I'm supposed to present in lab meeting in less than an hour, and I haven't been able to get the simplest thing to work!" After you help them calm down, they explain: through a collaboration with a fitness app, they have a 4GB file of high-precision weights of exactly 500 million people throughout the world. Even with 8GB of RAM, they get a MemoryError when trying to load the file in and find the average weight. They show you their code which worked fine when they tested it on a small number of weights:

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework2/Figures-in-homework-question/homework2_question3.jpg" style="zoom:200%;" />

Aha! You exclaim.
Explain what went wrong (6 points). Suggest a way of storing all the data in memory that would work (7 points), and suggest a strategy for calculating the average that would not require storing all the data in memory (7 points). 

Remember, your friend has to present soon, so keep your answers concise but thorough.


### Solution

#### >> Question answer:

1) The reason of memoryerror:

First, we use 4GB to load the data. Then use 2GB to change the data into float type. When the data is appended into the 'weights' list, the list also costs 2GB memory. Apart from that, variable sum and len also cost 2 bytes in total.

The total memory usage is over 8GB, that is why they got a memoryerror.


2) Suggestion of storing all the data in memory:



3) Suggestion for calculating the average that would not require storing all the data in memory:

Instead of using list to store all the data, I use a variable sum to store all the data, and a variable count to count the number of data. For each for loop, each line of data is added into variable sum, and the variable count increase by one. The average is calculated by sum divide by count(sum/count).

In this way, the memory cost are two variables.



## Exercise 4

### Question

Identify a data set online (10 points) that you find interesting that could potentially be used for the final project; the main requirements is that there needs to be many (hundreds or more) data items with several identifiable variables, at least one of which could be viewed as an output variable that you could predict from the others.

Describe the dataset (10 points) Your answer should address (but not be limited to): 
how many variables? 
Are the key variables explicitly specified or are they things you would have to derive (e.g. by inferring from text)? 
Are any of the variables exactly derivable from other variables? (i.e. are any of them redundant?) 
Are there any variables that could in principle be statistically predicted from other variables? 
How many rows/data points are there? 
Is the data in a standard format? If not, how could you convert it to a standard format?
Describe the terms of use and identify any key restrictions (e.g. do you have to officially apply to get access to the data? Are there certain types of analyses you can't do?) (5 points)

Remember: if you can't find explicit permission to use a given dataset, assume that you cannot do so.
Note: You're not committing to use this dataset for the project, but this will give you one option.



### Question answer: 

The online data set I chose is the [2020 Behavioral Risk Factor Surveillance System (BRFSS) Data](https://www.cdc.gov/brfss/index.html).

#### >> Why does this dataset meet the requirements?

The Behavioral Risk Factor Surveillance System (BRFSS) is the nation’s premier system of health-related telephone surveys that collect state data about U.S. residents regarding their health-related risk behaviors, chronic health conditions, and use of preventive services. 

The dataset has many data items since it contains 401,958 rows and 280 columns. 

The dataset has at least one of which could be viewed as an output variable that you could predict from the others. i.e., these data could be used to find the correlation between different features of people. For example, can we predict the mental health status of a person based on his income and education level? This might be a prototype of the final project, since the dataset has provided data of mental health level, income level and education level.

#### >> Brief description on the dataset:

1) The dataset has 279 variables. 

2) The key variables are represented as numerical values, further data processing is needed. For example, the state information of each person is represented as FIPS Code, 1 refers to Alabama, 2 refers to Alaska.

3) There are some variables that could be exactly derived from other variables. For example, the interview year(IYEAR), month(IMONTH) and day(IDAY) could be derived from the interview date of each person(IDATE).

4) There are some variables that could be statistically predicted from other variables. For example, the dataset has data of income level, education level and mental health level, which means I could predict mental health level based on income and education level.

5) There are 401,958 rows, 112,548,240 data points in total.

6) The data is in SAS format(.xpt file), I used the package 'foreign' of R to transfer it into csv format.

#### >> The term of use and key restrictions:

1) On the [website of BRFSS](https://www.cdc.gov/brfss/about/brfss_faq.htm). They said the survey data and comprehensive documentation (data files, codebooks, design documents, methodology, and more) for a given year are all available.

2) They do ask that any published material derived from the data acknowledge CDC’s BRFSS as the original source. 

Suggested Citation for Online BRFSS Database:
Centers for Disease Control and Prevention (CDC). Behavioral Risk Factor Surveillance System Survey Data. Atlanta, Georgia: U.S. Department of Health and Human Services, Centers for Disease Control and Prevention, [appropriate year].


## Data source

Data of exercise1 comes from [hw2-patients.xml](https://yale.instructure.com/courses/70314/files/5401025/download?download_frd=1).

Data of exercise2 comes from [the latest Human Reference Genome(GRCh38.p13)](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/405/GCA_000001405.28_GRCh38.p13/GCA_000001405.28_GRCh38.p13_genomic.fna.gz).

Data of exercise4 comes from [2020 BRFSS Data (SAS Transport Format)](https://www.cdc.gov/brfss/annual_data/2020/files/LLCP2020XPT.zip).



## Maintainer
@QingyangYu0529
| Name        | Email                | Organization                                                 |
| :---------: | ---------------------| ------------------------------------------------------------ |
| Qingyang Yu | qingyang.yu@yale.edu | Graduate student, Yale School of Public Health, Yale University |
