# Readme for HW #3

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

Use the requests module (or urllib) to use the Entrez API (see slides8) to identify the PubMed IDs for 1000 Alzheimers papers from 2019 and for 1000 cancer papers from 2019. (9 points)
Note: To search for a disease and a publication year, structure the term like: Alzheimers+AND+2019[pdat] (Here [pdat] indicates that this is a publication year, and the AND (has to be all caps) means both conditions should apply.) I'm asking for papers from 2019 instead of 2021 because they're still reasonably recent but the new ones may not have been fully curated and may still be missing MeSH terms... for the papers from 2019, if they're going to get MeSH terms, they were processed long ago.
There are of course many more papers of each category, but is there any overlap in the two sets of papers that you identified? (3 points)
Use the Entrez API via requests/urllib to pull the metadata for each such paper and save a JSON file storing each paper's title, abstract, MeSH terms (DescriptorName inside of MeshHeading), and the query that found it that is of the general form: (12 points)

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-homework-question/homework3_question1_1.jpg" style="zoom:150%;" />

Here 32008517 is the PubMed ID of one of the 2000 papers, specifically one that came from searching for Alzheimer's papers. You should include the full AbstractText and list of MeSH terms; I'm abridging here for clarity.
Hint: To do this, you'll probably want to look at one of the XML responses with a text editor so that you understand how it is structured.
Hint: Some papers like 32008517 (Links to an external site.) have multiple AbstractText fields (e.g. when the abstract is structured). Be sure to store all parts. You could do this in many ways, from using a dictionary or a list or simply concatenating with a space in between. Discuss any pros or cons of your choice in your readme (1 point).
Caution: the PubMed API allows a rate of at most one query at a time and no more than 3 per second unless you have an API key. To be safe, use 

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-homework-question/homework3_question1_2.jpg" style="zoom:150%;" />

after each query to the PubMed API. 
Note: This doesn't require 2002 separate queries. You can get the metadata for many articles at a time by using a comma separated list of ids. While GET queries have a total line length limit, you could use a POST query instead and get the information for all the papers in one pass. (We can use POST instead of GET here in part because this is not a RESTful API.)
Note: BioPython provides functions for accessing the PubMed API. Do not use them; use the requests module to do an HTTP or HTTPS request directly on a URL that you specify with the parameters that you specify. Why? Because this approach is general and will work in many contexts whereas BioPython only works for PubMed and only from Python.



### Solution

#### >> Code explanation: 

Imported module minidom and libraries requests, time, json.

1) Function get_id_of_disease() was defined to return the PubmedId list of a specific disease. First I used requests.get() to send a GET request to the specified url and returned a response object: search term is Alzheimers/cancer+AND+2019[pdat], retmode is xml, retmax = 1000. Then used minidom to parse strings of text from the response object, and got the Id elements by .getElementsByTagName(), saved into the list PubmedId. List IdList was created to save all the PubmedId. Finally I used for loop to get all the data of the elements' firstchild, and saved into the list IdList.

2) Function overlap_in_two_papers() was defined to determine whether there is a overlap in the two sets of papers. First I ran above function to get the PubmedId list from disease1 and disease2, and save into lists IdList1, IdList2, separately. Then turned list into set to remove the duplicates, found the overlap between two sets and returned the overlap.

3) Function pull_metadata() was defined, to pull the metadata for each paper of a specific disease. First I ran the function get_id_of_disease(), to get the PubmedId list of a specific disease. Then I created dictionary paper, to save the metadata for each paper of this disease. For each PubmedId, I sent a GET request to the url of each PubmedId and returned a response object, and parsed strings of text from the response object.

For ArticleTitle, first I got the ArticleTitle elements by .getElementByTagName(). If ArticleTitle is not empty, loop through childnodes of all the elements, and save the text message into Title. If AttributeError was reported, checked if the next childnode is a text node, and also saved the data of next childnode into Title.

AbstractText and Mesh are same as above.

Set the dictionary key as PubmedId, dictionary values include each paper's title, abstract, MeSH terms and query.

4) Ran the function pull_metadata(), and saved metadata of Alzheimer's into dictionary all_data, saved metadata of cancers into dictionary cancer_data. Then I used .update() to update the dictionary all_data, so that data from both Alzheimer's and cancer are saved into all_data. Ran the function overlap_in_two_papers(), to find the overlap in the two sets of papers. Changed the query of this overlap into 'Alzheimer's', 'cancer'. Finally the dictionary all_data was saved into a JSON file paper.json.

