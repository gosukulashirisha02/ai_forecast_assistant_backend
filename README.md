🌤 AI Weather Agent
An AI-powered Weather Assistant built using Streamlit, FastAPI, LangChain, Groq LLM, and OpenWeatherMap API. Users can ask weather-related questions in natural language, and the AI agent retrieves real-time weather data to generate intelligent responses.
Features:
Real-time weather information
AI-powered natural language responses
FastAPI backend
Streamlit frontend
LangChain Agent integration
Groq Llama 3.3 70B model
OpenWeatherMap API support
Tech Stack:
Frontend
Streamlit
Requests
Backend
FastAPI
LangChain
LangChain-Groq
OpenWeatherMap API
AI Model
Llama-3.3-70b-versatile (Groq)
Project Structure:
weather-agent/
│
├── backend/
│   ├── main.py
│   ├── .env
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── .streamlit/
│       └── secrets.toml
│
└── README.md
Get Weather
POST /get_weather

Parameters:

Parameter	Type	Description
city	string	City name
question	string	User weather query

Example:

POST /get_weather?city=Hyderabad&question=What is the weather today?
How It Works
User enters a city name.
User asks a weather-related question.
Streamlit sends the request to FastAPI.
LangChain Agent invokes the weather tool.
OpenWeatherMap API fetches live weather data.
Groq LLM generates a natural language response.
Response is displayed in Streamlit UI.
Demo:

Example Query:

City: Hyderabad
Question: Will it be hot today?

Example Response:

The current temperature in Hyderabad is 32°C with clear skies. It is expected to remain warm throughout the day.
Requirements:
fastapi
uvicorn
streamlit
requests
python-dotenv
langchain
langchain-groq
openweathermap-api