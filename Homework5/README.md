# Readme for HW #5

## Instruction

This readme file contains:

1)Instructions that are necessary for running scripts under this folder.

2)Answers to each question asked in the exercises 1-3.

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

2) For server implementation, script was in erercise1_3routes.py file. First load cleaned cancer data, and saved state name, FIPS code, age adjusted incidence rate, confidence interval, average annual count, recent trend into a tuple state_info.

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

> Then I implemented a server with three routes. Web pages were showed in the testing part. The first route correspond to homepage.html, the third route correspond to info.html and error.html.

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

```python
class Tree:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
    
    def __contains__(self, item):
        if self.value == item:
            return True
        elif self.left and item < self.value:
            return item in self.left
        elif self.right and item > self.value:
            return item in self.right
        else:
            return False

    def add(self, value):
        if self.value is None:
            self.value = value
        else:
            if self.value == value:
                self.value = value
            elif self.value < value:
                if self.right is None:
                    self.right = Tree(value)
                else:
                    self.right.add(value)
            else:
                if self.left is None:
                    self.left = Tree(value)
                else:
                    self.left.add(value)
```
> The class Tree includes function __init__, used to set the left and right part of the tree, which are initially empty(value = None). 

Add function is used to insert a single value into the tree for each time: If root is None, add value to the root. If root value is smaller than value to be added, value is added to the right part of the tree. Otherwise, value is added to the left part of the tree.

```python
    def PrintTreeInOrder(self):
        elements = []
        if self.left is not None:
            elements += self.left.PrintTreeInOrder()
        elements.append(self.value)
        if self.right is not None:
            elements += self.right.PrintTreeInOrder()
        return elements

    def PrintTreePreOrder(self):
        elements = [self.value]
        if self.left is not None:
            elements += self.left.PrintTreePreOrder()
        if self.right is not None:
            elements += self.right.PrintTreePreOrder()
        return elements

    def PrintTreePostOrder(self):
        elements = []
        if self.left is not None:
            elements += self.left.PrintTreePostOrder()
        if self.right is not None:
            elements += self.right.PrintTreePostOrder()
        elements.append(self.value)
        return elements
```
> Also set function PrintTreeInOrder(), PrintTreePreOrder(), and PrintTreePostOrder(), to test whether values are successfully added into the tree.

```python
def in_timing(n):
    times = []
    random_num = []
    random_in_num = []

    for i in range(n):
        num = random.randint(1,1000)
        random_num.append(num)
    for i in range(10):
        num = random.randint(1,1000)
        random_in_num.append(num)
        
    count = 0
    while(count <= 100):
        my_tree = Tree()
        for num in random_num:
            my_tree.add(num)
        start = time.perf_counter()
        for num in random_in_num:
            num in my_tree
        end = time.perf_counter()
        times.append(end - start)
        count = count + 1
    return statistics.median(times)
```
> Function in_timing() was defined to record running time of in operation. List random_num contains n randomly generated values that will be added into the tree. For each tree, it need to determine whether 10 randomly generated numbers are in the tree.
For each tree, repeated for 100 times and chose the median value of running time to avoid random error.

```python
ns = range(1, 10000)
in_running_time = [in_timing(int(n)) for n in tqdm(ns)]
start_pt = in_running_time[0]
_x2 = []
_x = []
for n in tqdm(ns):
    _x2.append(start_pt * (n**2))
for n in tqdm(ns):
    _x.append(start_pt * (n))
```
> ns is in a continuous range between 1 and 1000.


```python
ns = list(ns)
plt.plot(ns, in_running_time)
plt.plot(ns, _x)
plt.plot(ns, _x2)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("ns")
plt.ylabel("time(s)")
plt.legend(["time(s)","x","x^2"], ncol = 3)
plt.show
```
> I used matplotlib to visualize the relationship between n and running time in a log-log plot. Also included curve x and x^2.

```python
def setup_tree_timing(n):
    times = []
    random_num = []
    for i in range(n):
        num = random.randint(1,1000)
        random_num.append(num)

    count = 0
    while(count <= 100):
        start = time.perf_counter()
        my_tree = Tree(random_num[0])
        for num in random_num[1:]:
            my_tree.add(num)
        end = time.perf_counter()
        times.append(end - start)
        count = count + 1
    return statistics.median(times)

ns = range(1, 10000)
setup_running_time = [setup_tree_timing(int(n)) for n in tqdm(ns)]
start_pt = setup_running_time[0]
_x2 = []
_x = []
for n in tqdm(ns):
    _x2.append(start_pt * (n**2))
for n in tqdm(ns):
    _x.append(start_pt * (n))

ns = list(ns)
plt.plot(ns, setup_running_time)
plt.plot(ns, _x)
plt.plot(ns, _x2)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("ns")
plt.ylabel("time(s)")
plt.legend(["time(s)","x","x^2"], ncol = 3)
plt.show
```
> Similar to in_timing(), function setup_tree_timing() was defined to record running time of tree set up.