#### >> Question answer: 

1) There is a overlap in the two sets of papers that I identified, the pubmed id is 32501203.

2) In order to save all the AbstractText fields of some papers, when looping through childnodes of all the elements, if there is a AttributeError(which suggest there is a childnode of the childnode), I would use try/except AttributeError and save the data of the childnode of the childnode into Abstract, concatenate with other data with a space in between.

In this way, I could save all the data when a paper has multiple AbstractText fields. But the running time and memory cost inevitably increase, since for cases that AttributeError happens, I have to save the data of a childnode of the childnode.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-running-result/Exercise1/code-to-get-AbstractText.jpg" style="zoom:150%;" />




## Exercise 2

### Question:

This question refers to the Alzheimer's and cancer metadata stored in Exercise 1. It is not intended to involve any new queries to PubMed nor to make statements about PubMed beyond that of the papers whose data was obtained.
What fraction of the Alzheimer's papers have no MeSH terms? (2 points) What fraction of the cancer papers have no MeSH terms? (2 points) Comment on how the fractions compare. (1 point; i.e. if they're essentially the same, do you think that's a coincidence? If they're different, do you have any theories why?)
What are the 10 most common MeSH terms for the Alzheimer's papers whose metadata you found in Exercise 1? (2 points) Provide a graphic illustrating their relative frequency. (3 points)
What are the 10 most common MeSH terms for the cancer papers whose metadata you found in Exercise 1? (2 points) Provide a graphic illustrating their relative frequency. (3 points)
Make a labeled table with rows for each of the top 5 MeSH terms from the Alzheimer's query and columns for each of the top 5 MeSH terms from the cancer query. For the values in the table, provide the count of papers (combined, from both sets) having both the matching MeSH terms. (5 points) Ideally, you can have the computer generate the table directly, but if not you could use nested for loops, label your output, and manually assemble a table in your readme document. Comment on any findings or limitations from the table and any ways you see to get a better understanding of how the various MeSH terms relate to each other. (5 points)


### Solution

#### >> Code explanation: 

Imported libarary json.

1) Read JSON file using the open function. The file was parsed using json.load() method which gave us a dictionary named all_data. Then separated data into alzheimer's data(alz_data) and cancer's data(cancer_data) based on content in the Query. Used variable alz_count_noMesh, cancer_count_noMesh to save the number of Alzheimer's/cancer papers that have no MeSH terms. Used for loop to count number of keys that have no MeSH terms in the dictionary alz_data/cancer_data. Then the fraction was calculated.

2) Imported module Counter. A Counter is a collection where elements are stored as dictionary keys, and the key’s counts are stored as dictionary values. Function most_common_Mesh() was defined to find the 10 most common MeSH terms of a specific disease when a list is entered. I used the most_common() of Counter to find the most common elements of a list in python, and saved into the tuple top_10_Mesh. Then separated tuple top_10_Mesh into two lists top_10_Mesh_term, top_10_Mesh_frequency.

Lists alz_Mesh, cancer_Mesh are generated to save all the MeSH terms of Alzheimer's/cancer. Run function most_common_Mesh() on these two lists.

Imported libraries matplotlib and pandas to draw the bar charts.

3) Found the top 5 MeSH terms from Alzheimer's query, saved into the list alz_top_5_Mesh. Same as cancer, saved into the list cancer_top_5_Mesh. Then found the MeSH terms that both present in top 5 MeSH terms of Alzheimer's or cancers, save into the set same_Mesh. Function count_paper_top_5_Mesh() was defined, to return the counts of papers that have two of top 5 MeSH terms. First used nested for loop to traverse all the top 5 MeSH terms of Alzheimer's and cancer. If the MeSH terms of one paper have two of top 5 MeSH terms, variable count increases by one. Result was saved into tuple count_result.

Extracted only the counts, saved into the list table_content. Then split table_content into sublists in group of five. Dataframe df_table was created, in which the column name is top 5 MeSH terms of Alzheimer's. Data inside are the counts of papers having both the matching MeSH terms. Table was plotted using matplotlib.


#### >> Question answer: 

