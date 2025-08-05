from crewai import Agent

info_extractor = Agent(
    role="Info Extractor",
    goal="Extract features and reviews of the given products",
    backstory="Expert in gathering product info from the internet using internal logic.",
    allow_delegation=False,
)
