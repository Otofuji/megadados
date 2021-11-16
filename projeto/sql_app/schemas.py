from typing import List, Optional

from pydantic import BaseModel


class DisciplinaBase(BaseModel):
    course: str
    

class DisciplinaCreate(ItemBase):
    description: Optional[str]
    professor: Optional[str]
    annotation: Optional[str]


class Disciplina(ItemBase):
    pass
    
    class Config:
        orm_mode = True

