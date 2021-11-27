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




### Solution

#### >> Code explanation





#### >> Question answer




#### >> Testing



## Exercise 2


### Question

Extend the basic binary tree example from slides2 into a binary search tree that is initially empty (5 points).  Provide an add method that inserts a single numeric value at a time according to the rules for a binary search tree (5 points).
When this is done, you should be able to construct the tree from the slides via:

 my_tree = Tree() for item in [55, 62, 37, 49, 71, 14, 17]:     my_tree.add(item)




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
