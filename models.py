from typing import Optional, List
from pydantic import BaseModel
from enum import Enum
from uuid import UUID, uuid4


class YearsRange(BaseModel):
    pass

class Awards(BaseModel):
    pass

class Education(BaseModel):
    institusion_name: str
    title: str
    grade: Optional[int]
    scholarships_awards: Optional[list[Awards]]
    years: YearsRange
    
class Experience(BaseModel):
    role: str
    company: str
    years: YearsRange
    description: Optional[str]

class SkillCategory(str, Enum):
    soft = "soft"
    hard = "hard"
    language = "language"
    
class Skill(BaseModel):
    title: str
    category: Optional[SkillCategory]
    description: Optional[str]

class Project(BaseModel):
    title: str
    years: YearsRange
    description: Optional[str]    
    link: Optional [str]
    
class Resume(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    phone: Optional[str]
    email: Optional[str]
    linkdin_link: Optional[str]
    github_link: Optional[str]
    title: str
    education: Optional[List[Education]]
    experience: Optional[List[Experience]]
    skills: Optional[List[Skill]]
    projects: Optional[List[Project]]



    
    
    