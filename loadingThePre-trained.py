"""
This is a snippet from the pre-trained music recommendation app.py built just moments ago.
I did extract it to help me have a deeper understanding and a better explanation of importing pre-trained Models for Persistence
"""

from sklearn.tree import DecisionTreeClassifier
#joblib to save our pre-trained model
import pandas as pd
import joblib

# now loading the pre-trained model from our current local directory, without need to re-train
model = joblib.load('music-recommender-app.joblib')
# We use it to makee predictions.

predictions = model.predict([[22, 0]])
print(predictions)