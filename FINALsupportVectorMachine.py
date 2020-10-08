
# coding: utf-8

# In[2]:

#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVC
import joblib


# In[3]:

#importing the dataset
dataset = pd.read_csv("Dataset.csv")
dataset = dataset.drop('id', 1) #removing unwanted column
x = dataset.iloc[: , :-1].values
y = dataset.iloc[:, -1:].values
dataset.head()


# In[4]:

#spliting the dataset into training set and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.1, random_state =42 )


# In[5]:

# #applying grid search to find best performing parameters
# from sklearn.model_selection import GridSearchCV
# parameters = [{'C':[1, 10, 100, 1000], 'gamma': [ 0.1, 0.2,0.3, 0.5]}]
#
#
# # In[6]:
#
# grid_search = GridSearchCV(SVC(kernel='rbf' ), parameters,cv =5, n_jobs= -1)
#
#
# # In[7]:
#
# grid_search.fit(x_train, y_train.flatten())
#
#
# # In[ ]:
#
#
#
#
# # In[9]:
#
# #printing best parameters
# print("Best Accurancy =" +str( grid_search.best_score_))
# print("best parameters =" + str(grid_search.best_params_))

#fitting kernel SVM  with best parameters calculated 

classifier = SVC(C=100, kernel = 'rbf', gamma = 0.2 )
classifier.fit(x_train, y_train)

#predicting the tests set result
y_pred = classifier.predict(x_test)

#confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# print(confusion_matrix(y_test,  y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))



#pickle file joblib
# joblib.dump(classifier, 'svm.pkl')

