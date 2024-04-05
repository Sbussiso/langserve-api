from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from langchain.memory import ChatMessageHistory
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Initialize ChatGPT model with your OpenAI API key
model = ChatOpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))


# Define a prompt template for the user input
response = ChatPromptTemplate.from_template("you are a helpful AI assistant. PROMPT: {prompt}")


# Create an API route
@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Add the route for the one-shot chat API
add_routes(app, response | model, path="/gpt-one-shot")

#TODO: 
#add_routes(something | model, path="/gpt-mem-bare")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
