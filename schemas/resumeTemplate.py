from pydantic import BaseModel, Field


class Education(BaseModel):

    school: str = ""

    major: str = ""

    degree: str = ""



class Experience(BaseModel):

    company: str = ""

    role: str = ""

    description: str = ""



class Project(BaseModel):

    name: str = ""

    description: str = ""

    technologies: list[str] = []



class Resume(BaseModel):

    name: str = ""

    education: list[Education] = []

    experiences: list[Experience] = []

    projects: list[Project] = []

    skills: list[str] = []