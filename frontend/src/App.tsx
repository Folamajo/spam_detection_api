import axios from "axios"
import { useState } from "react"



function App() {
   const [inputValue, setInputValue] = useState<string>("")
   const [displayMessage, setDisplayMessage] = useState<string>("")

   const handleChange = (event:React.ChangeEvent<HTMLInputElement>) => {
      setInputValue(event.target.value)
   }

   const handleSubmit = async () =>{
      console.log("Submitting:", inputValue)
      setDisplayMessage(inputValue)
      setInputValue("")
      
      

      const response = await axios({
         method: "POST",
         url: "http://127.0.0.1:8000/",
         data: {
            "message" : inputValue
         }
      });
      console.log(response)
      
   }
   return (
      <>
         <input 
            type="text"
            value = {inputValue}
            onChange= {handleChange}
            placeholder="Enter message..."
         />
         <button
            onClick={handleSubmit}>
            Check
         </button>

         
         {
            displayMessage && (
               <h3>Your message: {displayMessage} is </h3>
            )
         }
         
      </>
   )
}

export default App
