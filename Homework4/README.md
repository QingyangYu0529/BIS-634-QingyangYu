# Readme for HW #4

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

Suppose we have a neural network for predicting the time between hospital readmissions for a certain subset of patients. Such a network would depends on many parameters, but for simplicity, let's assume there's only two parameters: a and b. Each parameter lies between 0 and 1 and represents the weights of two "synapses" in our model.
Using the [API at e.g.](http://ramcdougal.com/cgi-bin/error_function.py?a=0.4&b=0.2). 
one can find the prediction errors in arbitrary units of running our model with specified parameters (here a=0.4 and b=0.2, but you can change that).
Implement a two-dimensional version of the gradient descent algorithm to find optimal choices of a and b. (7 points) (Optimal here means values that minimize the error.) See slides 12 for a 1-dimensional implementation of the algorithm. Explain how you estimate the gradient given that you cannot directly compute the derivative (3 points), identify any numerical choices -- including but not limited to stopping criteria -- you made (3 points), and justify why you think they were reasonable choices (3 points).
It so happens that this error function has a local minimum and a global minimum. Find both locations (i.e. a, b values) querying the API as needed (5 points) and identify which corresponds to which (2 point). Briefly discuss how you would have tested for local vs global minima if you had not known how many minima there were. (2 points)
Important: a key part of this problem is the implementation of the algorithm; do not use a Python library for gradient descent or copy gradient descent code from a website.


### Solution

#### >> Code explanation

```python
def dfda(a, b, h):
    return (f(a + h,b) - f(a,b))/h

def dfdb(a, b, h):
    return (f(a,b + h) - f(a,b))/h

def gradf(a, b, h):
    return np.array([dfda(a, b, h), dfdb(a, b, h)]) 
```

Functions dfda(a,b,h), dfdb(a,b,h) were defined to retrun derivatives of f(a,b) with respect to a or b.
Function gradf(a,b,h) would return a 2D vector, which contains dfda(a,b,h) and dfdb(a,b,h).

```python
def two_dimension_grad_descent(init_guess, gamma, h, threshold):
    prev_guess = init_guess - 10 * threshold
    guess = init_guess
    
    # save values of a, b and f(a,b) into lists.
    guess_a = []
    guess_b = []
    f_result = []
    iteration = 0
 
    while norm(guess - prev_guess) > threshold and iteration < 5000:
        prev_guess = guess
        
        guess = guess - gamma * gradf(guess[0], guess[1], h)
        guess_a.append(guess[0])
        guess_b.append(guess[1])
        f_result.append(f(guess[0], guess[1]))
        iteration = iteration + 1
        
    print (f"The minimum value {f_result[-1]} occurs when a = {guess_a[-1]}, b = {guess_b[-1]}.")

```
In function two_dimension_grad_descent(), the stopping criteria contains two parts: only when norm of gradient is big enough(bigger than a artificial threshold), or the number of iteration is smaller than the maximum value, the while loop will continue.

Each time the parameters a and b were moved a little bit, in the direaction where f(a,b) decreases in a fastest speed.

#### >> Question answer

1) Since I cannot directly compute any derivative because I don't know the details of error function f(a,b), I used the definition of derivative f'(x) = f(x + h) - f(x)/h to approximate the gradient as below:

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework4/Figures-in-running-results/Exercise1/method-to-approximate-derivative.png" style="zoom:90%;" />

Since △a, △b are both small increments, same as △h. In the codes, I set △a and △b as h = 1e-4.

2) I set the learning rate gamma as 0.1, which is used to update parameters a and b, so that it could decrease in a rather fast speed(since common learning rate are 0.01, 0.0001, 0.05, 0.1).

For the stopping criteria: 1.when the norm of gradient is smaller than a artificial threshold(I set as 1e-8, which is small enough). 2.when the for-loop reaches a maximum number of iterations (I set the maximum value as 5000).

I set the small increment h as 1e-4, same as slide 12, which is samll enough to be in the derivative formula.

