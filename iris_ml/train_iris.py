"""
1.
Numpy is imported as a whole module and given and alias/nickname of np(handles numbers and arrays easily)
2.
Scikit-learn(sklearn) is a python library,
 a toolbox instead of building everything 
from scratch grab ready made tools.
3.
From sklearn module we now import things that we'll use in this projects
sklearn.datasets we get load_iris(load_iris is like the hello world of ML)
4.
Logistic Regression is our model(the brain of AI)
It answers yes or no questions or classification questions
5.
train_test_split 
In ML we dont want the computer to just memorize data so we split the data
into 2 Training data(computer uses this to learn patterns) and 
Testing data(computer is tested on this data...This is data it has not seen)
train_test_split sklearn function does this for us.

"""
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

"""
Imagine you are a flower scientist
You go to a garden and measure flowers
For each flower you write down: Sepal(length and width) Petal(width and length)
You also write the species(type) of the flower: Setosa,Virginica,Versicolor

So each flower has numbers that describe it(measurements) and an answer(species)
"""
#load the dataset into a variable called iris
iris = load_iris() 

"""The words target and data are conventional (standard names scikit-learn usesso everyone understands)"""
# features petal/sepal sizes
# X is where we keep the features(measurements of each flower)
# example row in x : [5.1,3.5,1.4.0.2]
"""
The input features(measurements, numbers we feed into the model)
"""
X = iris.data

#labels : iris species
#this is where we keep the labels(the species names but stored as numbers)
#eg: 0=Setosa, 1=Versicolor, 2=Virginica
"""
The output labels(the correct answers the species of the flowers)
"""
Y = iris.target

#so X are the inputs the flower measurements Y are the answers
# the actual flower species: Setosa, Versicolor, Virginica
#X is like questions and Y is like the answer key

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
"""
We need to split the data into 2 training data and testing data
Training set --> for computer to learn
Testing set  --> for computer to prove is learned
    ANALOGY
When studying for an exam you study using notes(training data)
When you a test to check if you actually learned(testing data)    
"""

"""
What this means is train some data in X and Y...Split it for testing and training using the train_test_split()
30% of the data should be for testing and the 70% for training our model
"""
#Seed random_state
"""
Think of shuffling a deck of cards..Without seed every shuffle is in a random order
With random_state=42...You shuffle the same way everytime
 so you and your friend can both play with the same card order
"""

clf = LogisticRegression(max_iter=200)
clf.fit(X_train, Y_train)

#clf = LogisticRegresssion(max_iter=200)
"""
LogisticRegression is the ML model we are using.
Think of it like choosing a type of calculator that knows how make decisions
"""
#clf is just the name of the model you can name it anything...clf = classifier
#max_iter= Try up to 200 iterations to figure out the best rules
"""
sometimes model needs to repeat calculations before it learns
"""

#clf.fit(X_train,Y_train)
"""
.fit() --> Is a function that tells the model to train or learn
X_train --> The flower measurements (petal length/width)--> Input Data
Y_train --> The correct flower species --> Output Data
"""
#calling the function basically means here are some questions X_train
#and here are the correct answers Y_train Study them and learn patterns

y_pred = clf.predict(X_test)
"""
clf is our trained model(like a student who has already
 studied with training data)
it now knows how flower measurements map to flower species.

.predict(X_test)
 --> predict() is a method(a function that belongs to clf)
 --> We give it X_test the measurements of flowers the model has never seen before
 --> It returns its best guesses for what species those flowers are
"""
#y_pred is the varible that stores the predictions
#It's like a list of guesses the model makes for all flowers in X_test

print(classification_report(Y_test, y_pred))
"""
y_test are the real answers(the actual flower species)--> The real answers
y_pred these are the model's guesses(predictions)--> The student's answers in the exam
"""
#classification_report(Y_test,Y_pred)
#This function compares the guesses and the real answers
"""
It creates a report card with metrics like:
Precision -> Out of all times model said class A how often was it right
Recall -> Out of all actuall class A items how many did the model catch?
F1-score -> A balanced score between precison and recall
Support -> How many test samples were in each class
"""