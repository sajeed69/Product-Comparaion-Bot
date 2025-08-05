
from crewai import Crew
from agents.info_extractor import info_extractor
from agents.comparator import comparator
from agents.recommender import recommender
from tasks.task_creator import create_tasks
from dotenv import load_dotenv

load_dotenv()

def run_comparison(product1, product2):
    tasks = create_tasks(info_extractor, comparator, recommender, product1, product2)

    crew = Crew(
        agents=[info_extractor, comparator, recommender],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()
    print("\nFinal Recommendation:\n", result)

if __name__ == "__main__":
    p1 = input("Enter first product: ")
    p2 = input("Enter second product: ")
    run_comparison(p1, p2)
