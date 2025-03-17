from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

# Crea un'app Flask
app = Flask(__name__)

# Configura la connessione a MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''
mysql = MySQL(app)


'''
@app.route('/')
def index():
    return render_template('index.html')
'''

@app.route('/chat', methods=['GET', 'POST'])
def chat_room():
    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO messages (username, message) VALUES (%s, %s)", (username, message))
        mysql.connection.commit()
        cursor.close()

        # Usa url_for per fare il redirect all'endpoint 'chat_room'
        return redirect(url_for('chat_room'))
    
    else:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT username, message FROM messages")
        messages = cursor.fetchall()
        cursor.close()

        return render_template('chat.html', messages=messages)

# Avvia l'app
if __name__ == '__main__':
    app.run(debug=True)
