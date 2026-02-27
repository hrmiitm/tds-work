# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "openai-agents>=0.10.2",
# ]
# ///
from agents import Agent, Runner # Class
import os
os.environ["OPENAI_AGENTS_DISABLE_TRACING"] = "1"


agent = Agent(
    name='Math Tutor',
    model='gpt-4.1-nano',
    instructions='You provide help with maths problems. You give answer along with resoning. You reply in short'
) # object of class Agent

result = Runner.run_sync(
    agent, 
    "Take the current date and time, add date, month, year and take theire square root"
)
print(result.final_output)













