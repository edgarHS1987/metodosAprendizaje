from flask import Flask,jsonify
from flask import render_template
from database import Alumno,Respuesta,Detalle
from peewee import fn
from flask import request,redirect
from flask import session
from database import database
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)
app.secret_key = 'preguntillas'


#login alumno
@app.route('/metodosAprendizaje',methods=['GET','POST'])
def metodosAprendizaje():
    if request.method == 'POST':
        #print('El usuario intento loguearse' + request.form)

        usuario = request.form['usuario']
        pas = request.form['psw']

        # si el usuario es correcto, crear la sesion y permitir acceder al test
        if usuario == 'alumno1' and pas == 'usuari0':
            print('Se capturaron ambos datos y se logueara')
            session['user'] = usuario
            return redirect('/takeTest')
        if usuario == 'maestro@gmail.com' and pas == 'maestro99':
            print('Se capturaron ambos datos y se logueara un maestro')
            session['user'] = usuario
            return redirect('/alumnos')
        
        database.close()
        return render_template("login.html")
    
    if request.method == 'GET':
        print('ingresaste a login')
        return render_template("login.html")

    
# url para finalizar el examen
@app.route('/endTest',methods = ['GET','POST'])
def endTest():
    if request.method == 'GET':
        session.clear()
        return render_template("finTest.html")

# pagina principal del maestro
@app.route('/adminTest',methods = ['GET','POST'])
def adminTest():
    if request.method == 'GET':
        return render_template("adminTest.html")


#graficar por grupo
@app.route('/graficacion',methods = ['GET','POST'])
def graficacion():
    if request.method == 'GET':
        if session.get('user') == None:
            return redirect('/metodosAprendizaje')

        reconnect_if_needed()
        distinct_grupos = Alumno.select(Alumno.gradoGrupo).distinct()

        database.close()

        return render_template("grafica.html",distinct_grupos=distinct_grupos)


#listar alumnos en tabla
@app.route('/alumnos',methods = ['GET','POST'])
def alumnos():
    if request.method == 'GET':
        if session.get('user') == None:
            return redirect('/metodosAprendizaje')
        
        reconnect_if_needed()
        distinct_grupos = Alumno.select(Alumno.gradoGrupo).distinct()
        database.close()

        return render_template("listaAlumnos.html",distinct_grupos=distinct_grupos)


#retorna json con listado
@app.route('/getAlumnos',methods = ['GET','POST'])
def getAlumnos():
    if request.method == 'GET':

        grupo = request.args.get('grupo')

        reconnect_if_needed()

        query = (Alumno
         .select(Alumno.gradoGrupo, Alumno.nombre, Alumno.apellido, Respuesta.resultado, 
                 Respuesta.porcentaje)
         .join(Respuesta, on=(Alumno.id == Respuesta.idAlumno))
         .where(Alumno.gradoGrupo == grupo)
         .order_by( Alumno.apellido )
         )
        
        #results = query.execute()
        array_datos=[]
        counter = 0
        for row in query:
            print(query)
            counter = counter + 1
            diccionario_datos={}
            diccionario_datos['numRegistro'] = counter
            diccionario_datos['Nombre'] = row.nombre
            diccionario_datos['Apellido'] = row.apellido
            diccionario_datos['Resultado'] = row.respuesta.resultado
            diccionario_datos['Porcentaje'] = row.respuesta.porcentaje
            array_datos.append(diccionario_datos)

        database.close()

        return jsonify({"data": array_datos})



#devuelve los datos para pintar la grafica
@app.route('/datosGrafica',methods = ['GET','POST'])
def datosGrafica():
    if request.method == 'GET':
        grupo = request.args.get('grupo')

        reconnect_if_needed()

        #query = "select resultado,count(*) as numero from respuestas A inner join alumnos B on A.idAlumno = B.id Where gradogrupo='8a' and resultado='Auditivo'"

        #total auditivos
        tipos_dic={"Auditivo","Visual","Lector/Escritor","Kinestesico"}

        array_datos=[]
        diccionario_datos={}
        for tipo in tipos_dic:

            query = (Respuesta
            .select(Respuesta.resultado, fn.COUNT(Respuesta.resultado).alias('numero'))
            .join(Alumno, on=(Respuesta.idAlumno == Alumno.id))
            .where((Alumno.gradoGrupo == grupo) & (Respuesta.resultado == tipo))
            .group_by(Respuesta.resultado)
            )

            results = query.execute()

            #diccionario_datos={}
            for row in results:
                llave = row.resultado
                if row.resultado == "Lector/Escritor":
                    llave = "Lector"
                diccionario_datos[llave] = row.numero

        array_datos.append(diccionario_datos)


        if len(array_datos) == 0:
            diccionario_datos['sindatos'] = 0
            array_datos.append(diccionario_datos)
        
        database.close()

        return jsonify({"data": array_datos})
        

    

