create table  alumnos(
idAlumno int AUTO_INCREMENT, 
nombre VARCHAR(100) NOT NULL,
apellido VARCHAR(100) NOT NULL,
gradoGrupo VARCHAR(2) NOT NULL
);

create table respuestas(
idTest int AUTO_INCREMENT,
idAlumno int NOT NULL,
respuesta1 VARCHAR(1) NOT NULL,
respuesta2 VARCHAR(1) NOT NULL,
respuesta3 VARCHAR(1) NOT NULL,
respuesta4 VARCHAR(1) NOT NULL,
respuesta5 VARCHAR(1) NOT NULL,
respuesta6 VARCHAR(1) NOT NULL,
respuesta7 VARCHAR(1) NOT NULL,
respuesta8 VARCHAR(1) NOT NULL,
respuesta9 VARCHAR(1) NOT NULL,
respuesta10 VARCHAR(1) NOT NULL,
respuesta11 VARCHAR(1) NOT NULL,
respuesta12 VARCHAR(1) NOT NULL,
respuesta13 VARCHAR(1) NOT NULL,
respuesta14 VARCHAR(1) NOT NULL,
respuesta15 VARCHAR(1) NOT NULL,
resultado
);