I set the initial guess value init_guess as a array, in which a = 0.1, b = 0.8(meet the requirements that they lie between 0 and 1). 

3) The local minimum is 1.100000005, when a = 0.21595000000038012, b = 0.6889500399996086.
The global minimum is 1.000000015, when a = 0.7119500099998601, b = 0.16895000000010207.

If I do not know how many minimums there were, I would 
try different combinations(e.g. a = 0.001, b = 0.999; a = 0.999, b = 0.001; a = 0.999, b = 0.999; a = 0.001, b = 0.001; a = 0.5, b = 0.5) of extreme values of a and b to find local and global minimums, values of other parameters remain the same.

The smallest value is global minimum, others are local minimum.




## Exercise 2

### Question

In this exercise, we'll look at the distribution of cities across the planet. The same approach would work for disease outbreaks. Begin by downloading the basic (free) data set from [Links to an external site](https://simplemaps.com/data/world-cities); this data is licensed CC BY 4.0. We will ignore everything except the locations of the cities, which are identified by 'lng' (longitude) and 'lat' (latitude).
Note: distance between two points on Earth is not proportional to the square root of the sum of the squares of the differences in coordinates because (1) latitude and longitude have different ranges, and (2) the Earth is round. Instead of using Euclidean distance, use the Haversine formula; a Python implementation can be found in the accepted answer to [Links to an external site](https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points)

As briefly introduced in slides13, k-means is an algorithm for automatically identifying clusters in data. Lloyd's algorithm (there are others) for k-means is simple: for a given k, pick k points at pseudo-random from your data set (this is called the Forgy method for initialization, there are other other strategies). These will be "seeds" for forming k clusters. Assign each data point to a cluster based on whichever seed point is closest. Iterate, using the centroid of each cluster as the seeds for the next round of point assignments. Repeat until convergence.
Modify the k-means code (or write your own) from slides13
to use the Haversine metric and work with our dataset (5 points). Note: since this algorithm uses (pseudo)randomness, you'll have to run it multiple times to get a sense of expected runtime. Visualize your results with a color-coded scatter plot (5 points); be sure to use an appropriate map projection (i.e. do not simply make x=longitude and y=latitude; 5 points). Use this algorithm to cluster the cities data for k=5, 7, and 15. Run it several times to get a sense of the variation of clusters for each k (share your plots) (5 points); comment briefly on the diversity of results for each k. (5 points)



### Solution


#### >> Code explanation

When I installed Basemap and tried to import it, there was an importerror: cannot import name 'dedent' from 'matplotlib.cbook'. I used codes to defind dedent [from this website](https://www.youtube.com/watch?v=MCl6qY7VqRM), then Basemap could work.

```python
loc_data = pd.read_csv("worldcities.csv")
loc_data = loc_data[['lng', 'lat']]
```

1) First I extracted the column 'lng', 'lat' from the file "worldcities.csv".

```python
def centers(df, k):
    pts = [np.array(pt) for pt in zip(df['lat'], df['lng'])]
    centers = random.sample(pts, k)
    old_cluster_ids, cluster_ids = None, [] # arbitrary but different
    while cluster_ids != old_cluster_ids:
        old_cluster_ids = list(cluster_ids)
        cluster_ids = []
        for pt in pts:
            min_cluster = - 1
            min_dist = float('inf')
            for i, center in enumerate(centers):
                # use Haversine function here.
                dist = haversine(pt[1], pt[0], center[1], center[0])
                if dist < min_dist:
                    min_cluster = i
                    min_dist = dist
            cluster_ids.append(min_cluster)
        df['cluster'] = cluster_ids
        cluster_pts = [[pt for pt, cluster in zip(pts, cluster_ids) if cluster == match]
                        for match in range(k)]
        centers = [sum(pts)/len(pts) for pts in cluster_pts]
        
    return df['cluster']

def haversine(lng1, lat1, lng2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])

    # haversine formula 
    dlng = lng2 - lng1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlng/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r
```