1) The number of Alzheimer's papers that have no MeSH terms is 164, which is 16% of total Alzheimer's papers.
The number of cancer papers that have no MeSH terms is 758, which is 76% of total cancer papers.

The fraction of cancer papers have no MeSH terms is much more than that of Alzheimer's papers. Compared with the term "Alzheimer's", "cancer" is a much broader term, which is associated with multiple non-cancer diseases, affecting people no matter what their nationality, genders, ages are, thus it is difficult to summarize the MeSH terms that related to "cancer"(it is not useful to list all the terms).

2) The 10 most common MeSH terms for the Alzheimer's papers are: Humans; Alzheimer Disease; Male; Female; Aged; Animals; Amyloid beta-Peptides; Brain; Aged, 80 and over; Cognitive Dysfunction.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-running-result/Exercise2/10-most-common-MeSH-terms-for-Alzheimer's-papers.jpg" style="zoom:150%;" />

The 10 most common MeSH terms for the cancer papers are: Humans; Female; Male; Middle Aged; Aged; Adult; Animals; Neoplasms; Retrospective Studies; Aged, 80 and over.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-running-result/Exercise2/10-most-common-MeSH-terms-for-cancer-papers.jpg" style="zoom:150%;" />

3) The table with rows(top 5 MeSH terms from Alzheimer's query) and columns(top 5 MeSH terms from cancer query) is as below, values in the table are the counts of papers having both the matching MeSH terms.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-running-result/Exercise2/table-for-5-most-common-MeSH-terms-for-Alzheimer's-or-cancer.jpg" style="zoom:150%;" />

Findings from the table: 

(1) The most popular MeSH term is "Humans": As one of the top 5 MeSH terms from both Alzheimer's and cancer papers, 922 of the papaers has this MeSH term.

(2) While on the contrary, among all the top 5 MeSH terms from both Alzheimer's and cancer papers, "Female" remain to be the least popular: 109 of the papers has this MeSH term.

(3) According to top 5 MeSH terms in Alzheimer's or cancer papers: Aged people are more likely to have Alzheimer's, while both middle aged and aged people are more likely to have cancers. Compared with female(appears in 109 of papers), male are more likely to have Alzheimer's and cancers(appears in 413 of papers).

Limitations from the table:
For all the top 5 Mesh terms in Alzheimer's or cancer papers, they are too general to describe a specific disease: 4 out of 5 Mesh terms are same regardless of disease.

From my perspective, although table could show the exact count of papers having both the matching MeSH terms, it is not a good choice for visualization. If using the network/sankey diagrams, I could get a better understanding of how various MeSH terms relate to each other.



## Exercise 3

### Question

Machine learning and data visualization strategies generally work best on data that is numeric, but exercise 1 gave us text data, and indeed text is common. Fortunately, modern NLP algorithms powered by machine learning trained on massive datasets exist that can take words (e.g. word2vec) or titles and abstracts (e.g. SPECTER) and return a vector of numbers in a way that similar items are given similar vectors. Since we have titles and abstracts, let's use SPECTER.
In particular, for each paper identified from exercise 1, compute the SPECTER embedding (a 768-dimensional vector). Keep track of which papers came from searching for Alzheimers, which came from searching for cancer. (5 points) If you are familiar with SPECTER and wish to do it another way, that's great, if not here's one approach based on [Links to an external site](https://github.com/allenai/specter):
Install pytorch (a deep learning library) by following the instructions [here](https://pytorch.org/get-started/locally/)
Install the huggingface transformers module: [pip install transformers](https://huggingface.co/)
provides access to a number of pre-trained NLP language models.)
Have your code load the SPECTER model (the first time you do this, it will take a bit to download the model; it will be stored locally for fast reuse later):

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-homework-question/homework3_question3_1.jpg" style="zoom:150%;" />

Process your dictionary of papers:

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-homework-question/homework3_question3_2.jpg" style="zoom:150%;" />

At this point, embeddings[i] is the 768-dim vector for the ith paper.
Apply principal component analysis (PCA) to identify the first three principal components. (5 points) I suggest using the sklearn module, e.g.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-homework-question/homework3_question3_3.jpg" style="zoom:150%;" />

Plot 2D scatter plots for PC0 vs PC1, PC0 vs PC2, and PC1 vs PC2; color code these by the search query used (Alzheimers vs cancer). (3 points) Comment on the separation or lack thereof, and any take-aways from that. (2 points)
Repeat the above using LDA instead of PCA. In your commentary, be sure to compare PCA vs LDA. (10 points)

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-homework-question/homework3_question3_4.jpg" style="zoom:150%;" />


### Solution


#### >> Code explanation: 

Imported AutoTokenizer, AutoModel, and loaded model and tokenizer.
Imported json, and load the file paper.json into dictionary all_data.
Imported pandas and sklearn.

1) I used the code provided in the exercise 3 as references.
For each paper, take the first token in the batch as the embedding. Then principal component analysis was applied to identify the first three principal components PC0, PC1, PC2. 

Imported library plotnine to draw the scatterplot between PC0 and PC1,PC0 and PC2, PC1 and PC2. Legends are three queries: Alzheimers, Alzheimers or cancer(outlier), cancer.

2) Imported classifier LinearDiscriminantAnalysis and library numpy.
First I created a one-dimensional vector y as target values: If query was Alzheimer's, y = 0; if query was Alzheimer's and cancer, y = 1; if query was cancer, y = 2. Then linear discriminant analysis was applied to identify the first two principal components PC0 and PC1.

Used library plotnine to draw the scatterplot between PC0 and PC1.


#### >> Question answer:

1) By labeling the PCA/LDA result with queries from the JSON file generated before, I could keep track of sources of papers, i.e, which paper came from searching for Alzheimers, which came from searching for cancer.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-running-result/Exercise3/code-to-keep-track-on-papers.jpg" style="zoom:150%;" />

