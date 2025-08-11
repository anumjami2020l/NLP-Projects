from phi.agent import Agent
# from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    # model=Groq(id="llama-3.3-70b-versatile")
    model=OpenAIChat(id="gpt-4o")
)

agent.print_response("Share a 2 sentence love story between dosa and samosa")

