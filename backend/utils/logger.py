import json
import os
from datetime import datetime

LOG_FILE = "logs/history.json"

def log_interaction(
    filename: str,
    question: str,
    answer: str, 
    sources: list
):
    """
    Log user Q&A interaction in JSON format
    """
    os.makedirs("logs", exist_ok = True)

    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "file": filename,
        "question": question,
        "answer": answer,
        "sources": sources
    }

    data = []

    # load existing json
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    
    # append new entry
    data.append(log_entry)
    # save back
    with open(LOG_FILE,'w', encoding="utf-8") as f:
        json.dump(data, f, indent= 4)
