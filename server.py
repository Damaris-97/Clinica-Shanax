from flask import Flask, flash, jsonify, redirect, render_template, request, url_for
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__, static_url_path='/static')
load_dotenv()

# Configuración de MySQL
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)

# Configuración de Flask-Login
app.secret_key = "mysecretkey"
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Modelo de usuario
class User(UserMixin):
    def _init_(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, email, password FROM users WHERE id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    if user:
        return User(user[0], user[1], user[2])
    return None

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Ruta de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, email, password FROM users WHERE email = %s AND password = %s", (email, password))
        user = cur.fetchone()
        cur.close()
        
        if user:
            user_obj = User(user[0], user[1], user[2])
            login_user(user_obj)
            return redirect(url_for('data'))
        else:
            flash('Los datos ingresados son incorrectos.', 'info')
    return render_template('login.html')

@app.route('/save', methods=['GET', 'POST'])
def add_paciente():
    if request.method == 'POST':
        nombre_completo = request.form['nombre_completo']
        dni = request.form['dni']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        edad = request.form['edad']
        genero = request.form['genero']
        comorbilidad = request.form['comorbilidad']
        tipo_grupo = request.form['tipo_grupo']

        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO pacientes (nombre_completo, dni, direccion, telefono, edad, genero, comorbilidad, tipo_grupo) 
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', (nombre_completo, dni, direccion, telefono, edad, genero, comorbilidad, tipo_grupo))
        mysql.connection.commit()
        cursor.close()
        flash('El paciente ha sido registrado exitosamente.', 'success')
    return render_template('add_paciente.html')


@app.route('/login')
def main():
    return render_template('login.html')

@app.route('/data')  # App Web
@login_required
def data():
    dni = request.args.get('dni')
    cur = mysql.connection.cursor()
    if dni:
        cur.execute('SELECT * FROM pacientes WHERE dni = %s', (dni,))
    else:
        cur.execute('SELECT * FROM pacientes')
    pacientes = cur.fetchall()
    cur.close()
    return render_template('index.html', pacientes=pacientes)

@app.route('/grafico')
def grafico():
    cur = mysql.connection.cursor()

    # Primer gráfico (tipo_grupo)
    cur.execute('SELECT tipo_grupo, COUNT(*) FROM pacientes GROUP BY tipo_grupo')
    data1 = cur.fetchall()
    labels1 = [row[0] for row in data1]
    values1 = [row[1] for row in data1]

    # Segundo gráfico (por zona)
    cur.execute('SELECT genero, COUNT(*) FROM pacientes GROUP BY genero')
    data2 = cur.fetchall()
    labels2 = [row[0] for row in data2]
    values2 = [row[1] for row in data2]

    cur.close()

    return render_template('graph.html', labels1=labels1, values1=values1, labels2=labels2, values2=values2)

@app.route('/edit/<id_paciente>')
@login_required
def get_client(id_paciente):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM pacientes WHERE id_paciente = %s', (id_paciente,))
    data = cur.fetchone()
    cur.close()
    return render_template('edit-paciente.html', paciente=data)

@app.route('/update/<id_paciente>', methods=['POST'])
@login_required
def update_paciente(id_paciente):
    if request.method == 'POST':
        nombre_completo = request.form['nombre_completo']
        dni = request.form['dni']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        edad = request.form['edad']
        genero = request.form['genero']
        comorbilidad = request.form['comorbilidad']
        tipo_grupo = request.form['tipo_grupo']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE pacientes
            SET nombre_completo = %s,
                dni = %s,
                direccion = %s,
                telefono = %s,
                edad = %s,
                genero = %s,
                comorbilidad = %s,
                tipo_grupo = %s
            WHERE id_paciente = %s
        """, (nombre_completo, dni, direccion, telefono, edad, genero, comorbilidad, tipo_grupo, id_paciente))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('data'))

@app.route('/delete/<id_paciente>', methods=['GET', 'POST'])
def delete_paciente(id_paciente):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM pacientes WHERE id_paciente = %s', (id_paciente,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('data'))

# Server
if __name__ == '__main__':
    app.run(port=5000, debug=True)
