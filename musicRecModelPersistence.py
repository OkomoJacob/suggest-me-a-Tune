"""
This is a snippet from the music recommendation app.
I did extract it to help me have a deeper understanding and a better explanation of Model Persistence
"""

from sklearn.tree import DecisionTreeClassifier
#joblib to save our pre-trained model
from sklearn.externals import joblib 
import pandas as pd

musicData = pd.read_csv('music.csv')
X = musicData.drop(columns=['genre'])