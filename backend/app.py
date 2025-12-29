from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
print("🔌 [3/4] Importing Pipeline...")      # DEBUG PRINT
from pipeline import agri_translate_pipeline

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Req(BaseModel):
    text: str

@app.post("/translate")
def translate(req: Req):
    print(f"📨 [INCOMING] Received text: {req.text}")  # DEBUG PRINT
    
    try:
        result = agri_translate_pipeline(req.text)
        print(f"📤 [OUTGOING] Result: {result}")      # DEBUG PRINT
        return {"hindi": result}
    except Exception as e:
        print(f"❌ ERROR inside pipeline: {e}")       # DEBUG PRINT
        return {"hindi": "Server Error during translation"}

print("🚀 [4/4] Server Startup Complete. Waiting for requests...") # DEBUG PRINT