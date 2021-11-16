# git@github.com:Otofuji/megadados.git
# https://fastapi.tiangolo.com

#####################################
# REQUIREMENTS
# $ python -m pip install --upgrade pip
# $ pip install fastapi
# $ pip install "uvicorn[standard]"
# $ pip install SQLAlchemy

# COMPATIBLE WITH PYTHON 3.8.8

# RUN SERVER USING
# $ uvicorn main:notas --reload

#                             CHECKLIST
#
# [x] PUT         REQ-01      usuário pode criar disciplina
# [x] GET         REQ-02      disciplina tem nome único (obrigatório)
# [x] GET         REQ-03      disciplina tem nome de professor (opcional)
# [x] GET         REQ-04      disciplina tem campo de anotação livre (texto)
# [x] DELETE      REQ-05      usuário pode deletar disciplina
# [x] GET         REQ-06      usuário pode listar os nomes de suas disciplinas
# [x] PUT         REQ-07      usuário pode modificar as informações de uma disciplina, incluindo seu nome
# [x] PUT         REQ-08      usuário pode adicionar uma nota a uma disciplina
# [x] DELETE      REQ-09      usuário pode deletar uma nota de uma disciplina
# [x] GET         REQ-10      usuário pode listar as notas de uma disciplina
# [x] PUT         REQ-11      usuário pode modificar uma nota de uma disciplina
#
#####################################

from typing import Optional, Dict, List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from pydantic import BaseModel, Field

models.Base.metadata.create_all(bind=engine)

notas = FastAPI(title="Controle de Notas",
    description='Projeto da disciplina Megadados',
    version="0.0.2",
    terms_of_service="https://github.com/Otofuji/megadados",
    contact={
        "name": "Eric Fernando Otofuji Abrantes, Henrique Mualem Marti, Marco Moliterno Pena Piacentini",
        "url": "https://github.com/Otofuji/megadados",
        "email": "ericfoa@al.insper.edu.br",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@notas.put("/disciplinas/{course}")
def PutDisciplinas(course: str, description: Optional[str], professor: Optional[str], annotation: Optional[str]):
    schemas = {
            "course": course,
            "description":  description,
            "professor": professor,
            "annotation": annotation,
    }

    db_disciplina = crud.put_disciplina(db=db, schemas)

    return crud.get_disciplina(db=db, course)


@notas.get("/disciplinas/{course}")
def GetDisciplinas(course: str):
    return crud.get_disciplina(db=db, course)


@notas.delete("/disciplinas/{course}")
def ApagaDisciplinas(course):
    return crud.del_disciplina(db=db, course)

@notas.get("/disciplinas")
def ListaDisciplinas():
    return crud.get_disciplinas(db=db, 0, 100)

@notas.put("/disciplinas/rename/{course}")
def RenomeiaDisciplinas(currentname: str, newname: str): 
    return crud.rnm_disciplina(db=db, currentname, newname)

@notas.get("/disciplinas/{course}/grades")
def Notas(course: str):
    return crud.get_grade(db=db, course)
