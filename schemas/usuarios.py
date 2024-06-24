from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

class UsuarioBase(BaseModel):
    id:Optional[int|None]=Field(default=None)
    nombre:str=Field(title="nombre")
    email:EmailStr=Field(examples=["nombre@gmail.com"])
    rol:Literal['Cliente','Administrador']= Field(default='Cliente', examples=['Cliente | Administrador'])

    class Config:
        from_attributes = False
        orm_mode = True # indica a Pydantic que debe convertir automáticamente los objetos SQLAlchemy en modelos Pydantic.


class Usuario(UsuarioBase):
    hashed_password:str = Field(min_length=8)

    class Config:
        from_attributes = True

