from fastapi import FastAPI
from pydantic import BaseModel
from app.models.ai_model import get_ai_response
from app.automation.browser import perform_browser_actions

app = FastAPI()

class Instruction(BaseModel):
    text: str

@app.post("/execute")
def execute_instruction(instruction: Instruction):
    ai_response = get_ai_response(instruction.text)
    perform_browser_actions(ai_response)
    return {"message": "Task executed successfully"}