#para hacer pruebas de funciones
@app.route('/test',methods = ['GET','POST'])
def test():

    reconnect_if_needed()
    
    query = (Respuesta.select().where(Respuesta.idAlumno == 1 ))

    for campo in query:
        print(campo.idAlumno)
        print(campo.respuesta1)

    database.close()

    return render_template("login.html")



@app.route('/takeTest',methods = ['GET','POST'])
def takeTest():

    if request.method == 'POST':
        print('hiciste post')
        nombrealumno = request.form['nombreAlumno']
        apellido = request.form['apellidoAlumno']
        grupo = request.form['gradoGrupo']
        r1 = request.form['radios1']
        r2 = request.form['radios2']
        r3 = request.form['radios3']
        r4 = request.form['radios4']
        r5 = request.form['radios5']
        r6 = request.form['radios6']
        r7 = request.form['radios7']
        r8 = request.form['radios8']
        r9 = request.form['radios9']
        r10 = request.form['radios10']
        r11 = request.form['radios11']
        r12 = request.form['radios12']
        r13 = request.form['radios13']
        r14 = request.form['radios14']
        r15 = request.form['radios15']
        r16 = request.form['radios16']

        respuestasDic = dict()
        respuestasDic['res1'] = r1
        respuestasDic['res2'] = r2
        respuestasDic['res3'] = r3
        respuestasDic['res4'] = r4
        respuestasDic['res5'] = r5
        respuestasDic['res6'] = r6
        respuestasDic['res7'] = r7
        respuestasDic['res8'] = r8
        respuestasDic['res9'] = r9
        respuestasDic['res10'] = r10
        respuestasDic['res11'] = r11
        respuestasDic['res12'] = r12
        respuestasDic['res13'] = r13
        respuestasDic['res14'] = r14
        respuestasDic['res15'] = r15
        respuestasDic['res16'] = r16

        reconnect_if_needed()

        alumno_id = Alumno.create(nombre=nombrealumno.upper(),apellido=apellido.upper(),gradoGrupo=grupo.upper())

        for r in respuestasDic:
            Detalle.create(idAlumno=alumno_id,respuesta=respuestasDic[r])
        
        #select count(*) conteo,respuesta from detalles where idAlumno=2 group by respuesta order by conteo;
        query = (Detalle
                .select(fn.COUNT(Detalle.respuesta).alias('conteo'), Detalle.respuesta)
                .where(Detalle.idAlumno == alumno_id)
                .group_by(Detalle.respuesta)
                .order_by(fn.COUNT().alias('conteo'))
                )
        
        results = query.execute()
        resultadoTest = ''
        porcentajeResultado = 0.0
        res = 0
        for row in results:
            resultadoTest = row.respuesta
            print(resultadoTest)
            res = int(row.conteo)
            porcentajeResultado = ( res*100 )/16
        

        #obtiene el total de mayor respuestas

        
        Respuesta.create(idAlumno=alumno_id,respuesta1=r1,respuesta2=r2,respuesta3=r3,respuesta4=r4,respuesta5=r5,
                         respuesta6=r6, respuesta7=r7, respuesta8=r8 , respuesta9=r9, respuesta10=r10, respuesta11=r11,
                         respuesta12=r12, respuesta13=r13, respuesta14=r14, respuesta15=r15, respuesta16=r16, 
                         resultado=resultadoTest, porcentaje=porcentajeResultado)



        return redirect('/endTest')

    if request.method == 'GET':
        if session.get('user') == None:
            return redirect('/metodosAprendizaje')
        else:
            return render_template("examen.html")

def reconnect_if_needed():
    try:
        database.connect()
    except OperationalError as e:
        if 'Lost connection' in str(e) or 'timeout' in str(e):
            database.close()
            database.connect()

if __name__ == '__main__':
    app.run(debug=True)