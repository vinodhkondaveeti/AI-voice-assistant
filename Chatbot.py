import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import requests
import re
import webbrowser
import sympy as sp

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Configure the Google Generative AI API
genai.configure(api_key="AIzaSyDhiBzat_mPxk8ROkl28JESS_-SAHwhktc")

# Set your OpenWeatherMap API key here
OPENWEATHERMAP_API_KEY = 'your_openweathermap_api_key_here'

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
)

# Initialize the conversation history
conversation_history = [
    {
        "role": "user",
        "parts": ["hello"],
    },
    {
        "role": "model",
        "parts": ["Hello! What can I do for you today?"],
    },
]

chat_session = model.start_chat(history=conversation_history)

recognizer = sr.Recognizer()

def recognize_speech_from_mic():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening... (say 'stop' to change mode)")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print("You said: " + text)

            if text.lower() == "stop":
                return "stop"

            return text

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    return None

def clean_text(text):
    # Remove unnecessary symbols and keep only meaningful content
    text = re.sub(r'[^\w\s,.!?]', '', text)
    return text

def get_weather(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHERMAP_API_KEY}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"The weather in {city_name} is currently {weather_description} with a temperature of {temperature}°C."
    else:
        return "Sorry, I couldn't retrieve the weather information."

def solve_math(expression):
    try:
        steps = []
        expr = sp.sympify(expression)
        result = sp.simplify(expr)
        steps.append(f"Original expression: {expression}")
        steps.append(f"Simplified result: {result}")

        step_by_step = sp.pretty(expr, use_unicode=True)
        steps.append(f"Steps:\n{step_by_step}")

        # Print the steps in a user-friendly manner
        for step in steps:
            print(step)

        return f"The result of {expression} is {result}."
    except Exception as e:
        return f"Sorry, I couldn't solve that expression. Error: {e}"

def provide_educational_resources(topic):
    resources = {
        "math": "https://www.khanacademy.org/math",
        "science": "https://www.khanacademy.org/science",
        "history": "https://www.khanacademy.org/humanities/history",
        "programming": "https://www.khanacademy.org/computing/computer-programming",
    }
    return resources.get(topic.lower(), "Sorry, I couldn't find resources for that topic.")

def get_response(text):
    if text.lower().startswith("weather"):
        parts = text.split()
        if len(parts) >= 2:
            city = parts[1]
            weather_response = get_weather(city)
            print("bujji: " + weather_response)
            engine.say(weather_response)
            engine.runAndWait()
            return

    if text.lower().startswith("solve"):
        expression = text[6:]
        math_response = solve_math(expression)
        print("bujji: " + math_response)
        engine.say(math_response.split(':')[-1].strip())  # Only speak the final result
        engine.runAndWait()
        return

    if text.lower().startswith("resources"):
        topic = text[10:]
        resource_response = provide_educational_resources(topic)
        print("bujji: " + resource_response)
        engine.say(resource_response)
        engine.runAndWait()
        webbrowser.open(resource_response)
        return

    conversation_history.append({
        "role": "user",
        "parts": [text],
    })

    response = chat_session.send_message(text)

    # Append model response to conversation history
    clean_response = clean_text(response.text)
    conversation_history.append({
        "role": "model",
        "parts": [clean_response],
    })

    print("bujji: " + clean_response)
    engine.say(clean_response)
    engine.runAndWait()

def introduce_buji():
    intro_text = "Hello, I am your assistant. how can i help you?"
    print("bujji: " + intro_text)
    engine.say(intro_text)
    engine.runAndWait()

def main():
    introduce_buji()

    while True:
        user_input_mode = input("Do you want to speak, type, or exit? (speak/type/exit): ").strip().lower()

        if user_input_mode == "exit":
            print("bujji: Goodbye!")
            engine.say("Goodbye!")
            engine.runAndWait()
            break
        elif user_input_mode == "speak":
            while True:
                text = recognize_speech_from_mic()
                if text == "stop":
                    break
                if text:
                    get_response(text)
        elif user_input_mode == "type":
            while True:
                text = input("You: ").strip()
                if text.lower() == "stop":
                    break
                get_response(text)
        else:
            print("Invalid input. Please type 'speak' to use voice input, 'type' to use text input, or 'exit' to quit.")

if __name__ == "__main__":
    main()






