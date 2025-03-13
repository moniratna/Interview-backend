import json
import os
from fastapi import HTTPException
from typing import List


def read_profit_and_loss_data(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data = json.load(file)
        return data

def read_balance_sheet_data(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data = json.load(file)
        return data