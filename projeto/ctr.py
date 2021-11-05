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
# [x] PUT         REQ-07      usuário pode modificar as informações de uma disciplina, incluindo seu nome
# [x] PUT         REQ-08      usuário pode adicionar uma nota a uma disciplina
# [x] DELETE      REQ-09      usuário pode deletar uma nota de uma disciplina
# [ ] GET         REQ-10      usuário pode listar as notas de uma disciplina
# [x] PUT         REQ-11      usuário pode modificar uma nota de uma disciplina
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


# REQ-01 | REQ-02 | REQ-03 | REQ-04 | REQ-06
# TODO verificar bug de campos opcionais estarem como requeridos na aplicação

#   Inicialmente, seria mais intuitivo usar o método POST por se tratar de criação de novos recursos. Porém, pensando em termos de idempotência, optamos por usar o método PUT, com base nas informações constantes das páginas 10, 12 e 13 do manual "RESTful Service Best Practices" de Todd Fredrich. 

#   Vale ressaltar que PUT, embora normalmente usado para atualização de recursos, também pode ser usado para criação de recursos quando é importante que seja idempotente. Todd Fredrich ainda adiciona que devemos usar PUT quando o cliente está a cargo de decidir qual é a URI, que é exatamente o caso aqui: o usuário define o nome da disciplina. 

#   Além disso, o requisito REQ-02 exige que a disciplina tenha nome único. Para isso ser possível em REST, o recurso tem que obrigatoriamente ser idempotente. Se usássemos POST, não seria idempotente e, portanto, violaríamos REQ-02. Portanto, o único método correto para a criação de disciplinas é o PUT. 

#   Esta chamada satisfaz REQ-01 (usuário pode criar disciplina), bem como REQ-02, REQ-03 e REQ-04, tendo os campos requeridos que uma disciplina possua. Também é uma implementação parcial do REQ-06, que será completado mais abaixo. 

@notas.put("/disciplinas/{course}")
async def PutDisciplinas(course: str, description: Optional[str], professor: Optional[str], annotation: Optional[str]):
    return {"course": course} 

#TODO verificar bug - 500 internal server error
@notas.get("/disciplinas/{course}")
async def GetDisciplinas(course: str):
    return {"course": course, "description": description, "professor": professor, "annotation": annotation} 


# REQ-05
@notas.delete("/disciplinas/{course}")
async def ApagaDisciplinas(course):
    return None

#TODO REQ-06
@notas.get("/disciplinas")
async def ListaDisciplinas():
    return None


#REQ-07
#   Usamos PUT para a criação da disciplina acima. O mesmo comando pode atualizar qualquer um dos componentes da disciplina, exceto seu nome. Ou seja, executar PUT/disciplinas/{course} acima já atualiza por si só conteúdo existente, mas não o nome da disciplina. Para isso, criamos este método que especificamente tem por intenção atualizar o nome da disciplina. As demais atualizações do REQ-06 vêm junto com o recurso que implementou REQ-01 acima. 

@notas.put("/disciplinas/rename/{course}")
async def RenomeiaDisciplinas(oldcourse: str, description: Optional[str], professor: Optional[str], annotation: Optional[str], newcourse: str): 
    PutDisciplinas(newcourse, description, professor, annotation)
    ApagaDisciplinas(oldcourse)
    return {"course": newcourse}




#REQ-10
@notas.get("disciplinas/{course}/grades")
async def Notas(course: str):
    return ("notas": annotation)

