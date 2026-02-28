from pydantic import BaseModel
from typing import List, Optional


class Project(BaseModel):
    description: str
    tools: List[str]
    metrics: Optional[List[str]]


class Experience(BaseModel):
    company: str
    role: str
    duration_months: Optional[int]
    projects: Optional[List[Project]]


class ResumeData(BaseModel):
    skills: List[str]
    experience: List[Experience]
    achievements: Optional[List[str]]