from crewai.flow import Flow ,start,listen
from pydantic import BaseModel
from multicrew.crews.blog_layout_crew.BlogLayoutCrew import BlogLayoutCrew
from multicrew.crews.blog_writer_crew.BlogWriterCrew import BlogWriterCrew

class BlogState(BaseModel):
    blogtopic : str = ''
    bloglayout : str = ''
    blogpost : str = ''

class Blog(Flow[BlogState]):
    """Blog: Flow Start"""
    @start()
    def blogtopic(self):
        topic = input("Enter the blog topic: ")
        self.blogtopic = topic
    
    @listen(blogtopic)
    def generate_bloglayout(self) -> str:
        result = BlogLayoutCrew().crew().kickoff(inputs={'topic': self.blogtopic})
        self.bloglayout = result.raw
        return result.raw
    
    @listen(generate_bloglayout)
    def generate_blogpost(self) -> str:
        self.blogpost = BlogWriterCrew().crew().kickoff(inputs={'layout': self.bloglayout})
        return self.blogpost

def kickoff():
    blog = Blog()
    blog.kickoff()

def main():
    print("Hello from multicrew!")
    kickoff()
