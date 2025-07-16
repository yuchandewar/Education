import requests
import json

# Configuration
URL = "http://192.168.56.1:1234/v1/chat/completions"  # Default LM Studio server endpoint
MODEL_NAME = "deepseek-r1-distill-qwen-1.5b"  # Replace with your exact DeepSeek model name
TEMPERATURE = 0.7  # Controls randomness (0.0 to 1.0)

def send_message(message):
    """Send a message to the DeepSeek model and return its response."""
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": message}],
        "temperature": TEMPERATURE
        # No max_tokens specified, allowing the model to use its default maximum
    }
    
    try:
        response = requests.post(URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to the local server. Ensure LM Studio is running."
    except requests.exceptions.HTTPError as e:
        return f"Error: HTTP {e.response.status_code} - {e.response.text}"
    except KeyError:
        return "Error: Unexpected response format from the server."

def chat():
    """Main chat loop."""
    print("Starting chat with DeepSeek (no token limit). Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        if not user_input.strip():
            print("Please enter a message.")
            continue
        
        response = send_message(user_input)
        print(f"DeepSeek: {response}")

if __name__ == "__main__":
    # Verify Python and requests are installed
    try:
        requests.get("http://192.168.56.1:1234")  # Quick check if server is up
        print("Connected to local server. Starting chat...")
    except requests.exceptions.ConnectionError:
        print("Warning: Could not connect to http://192.168.56.1:1234. Ensure LM Studio is running with the server enabled.")
    
    chat()

    
# Run the script
# lms   # Check if the server is running

# lms serve  # Start the server

# lms server start  # Start the server

# ipconfig  # Find the IP address of the host machine

# python todo.py  # Run the script

# stop - Stops the local server