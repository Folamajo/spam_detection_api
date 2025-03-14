import pickle
from fastapi import FastAPI

#Step 1: Create FastAPI app
# Step 2: Load Model and Vectoriser on Startup from models/spam_classifier.pkl, models/vectorizer.pkl
# Step 3: Define /predict Endpoint
# Step 4: Handle Input Validation

#Sample

sample_prediction = [
   "Please verify your Bank of America account information to avoid a hold on your account. Click here to confirm ",
   "You’ve been overcharged for your 2021 taxes. Get your IRS tax refund here",
   "Get delivery updates on your USPS order",
   "Thank you for paying last month’s bill. We’re rewarding our very best customers with a gift for their loyalty. Click here"
]
#Load the model from models/spam_classifier.pkl, models/vectorizer.pkl
with open("../models/spam_classifier.pkl", "rb") as saved_model:
   loaded_model = pickle.load(saved_model)

with open("../models/vectorizer.pkl", "rb") as saved_vectorizer:
   loaded_vectorizer = pickle.load(saved_vectorizer)

transformed_list = loaded_vectorizer.transform(sample_prediction)
model_prediction = loaded_model.predict(transformed_list)

print(model_prediction)


app = FastAPI()

@app.post("/")
async def root():
   return {"message: Hello World"}
# Log success or failure
# Store in global variables so /predict can use them

#ERROR HANDLING
# Ensure text is present in request
# Ensure test is a non-empty string
#Return error if validation fails 

# PLAN LOGGING AND DEBUGGING
#What should be logged at startup 
   # - Model and vectorizer successfully loaded
   # - Model and/ or  Vectorizer failed to load
#REQUEST LOGS
   #- Log each request /predict 
   # # Log what text was received and what was sent

#ERROR LOGS
   # Log validation error ("missing input", "inappropriate input")
   #Log unexpected errors (e.g. Model failed to predict)

   # use logging MODULE

