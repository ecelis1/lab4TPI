from config.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Eventos(Base):

    __tablename__ = 'eventos'

    id = Column(Integer, primary_key = True, autoincrement='auto')
    nombre = Column(String(30), nullable=False)
    descripcion = Column(String(256))
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    lugar = Column(String(128), nullable=False)
    cupos = Column(Integer, nullable= False)
    categoria_id = Column(Integer, ForeignKey('categorias.id'), nullable=False)

    categoria = relationship('Categorias', lazy='joined', back_populates='eventos')
    inscripciones = relationship('Inscripciones', lazy='joined', back_populates='evento')

    class Config:
        from_attributes = True