#### >> Question answer


<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework5/Figures-in-running-results/Exercise2/testing1.png" style="zoom:250%;" />

> For in operation, from the log-log plot we could see that the curve is in the shape of logn. When n is sufficiently large(~10000), the running time required for checking if a number is in the tree as a function of n is almost horizontal.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework5/Figures-in-running-results/Exercise2/testing2.png" style="zoom:250%;" />

> For tree set up, from the log-log plot we could see that the curve is between a curve that is y=n and one that is y=n^2, indicating that the time to setup the tree is O(n logn).




#### >> Testing

```python
my_tree = Tree()
for item in [55, 62, 37, 49, 71, 14, 17]:     
    my_tree.add(item)
```

> In order to test the add method, first I constructed a tree as follows.

```python
my_tree.PrintTreeInOrder()
my_tree.PrintTreePreOrder()
my_tree.PrintTreePostOrder()
```

> Then I run function PrintTreeInOrder(), PrintTreePreOrder(), and PrintTreePostOrder(), to see whether above values are successfully added into the tree. Results are as follows.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework5/Figures-in-running-results/Exercise2/testing3.png" style="zoom:250%;" />


```python
my_tree.__contains__(55)
my_tree.__contains__(42)
55 in my_tree
42 in my_tree
```
> After replacing the contains method with __contains__, test this method by using above code. 55 in my_tree showed True, while 42 in my_tree showed False.




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

```python
data = pd.read_excel('Rice_Osmancik_Cammeo_Dataset.xlsx')
for column in data[['AREA','PERIMETER','MAJORAXIS','MINORAXIS','ECCENTRICITY','CONVEX_AREA','EXTENT']]:
    data[column] = (data[column] - data[column].mean())/data[column].std()
```
> Loaded data and normalized the seven quantitative columns to a mean of 0 and standard deviation 1.

```python
column_names = data.columns.values.tolist()
column_names.pop()

from sklearn import decomposition
pca = decomposition.PCA(n_components=2)
data_reduced = pca.fit_transform(data[column_names])
pc0 = data_reduced[:, 0]
pc1 = data_reduced[:, 1]

pc0_list = pc0.tolist()
pc1_list = pc1.tolist()
df_pc0_pc1_class = pd.DataFrame({'PC0': pc0_list,'PC1': pc1_list,'Class': data['CLASS']})

(p9.ggplot(data = df_pc0_pc1_class, mapping = p9.aes(x='PC0', y='PC1'))
+ p9.geom_point(p9.aes(x = 'PC0', y = 'PC1', color = 'Class'))
+ p9.labs(title = "Scatter plot for PC0 vs PC1"))
```
> Took the first seven columns and save into list column_name, reduced the data to two dimensions using PCA from sklearn. Used plotnine to draw scatterplot, which was color-coded by type of rice. Red refers to "Cammeo", blue refers to "Osmancik".

```python
class Point:
    def __init__(self, x, y, classes):
        self.x = x
        self.y = y
        self.classes = classes

class Rectangle:
    def __init__(self, x, y, wid, hgt):
        self.x = x
        self.y = y
        self.wid = wid
        self.hgt = hgt
    
    def within(self, point, distance):
        def point_distance(x1, y1, x2, y2):
            value = (x1 - x2)**2 + (y1-y2)**2
            return math.sqrt(value)
        min_x = self.x - self.wid
        min_y = self.y - self.hgt
        max_x = self.x + self.wid
        max_y = self.y + self.hgt
        if point.x >= max_x:
            if point.y >= max_y:
                if (point_distance(max_x, max_y, point.x, point.y)) <= distance:
                    return True
                else: return False
            elif point.y <= min_y:
                if (point_distance(max_x, min_y, point.x, point.y)) < distance:
                    return True
                else: return False
            elif min_y < point.y < max_y:
                if (point_distance(max_x, 0, point.x, 0)) <= distance:
                    return True
                else: return False
        elif point.x <= min_x:
            if point.y >= max_y:
                if (point_distance(min_x, max_y, point.x, point.y)) < distance:
                    return True
                else: return False
            elif point.y <= min_y:
                if (point_distance(min_x, min_y, point.x, point.y)) < distance:
                    return True
                else: return False
            elif min_y <= point.y <= max_y:
                if (point_distance(min_x, 0, point.x, 0)) < distance:
                    return True
                else: return False
        elif min_x <= point.x <= max_x:
            if point.y >= max_y:
                if (point_distance(0, max_y, 0, point.y)) < distance:
                    return True
                else: return False
            elif point.y <= min_y:
                if (point_distance(0, min_y, 0, point.y)) < distance:
                    return True
                else: return False
            elif min_y <= point.y <= max_y:
                return True
```
> In order to set up a quad tree, first class Point was used to associate data with point, each point contains data x, y, class. Class Rectangle was used to save the width, height of the quadtree, in which (x,y) is the center point of rectangle, wid, hgt were the 1/2 width and height of the rectangle region. Function within() was defined to validate whether the rectangle is within the circle, whose center point is point.x, point.y.

