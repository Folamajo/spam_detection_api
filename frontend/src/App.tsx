import axios, { AxiosError } from "axios"
import { useState } from "react"



function App() {
   const [inputValue, setInputValue] = useState<string>("")
   const [displayMessage, setDisplayMessage] = useState<string>("")
   const [result, setResult] = useState<string>("")
   const [errorMessage, setErrorMessage] = useState<string>("")

   const handleChange = (event:React.ChangeEvent<HTMLTextAreaElement>) => {
      setDisplayMessage("")
      setErrorMessage("")
      setInputValue(event.target.value)
   }

   const handleSubmit = async () =>{
      setDisplayMessage("")
      if (inputValue.trim() == ""){
         setErrorMessage("Please enter text before checking")
         return;
      }
      
      setInputValue("")
      setErrorMessage("")
      try{
         const response = await axios.post( "http://127.0.0.1:8000/", {
            message : inputValue
            
         })
            setDisplayMessage(inputValue)
            setResult(response.data[0])
            console.log(response)
         
      }catch(error){
         if(axios.isAxiosError(error)){
            if(error.code === "ERR_NETWORK"){
               setErrorMessage("Unable to connect to the server.")
            }

            if(error.response?.status === 400){
               setErrorMessage("You entered an Invalid input.")
            }
            else if (error.response?.status === 404){
               setErrorMessage("Requested resource was not found.")
            }
            else if (error.response?.status === 500){
               setErrorMessage("Something went wrong on our end. Please try again later.")
            }
            else {
               setErrorMessage("Something went wrong. Please try again later.")
            }

            
         }else{
            console.error(error)
         }
      }
      
      // console.log(response.data[1])
      
   }
   return (
      <>
      <div id ="container">
         <textarea 
            
            value = {inputValue}
            onChange= {handleChange}
            placeholder="Enter message..."
            id ="input_box"
         />

         {
            errorMessage && (
               <p>{errorMessage}</p>
            )
         }
         <button
            onClick={handleSubmit}>
            <strong>Check</strong>
         </button>

         
         {
            displayMessage && (
               <div id="user_display">
                  <p className = "user_display"><em>"{displayMessage}"</em></p>
                  {result == "spam" && <p className = "spam_result" >This is most likely <strong>spam</strong>.</p> }
                  {result == "not spam" && <p className = "spam_result" >This is most likely <strong>not spam</strong>.</p> }
               </div>
            )
         }
         
      </div>
      </>
   )
}

export default App
