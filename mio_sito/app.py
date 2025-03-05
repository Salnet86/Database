from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configurazione del database
app.config['MYSQL_HOST'] = 'localhost'  # Cambia con il tuo host, ad esempio su Heroku
app.config['MYSQL_USER'] = 'your_user'  # Cambia con il tuo utente
app.config['MYSQL_PASSWORD'] = 'your_password'  # Cambia con la tua password
app.config['MYSQL_DB'] = 'your_database'  # Cambia con il tuo database

# Configurazione di Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Cambia con il tuo server SMTP
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # Cambia con la tua email
app.config['MAIL_PASSWORD'] = 'your_password'  # Cambia con la tua password

mysql = MySQL(app)
mail = Mail(app)
socketio = SocketIO(app)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Registrazione
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        cognome = request.form['cognome']
        anno_nascita = request.form['anno_nascita']
        data_nascita = request.form['data_nascita']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (nome, cognome, anno_nascita, data_nascita, email, password) VALUES (%s, %s, %s, %s, %s, %s)", 
                    (nome, cognome, anno_nascita, data_nascita, email, password))
        mysql.connection.commit()
        cur.close()
        flash('Registrazione avvenuta con successo!')
        return redirect(url_for('index'))
    return render_template('register.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()
        if user and check_password_hash(user[6], password):  # user[6] è la password
            session['user_id'] = user[0]  # user[0] è l'id
            return redirect(url_for('admin_area'))
        else:
            flash('Email o password errati!')
    return render_template('login.html')

# Area amministrativa
@app.route('/admin_area')
def admin_area():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM uploads WHERE user_id = %s", (session['user_id'],))
    files = cur.fetchall()
    cur.execute("SELECT COUNT(*) FROM visits WHERE user_id = %s", (session['user_id'],))
    visit_count = cur.fetchone()[0]
    cur.close()
    return render_template('admin_area.html', files=files, visit_count=visit_count)

# Caricamento file
@app.route('/upload', methods=['POST'])
def upload():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if 'file' not in request.files:
        flash('Nessun file selezionato!')
        return redirect(url_for('admin_area'))
    
    file = request.files['file']
    if file:
        file_data = file.read()
        file_name = file.filename
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO uploads (user_id, file_name, file_data) VALUES (%s, %s, %s)", 
                    (session['user_id'], file_name, file_data))
        mysql.connection.commit()
        cur.close()
        flash('File caricato con successo!')
    return redirect(url_for('admin_area'))

# Eliminare file
@app.route('/delete_file/<int:file_id>')
def delete_file(file_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM uploads WHERE id = %s AND user_id = %s", (file_id, session['user_id']))
    mysql.connection.commit()
    cur.close()
    flash('File cancellato con successo!')
    return redirect(url_for('admin_area'))

# Inviare email
@app.route('/send_email', methods=['POST'])
def send_email():
    msg = Message('Hello', sender='your_email@example.com', recipients=['recipient@example.com'])
    msg.body = 'This is a test email.'
    mail.send(msg)
    flash('Email inviata con successo!')
    return redirect(url_for('admin_area'))

# Chat istantanea
@app.route('/chat')
def chat():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(msg):
    emit('message', msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
