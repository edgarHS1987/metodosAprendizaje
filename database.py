from peewee import *
from decouple import config

database = {}

def get_database( escuela ):

    if escuela == 'secundaria':
        database = MySQLDatabase(
            'metodosaprendizaje',
            #user = 'root',
            #password = config('DBPASSWORD'),
            #password = '',
            user = 'edgar',
            password = 'test',
            port=3306,
            host='localhost'
        )
    if escuela == 'colegio':
        database = MySQLDatabase(
            'metodoscolegio',
            #user = 'root',
            #password = config('DBPASSWORD'),
            password = '',
            user = 'edgar',
            password = 'test',
            port=3306,
            host='localhost'
        )

    return database


def get_models( escuela ):
    global database
    database = get_database( escuela )

    class Alumno(Model):
        nombre = TextField()
        apellido = TextField()
        gradoGrupo = TextField()

        class Meta:
            database = database
            db_table = 'alumnos'

    class Respuesta(Model):
        idAlumno = TextField()
        respuesta1 = TextField()
        respuesta2 = TextField()
        respuesta3 = TextField()
        respuesta4 = TextField()
        respuesta5 = TextField()
        respuesta6 = TextField()
        respuesta7 = TextField()
        respuesta8 = TextField()
        respuesta9 = TextField()
        respuesta10 = TextField()
        respuesta11 = TextField()
        respuesta12 = TextField()
        respuesta13 = TextField()
        respuesta14 = TextField()
        respuesta15 = TextField()
        respuesta16 = TextField()
        resultado = TextField()
        porcentaje = FloatField()

        class Meta:
            database = database
            db_table = 'respuestas'

    class Detalle(Model):
        idAlumno = TextField()
        respuesta = TextField()

        class Meta:
            database = database
            db_table = 'detalles'

    database.create_tables([Alumno,Respuesta,Detalle])

    return Alumno,Respuesta,Detalle