2) Function centers() was used to find the cluster center by k-means clustering. In the function, I used Haversine formula to calculate the distance between two GPS points. The function continuouslly repeated until convergence, the coordinates of k centers were returned as result.

```python
def draw_figure(cluster,k):
    plt.figure(figsize=(15,9))
    map = Basemap(projection='robin', lat_0 = 0, lon_0 = 0, resolution = 'c')
    # draw coastlines.
    map.drawcoastlines()
    # convert to map projection coordinates.
    x, y = map(lngs, lats)
    map.scatter(x, y, c = cluster, cmap = 'jet', s = 0.6, alpha = 0.3 )
    map.drawmapboundary(fill_color='aqua')
    plt.title(f"Distribution of world cities when k = {k}", color = 'white', fontsize = 15)
    plt.show()

def runtime(k):
    times = []
    start = time.time()
    cluster = list(centers(loc_data,k))
    end = time.time()
    times.append(end - start)
    print (f"The runtime when k = {k} is {times[0]} second.")
    return cluster
```

3) Instead of simply making x = lng and y = lat, I used Robinson Projection, which is a common map projection of a world map, and convert my x and y values(original coordinates) to map projection coordinates.

4) Function draw_figure() and runtime() were used to visualize results with color-coded scatterplots, and to record the runtime of k-means cluster.

```python
for count in range(10):
    # set k = 5, 7 and 15. find the cluster center and draw the figures.
    cluster_k5 = runtime(5)
    draw_figure(cluster_k5,5)
    cluster_k7 = runtime(7)
    draw_figure(cluster_k7,7)
    cluster_k15 = runtime(15)
    draw_figure(cluster_k15,15)
```

5) I set k = 5, 7 and 15, and run 10 times for each k to see the results.


#### >> Question answer

1) About runtime of the algorithm:

Runtime tends to change in a wide range. For k = 5 , it took approximately 10 seconds. For k = 7, it took approximately 15 seconds. For k = 15, it took approximately 54 seconds.

2) About variation of clusters for each k:

Since Antarctica does not have cities, the other six continents were considered.

When k = 5, the two adjacent continents (e.g. Asia and Australia, North America and South America, Europe and Africa) always merge together.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework4/Figures-in-running-results/Exercise2/North-America-and-South-America-merges.png" style="zoom:90%;" />

> k = 5, when North America and South America merge together.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework4/Figures-in-running-results/Exercise2/Asia-and-Australia-merges.png" style="zoom:90%;" />

> k = 5, when Asia and Australia merge together.

When k = 7, Asia was more often to be split into two clusters, since it is the biggest continent.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework4/Figures-in-running-results/Exercise2/Asia-split-into-two-clusters1.png" style="zoom:90%;" />


<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework4/Figures-in-running-results/Exercise2/Asia-split-into-two-clusters2.png" style="zoom:90%;" />

> k = 7, when Asia was split into two clusters.



## Exercise 3

### Question

