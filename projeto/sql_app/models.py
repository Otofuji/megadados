from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Disciplina(Base):
    __tablename__: "disciplna"
    
    course = Column(String, primary_key=True, index=True)
    description = Column(String, index=True)
    professor = Column(String, index=True)
    annotation = Column(String, index=True)

