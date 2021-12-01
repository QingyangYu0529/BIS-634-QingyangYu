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

```python
cancer_data = pd.read_csv("cancer_data.csv", skiprows = 8)
cancer_data = cancer_data.drop(cancer_data.index[53:86])
cancer_data['State'] = cancer_data['State'].map(lambda x: x[:-3])
cancer_data = cancer_data.rename(columns = {" FIPS": "FIPS"})
cancer_data['FIPS'] = (cancer_data['FIPS']/1000).map("{:,.0f}".format)
cancer_data['Average Annual Count'] = cancer_data['Average Annual Count'].map(lambda x: '%.0f' % x)
cancer_data.to_csv('cleaned_cancer_data.csv', index=False)
```

1) For data cleaning, first I used "skiprow = n" to remove the first 8 rows of data. Then I used set_option to display the whole dataframe cancer_data. Also I used drop() to remove the last few rows that do not contain data. I used map() to run a lambda function over the column State, to remove the number and brackets in the column State. I also use map() to standardize the columns FIPS and Average Annual Count to integer precision. Finally the cleaned cancer data was saved into csv file cleaned_cancer_data.csv.

```python
import pandas as pd
cancer_data = pd.read_csv("cleaned_cancer_data.csv")

state_name = cancer_data['State'].tolist()
state_name = [item.lower() for item in state_name]
FIPS_code = cancer_data['FIPS'].tolist()
Lower_CI = cancer_data['Lower 95% Confidence Interval'].tolist()
Upper_CI = cancer_data['Upper 95% Confidence Interval'].tolist()
average_annual_count = cancer_data['Average Annual Count'].tolist()
recent_trend = cancer_data['Recent Trend'].tolist()
age_adjusted_IR = cancer_data['Age-Adjusted Incidence Rate([rate note]) - cases per 100,000'].tolist()
state_info = list(tuple(zip(state_name, FIPS_code, age_adjusted_IR, Lower_CI, Upper_CI, average_annual_count, recent_trend)))
```

2) For server implementation, script was in 3routes.py file. First load cleaned cancer data, and saved state name, FIPS code, age adjusted incidence rate, confidence interval, average annual count, recent trend into a tuple state_info.

```python
from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/state/<string:name>")
def get_info():
    import json
    dics = {}
    for item in state_name:
        dics[item] = age_adjusted_IR[state_name.index(item)]
    json_object = json.dumps(dics)
    return json_object

@app.route("/info", methods=["GET"])
def info():
    usertext = request.args.get("usertext")
    result = ""
    IR = 0
    FIPS = 0
    CI = ""
    AAC = 0
    rec_trend = ""
    if usertext.lower() in state_name:
        for item in state_info: 
            if usertext == item[0]:
                FIPS = item[1]
                IR = item[2]
                CI = "(" + str(item[3]) + "," + str(item[4]) + ")"
                AAC = int(item[5])
                rec_trend = item[6]
        result += f"The state name is {usertext}, the age-adjusted incidence rate(cases per 100k) is {IR}.\n" 
        return render_template("info.html", analysis = result, FIPS = FIPS, IR = IR, CI = CI, AAC = AAC, rec_trend = rec_trend, usertext = usertext)
    else:
        result += f"Error: the state name {usertext} is invalid.\n"
        return render_template("error.html", analysis = result, usertext = usertext)
    
if __name__ == "__main__":
    app.run(debug = True)
```

> Then I implemented a server with three routes. Web page is in the testing part. The first route correspond to homepage.html, the third route correspond to info.html and error.html.

```python
cancer_data0 = pd.read_csv("cleaned_cancer_data.csv")
cancer_data0 = cancer_data0[['State','Average Annual Count']]
cancer_data0 = cancer_data0.drop(cancer_data.index[0])
cancer_data_list = cancer_data0.dropna().values.tolist()
low, high = min([x[1] for x in cancer_data_list]), max([x[1] for x in cancer_data_list])

map = (Map()
    .add("", cancer_data_list, maptype = "美国", is_map_symbol_show = False)
    .set_series_opts(label_opts = opts.LabelOpts(is_show = False))
    .set_global_opts(visualmap_opts = opts.VisualMapOpts(max_ = high, min_ = low),
                     title_opts = opts.TitleOpts(
                         title = "United State cancer cases")
                     )
)
map.render(path = "templates\map.html")
```

3) For map drawing, first I integrated columns state, average annual count into list cancer_data_list, found the lowest and highest cases and save into variables low, high. Then I used Pyecharts to draw the US map, saved as html file map.html using map.render().



#### >> Question answer

1) In exercise 1, incidence data comes from [National Program of Cancer Registries](https://www.cdc.gov/cancer/npcr/), [Centers for Disease Control and Prevention and by the National Cancer Institute's Surveillance, Epidemiology, and End Results (SEER) Program](https://seer.cancer.gov/).
Also mentioned in the Data Source part.

2) For data cleaning, first I removed the first 8 rows of data, also removed the last few rows that do not contain data. Then I removed the number and brackets in the column State. I standardized the columns FIPS and Average Annual Count to integer precision.

3) In the third route of my server @app.route("/info", methods=["GET"]): Since I have already transferred the input string and list of state names into lowercase, when someone search for a state name, the capitalization does not matter, only misspell matters. For instance, if someone input new york, the website will show the data of state New York.

4) I took exercise 1 one step beyond by: 

(1) Provide more data in the info page: it will display the state name, FIPS code, age adjusted incidence rate(cases per 100k), confidence interval, average annual count, recent trend(falling/stable).

(2) Draw a map of United State cancer cases, it would show the state name and average cancer cases of the chosen state. The legend showed the minimum and maximum cases and the state you choose. Map was saved as html file map.html.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework5/Figures-in-running-results/Exercise1/map-example.png" style="zoom:150%;" />



#### >> Testing

If I enter "new york" or "New York" in the search bar and press "search for info" button, both results are same, thus capitalization does not matter.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework5/Figures-in-running-results/Exercise1/testing1.png" style="zoom:150%;" />

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework5/Figures-in-running-results/Exercise1/testing2.png" style="zoom:150%;" />

A table displaya the state name, FIPS code, age adjusted incidence rate(cases per 100k), confidence interval, average annual count, recent trend(falling/stable). User could click here then turn to homepage.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework5/Figures-in-running-results/Exercise1/testing3.png" style="zoom:150%;" />

If I enter "abc" in the search bar and press "search for info" button, it would show Error: the state name abc is invalid. Also could click here then turn to homepage.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework5/Figures-in-running-results/Exercise1/testing4.png" style="zoom:150%;" />

If I click here in the homepage, it would show the United State cancer cases map.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework5/Figures-in-running-results/Exercise1/testing5.png" style="zoom:150%;" />

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework5/Figures-in-running-results/Exercise1/map-example.png" style="zoom:150%;" />


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
