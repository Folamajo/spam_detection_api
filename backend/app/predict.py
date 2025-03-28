import pickle
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
with open("/Users/fola/Documents/Projects/spam_detection_api/backend/models/spam_classifier.pkl", "rb") as saved_model:
   loaded_model = pickle.load(saved_model)

with open("/Users/fola/Documents/Projects/spam_detection_api/backend/models/vectorizer.pkl", "rb") as saved_vectorizer:
   loaded_vectorizer = pickle.load(saved_vectorizer)

transformed_list = loaded_vectorizer.transform(sample_prediction)
model_prediction = loaded_model.predict(transformed_list)

print(model_prediction)

class Message(BaseModel):
   message: str

labels = {
   0 : "not spam",
   1 : "spam"
}
   
app = FastAPI()

origins = [
   "http://localhost:5173"
]

app.add_middleware(
   CORSMiddleware,
   allow_origins = origins,
   allow_credentials = True,
   allow_methods = ["*"],
   allow_headers = ["*"],
)
@app.post("/")
async def spam_checker(message: Message):

   
   #Use vectorizer to transform the input
   transformed_message = loaded_vectorizer.transform([message.message])
   predict_spam = loaded_model.predict(transformed_message)
   #Pass the transformed input to the model for prediction
   #Return the prediction

   return {"status: ", labels[predict_spam[0]]}




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

