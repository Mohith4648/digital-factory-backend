from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

# Temporary storage to show we are receiving data
logs_db = []

@app.get("/")
def home():
    return {"message": "Digital Factory Brain is Online"}

@app.post("/log")
def receive_log(data: dict):
    # Add timestamp and save the log
    data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logs_db.append(data)
    print(f"Received log: {data}")
    return {"status": "success", "received": data}

@app.get("/dashboard-data")
def get_logs():
    return logs_db[-10:] # Return last 10 logs for the frontend