```python
class QuadTree:
    def __init__(self, boundary, points_list, max_point):
        self.boundary = boundary
        self.points_list = points_list
        self.max_point = max_point
        self.isleaf = False
        self.divided = False
        self.upperleft, self.upperright, self.lowerleft, self.lowerright = None, None, None, None
        self.construct()

    def subdivide(self):
        x = self.boundary.x
        y = self.boundary.y
        wid = self.boundary.wid
        hgt = self.boundary.hgt
        upperright = Rectangle(x + wid/2, y + hgt/2, wid/2, hgt/2)
        upperleft = Rectangle(x - wid/2, y + hgt/2, wid/2, hgt/2)
        lowerleft = Rectangle(x - wid/2, y - hgt/2, wid/2, hgt/2)
        lowerright = Rectangle(x + wid/2, y - hgt/2, wid/2, hgt/2)
        upperright_point, upperleft_point, lowerright_point, lowerleft_point = [], [], [], []
        for point in self.points_list:
            if point.x > x and point.y >= y:
                upperright_point.append(point)
        for point in self.points_list:
            if point.x <= x and point.y >= y:
                upperleft_point.append(point)
        for point in self.points_list:
            if point.x <= x and point.y < y:
                lowerleft_point.append(point)
        for point in self.points_list:
            if point.x > x and point.y < y:
                lowerright_point.append(point)
        self.upperright = QuadTree(upperright, upperright_point, self.max_point)
        self.upperleft = QuadTree(upperleft, upperleft_point, self.max_point)
        self.lowerleft = QuadTree(lowerleft, lowerleft_point, self.max_point)
        self.lowerright = QuadTree(lowerright, lowerright_point, self.max_point)

    def construct(self):
        if len(self.points_list) > self.max_point:
            if self.divided is False:
                self.subdivide()
                self.divided = True
                self.points_list = []
        else:
            self.isleaf = True
            return True
```
> Class QuadTree was used to set up the quadtree, in which boundary was used to store the detailed information about rectangule: width, height, center point, max_point was the maximum number of points could be stored in the tree, points_list included points stored in the tree, subdivided was used to mark the tree status: whether it is subdivided, upperleft, upperright, lowerleft, lowerright were subnodes stored under the parent node in the tree.

> Function subdivide() was defined to subdivide the quad tree into 4 sub quad tree, and distribute the points into each sub quad tree. Function construct() was defined to determin whether to keep constructing the quad tree: If all the points in the points_list have been added into the quad tree, then stop subdivide.

```python
def KNN(quad, pnt,k):     
    res = []
    for p in pnt:
        stack = [quad]
        r = (float('-inf'),"")
        point_list = []
        while len(stack):
            cur = stack.pop(-1)
            if cur.isleaf is True and cur.boundary.within(p,-r[0]) is True:
                for i in cur.points_list:
                        if len(point_list) < k:
                            distance = math.sqrt((i.x - p.x)**2+(i.y - p.y)**2)
                            heapq.heappush(point_list,(-distance, i.classes))
                            r = heapq.nsmallest(1, point_list)[0]
                        elif math.sqrt((i.x - p.x)**2+(i.y - p.y)**2)<-r[0]:
                            distance = math.sqrt((i.x - p.x)**2+(i.y - p.y)**2)
                            heapq.heappop(point_list)
                            heapq.heappush(point_list, (-distance, i.classes))
                            r = heapq.nsmallest(1,point_list)[0]
            elif cur.isleaf is False:
                if cur.boundary.within(p,-r[0]):
                    if cur.upperleft is not None:
                        stack.append(cur.upperleft)
                    if cur.lowerright is not None:
                        stack.append(cur.lowerright)
                    if cur.upperright is not None:
                        stack.append(cur.upperright)
                    if cur.lowerleft is not None:
                        stack.append(cur.lowerleft)
        res.append(mode([itr[1] for itr in point_list]))
    return res 
```
> In the function KNN(), quad tree was saved into a stack. Then I used heapq function, to efficiently sort the queue.

