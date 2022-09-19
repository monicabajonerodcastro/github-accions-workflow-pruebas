import datetime
#from Comunidad.base import Session, engine, Base
#from sqlalchemy import Column, Integer, String

class Persona:
    #__tablename__ = 'persona'
    #id = Column(Integer, primary_key=True)
    #nombre = Column(String)
    #edad = Column(Integer)

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def asignar_edad(self, edad):
        self.__edad = edad

    def asignar_nombre(self, nombre):
        self.__nombre = nombre

    def dar_edad(self):
        return(self.__edad)

    def dar_nombre(self):
        return(self.__nombre)

    def calcular_anio_nacimiento(self, ya_cumplio_anios):
        anio_actual = datetime.datetime.now().year
        if ya_cumplio_anios:
            return (anio_actual - self.__edad)
        else:
            return (anio_actual - self.__edad - 1)

'''
    def almacenar(self):
        Base.metadata.create_all(engine)
        session = Session()
        session.add(self)
        session.commit()
        session.close()

    def recuperar(self, nombre, edad):
        session = Session()
        persona = session.query(Persona).filter(Persona.nombre == nombre and Persona.edad == edad).first()
        session.close()
        self.nombre = persona.nombre
        self.edad = persona.edad
        self.id = persona.id
'''