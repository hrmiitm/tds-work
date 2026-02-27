# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "openai-agents>=0.10.2",
# ]
# ///
from agents import Agent, Runner, function_tool # Class
from pydantic import BaseModel, Field
from datetime import datetime

import os
os.environ["OPENAI_AGENTS_DISABLE_TRACING"] = "1"


class TimeResponse(BaseModel):
    date: int = Field(..., description="The date of the current date and time i.e. 05 or 10")
    month: int = Field(..., description="The month of the current date and time i.e. 01 or 02")
    year: int = Field(..., description="The year of the current date and time i.e. 2026")
    time: str = Field(..., description="The time of the current date and time i.e. 10:30:45")

    date_sum: int = Field(..., description="The sum of date, month and year")
    sqrt_date_sum: float = Field(..., description="The square root of the sum of date, month and year")
    reasoning: str = Field(..., description="The reasoning for the calcluation in details")



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
    instructions='You provide help with maths problems. You give answer along with resoning. You reply in short',
    output_type=TimeResponse
) # object of class Agent

result = Runner.run_sync(
    agent, 
    "Take the current date and time, add date, month, year and take theire square root"
)

objectOfClass_TimeReponse = result.final_output_as(TimeResponse)
# print(objectOfClass_TimeReponse)

print("Date: ", objectOfClass_TimeReponse.date, type(objectOfClass_TimeReponse.date))
print("Month: ", objectOfClass_TimeReponse.month)
print("Year: ", objectOfClass_TimeReponse.year)
print("Time: ", objectOfClass_TimeReponse.time)
print("Date Sum: ", objectOfClass_TimeReponse.date_sum)
print("Square Root of Date Sum: ", objectOfClass_TimeReponse.sqrt_date_sum)
print("Reasoning: ", objectOfClass_TimeReponse.reasoning)
















