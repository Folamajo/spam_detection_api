#Step 1: Create FastAPI app
# Step 2: Load Model and Vectoriser on Startup from models/spam_classifier.pkl, models/vectorizer.pkl
# Step 3: Define /predict Endpoint
# Step 4: Handle Input Validation


#Load the model from models/spam_classifier.pkl, models/vectorizer.pkl
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