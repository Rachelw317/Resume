from pydantic import BaseModel


class JD(BaseModel):

    job_title: str = ""

    company: str = ""

    responsibilities: list[str] = []

    required_skills: list[str] = []

    preferred_skills: list[str] = []

    requirements: list[str] = []