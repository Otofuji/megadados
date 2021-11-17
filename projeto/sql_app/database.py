from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import pymysql

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://os.environ['USER']:os.environ['TERM_PROGRAM']@localhost:3306" #TODO verificar URL para MYSQL e modificações necessárias. A mudança deve ser apenas nesta linha… (ou a de baixo)
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