In class, we discussed two different strategies for computing the Fibonacci sequence: directly with the recursive strategy, and recursive but modified using lru_cache. Implement both (yes, I know, I gave you implementations on the slides, but try to do this exercise from scratch as much as possible) (5 points), time them as functions of n (5 points), and display this in the way you think is best (5 points). Discuss your choices (e.g. why those n and why you're displaying it that way; 5 points) and your results (5 points).


### Solution


#### >> Code explanation



#### >> Question answer






## Exercise 4

### Question

Implement a function that takes two strings and returns an optimal local alignment (6 points) and score (6 points) using the Smith-Waterman algorithm; insert "-" as needed to indicate a gap (this is part of the alignment points). Your function should also take and correctly use three keyword arguments with defaults as follows: match=1, gap_penalty=1, mismatch_penalty=1 (6 points). Here, that is a penalty of one will be applied to match scores for each missing or changed letter.

```python
For example:
seq1, seq2, score = align('tgcatcgagaccctacgtgac', 'actagacctagcatcgac')
# there are several possible results, but one is:
# seq1 = agacccta-cgt-gac
# seq2 = aga-cctagcatcgac
# score = 8 (true for all results)
seq1, seq2, score = align('tgcatcgagaccctacgtgac', 'actagacctagcatcgac', gap_penalty=2)
# there is only one possibility: seq1 = seq2 = gcatcga, score=7
```

Test it, and explain how your tests show that your function works. Be sure to test other values of match, gap_penalty, and mismatch_penalty (7 points).


#### >> Code explanation

```python
def scoring_matrix(seq1, seq2, match, mismatch, gap_penalty):
    # generate a matrix with zeros, size is (seq1+1)*(seq2+1).
    matrix = np.zeros((len(seq1) + 1, len(seq2) + 1), int)

    max_score = 0
    max_pos = 0
    for i, j in itertools.product(range(1, matrix.shape[0]), range(1, matrix.shape[1])):
        # if bases in the position[i-1] and [j-1] match each other, add match score.
        if seq1[i - 1] == seq2[j - 1]:
            match_score = matrix[i - 1, j - 1] + match
        # if bases in the position[i-1] and [j-1] do not match each other, substract mismatch score.
        else:
            match_score = matrix[i - 1, j - 1] - mismatch
        # return the value in the position[i-1,j] and [i,j-1], substract gap_penalty.
        deletion = matrix[i - 1, j] - gap_penalty
        insertion = matrix[i, j - 1] - gap_penalty
        # take the largest value among match_score, deletion, insertion and zero.
        score = max(match_score, deletion, insertion, 0)
        matrix[i, j] = score
        # find the position that has largest value in the matrix to traceback.
        if score > max_score:
            max_score = score
            max_pos = (i, j)
    print (matrix)
    return matrix, max_pos
```

1) Function scoring_matrix(), was defined to set and calculate the scoring matrix. First a matrix with zeros was generated, size was (length of seq1+1)*(length of seq2+1). For each position(i,j), calculate the match_score, deletion, insertion according to scoring rule, then took the largest value among match_score, deletion, insertion and zero.
Also found the position that has largest value in the matrix to traceback, saved into variable max_pos.

```python
def next_move(matrix, x, y):
    diagonal = matrix[x-1][y-1]
    up = matrix[x-1][y]
    left = matrix[x][y-1]
    if diagonal >= up and diagonal >= left:
        if diagonal != 0:
            # 1 means go to diagonal direction.
            return 1
            # 0 means end. no more movement.
        else: return 0
    elif up > diagonal and up >= left:
        if up != 0:
            # 2 means go to up direction.
            return 2
        else: return 0
    elif left > diagonal and left > up:
        if left != 0:
            # 3 means go to left direction.
            return 3
        else: return 0
    else:
        print("error")
```

2) Function next_move() was defined to decide the next move when traceback(return as a value). Among the diagonal, up and left directions, always go to the position that has largest value, recorded the position: 0 means end, no more movement. 1 means go to diagonal direction. 2 means go to up direction. 3 means go to left direction.

```python
def traceback(seq1, seq2, matrix, start_pos):
    # lists aligned_seq1, aligned_seq2 are used to save the aligned results.
    aligned_seq1 = []
    aligned_seq2 = []
    x, y = start_pos
    move = next_move(matrix, x, y)
    # if next move is end, break while loop.
    while move != 0:
        # if next move is diagonal direction.
        if move == 1:
            aligned_seq1.append(seq1[x-1])
            aligned_seq2.append(seq2[y-1])
            x = x - 1
            y = y - 1
        # if next move is up direction.
        elif move == 2:
            aligned_seq1.append(seq1[x-1])
            aligned_seq2.append('-')
            x = x - 1
        # if next move is left direction.
        else:
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[y-1])
            y = y - 1

        move = next_move(matrix, x, y)
    
    aligned_seq1.append(seq1[x - 1])
    aligned_seq2.append(seq2[y - 1])

    return ''.join(reversed(aligned_seq1)), ''.join(reversed(aligned_seq2))
```

