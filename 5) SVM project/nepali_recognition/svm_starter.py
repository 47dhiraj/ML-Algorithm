import pandas as pd
import joblib                   #joblib helps to save your machine learning models .. so that it provides fast & speed to your system
import numpy as np
import matplotlib.pyplot as plt  

from sklearn import svm                                    # sklearn batw support vector machine lai import gareko

from sklearn import metrics
from sklearn.model_selection import train_test_split       # it split your data into train & test data points


##Step 1: Get Data from CSV

df = pd.read_csv("csv/dataset.csv", encoding="utf-8")
# print(df.shape)

##Step 2: Seperate Labels and Features
 
X = df.drop(['label'], axis=1)          # x ma features rakhne vayera label vanni column lai falera.. baki sabbai 784 pixel columns lai features garayeko
Y = df['label']                         # y ma target rakhne garincha... so label vaanni single column lai as target y ma rakheko
# print(Y)

# For checking number of the unique classess of Y or target 
# print(len(np.unique(Y)))          # yedi number of class 1 matra aayo vani, model.fit(X_train,Y_train) command nai run hudaina i.e yo python ko nai feature ho,, model.fit() garera model lai train garna ko lagi Y ma classess jahile 2 or 2 vanda badi huncha parcha so, 1 ta matra class vayo vani error aaucha

# # splitting your dataset into training and testing data
X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.1,random_state=38)        # random_state ma jun sukai auta number rakhdiye huncha.. i.e output aaune bela ma harek execution ma random output naaaos vanna ko lagi ho
# print(X_train)
# print(Y_train)
# print(Y_test)

# ##Step 3: Make sure you have the correct Feature / label combination in training



##Step 4: Build a Model and Save it

# # model = svm.SVC(gamma='auto')           # by default it uses the rbf kernel (i.e yeti bela rbf kernel use gari rako cha) #support vector machine ko support vector classifier ko model instance create gareko
model = svm.SVC(gamma='auto', kernel='linear')
model.fit(X_train,Y_train)                   # yo line ma y ko number of classes has to be greater than one

joblib.dump(model, "model/svm_36label")         # joblib.dump() le tmro machine learning model lai save garaune kaam garcha

##Step5 : Print Accuracy 
print("Accuracy Score",model.score(X_test,Y_test))             

# Alternative way for viewing model score ==> metrics.accuracy_score()









