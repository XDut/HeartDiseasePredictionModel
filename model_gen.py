import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import pickle
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data = pd.read_csv('./heart.csv')

x = data.iloc[:, :-1].values

y = data.iloc[:, -1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=1)

model = RandomForestClassifier(random_state=1)# get instance of model

model.fit(x_train, y_train) # Train/Fit model

y_pred = model.predict(x_test) # get y predictions

pickle.dump(model, open('model.sav', 'wb'))

