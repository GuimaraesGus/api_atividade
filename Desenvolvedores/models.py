from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///desenvolvedores.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Programador(Base):
    __tablename__ = 'programador'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)
    email = Column(String(40))

    def __repr__(self):
        return '<Programador {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Habilidades(Base):
    __tablename__ = 'habilidades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)

    def __repr__(self):
        return '<Habilidade {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class ProgramadorHabilidade(Base):
    __tablename__ = 'programador_habilidade'
    id = Column(Integer, primary_key=True)
    programador_id = Column(Integer, ForeignKey('programador.id'))
    programador = relationship("Programador")
    habilidade_id = Column(Integer, ForeignKey('habilidades.id'))
    habilidade = relationship("Habilidades")

    def __repr__(self):
        return '<Programador {}, Habilidade {}>'.format(self.programador, self.habilidade)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()