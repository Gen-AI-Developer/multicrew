from crewai.project import CrewBase, agent, task,crew
from crewai import LLM, Agent, Task, Process, Crew

@CrewBase
class BlogWriterCrew:
    """ Crew Base Class"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def blog_writer(self) ->Agent:
        return Agent(
            config=self.agents_config['blog_writer'],
        )

    @task
    def write_blog(self) -> Task:
        return Task(
            config=self.tasks_config['write_blog'],   
        ) 
    @crew
    def crew(self) -> Crew:
        """Creates the  Crew for the Blog writer Agent/Task"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )