from models.eventos import Eventos as EventosModel
from schemas.eventos import Eventos
from fastapi import HTTPException,status
from sqlalchemy.exc import IntegrityError
from services.categorias import CategoriaService
from datetime import datetime, date

class EventoService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_evento(self):
        result = self.db.query(EventosModel).all()
        return result

    def get_evento_id(self, id):
        result = self.db.query(EventosModel).filter(EventosModel.id == id).first()
        return result

    def get_evento_by_category(self, evento):
        result = self.db.query(EventosModel).filter(EventosModel.categoria_id == evento).all()
        return result

    def create_evento(self, evento: Eventos):
        try:
            resultCategoria=CategoriaService(self.db).get_categoria_id(evento.categoria_id)

            if resultCategoria == None :
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La Categoria ingresada no es valida.")
            
            new_evento = EventosModel(**evento.dict())
            self.db.add(new_evento)
            self.db.commit()
            return 
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(status_code=400, detail=f"Error.")    
    
    def update_evento(self, id: int, data: Eventos):
        evento = self.db.query(EventosModel).filter(EventosModel.id == id).first()
        evento.nombre = data.nombre
        evento.descripcion = data.descripcion
        evento.fecha_inicio = data.fecha_inicio
        evento.fecha_fin = data.fecha_fin
        evento.lugar = data.lugar
        evento.cupos = data.cupos
        evento.categoria_id = data.categoria_id
        self.db.commit()
        return

    def delete_evento(self, id: int):
       result =self.db.query(EventosModel).filter(EventosModel.id == id).delete()
       if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La evento no existe.")
       self.db.commit()
       return
    
    ##Obtener la lista de eventos disponibles.
    def get_evento_disponibles(self, fecha: date):
        result = self.db.query(Eventos).filter(Eventos.fecha_inicio >= fecha).all()
        return result

    ##Buscar eventos por nombre o descripción.
     
    def get_evento_nombre(self, nombre):
        result = self.db.query(EventosModel).filter(EventosModel.nombre == nombre).first()
        return result
    
    def get_evento_descripcion(self, descripcion):
        result = self.db.query(EventosModel).filter(EventosModel.descripcion == descripcion).first()
        return result
    
    def get_evento_cupos(self, evento_id: int):
        evento = self.db.query(EventosModel).filter(EventosModel.id == evento_id).first()
        return evento.cupos if evento else None

    def set_eventos_cupos(self, evento_id: int, new_cupos: int):
        evento = self.db.query(EventosModel).filter(EventosModel.id == evento_id).first()
        if evento:
            evento.cupos = new_cupos
            self.db.commit()