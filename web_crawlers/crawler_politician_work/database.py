import os
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = os.getenv("DATABASE_URI")
engine = create_engine(DATABASE_URI)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Proposicoes(Base):
    __tablename__ = 'proposicoes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    processo = Column(String(50))
    ano = Column(String(10))
    tipo = Column(String(50))
    assunto = Column(Text)
    data = Column(String(50))
    situacao = Column(String(50))
    arquivo = Column(String(255))
    autor = Column(String(50))
    
def init_db():
    Base.metadata.create_all(engine)
    
def insert_data(data):
    session = Session()
    for item in data:
        proposicoes = Proposicoes(
            processo=item['processo']
            ano= item['ano']
            tipo= item['tipo']
            assunto= item['assunto']
            data= item['data']
            situacao= item['situacao']
            arquivo= item['arquivo']
            autor = item['autor']
        )
        session.add(proposicoes)
    session.commit()
    session.close()
    print("insert data sucess!")
        
    
