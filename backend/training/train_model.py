# Step 1: Load Data from CSV
# Step 2: Vectorize text
# Step 3: Train Model
# Step 4: Save Model and Vectorizer

#Save models as models/spam_classifier.pkl
# Save vectorizer as models/vectorizer.pkl
#use joblib for both 
#TRAIN
#1- Import libraries
#2-  Load and prepare the dataset
#3- split into training and testing training_data
#4- convert text into numeric representation
#5- train the naive bayes model 
#6- evaluate the model 
#7- Save the model

#TESTING TRAINING PROCESS
   #When we run train_model.py:
      #Make sure no errors happen
      # Check spam_classifier.pkl and vectorizer.pkl actually appear in your models/folder
      # Check the file sizes they should not be empty
      # print a sample prediction from the trained model.

#1- Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer #Converts text into numerical TF-IDF features
from sklearn.model_selection import train_test_split #Splits the dataset
from sklearn.naive_bayes import MultinomialNB #Naive Bayes classifier
from sklearn.preprocessing import LabelEncoder #Helps to convert labels to numberic values
from sklearn.metrics import accuracy_score, classification_report # type: ignore
import pickle

#2- Loading the dataset

label_encoder = LabelEncoder()
path_to_file ="/Users/fola/Documents/Projects/spam_detection_api/training/spam_data.csv"
training_data = pd.read_csv(path_to_file)
training_data["Label"] = label_encoder.fit_transform(training_data["Label"])
# print(training_data)

#3- Split dataset
X_train, X_test, y_train, y_test = train_test_split(training_data["Text"], training_data["Label"], test_size=0.2, random_state=42)

#4-Convert Text into numberical representation
#Vectorise text using TF-IDF
vectorizer = TfidfVectorizer(lowercase=True, stop_words='english', ngram_range =(1,2))
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


print("training data shape:", X_train_tfidf.shape)
print("testing data shape:", X_test_tfidf.shape)

#5 - TRAINING THE NAIVE BAYESMODEL 
model = MultinomialNB()
model.fit(X_train_tfidf, y_train )

#Predictions
model_predictions = model.predict(X_test_tfidf)

#6-EVALUATE MODEL PERFORMANCE 
accuracy = accuracy_score(model_predictions, y_test)
print(accuracy)
print(classification_report(y_test, model_predictions)) #0.75 accurately prdicted 75% of data

with open("../models/spam_classifier.pkl", "wb") as saved_model:
   pickle.dump(model, saved_model)

with open("../models/vectorizer.pkl", "wb") as saved_vectorizer:
   pickle.dump(vectorizer, saved_vectorizer)
#7- IMPROVE SCORE


# Result after testing
# training data shape: (13, 54)
# testing data shape: (4, 54)


# transformed_data = vectorizer.fit_transform(training_data["Text"])
# print(transformed_data)
# #Prind the shape this gives us rows and columns
# print(transformed_data.shape)
# print("Tranformed first text message", transformed_data.toarray()[0])


#3- Split dataset into 80% training and 20% testing

# print(training_data.shape)
# print(training_data.dtypes)


