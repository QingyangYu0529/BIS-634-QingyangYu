# Readme for HW #5

## Instruction

This readme file contains:

1)Instructions that are necessary for running scripts under this folder.

2)Answers to each question asked in the exercises 1-5.

3)How I proved my code was correct using different tests.

4)Code as appendix.

5)Any other relevant information. 


## Support

If you have any question, please feel free to [contact me](https://github.com/QingyangYu0529/BIS-634-QingyangYu#Maintainer).

Any comments or insights would be greatly appreciated.


## Exercise 1


### Question

Go to [Links to an external site](https://statecancerprofiles.cancer.gov/incidencerates/index.php) from the National Cancer Institute, search across the entire "area" of the United States at the "area type" resolution of By State, for all cancer sites, all races, all sexes, and all ages. Export the data (this will give you a CSV file).

Perform any necessary data cleaning (e.g. you'll probably want to get rid of the numbers in e.g. "Connecticut(7)" which refer to data source information as well as remove lines that aren't part of the table). Include the cleaned CSV file in your homework submission, and make sure your readme includes a citation of where the original data came from and how you changed the csv file. (5 points)
Using Flask, implement a server that provides three routes (5 points each):

Using Flask, implement a server that provides three routes (5 points each):
@app.route("/")
 the index/homepage written in HTML which prompts the user to enter a state and provides a button, which passes this information to /info
@app.route("/state/<string:name>")
 an API that returns JSON-encoded data containing the name of the state and the age-adjusted incidence rate (cases per 100k) 
@app.route("/info", methods=["GET"])
 a web page that takes the name of the state as a GET argument and (1) if the state name is valid, displays the same information as the API above, but does so by putting it in an HTML page, or (2) displays an error if the state name is invalid (discuss what counts as valid and invalid in your readme; e.g. does capitalization matter?)
either way, include a link back to the homepage /

You've now completed most of this course, so you're now qualified to choose the next step. Take this exercise one step beyond that which is described above in a way that you think is appropriate, and discuss your extension in your readme. (e.g. you might show maps, or provide more data, or use CSS/JS to make the page prettier or more interactive, or use a database, or...) (5 points).


### Solution

#### >> Code explanation





#### >> Question answer

1) In exercise 1, incidence data comes from [National Program of Cancer Registries](https://www.cdc.gov/cancer/npcr/), [Centers for Disease Control and Prevention and by the National Cancer Institute's Surveillance, Epidemiology, and End Results (SEER) Program](https://seer.cancer.gov/).

Also mentioned in the Data Source part.



#### >> Testing





## Exercise 2


### Question

Extend the basic binary tree example from slides2 into a binary search tree that is initially empty (5 points).  Provide an add method that inserts a single numeric value at a time according to the rules for a binary search tree (5 points).
When this is done, you should be able to construct the tree from the slides via:

 my_tree = Tree() for item in [55, 62, 37, 49, 71, 14, 17]:     my_tree.add(item)

Replace the contains method of the tree with the following __contains__ method. The change in name will allow you to use the in operator; e.g. after this change, 55 in my_tree should be True in the above example, whereas 42 in my_tree would be False. Test this. (5 points). (Edited 2021-11-16 because the version from the slides was a generic binary tree but not a binary search tree, which allows us to search more efficiently):

 def __contains__(self, item):
  if self.value == item:
    return True
  elif self.left and item < self.value:
    return item in self.left
  elif self.right and item > self.value:
    return item in self.right
  else:
    return False

__contains__ is an example of what's known as a magic method; such methods allow new data structures you might create to work like built-in data types. For more on magic methods, search the web, or start with [this page](https://python-course.eu/oop/magic-methods.php).

Using various sizes n of trees (populated with random data) and sufficiently many calls to in (each individual call should be very fast, so you may have to run many repeated tests), demonstrate that in is executing in O(log n) times; on a log-log plot, for sufficiently large n, the graph of time required for checking if a number is in the tree as a function of n should be almost horizontal. (5 points).
This speed is not free. Provide supporting evidence that the time to setup the tree is O(n log n) by timing it for various sized ns and showing that the runtime lies between a curve that is O(n) and one that is O(n**2). (5 points)



### Solution


#### >> Code explanation




#### >> Question answer



#### >> Testing



## Exercise 3

### Question

Implement a two-dimensional k-nearest neighbors classifier (in particular, do not use sklearn for k-nearest neighbors here): given a list of (x, y; class) data, store this data in a quad-tree (14 points). Given a new (x, y) point and a value of k (the number of nearest neighbors to examine), it should be able to identify the most common class within those k nearest neighbors (14 points). You may assume distance will be measured using the traditional euclidean distance.
[Cinar and Koklu (2019)](https://www.ijisae.org/IJISAE/article/view/1068) used various machine learning strategies to predict the type of rice based on image analysis. In this exercise, we'll do something similar.
Begin by going to the journal [page](https://www.ijisae.org/IJISAE/article/view/1068) and downloading the rice dataset (there's a dataset button on the right). Note that you can load data directly from the excel file via:

data = pd.read_excel('Rice_Osmancik_Cammeo_Dataset.xlsx')

Normalize the seven quantitative columns to a mean of 0 and standard deviation 1. (3 points)
Reduce the data to two dimensions using PCA. You can do this with e.g.:、

from sklearn import decomposition
pca = decomposition.PCA(n_components=2)
data_reduced = pca.fit_transform(data[my_cols])
pc0 = data_reduced[:, 0]
pc1 = data_reduced[:, 1]

That is, pc0 can be thought of as a vector of x-values, pc1 as a vector of y-values, and data["CLASS"] as a vector of the corresponding types of rice.
Plot this on a scatterplot, color-coding by type of rice. (3 points)
Comment on what the graph suggests about the effeciveness of using k-nearest neighbors on this 2-dimensional reduction of the data to predict the type of rice. (4 points)
Using 5-fold cross-validation with your k-nearest neighbors implementation, give the confusion matrix for predicting the type of rice with k=1. (4 points) Repeat for k=5. (4 points)
Provide a brief interpretation of what the confusion matrix results mean. (4 points)
Recall: when you're doing cross-validation, you have training and test sets. All normalization must be based on the training set mean and standard deviation, not on data including the test set. Once the pca reduction has been trained, you can apply it to test data via, e.g.

test_data_reduced = pca.transform(test_data[my_cols])

(Note: we use .fit_transform with the training data and .transform with the test data.)


### Solution


#### >> Code explanation




#### >> Question answer




#### >> Testing







## Data source

In exercise 1, incidence data comes from [National Program of Cancer Registries](https://www.cdc.gov/cancer/npcr/), [Centers for Disease Control and Prevention and by the National Cancer Institute's Surveillance, Epidemiology, and End Results (SEER) Program](https://seer.cancer.gov/).



## Maintainer
@QingyangYu0529
| Name        | Email                | Organization                                                 |
| :---------: | ---------------------| ------------------------------------------------------------ |
| Qingyang Yu | qingyang.yu@yale.edu | Graduate student, Yale School of Public Health, Yale University |
