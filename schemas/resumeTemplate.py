from pydantic import BaseModel

class Education(BaseModel):
    school: str
    major: str
    degree: str
    start_date: str
    end_date: str

class Experience(BaseModel):
    company: str
    position: str
    start_date: str
    end_date: str
    description: str
    
class Project(BaseModel):
    name: str
    description: str
    technologies: list[str]
    start_date: str
    end_date: str
    
class Resume(BaseModel):
    name: str
    education: list[Education]
    experience: list[Experience]
    projects: list[Project]