2) 2D scatter plots for PC0 vs PC1, PC0 vs PC2, and PC1 vs PC2 are as follows, colored by the search query: 'Alzheimers', 'cancer', 'Alzheimers and cancer'.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-running-result/Exercise3/scatter-plot-for-PC0-PC1-using-PCA.jpg" style="zoom:150%;" />

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-running-result/Exercise3/scatter-plot-for-PC0-PC2-using-PCA.jpg" style="zoom:150%;" />

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-running-result/Exercise3/scatter-plot-for-PC1-PC2-using-PCA.jpg" style="zoom:150%;" />

Among these three figures, PC0 vs PC1, PC0 vs PC2 show more obvious separation between different queries('Alzheimers', 'cancer', 'Alzheimers and cancer'). While PC1 vs PC2 cannot separate different queries. Note that the overlap(showed in green) could be seen from PC0 vs PC1. 


3) For sklearn of LDA, the number of components n_components is the minimum of [number of classes - 1 and number of features]. Since I want the n_component to be at least 2, n_classes should be at least 3. That is why I chose to separate my data into three classes: For Alzheimer's, target value y = 0, for Alzheimer's and cancer, target value y = 1, for cancer, target value y = 2.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-running-result/Exercise3/scatter-plot-for-PC0-PC1-using-LDA.jpg" style="zoom:150%;" />


Differences between LDA and PCA: The main goal of LDA is classification. It is aimed to find a low-dimensional direction and minimize variance within each projected class and maximize variance between different projected classes. LDA needs labels since it wants to evaluate the accuracy of classification. 

While the main goal of PCA is dimension reduction. It is aimed to maximize variance within each projected class.

Both LDA and PCA could reduce dimension.




## Exercise 4

### Question

In slides3, we introduced the merge sort, a recursive sorting algorithm that works by recursively splitting the data in two until there is at most one data point in a group to be sorted. (Groups of size 0 or 1 cannot be out of order.) Sorted sub-lists are then merged. See the implementation in the slides for details or feel free to search online for more information.
Describe in words how you would parallelize this algorithm to work with two processes (5 points) and how you would validate the results and the speedup (5 points).
Extra credit: Use the multiprocessing module to implement a 2 process parallel version of the merge sort from slides3. Demonstrate that your solution can achieve at least a speedup of 1.5x. (5 points)



#### >> Question answer: 









## Exercise 5

### Question

Do data exploration on the dataset you identified in exercise 4 in the last homework, and present a representative set of figures that gives insight into the data. Comment on the insights gained. (5 points)
Are there any missing values in your data? (Whether the answer is yes or no, include in your answer the code you used to come to this conclusion.) If so, quantify. Do they appear to be MAR/MCAR/MNAR? Explain. (5 points) <-- This will be discussed in class on October 12.
Identify any data cleaning needs and write code to perform them. If the data does not need to be cleaned, explain how you reached this conclusion. (5 points)



