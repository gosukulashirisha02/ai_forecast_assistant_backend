from fastapi import FastAPI

from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain.tools import tool 
import requests
from dotenv import load_dotenv
load_dotenv()

import os





app=FastAPI()
OPENWEATHER_API_KEY=os.getenv("OPENWEATHER_API_KEY")

llm=ChatGroq(
    model="llama-3.3-70b-versatile",
   api_key=os.getenv("GROQ_API_KEY")
)

@tool
def get_temp_details(city:str):
    """
    this is to get city details
    """
    res=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}")
    data=res.json()
    return data

agent=create_agent(
    model="llm",
    tools=[get_temp_details]
)
@app.post("/get_weather")
def incomig_weather_params(
    city:str=Query(...),
    question:str=Query(...)
):
    
    result=agent.invoke({
        "message":[{"role":"user","content":f"city:{city} question:{question}"}]
    })
    return result