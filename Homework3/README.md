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

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-homework-question/homework3_question1_1.jpg" style="zoom:300%;" />

Here 32008517 is the PubMed ID of one of the 2000 papers, specifically one that came from searching for Alzheimer's papers. You should include the full AbstractText and list of MeSH terms; I'm abridging here for clarity.
Hint: To do this, you'll probably want to look at one of the XML responses with a text editor so that you understand how it is structured.
Hint: Some papers like 32008517 (Links to an external site.) have multiple AbstractText fields (e.g. when the abstract is structured). Be sure to store all parts. You could do this in many ways, from using a dictionary or a list or simply concatenating with a space in between. Discuss any pros or cons of your choice in your readme (1 point).
Caution: the PubMed API allows a rate of at most one query at a time and no more than 3 per second unless you have an API key. To be safe, use 

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-homework-question/homework3_question1_2.jpg" style="zoom:300%;" />

after each query to the PubMed API. 
Note: This doesn't require 2002 separate queries. You can get the metadata for many articles at a time by using a comma separated list of ids. While GET queries have a total line length limit, you could use a POST query instead and get the information for all the papers in one pass. (We can use POST instead of GET here in part because this is not a RESTful API.)
Note: BioPython provides functions for accessing the PubMed API. Do not use them; use the requests module to do an HTTP or HTTPS request directly on a URL that you specify with the parameters that you specify. Why? Because this approach is general and will work in many contexts whereas BioPython only works for PubMed and only from Python.



### Solution


#### >> Code explanation: 

Imported modules requests and minidom to parse the file.

1) 


#### >> Question answer: 

1) There is a overlap in the two sets of papers that I identified, the pubmed id is 32501203.









## Exercise 2

### Question:

This question refers to the Alzheimer's and cancer metadata stored in Exercise 1. It is not intended to involve any new queries to PubMed nor to make statements about PubMed beyond that of the papers whose data was obtained.
What fraction of the Alzheimer's papers have no MeSH terms? (2 points) What fraction of the cancer papers have no MeSH terms? (2 points) Comment on how the fractions compare. (1 point; i.e. if they're essentially the same, do you think that's a coincidence? If they're different, do you have any theories why?)
What are the 10 most common MeSH terms for the Alzheimer's papers whose metadata you found in Exercise 1? (2 points) Provide a graphic illustrating their relative frequency. (3 points)
What are the 10 most common MeSH terms for the cancer papers whose metadata you found in Exercise 1? (2 points) Provide a graphic illustrating their relative frequency. (3 points)
Make a labeled table with rows for each of the top 5 MeSH terms from the Alzheimer's query and columns for each of the top 5 MeSH terms from the cancer query. For the values in the table, provide the count of papers (combined, from both sets) having both the matching MeSH terms. (5 points) Ideally, you can have the computer generate the table directly, but if not you could use nested for loops, label your output, and manually assemble a table in your readme document. Comment on any findings or limitations from the table and any ways you see to get a better understanding of how the various MeSH terms relate to each other. (5 points)


### Solution

#### >> Code explanation: 

1)



#### >> Question answer: 

1) The number of Alzheimer's papers that have no MeSH terms is 164, which is 16% of total Alzheimer's papers.
The number of cancer papers that have no MeSH terms is 758, which is 76% of total cancer papers.

The fraction of cancer papers have no MeSH terms is much more than that of Alzheimer's papers. Compared with the term "Alzheimer's", "cancer" is a much broader term, which is associated with multiple non-cancer diseases, affecting people no matter what their nationality, genders, ages are, thus it is difficult to summarize the MeSH terms that related to "cancer"(it is not useful to list all the terms).

2) The 10 most common MeSH terms for the Alzheimer's papers are: Humans; Alzheimer Disease; Male; Female; Aged; Animals; Amyloid beta-Peptides; Brain; Aged, 80 and over; Cognitive Dysfunction.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-running-result/Exercise2/10-most-common-MeSH-terms-for-Alzheimer's-papers.jpg" style="zoom:300%;" />

The 10 most common MeSH terms for the cancer papers are: Humans; Female; Male; Middle Aged; Aged; Adult; Animals; Neoplasms; Retrospective Studies; Aged, 80 and over.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-running-result/Exercise2/10-most-common-MeSH-terms-for-cancer-papers.jpg" style="zoom:300%;" />


#### >> Testing process:

1) 



## Exercise 3

### Question

