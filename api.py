from fastapi import FastAPI
app = FastAPI()
@app.post("/process")
def process_message(message: str):
  return{
    "message" : message.upper()
    
  }
