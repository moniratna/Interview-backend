from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from service import read_profit_and_loss_data
from service import read_balance_sheet_data
from config import config
from typing import List
import uvicorn
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/quickbooks/profit-and-loss")
async def read_profit_and_loss():
    file_path = config.data_file_path
    try:
        result = read_profit_and_loss_data(file_path)
        return result
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error reading JSON data")

@app.get("/quickbooks/balance-sheet")
async def read_profit_and_loss():
    file_path = config.data_balance_sheet
    try:
        result = read_balance_sheet_data(file_path)
        return result
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error reading JSON data")
 
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
