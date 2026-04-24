from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

@CrewBase
class ResearchAndBlogCrew():
    
    # Path to your YAML files
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    # ============= Agents ====================
    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["report_generator"],
            verbose=True, # Shows what the researcher is doing
            allow_delegation=False
        )
        
    @agent
    def blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["blog_writer"],
            verbose=True, # Shows the writing process
            allow_delegation=False
        )
        
    # ============== Tasks ===========================
    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config["report_task"]
        )
        
    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["blog_writing_task"],
            output_file="blogs/ai_engineering_career_path.md" # Make sure 'blogs' folder exists!
        )
        
    # ================ Crew ===============================
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, 
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )