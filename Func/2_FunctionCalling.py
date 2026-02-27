# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "openai-agents>=0.10.2",
# ]
# ///
from agents import Agent, Runner, function_tool # Class
from datetime import datetime

import os
os.environ["OPENAI_AGENTS_DISABLE_TRACING"] = "1"

@function_tool
def get_current_date():
    """
    Returns the current date and time

    Args:
        None

    Returns:
        str: Current date and time in the format "YYYY-MM-DD HH:MM:SS"
    """
    print("-----------Hey your agent has called me------------")
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


agent = Agent(
    name='Math Tutor',
    model='gpt-4.1-nano',
    tools=[get_current_date],
    instructions='You provide help with maths problems. You give answer along with resoning. You reply in short'
) # object of class Agent

result = Runner.run_sync(
    agent, 
    "Take the current date and time, add date, month, year and take theire square root"
)
print(result.final_output)













