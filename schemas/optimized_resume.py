from pydantic import BaseModel


class OptimizedResume(BaseModel):

    name: str = ""

    education: list[str] = []

    experiences: list[str] = []

    projects: list[str] = []

    skills: list[str] = []

    modification_notes: list[str] = []