# git@github.com:Otofuji/megadados.git
# https://fastapi.tiangolo.com
# async version

#####################################
# REQUIREMENTS
# $ python -m pip install --upgrade pip
# $ pip install fastapi
# $ pip install "uvicorn[standard]"

# COMPATIBLE WITH PYTHON 3.8.8

# RUN SERVER USING
# $ uvicorn ctr:notas --reload

#                             CHECKLIST
#
# [x] PUT         REQ-01      usuário pode criar disciplina
# [x] GET         REQ-02      disciplina tem nome único (obrigatório)
# [x] GET         REQ-03      disciplina tem nome de professor (opcional)
# [x] GET         REQ-04      disciplina tem campo de anotação livre (texto)
# [x] DELETE      REQ-05      usuário pode deletar disciplina
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
    course: str = Field(..., example="Megadados")
    description: Optional[str] = Field(None, example="DBA")
    professor: Optional[str] = Field(None, example="Fábio Ayres")
    annotation: Optional[str] = Field(None, example="Lorem ipsum dolor sit amet")
    #grade: Dict[str, float] #https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

    class Config:
        schema_extra = {
            "example": {
                "course": "MEGADADOS",
                "description": "DBA",
                "professor": "FÁBIO AYRES",
                "annotation": "Lorem ipsum dolor sit amet",
                #"grade": "{'P1': 8.25}"
            }
        }


# REQ-01 | REQ-02 | REQ-03 | REQ-04
# TODO verificar bug de campos opcionais estarem como requeridos na aplicação

#   Inicialmente, seria mais intuitivo usar o método POST por se tratar de criação de novos recursos. Porém, pensando em termos de idempotência, optamos por usar o método PUT, com base nas informações constantes das páginas 10, 12 e 13 do manual "RESTful Service Best Practices" de Todd Fredrich. 

#   Vale ressaltar que PUT, embora normalmente usado para atualização de recursos, também pode ser usado para criação de recursos quando é importante que seja idempotente. Todd Fredrich ainda adiciona que devemos usar PUT quando o cliente está a cargo de decidir qual é a URI, que é exatamente o caso aqui: o usuário define o nome da disciplina. 

#   Além disso, o requisito REQ-02 exige que a disciplina tenha nome único. Para isso ser possível em REST, o recurso tem que obrigatoriamente ser idempotente. Se usássemos POST, não seria idempotente e, portanto, violaríamos REQ-02. Portanto, o único método correto para a criação de disciplinas é o PUT. 

#   Esta chamada satisfaz REQ-01 (usuário pode criar disciplina), bem como REQ-02, REQ-03 e REQ-04, tendo os campos requeridos que uma disciplina possua.

@notas.put("/disciplinas/{course}")
async def CriaDisciplinas(course: str, description: Optional[str], professor: Optional[str], annotation: Optional[str]):
    return {"course": course} 


# REQ-05
@notas.delete("/disciplinas/{course}")
async def ApagaDisciplinas(course):
    return None

#TODO REQ-06


#TODO REQ-07


#TODO REQ-08


#TODO REQ-10


#TODO REQ-11

