# projects/pizzaDS
Dataset consists of nine columns namely brand, id, moisture, protein, fat, ash, sodium, carbohydrates and calories. Among these, brand is a dependent variable and apart from id remaining all are independent variables.
The objective of the dataset is to find the brand based on the values of moisture, protein, fat, ash, sodium, carbohydrates and calcium using KNN algorithm.
import required libraries
plotted top 5 rows of a dataset using .head()
categorized columns as dependnt(X) and independent variables(Y)
Since we want to plot brands with different colors, changed each brand to a unique number as cmap accepts series of numbers.
describes the statistical summary of the dataset.
Check if there are any null values.
Plotted different classes w.r.t their instances to check if the dataset is baised or not.
Split the dataset into training and testing. Here taken default which is 75% of training data and 25% of testing data.
plotted relation of independent variables. Here, we can draw various conclusions like as fat increases calories increases, sodium and ash directly related etc.
Using KNN Algorithm to find the accuracy of the model (KNN because it is a balaced DS, optimal number of classes and instances)
checking various algorithms, and metrics to find the nearest neighbors and accuracy of the model is determined.
Here we got 108 unique predictions, out of these we got 3 unique brands outputs for the test data and the accuracy is 81.3%
Taken the max value prediction parameters.
To test the model accuracy, we use k fold cross validation and leave one out method.
For k fold cross validation(k=5). Here the entire data is divided as 80% training and 1st 20% fold as testing (100/5). In a similar fashion,accuracy is tested on 5 different folds. Avg of all these is taken.
For leave one out method, entire data is given for training and 1 data point is used for testing. Here the accuray will be more as majority of the dataset is given training.  

