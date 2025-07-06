import requests
import pdfplumber
from PIL import Image
import pytesseract
import pyttsx3
import sys

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# Function to query LM Studio's local API
def get_lmstudio_response(prompt):
    url = "http://localhost:1234/v1/completions"  # LM Studio default endpoint
    headers = {"Content-Type": "application/json"}
    data = {
        "prompt": prompt,
        "max_tokens": 500,
        "temperature": 0.7,
        
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["text"].strip()
    except Exception as e:
        return f"Sorry, I hit a snag with the API: {e}"

# Function to speak and print a response
def say_and_print(text):
    print(f"Me: {text}")
    engine.say(text)
    engine.runAndWait()

# Summarize PDF
def summarize_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    prompt = f"Hey, summarize this like we’re chatting:\n\n{text}"
    return get_lmstudio_response(prompt)

# Process image
def process_image(file_path):
    img = Image.open(file_path)
    text = pytesseract.image_to_string(img)
    prompt = f"Yo, tell me about this image casually. Here’s the text I got: {text}"
    return get_lmstudio_response(prompt)

# Main chat loop
def chat_agent():
    say_and_print("Hey there! I’m your talking AI buddy running on LM Studio. Type 'exit' to quit, or let’s chat!")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            say_and_print("Catch you later!")
            break
        elif "summarize pdf" in user_input:
            file_path = input("Drop the PDF file path here: ")
            try:
                summary = summarize_pdf(file_path)
                say_and_print(f"Alright, here’s the rundown: {summary}")
            except Exception as e:
                say_and_print(f"Whoops, something’s up with the PDF: {e}")
        elif "image" in user_input:
            file_path = input("Gimme the image file path: ")
            try:
                result = process_image(file_path)
                say_and_print(f"Here’s what I think about that image: {result}")
            except Exception as e:
                say_and_print(f"Hmm, couldn’t figure out that image: {e}")
        else:
            response = get_lmstudio_response(user_input)
            say_and_print(response)

if __name__ == "__main__":
    chat_agent()