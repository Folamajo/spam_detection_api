# Step 1: Load Data from CSV
# Step 2: Vectorize text
# Step 3: Train Model
# Step 4: Save Model and Vectorizer

#Save models as models/spam_classifier.pkl
# Save vectorizer as models/vectorizer.pkl
#use joblib for both 

#TESTING TRAINING PROCESS
   #When we run train_model.py:
      #Make sure no errors happen
      # Check spam_classifier.pkl and vectorizer.pkl actually appear in your models/folder
      # Check the file sizes they should not be empty
      # print a sample prediction from the trained model.


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

#Loading the dataset
path_to_file ="/Users/fola/Documents/Projects/spam_detection_api/training/spam_data.csv"
training_data = pd.read_csv(path_to_file)

# print(training_data)

vectorizer = TfidfVectorizer(lowercase=True, stop_words='english')
transformed_data = vectorizer.fit_transform(training_data["Text"])
print(transformed_data)
#Prind the cshape this gives us rows and columns
print(transformed_data.shape)
print("Tranformed first text message", transformed_data.toarray()[0])

# print(training_data.shape)
# print(training_data.dtypes)