3) Function traceback() was defined to traceback from the calculated scoring matrix, to get the optimal alignment of seq1 with seq2. If next move was diagonal, saved seq1[x-1], seq2[y-1] into lists aligned_seq1, aligned_seq2. If next move was up, saved seq1[x-1] and '-'(indicate a gap) into lists aligned_seq1, aligned_seq2. If next move was left, saved '-' and seq2[y-1] into lists aligned_seq1, aligned_seq2.

```python
def smith_waterman(seq1, seq2, match, mismatch, gap_penalty):
    # calculate and generate scoring matrix.
    matrix, start_pos = scoring_matrix(seq1, seq2, match, mismatch, gap_penalty)
    # traceback to get the optimal alignment of seq1 with seq2.
    seq1_aligned, seq2_aligned = traceback(seq1, seq2, matrix, start_pos)
    # final score is the value in the position start_pos of the matrix.
    final_score = matrix[start_pos[0]][start_pos[1]]
    print ("aligned seq1 = ", seq1_aligned)
    print ("aligned seq2 = ", seq2_aligned)
    print ("score is" , final_score)
```

4) Function smith_waterman() combined above three functions, returned aligned seq1, aligned seq2 and match score.


#### >> Testing

First I used sequences in the exercise 4(seq1 = 'tgcatcgagaccctacgtgac', seq2 = 'actagacctagcatcgac'), . It turned out that match score was 8, aligned seq1 was agacccta-cgt-gac, aligned seq2 was agacc-tagcatcgac. According to the scoring rule, match score = 12*1(match) - 1*1(mismatch, g->a) - 3*1(gap) = 8, which was consistent with the printed score.

Then I used another pair of sequences in the exercise 4(seq1 = 'tgcatcgagaccctacgtgac', seq2 = 'actagacctagcatcgac'), and set gap penalty as 2. It turned out match score was 7, aligned seq1 was gcatcga, aligned seq2 was gcatcga. According to the scoring rule, match score = 7*1(match), which was also consistent with the printed score.

I also used other other values of match, gap_penalty, and mismatch_penalty for testing. Results were compared with the [website](http://rna.informatik.uni-freiburg.de/Teaching/index.jsp?toolName=Smith-Waterman)(if you input seq1, seq2, match, mismatch, gap_penalty, this website could return the aligned sequence and match score).

1) Seq1 = 'tgccgttgaatcg', seq2 = 'ctccttggaacg'. Match = 1, mismatch = 1, gap = 1.
Match score was 6, aligned seq1 was ccgttg-aatcg
aligned seq2 was cc-ttggaa-cg, same as result from website.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework4/Figures-in-running-results/Exercise4/website-result1.png" style="zoom:90%;" />

2) If changed match = 2, mismatch = 2, gap = 2.
Match score was 12, aligned seq1 was ccgttg-aatcg
aligned seq2 was cc-ttggaa-cg, same as result from website.

<img src="https://github.com/QingyangYu0529/BIS-634-QingyangYu/blob/main/Homework4/Figures-in-running-results/Exercise4/website-result2.png" style="zoom:90%;" />

3) Seq1 = 'TGCCGTTGAATCG', seq2 = 'CTCCTTGGAACG'. Match = 1, mismatch = 1, gap = 1.
Match score was 6, aligned seq1 was ccgttg-aatcg
aligned seq2 was cc-ttggaa-cg, same as result from website.


## Data source

In exercise 2, data comes from [simplemaps.com](https://simplemaps.com/data/world-cities).



## Maintainer
@QingyangYu0529
| Name        | Email                | Organization                                                 |
| :---------: | ---------------------| ------------------------------------------------------------ |
| Qingyang Yu | qingyang.yu@yale.edu | Graduate student, Yale School of Public Health, Yale University |
