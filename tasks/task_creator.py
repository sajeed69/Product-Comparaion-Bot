from crewai import Task

def create_tasks(info_extractor, comparator, recommender, product1, product2):
    # Simulate fake search here directly
    info_summary = (
        f"Product 1 ({product1}): Placeholder specs and reviews.\n"
        f"Product 2 ({product2}): Placeholder specs and reviews."
    )

    task1 = Task(
        description=f"Gather and summarize product info:\n{info_summary}",
        expected_output="Summarized details of both products.",
        agent=info_extractor,
    )

    task2 = Task(
        description="Compare the two products based on the extracted info.",
        expected_output="Comparison of product features, pros, and cons.",
        agent=comparator,
        context=[task1]
    )

    task3 = Task(
        description="Based on the comparison, recommend the better product.",
        expected_output="Clear recommendation with justification.",
        agent=recommender,
        context=[task2]
    )

    return [task1, task2, task3]
