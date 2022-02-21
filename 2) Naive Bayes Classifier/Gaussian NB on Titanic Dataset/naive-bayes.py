import pandas as pd
import matplotlib.pyplot as plt  
from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn.metrics import mean_squared_error   




dataframe = pd.read_csv("titanic.csv")

dataframe = dataframe.drop(["Name"],axis=1)

print(dataframe.describe())


ages = dataframe["Age"].values
fares = dataframe["Fare"].values
survived = dataframe["Survived"].values
colors = []
for item in survived:
	if item == 0:
		colors.append('red') 
	else:
		colors.append('green')	



Features = dataframe.drop(['Survived'],axis=1).values
Targets = dataframe['Survived'].values

Features_train, Targets_train = Features[0:710], Targets[0:710]
Features_test, Targets_test = Features[710:], Targets[710:] 

model = GaussianNB()
model.fit(Features_train,Targets_train)
predicted_values = model.predict(Features_test)

for item in zip(Targets_test,predicted_values):
	print("Actual was: ", item[0], "Predicted was: ", item[1])

print("Accuracy is", model.score(Features_test,Targets_test)) 