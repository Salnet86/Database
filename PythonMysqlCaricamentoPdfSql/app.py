from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import mysql.connector
import base64
import magic
from flask import send_file, abort
import io
import requests
from datetime import datetime
from user_agents import parse


app = Flask(__name__)



# Configura la connessione a MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''
mysql = MySQL(app)



@app.route('/insersci',  methods=['GET', 'POST'])
def inserisci():
    log_visitor_ip()
    if request.method == "POST":
        nome = request.form["nome"]
        cognome = request.form["cognome"]
        email = request.form["email"]
        codice_fiscale = request.form["codice_fiscale"]
        numero_telefono= request.form["numero_telefono"]
        password = request.form["password"]
        query = "INSERT INTO utenti (nome, cognome, email,codice_fiscale,numero_telefono, password_hash) VALUES (%s, %s, %s, %s, %s, %s)"
        try:
            cursor = mysql.connection.cursor()  
            cursor.execute(query, (nome, cognome, email,codice_fiscale,numero_telefono, password))  
            mysql.connection.commit()  
            cursor.close()  
            return "Registrazione avvenuta con successo!"
        except Exception as e:
            return f"Errore: {e}"  
       
  



    return render_template('registrazione.html')







@app.route('/file', methods=['GET', 'POST'])
def uppload_file():
    log_visitor_ip()
    if request.method == "POST":
        descrizione = request.form["descrizione"]
        file = request.files["file"]
        
        # Leggi il contenuto binario del file
        file_content = file.read()  # Ottieni i dati binari del file
        
        # Verifica che il file abbia un contenuto
        if not file_content:
            return "Errore: Il file è vuoto"
        
        query = "INSERT INTO caricamento (descrizione, file) VALUES (%s, %s)"  # Usa 'file' invece di 'file_content'
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(query, (descrizione, file_content))  # Passa il contenuto binario
            mysql.connection.commit()
            cursor.close()
            return "Caricamento file avvenuto con successo!"
        except Exception as e:
            return f"Errore: {e}"

    return render_template("carica_file.html")





@app.route('/backeca', methods=['GET', 'POST'])
def backeca():
    log_visitor_ip()
    cursor = mysql.connection.cursor()
    query = "SELECT id, descrizione, file FROM caricamento"
    cursor.execute(query)
    file_data = cursor.fetchall()
    cursor.close()

    modified_data = []
    for dati in file_data:
        dati_list = list(dati)
        dati_list[2] = base64.b64encode(dati_list[2]).decode('utf-8')  # Codifica Base64
        modified_data.append(tuple(dati_list))

    if request.method == 'POST':
        id = request.form['id']
        delete_file = "DELETE FROM caricamento WHERE id = %s"  # Cambia il nome della tabella
        cursor = mysql.connection.cursor() 
        cursor.execute(delete_file, (id,))
        mysql.connection.commit() 
        cursor.close()
        return redirect(url_for('backeca'))  # Redirect alla stessa pagina dopo l'eliminazione

    return render_template('backeca.html', data=modified_data)




@app.route('/visualizza', methods=['GET'])
def visualizza():
    log_visitor_ip()
    cursor = mysql.connection.cursor()
    query = "SELECT id, descrizione, file FROM caricamento"
    cursor.execute(query)
    file_data = cursor.fetchall()
    cursor.close()

    modified_data = []
    for dati in file_data:
        dati_list = list(dati)
        dati_list[2] = base64.b64encode(dati_list[2]).decode('utf-8')  # Codifica Base64
        modified_data.append(tuple(dati_list))
        
    return render_template('visualizza.html', data=modified_data)



def log_visitor_ip():
    # Ottieni l'indirizzo IP del visitatore
    ip_address = request.remote_addr
    
    # Ottieni il timestamp dell'accesso
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Ottieni il user agent del visitatore
    user_agent = request.headers.get('User-Agent')
    
    # Usa la libreria user_agents per ottenere informazioni sul dispositivo
    user_agent_info = parse(user_agent)
    
    # Estrai informazioni sul dispositivo
    device = user_agent_info.device.family  # Tipo di dispositivo (es. 'iPhone', 'PC')
    os = user_agent_info.os.family  # Sistema operativo (es. 'iOS', 'Windows')
    browser = user_agent_info.browser.family  # Browser (es. 'Safari', 'Chrome')
    
    # Usa ipinfo.io per ottenere le informazioni geografiche
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        data = response.json()
        
        # Estrai le informazioni di geolocalizzazione
        city = data.get("city", "Unknown")
        region = data.get("region", "Unknown")
        country = data.get("country", "Unknown")
        location = f"{city}, {region}, {country}"
    except requests.exceptions.RequestException:
        # In caso di errore nella richiesta, imposta valori di default
        location = "Unknown Location"
    
    # Scrivi l'IP, il timestamp, la posizione e il dispositivo nel file di log
    with open("visitor_ips.log", "a") as log_file:
        log_file.write(f"IP: {ip_address} - Time: {timestamp} - Location: {location} - Device: {device} - OS: {os} - Browser: {browser}\n")






@app.route('/home')
def index():
    # Log dell'IP del visitatore quando la pagina viene caricata
    log_visitor_ip()
    
    return render_template("index.html")




























if __name__ == '__main__':
    app.run(debug=True)