Machine learning and data visualization strategies generally work best on data that is numeric, but exercise 1 gave us text data, and indeed text is common. Fortunately, modern NLP algorithms powered by machine learning trained on massive datasets exist that can take words (e.g. word2vec) or titles and abstracts (e.g. SPECTER) and return a vector of numbers in a way that similar items are given similar vectors. Since we have titles and abstracts, let's use SPECTER.
In particular, for each paper identified from exercise 1, compute the SPECTER embedding (a 768-dimensional vector). Keep track of which papers came from searching for Alzheimers, which came from searching for cancer. (5 points) If you are familiar with SPECTER and wish to do it another way, that's great, if not here's one approach based on [Links to an external site](https://github.com/allenai/specter):
Install pytorch (a deep learning library) by following the instructions [here](https://pytorch.org/get-started/locally/)
Install the huggingface transformers module: [pip install transformers](https://huggingface.co/)
provides access to a number of pre-trained NLP language models.)
Have your code load the SPECTER model (the first time you do this, it will take a bit to download the model; it will be stored locally for fast reuse later):

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-homework-question/homework3_question3_1.jpg" style="zoom:300%;" />

Process your dictionary of papers:

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-homework-question/homework3_question3_2.jpg" style="zoom:300%;" />

At this point, embeddings[i] is the 768-dim vector for the ith paper.
Apply principal component analysis (PCA) to identify the first three principal components. (5 points) I suggest using the sklearn module, e.g.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-homework-question/homework3_question3_3.jpg" style="zoom:300%;" />

Plot 2D scatter plots for PC0 vs PC1, PC0 vs PC2, and PC1 vs PC2; color code these by the search query used (Alzheimers vs cancer). (3 points) Comment on the separation or lack thereof, and any take-aways from that. (2 points)
Repeat the above using LDA instead of PCA. In your commentary, be sure to compare PCA vs LDA. (10 points)

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework3/Figures-in-homework-question/homework3_question3_4.jpg" style="zoom:300%;" />


### Solution


#### >> Code explanation: 




#### >> Question answer:

1)


#### >> Testing process:

1) 



## Exercise 4

### Question

In slides3, we introduced the merge sort, a recursive sorting algorithm that works by recursively splitting the data in two until there is at most one data point in a group to be sorted. (Groups of size 0 or 1 cannot be out of order.) Sorted sub-lists are then merged. See the implementation in the slides for details or feel free to search online for more information.
Describe in words how you would parallelize this algorithm to work with two processes (5 points) and how you would validate the results and the speedup (5 points).
Extra credit: Use the multiprocessing module to implement a 2 process parallel version of the merge sort from slides3. Demonstrate that your solution can achieve at least a speedup of 1.5x. (5 points)



#### >> Code explanation: 


#### >> Question answer: 


#### >> Testing process:




## Exercise 5

### Question

Do data exploration on the dataset you identified in exercise 4 in the last homework, and present a representative set of figures that gives insight into the data. Comment on the insights gained. (5 points)
Are there any missing values in your data? (Whether the answer is yes or no, include in your answer the code you used to come to this conclusion.) If so, quantify. Do they appear to be MAR/MCAR/MNAR? Explain. (5 points) <-- This will be discussed in class on October 12.
Identify any data cleaning needs and write code to perform them. If the data does not need to be cleaned, explain how you reached this conclusion. (5 points)



#### >> Code explanation: 


#### >> Question answer: 
1)


2) Yes, there are missing values in my data. I used isnull().sum() to count the number of(or quantify) missing values in each column. 

From my perspective, these missing values are MAR, since there is a correlation between the ages of population and missing values: Most of the missing values come from columns _CLNSCPY, _SGMSCPY, _SGMS10Y, _RFBLDS4, _STOLDNA, _VIRCOLN, _SBONTIM, _CRCREC1. According to the codebook, these variables are data target at respondents aged 50-75, e.g., _STOLDNA refers to respondents aged 50-75 who have had a stool DNA test within the past three years. For people whose age are not in the range of 50 to 75, these columns are filled with missing values.



#### >> Testing process:



## Data source

Data of exercise1 comes from [hw2-patients.xml](https://yale.instructure.com/courses/70314/files/5401025/download?download_frd=1).

Data of exercise2 comes from [the latest Human Reference Genome(GRCh38.p13)](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/405/GCA_000001405.28_GRCh38.p13/GCA_000001405.28_GRCh38.p13_genomic.fna.gz).

Data of exercise4 comes from [2020 BRFSS Data (SAS Transport Format)](https://www.cdc.gov/brfss/annual_data/2020/files/LLCP2020XPT.zip).



## Maintainer
@QingyangYu0529
| Name        | Email                | Organization                                                 |
| :---------: | ---------------------| ------------------------------------------------------------ |
| Qingyang Yu | qingyang.yu@yale.edu | Graduate student, Yale School of Public Health, Yale University |