```python
def show_matrix(k):
    kfold_data = KFold(5)
    result_quadtree = []
    result_true = []
    result_naive = []

    X = data.loc[:, data.columns!='CLASS']
    y = data['CLASS']
    for train_index, test_index in kfold_data.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y[train_index], y[test_index]

        data_reduced = pca.fit_transform(X_train[column_names])
        test_data_reduced = pca.transform(X_test[column_names])
        pc0 = data_reduced[:, 0]
        test_pc1 = test_data_reduced[:, 1]
        test_pc0 = test_data_reduced[:, 0]
        pc1 = data_reduced[:, 1]       
        xlim_min = min(pc0)
        ylim_min = min(pc1)
        xlim_max = max(pc0)
        ylim_max = max(pc1)

        boundary = Rectangle((xlim_max + xlim_min)/2, (ylim_max + ylim_min)/2, (xlim_max - xlim_min)/2, (ylim_max - ylim_min)/2)
        quadtree = QuadTree(boundary, [Point(pc0[k],pc1[k], y_train.iloc[k]) for k in range(len(pc0))], 10)
        knn_result = KNN(quadtree, [Point(test_pc0[k], test_pc1[k], y_test.iloc[k]) for k in range(len(test_pc0))], k)
        y_pred = cross_validation(list(zip(pc1, pc0, y_train)), list(zip(test_pc1, test_pc0, y_test)), k)

        result_quadtree = result_quadtree + knn_result
        result_true = result_true + y_test.to_list()
        result_naive = result_naive + y_pred
        
        
    print("The confusion matrix of k nearest neighbors based on quad tree data structure is:")    
    print(confusion_matrix(result_true, result_quadtree))
    print("The confusion matrix of naive k nearest neighbors is:") 
    print(confusion_matrix(result_true, result_naive))
```
> Function show_matrix() was defined to perform the k fold cross-validation and generate confusion matrix by using sklearn.



#### >> Question answer

1) Scatterplot color-coded by type of rice is below:

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework5/Figures-in-running-results/Exercise3/scatterplot.png" style="zoom:250%;" />

> Comment on the 2-dimensional reduction result: It is not quite efficient to classify the data using PCA method, according to the scatterplot, about 1/3 of data points that are either classfied as "Cammeo" or "Osmancik" showed overlapping. 

2) When k = 1, the confusion matrix is [1335 295 261 1919], indicates that the true positive is 1335, false nagative is 295, false positive is 261, true negative is 1919. Thus the sensitivity of matrix is 0.819, the specificity of matrix is 0.880.

When k = 5, the confusion matrix is [1388 242 211 1969], indicates that the true positive is 1388, false nagative is 242, false positive is 211, true negative is 1969. Thus the sensitivity of matrix is 0.852, the specificity of matrix is 0.903. Consequently, when k = 5, the prediction result is better.



#### >> Testing

To test the result of quad tree k nearest neighbors, I also implemented naive k nearest neighbors method. 

```python
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += (row1[i] - row2[i])**2
    return math.sqrt(distance)
```
> euclidean_distance() was defined to calculate the euclidean distance between each train row and each test row. In the for loop, i was the index to a specific column, used for loop to calculate euclidean distance of each data from row1 and row2, and sumed up. 

```python
def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors
```
> get_neighbors() was defined to sort all of the records in the training dataset by their distance to new data, and returned top k similar neighbors. First distance for each record in the dataset was saved as a tuple, then sorted the list of tuples by distance in descending order. Then sorted tuple distance based on euclidean distance, and retrieved the neighbors.

```python
def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction
```
> classification() was defined to return the most represented class among the neighbors. Used max() to take a set of unique class values. For each class value in the set, called the count on the list of class values.

```python
def cross_validation(train, test, num_neighbors):
    predictions = list()
    for row in test:
        output = predict_classification(train, row, num_neighbors)
        predictions.append(output)
    return(predictions) 
```
> cross_validation() was defined to perform the cross-validation of k nearest neighbors.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework5/Figures-in-running-results/Exercise3/testing-result.png" style="zoom:250%;" />

> When k = 1 and k = 5, the results of k nearest neighbors based on quad tree data structure are same as the results of naive k nearest neighbors.



## Data source

In exercise 1, incidence data comes from [National Program of Cancer Registries](https://www.cdc.gov/cancer/npcr/), [Centers for Disease Control and Prevention and by the National Cancer Institute's Surveillance, Epidemiology, and End Results (SEER) Program](https://seer.cancer.gov/).

Code references: https://scipython.com/blog/quadtrees-2-implementation-in-python/, https://www.fatalerrors.org/a/k-nearest-neighbor-query-based-on-k-dimension-tree-of-knn-algorithm.html, https://docs.python.org/3/library/heapq.html, https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/, https://www.askpython.com/python/examples/k-fold-cross-validation



## Maintainer
@QingyangYu0529
| Name        | Email                | Organization                                                 |
| :---------: | ---------------------| ------------------------------------------------------------ |
| Qingyang Yu | qingyang.yu@yale.edu | Graduate student, Yale School of Public Health, Yale University |
