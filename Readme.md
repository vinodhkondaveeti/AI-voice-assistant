


<div align="center">
  <h1>🎤 AI Voice Assistant</h1>
  <p><strong>A Python-based intelligent voice assistant with Gemini AI integration</strong></p>
  
  <img src="./assets/demo.gif" width="60%" alt="AI Voice Assistant Demo">
  
  <p>
    <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" alt="Python">
    <img src="https://img.shields.io/badge/AI-Gemini_1.5-FF6F00?logo=google-ai" alt="Gemini AI">
    <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  </p>
</div>
<br><br>

## 📌 Project Overview
This AI voice assistant combines speech recognition, natural language processing, and task automation to:
- Process both voice and text inputs
- Provide intelligent responses using Google's Gemini AI
- Perform practical tasks (weather, math, education)
- Demonstrate core AI/ML concepts in Python


<br><br>
## 🛠️ Tech Stack
<table>
  <tr>
    <th>Component</th>
    <th>Technologies</th>
  </tr>
  <tr>
    <td><strong>Core</strong></td>
    <td>Python 3.10+</td>
  </tr>
  <tr>
    <td><strong>Speech Processing</strong></td>
    <td>speech_recognition, pyttsx3</td>
  </tr>
  <tr>
    <td><strong>AI Engine</strong></td>
    <td>Google Gemini 1.5 Flash</td>
  </tr>
  <tr>
    <td><strong>APIs</strong></td>
    <td>OpenWeatherMap, Khan Academy</td>
  </tr>
  <tr>
    <td><strong>Math Engine</strong></td>
    <td>SymPy</td>
  </tr>
</table>
<br><br>


## 🚀 Quick Start
```bash
# Clone repository
git clone https://github.com/vinodhkondaveeti/AI-voice-assistant
AI-voice-assistant

# Install dependencies
pip install -r requirements.txt

# Configure API keys
GEMINI_API_KEY = AIzaSyDhiBzat_mPxk8ROkl28JESS_-SAHwhktc
OWM_API_KEY= Enter your OWM_API_KEY (for responding the weather report)

# Run the assistant
python main.py
 ```


<br><br>
## 💡 Key Features
<details> <summary><b>🔊 Voice Interaction</b></summary> <br> Uses speech_recognition library to convert speech to text and pyttsx3 for text-to-speech responses. </details><details> <summary><b>🌦️ Weather Forecasts</b></summary> <br> ```python def get_weather(city_name): url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}" response = requests.get(url) # Returns formatted weather data ``` </details><details> <summary><b>➗ Math Solver</b></summary> <br> ```python def solve_math(expression): expr = sp.sympify(expression) result = sp.simplify(expr) # Returns step-by-step solution ``` </details>


<br><br>
### 📋 Usage Examples  
| Command       | Action |  
|-----------------|------------|  
| **weather in India**        | Get India's weather |  
| **solve 2x + 5 = 15**      | Solve algebraic equation |  
| **resources programming**          | Open programming learning resources |  
| **stop**        | Change input mode | 


<br><br>
### 🌟 Future Enhancements
- Add multilingual support
- Implement wake-word detection
- Develop GUI interface
- Add calendar/reminder functionality


<br><br>

<div align="center"> <p>⭐ Star this Repository if you like this project!</p> </div> 
