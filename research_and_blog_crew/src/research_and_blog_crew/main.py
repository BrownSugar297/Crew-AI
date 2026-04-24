from research_and_blog_crew.crew import ResearchAndBlogCrew





def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI Engineering Career Path and Opportunities in Bangladesh 2026',
    }

    try:
        ResearchAndBlogCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


