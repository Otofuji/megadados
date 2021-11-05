# git@github.com:Otofuji/megadados.git
# https://fastapi.tiangolo.com
# async version

#####################################
# REQUIREMENTS
# $ python -m pip install --upgrade pip
# $ pip install fastapi
# $ pip install "uvicorn[standard]"

#COMPATIBLE WITH PYTHON 3.8.8

# RUN SERVER USING
# $ uvicorn ctr:notas --reload

#                             CHECKLIST
#
# [ ] POST        REQ-01      usuário pode criar disciplina
# [ ] GET         REQ-02      disciplina tem nome único (obrigatório)
# [ ] GET         REQ-03      disciplina tem nome de professor (opcional)
# [ ] GET         REQ-04      disciplina tem campo de anotação livre (texto)
# [ ] DELETE      REQ-05      usuário pode deletar disciplina
# [ ] GET         REQ-06      usuário pode listar os nomes de suas disciplinas
# [ ] PUT         REQ-07      usuário pode modificar as informações de uma disciplina, incluindo seu nome
# [ ] POST        REQ-08      usuário pode adicionar uma nota a uma disciplina
# [ ] DELETE      REQ-09      usuário pode deletar uma nota de uma disciplina
# [ ] GET         REQ-10      usuário pode listar as notas de uma disciplina
# [ ] PUT         REQ-11      usuário pode modificar uma nota de uma disciplina
#
#####################################

from typing import Optional, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

notas = FastAPI()

class Disciplina(BaseModel):
    name: str = Field(..., example="Megadados")
    description: Optional[str] = Field(None, example="DBA")
    professor: Optional[str] = Field(None, example="Fábio Ayres")
    annotation: Optional[str] = Field(None, example="Lorem ipsum dolor sit amet")
    grade: Dict[str, float] = Field(..., example={'P1': 8.25}, description="grades dict") #https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html -> https://www.programcreek.com/python/example/112465/pydantic.Field


#TODO corrigir schema
    class Config:
        schema_extra = {
            "example": {
                "name": "MEGADADOS",
                "description": "DBA",
                "professor": "FÁBIO AYRES",
                "annotation": "Lorem ipsum dolor sit amet",
                "grade": "{'P1': 8.25}"
            }
        }
""" 
#DO TUTORIAL - INICIO
@notas.get("/")
async def read_root():
    return {"Hello": "World"}


@notas.get("/items/{item_id}")0
async def read_item(item_id: int, q: Optional[str] = None):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "q": q}

@notas.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id} 

#DO TUTORIAL - FIM
 """



#TODO REQ-01
@notas.post("/{Disciplina}")
async def CriaDisciplinas(name: str, description: Optional[str], professor: Optional[str], annotation: Optional[str]):
    return None

#TODO REQ-02
@notas.get("/disciplina/{Disciplina}")
async def DisciplinaNomes(args):
    return None

#TODO REQ-03
@notas.get("/disciplina/{Disciplina}")
async def DisciplinaProfessores(args):
    return None

#TODO REQ-04
@notas.get("/disciplina/{Disciplina}")
async def DisciplinaTextos(args):
    return None

#TODO REQ-05
@notas.delete("/disciplina/{Disciplina}")
async def ApagaDisciplinas(args):
    return None

#TODO REQ-06
@notas.get("/disciplina/{Disciplina}")
async def ListaDisciplinas(args):
    return None

#TODO REQ-07
@notas.put("/disciplina/{Disciplina}")
async def AtualizaDisciplinas(name: str, description: Optional[str], professor: Optional[str], annotation: Optional[str]):
    return None

#TODO REQ-08
@notas.post("/disciplina/{Disciplina}")
async def PublicaNotas(args):
    return None

#TODO REQ-09
@notas.delete("/disciplina/{Disciplina}")
async def ApagaNotas(args):
    return None

#TODO REQ-10
@notas.get("/disciplina/{Disciplina}")
async def ListaNotas(args):
    return None

#TODO REQ-11
@notas.put("/disciplina/{Disciplina}")
async def AtualizaNotas(args):
    return None
