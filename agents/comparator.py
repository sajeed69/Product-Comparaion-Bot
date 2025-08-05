
from crewai import Agent

comparator = Agent(
    role="Comparator",
    goal="Compare two products based on extracted information",
    backstory="An experienced analyst who can critically evaluate features and reviews to compare products.",
    allow_delegation=False
)
