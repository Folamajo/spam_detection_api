This is a Spam Detection AI Application. 
A Naive bayes model was trained to detect text that is sent 
by user to FAST API application. A response is sent back to the user letting them know if it is spam or not 

Users should send POST request to /predict with JSON like:
   { "text": "You have won a free prize!" }

A successful response will be returned like :
   {"label": "Spam"}

An unsuccessful response will be:
   {"error": "Text field is required"}

To run the API locally use command :
   uvicorn app.main:app --reload


