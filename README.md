


## Steps I followed in this Machine Learning App Developement
##### The steps below are `generally` the correct steps to follow for any ML model developement.
### 1. Import the Data

- This often invloves the data that the model will use to learn, and therefore grow intelligence from
- This normally in the form of CSV, Data pulled from an API
  
### 2. Clean the Data
- Involves tasks e.g Removing duplicates, filling blanks, `to ensure that our model only learns correct patterns for the best results` .Can at times involve encoding from text to numerical values.
- 
### 3. Split the data into Train/Testing Sets
- Assign about 80% for Testing it and test its performance with the rest
  
### 4. Create a Model
- Involves `Selecting an Algorithm` to Analyse the imported Data
- This normally depends on the project you're doing.Examples include
    - Decision Trees
    - NN
A good Example is the `scikit-learn` library that has a lot of ML Algorithms.

### 5. Train the Model

- We feed it with thee training data and ask it to learn the patterns in it.

### 6. Make predictions
- We feed it with a test data and ask it, from whatever it learnt, is this a Cat/Dog, Bottle/Tin, Boy/Girl, Male/Female, Mask/No Mask e.t.c
- Predictions are however never accurate but are graded in measure of confidence.The more you train it, the more it uilds confidence in it's Answer.

### 7. Evaluate and Improve the performance of the Model
- This is involves fine-tuning the parameters of our model for better accuracy or selecting another model that will produce better results.
