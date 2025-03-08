from crewai.project import CrewBase, agent, task,crew
from crewai import LLM, Agent, Task, Process, Crew
import os
api_key = os.getenv('GEMINI_API_KEY')
@CrewBase
class BlogLayoutCrew:
    """ Crew Base Class"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    llmm = LLM(
        model="gemini/gemini-1.5-flash",
        temperature=0.7,
        # vertex_credentials=vertex_credentials_json
    )
    # print(agents_config, tasks_config)
    @agent
    def blog_layout_writer(self) ->Agent:
        """Blog Layout Writer Agent"""
        return Agent(
            config=self.agents_config['blog_layout_writer'],
             llm=self.llmm,
        )


    @agent
    def blog_layout_verifier(self) ->Agent:
        """ Blog Verifier Agent"""
        return Agent(
            config=self.agents_config['blog_layout_verifier'],
        )
    @task
    def write_blog_layout(self) -> Task:
        """Write Blog Layout Task"""
        return Task(
            config=self.tasks_config['write_blog_layout'],   
        ) 
    @task
    def verify_blog_layout(self) -> Task:
        """ Blog Verifier Tasks"""
        return Task(
            config=self.tasks_config['verify_blog_layout'],   
        ) 
  
    @crew
    def crew(self) -> Crew:
        """Creates the  Crew for the Blog Layout Agent/Task"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )