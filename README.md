## Detailed Explanation about this Mini Project and More about Machine Learning for General Predictive Analytics
The custome made music.csv file has `3 columns Age, gender(1; Male, 0; Female)`
I've mentioned a bit of `Model Persistence` at the end, so just scroll through.

### Steps I followed in this Machine Learning App Developement
##### The steps below are `generally` the correct steps to follow for any ML model developement.
#### 1. Import the Data

- This often invloves the data that the model will use to learn, and therefore grow intelligence from
- This normally in the form of CSV, Data pulled from an API
  
#### 2. Clean the Data
- Involves tasks e.g Removing duplicates, filling blanks, `to ensure that our model only learns correct patterns for the best results` .Can at times involve encoding from text to numerical values.
- 
#### 3. Split the data into Train/Testing Sets
- Assign about 80% for Testing it and test its performance with the rest
  
#### 4. Create a Model
- Involves `Selecting an Algorithm` to Analyse the imported Data
- This normally depends on the project you're doing.Examples include
    - Decision Trees
    - NN <br>
- A good Example is the `scikit-learn` library that has a lot of ML Algorithms.

#### 5. Train the Model

- We feed it with thee training data and ask it to learn the patterns in it.

#### 6. Make predictions
- We feed it with a test data and ask it, from whatever it learnt, is this a Cat/Dog, Bottle/Tin, Boy/Girl, Male/Female, Mask/No Mask e.t.c
- Predictions are however never accurate but are graded in measure of confidence.The more you train it, the more it uilds confidence in it's Answer.

#### 7. Evaluate and Improve the performance of the Model
- This is involves fine-tuning the parameters of our model for better accuracy or selecting another model that will produce better results.

### Model Persistence
-This involves creating a model, training it and fine-tuning it and finally saving it as an importable `.joblib` file.
This saves us the burden of re-training the model again and again when a new user needs tto perform predictions and do evaluations.
Again this saves us the burden of computational complexity and expenses.

So we'll use the `joblib` object (Which has many methods for saving and loading models) `from sklearn.externals` library(For python 2.x upto) and `import jolib` for python 3.X