#### >> Code explanation: 

Imported libraries pandas and matplotlib. The BRFSS dataset and other corresponding datasets(state_FIPS, income_value, education_value, which are used for data processing) were loaded. 

1) In order to explore the state data('_STATE'), first I replaced the _STATE column based on STATE_NAME, FIPS CODE from another dataframe state_FIPS. Then I counted the frequencies of each state using value_counts(), and saved into the dataframe df_state_frequency.

I used matplotlib to draw the bar charts of participants' states. The figure size, x/y label names, x/y sticks, figure title were set.

Same for variable sex(_SEX), income(_INCOMG) and education level(_EDUCAG').

2) To do the data cleaning, first I checked whether there are duplicates in the dataset data_2020. Then I counted the missing values of each column in the dataset, and saved into the dataframe data_2020_missing. In data_2020_missing, only kept the variables that count_missing_values > 1000. Then I cleaned the dataset data_2020, so that it only contains variables that have < 1000 missing values (i.e., drop the entire field if there are > 1000 missing values in this field).


#### >> Question answer: 

1) 

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-running-result/Exercise5/barplot-of-participant-sex-frequency.jpg" style="zoom:150%;" />

>> From the barplot of participants' sex, we could see that among participants in the Behavioral Risk Factor Surveillance System (BRFSS), there are more females than males(1.185:1). In addition, BRFSS has collected sex data of all participants since there is no missing values.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-running-result/Exercise5/barplot-of-participant-state-frequency.jpg" style="zoom:150%;" />

>> From the barplot of participants' state, we could see that among participants in the BRFSS, most people are from states such as Minnesota, Nebraska, New York, Ohio, and Maryland. This might cause selection bias since some most populated states(California, Texas, Florida, Pennsylvania) have fewer participants. This study was not conducted by using proportional sampling of state population.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-running-result/Exercise5/barplot-of-participant-income-frequency.jpg" style="zoom:150%;" />

>> From the barplot of participants' income, we could see that among participants in the BRFSS, most people's annual household income are over $50,000. However, there are a large proportion of participants(n = 80057) who did not report their annual income, which could also cause bias to the study results.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-running-result/Exercise5/barplot-of-participant-educationlevel-frequency.jpg" style="zoom:150%;" />

>> From the barplot of participants' education level, we could see that among participants in the BRFSS, most people are college/technical school graduated(n = 155340), college/technical school attended(n = 111387) and high school graduated(n = 107096). Since there are fewer missing values(n = 1887), the data seems to be reliable and could be used for further analysis.


2) Yes, there are missing values in my data. I used isnull().sum() to count the number of(or quantify) missing values in each column. 

From my perspective, these missing values are MAR, since there is a correlation between the ages of population and missing values: Most of the missing values come from columns _CLNSCPY, _SGMSCPY, _SGMS10Y, _RFBLDS4, _STOLDNA, _VIRCOLN, _SBONTIM, _CRCREC1. According to the codebook, these variables are data target at respondents aged 50-75, e.g., _STOLDNA refers to respondents aged 50-75 who have had a stool DNA test within the past three years. For people whose age are not in the range of 50 to 75, these columns are filled with missing values.

3) I checked whether there are duplicates in the dataset(the answer is no). The strategy I used for missing values was to drop the entire field(column) if there are over 1000 missing values in this field.




## Data source

Data of exercise 1-3 comes from [Entrez programming utilities](https://www.ncbi.nlm.nih.gov/books/NBK25500/).

In exercise 3, I also used [SPECTER](https://github.com/allenai/specter), [pytorch](https://pytorch.org/get-started/locally/), [transformers](https://huggingface.co/) and [sklearn](https://scikit-learn.org/stable/index.html).

Data of exercise 5 comes from [2020 BRFSS Data (SAS Transport Format)](https://www.cdc.gov/brfss/annual_data/2020/files/LLCP2020XPT.zip).

Unfortunately, the dataset is too large to be uploaded(307Mb).



## Maintainer
@QingyangYu0529
| Name        | Email                | Organization                                                 |
| :---------: | ---------------------| ------------------------------------------------------------ |
| Qingyang Yu | qingyang.yu@yale.edu | Graduate student, Yale School of Public Health, Yale University |
