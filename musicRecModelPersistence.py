"""
This is a snippet from the music recommendation app.
I did extract it to help me have a deeper understanding and a better explanation of Model Persistence
"""

from sklearn.tree import DecisionTreeClassifier
#joblib to save our pre-trained model
import pandas as pd
import joblib


musicData = pd.read_csv('music.csv')
X = musicData.drop(columns=['genre'])
y = musicData['genre']

model = DecisionTreeClassifier()
model.fit(X, y)

# now saving the pre-trained model
joblib.dump(model, 'music-recommender-app.joblib')