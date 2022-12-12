from typing import Optional, List
from pydantic import BaseModel
from enum import Enum


class Awards():
    pass

class YearsRange(BaseModel):
    pass
class Education(BaseModel):
    institusion_name: str
    title: str
    grade: Optional[int]
    scholarships_awards: Optional[list[Awrads]]
    years: YearsRange
    
class Resume(BaseModel):
    first_name: str
    last_name: str
    phone: Optional[str]
    email: Optional[str]
    linkdin_link: Optional[str]
    github_link: Optional[str]
    title: str
    education: Optional[List[Education]]
    
class Education(BaseModel):
    institusion_name: str
    