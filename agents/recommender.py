
from crewai import Agent

recommender = Agent(
    role="Recommender",
    goal="Recommend the best product among two based on the comparison",
    backstory="A product expert who can identify the best choice for users based on insights.",
    allow_delegation=False
)
