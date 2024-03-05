# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "K-means has problems when the data contains outliers. Becasue K-means minimize the variance within each cluster, which can be significantly affected by outliers. But hierarchical clustering can more easily isolate outliers as single-point clusters or merge them at a later stage in the process without significantly affecting the overall clustering structure"

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "In k mean, different cluster assignments in different runs, especially in complex datasets or when the number of clusters is not clearly defined.But hierarchical clustering constructs a dendrogram by iteratively merging the closest clusters based on a distance metric and linkage criterion (single, complete, or average linkage). Once the process starts with individual points as clusters, it follows a strict set of rules to merge clusters, leading to the same clustering result every time for a given dataset and set of parameters"

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "It denpend on on the context.While k-means is efficient in many scenarios, its performance and suitability can vary depending on the dataset's characteristics, the number of dimensions, and the shape and size of the data distribution. Other clustering algorithms might be more efficient or appropriate for specific types of data or clustering objectives"

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "SSE improves in each iteration of K-means until it reaches a local or global minima."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = " it means the distances between the data points and their respective cluster centroids are getting smaller, which d"

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "average distance between cluster centroids and the overall dataset centroid is increasing, implying that clusters are more spread out from each other."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "Because SSB + SSE = constant"

    # type: bool (True/False)
    answers["(h)"] = False

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "In K-means clustering, SSE (Sum of Squared Errors) represents the total within-cluster variation, while BSS (Between Sum of Squares) represents the total between-cluster variation. These two metrics are not constant during the clustering process"

    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "The relationship between cohesion and separation depends on various factors such as the dataset's structure, the number of clusters, and the initial placement of centroids."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "centroid move untill SSE is minimum"

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "it is hard for k-means method to cluster this shape points"

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Midlle centroid is farther away from the nearest data point than other centroid"

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4*(R^2)"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*((a^2)+(b^2)+(R^2))" 

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "9(R^2)"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 0

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "becasue A, B have 100 data point, which is smaller than C."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "becasue A, B and C cicle show same distance"

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 1

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Two initial centroid. A and B show close distance"

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] =  set({"Group A", "Group B"})

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The distance between the closest data points in sets A and B is shorter than that between A and C  "

    # type: set
    answers["(b)"] = set({"Group A", "Group C"})

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The distance between the farthest data points in sets A and C is shorter than that between A and B"

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = set({'BCEFIJLM'})

    # type: set
    answers["(a) boundary"] = set({'DG'})

    # type: set
    answers["(a) noise"] =set({'AH'})
    
    # type: set
    answers["(b) cluster 1"] = set({'BCDEFG'})

    # type: set
    answers["(b) cluster 2"] = set({'JLIM'})

    # type: set
    answers["(b) cluster 3"] = set({'None'})

    # type: set
    answers["(b) cluster 4"] = set({'None'})
    
    # type: set
    answers["(c)-a core"] = set({'BCDEFGIJLM'})

    # type: set
    answers["(c)-a boundary"] = set({'AH'})

    # type: set
    answers["(c)-a noise"] = set({'None'})

    # type: set
    answers["(c)-b cluster 1"] = set({'ABCDEFG'})

    # type: set
    answers["(c)-b cluster 2"] = set({'HIJLM'})

    # type: set
    answers["(c)-b cluster 3"] = set({'None'})

    # type: set
    answers["(c)-b cluster 4"] = set({'None'})

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "because it show lowest purity."

    # type: string
    answers["(b)"] = "Cluster4"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "because it show higest purity. Water show heghest"

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "two data set are not purified, two clusters are not highly converged "

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = ""

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = " two clusters are not highly converged"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = ""

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = ""

    # type: string
    answers["(b) Row 1"] = "A"

    # type: string
    answers["(b) Row 2"] = "B"

    # type: string
    answers["(b) Row 3"] = "C"

    # type: string
    answers["(b) Row 4"] = "D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = ""

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['hierarchical','overlapping','complete']

    # type: list
    answers["(b)"] = ['partitional','exclusive','complete']

    # type: list
    answers["(c)"] = ['partitional','exclusive','incomplete']

    # type: list
    answers["(d)"] = ['hierarchical','overlapping','incomplete']

    # type: list
    answers["(e)"] = ['partitional','exclusive','complete']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "A student has only one letter,  every student will get the grade."

    return answers


# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "Yes"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = " In small eps, there will be a boundary between the light side and the dark side. It can distinguish the different part. For B, we can use a large min_samples, so it will distinguish the dark side, we get what we want."

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "No"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "k-means is not a good way to cluster unnormal distribution datasets. Clusters are spherical and similar size, it is not useful in this case."

    # type: string
    answers["(c)"] = "spectral clustering"

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
