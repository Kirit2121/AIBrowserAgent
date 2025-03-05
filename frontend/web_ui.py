import gradio as gr
from app.models.ai_model import get_ai_response
from app.automation.browser import perform_browser_actions

def process_instruction(instruction):
    ai_response = get_ai_response(instruction)
    perform_browser_actions(ai_response)
    return f"Executed: {instruction}"

iface = gr.Interface(fn=process_instruction, inputs="text", outputs="text", title="KT AI Browser Agent")
iface.launch()
