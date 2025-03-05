import requests

OLLAMA_URL = "http://192.168.1.7:11434/api/generate"

def get_ai_response(prompt):
    """Sends a request to Ollama's HTTP API and returns the AI response."""
    data = {
        "model": "qwen2.5-coder:latest",  # Ensure the correct model is being used
        "prompt": f"Convert this instruction into structured steps: {prompt}",
        "stream": False  # Set to True if you want streaming responses
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=data, timeout=30)  # Timeout prevents hanging requests
        response.raise_for_status()  # Raise an error for HTTP issues
        
        # Extract AI-generated response
        return response.json().get("response", "⚠️ No response from AI")
    
    except requests.exceptions.RequestException as e:
        return f"⚠️ Error connecting to Ollama: {e}"


