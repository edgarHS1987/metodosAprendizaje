## Creamos el usuario
adduser <metodos>

## Agregar el usuario a grupo de administradores
usermod -aG sudo <metodos>
la contraseña es la misma "metodos"

## Cambiar al nuevo usuario
su - <metodos>

## Clonar el repositorio
git clone <repositorio>

## instalar dependencias
pip install -r requirements.txt
python3 -m venv env




yproject.sock -m 007 wsgi:app

asi estaba antes
xecStart=/root/project/metodosAprendizaje/env/bin/gunicorn --workers 3 --bind unix:/run/metodosAprendizaje.sock main:app

configuracion para que nginx lea mi configuracion
sudo ln -s /etc/nginx/sites-available/flask /etc/nginx/sites-enabled/


from main import app

if __name__ == "__main__":
    app.run()

server_name 146.190.222.125;

## Secundaria Jose Vasconselos
Usuario Profesor = maestro@gmail.com
Password = maestro99

Alumno = alumno1
Password = usuari0

## Colegio Nuevo Humanismo
Usuario Profesor = colegio@mail.com
Password = maestro99

Alumno = colegiotest
Password = usuari0

