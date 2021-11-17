from sqlalchemy.orm import Session

import models, schemas


def put_disciplina(db: Session, course: schemas.DisciplinaCreate):
    db_disciplina = models.Disciplina(course = disciplina.course, description = disciplina.description, professor = disciplina.professor, annotation = disciplina.annotation)
    db.add(db_disciplina)
    db.commit()
    db.refresh(db_disciplina)
    return db_disciplina

#   get_discipliNA, no singular
def get_disciplina(db: Session, course: str):
    return db.query(models.Disciplina).filter(models.Disciplina.course == course).first()

def del_disciplina(db: Session, course:str):
    db.delete(db.disciplina).where(db.disciplina.course == course) #https://docs.sqlalchemy.org/en/14/core/dml.html
    db.commit()
    return None

#   get_discipliNAS, no plural
def get_disciplinas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Disciplina).offset(skip).limit(limit).all()

def rnm_disciplina(db: Session, currentname: str, newname: str):
    db.update(db.disciplina).where(db.disciplina.course == currentname).values(course = newname) #https://docs.sqlalchemy.org/en/14/core/dml.html
    db.commit()
    return None

def get_grade(db: Session, course: str):
    return db.query(models.Disciplina.annotation).filter(models.Disciplina.course == course).first()