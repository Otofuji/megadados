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



##################################################################################################################################################################################################################################################################################################################



@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
