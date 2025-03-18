from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import mysql.connector
import base64

app = Flask(__name__)



# Configura la connessione a MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''
mysql = MySQL(app)


'''
@app.route('/home')
def Index():
	return render_template('index.html')
'''







@app.route('/inser', methods=['GET', 'POST'])
def registrazione():
    if request.method == "POST":
        nome = request.form["nome"]
        cognome = request.form["cognome"]
        data = request.form["data"]
        email = request.form["email"]
        cod = request.form["cod"]
        password = request.form["password"]

      
        query = "INSERT INTO utente (nome, cognome, data_nascita, email, codice_fiscale, password_hash) VALUES (%s, %s, %s, %s, %s, %s)"
        
        try:
            cursor = mysql.connection.cursor()  
            cursor.execute(query, (nome, cognome, data, email, cod, password))  
            mysql.connection.commit()  
            cursor.close()  
            return "Registrazione avvenuta con successo!"
        except Exception as e:
            return f"Errore: {e}"  
    return render_template('registrazione.html') 

		 
		
	
@app.route('/record', methods=['GET', 'POST'])
def amministratrice():
    try:
        cursor = mysql.connection.cursor()  
        query = "SELECT id, nome, cognome, data_nascita, email, codice_fiscale, password_hash FROM utente"
        cursor.execute(query)
        data = cursor.fetchall()  
        cursor.close()
       

       #metodo cancella i dati dal database 
        if request.method == 'POST':
            id = request.form['id'] 
            delete_query = "DELETE FROM utente WHERE id = %s" 
            cursor = mysql.connection.cursor() 
            cursor.execute(delete_query, (id,))
            mysql.connection.commit() 
            cursor.close()  

            return redirect(url_for('amministratrice'))  #nome funzione def amministratrice():

        return render_template('record.html', data=data) 
    except Exception as e:
        return f"Errore: {e}"



    



        return render_template('record.html', data=data)  
    except Exception as e:
        return f"Errore: {e}"




@app.route('/file', methods=['GET', 'POST'])
def panello():
    if request.method == "POST":
        nome_foto = request.form["nome_foto"]  
        file = request.files["file"]  
        # Leggi il contenuto del file (importante per inserire i dati binari nel database)
        file_data = file.read()

        query = "INSERT INTO panell (nome_foto, file) VALUES (%s, %s)"
        
        try:
            cursor = mysql.connection.cursor() 
            cursor.execute(query, (nome_foto, file_data))  
            mysql.connection.commit()  
            cursor.close()  # Chiudi il cursore
            return "File e nome foto caricati con successo!"  
        except Exception as e:
            return f"Errore: {e}" 

    return render_template('panello.html')  # Mostra la pagina






@app.route('/img', methods=['GET', 'POST'])
def file_read():
    try:
        cursor = mysql.connection.cursor()  
        query = "SELECT id, nome_foto, file FROM panell"
        cursor.execute(query)
        file_data = cursor.fetchall()  # Ottieni tutti i dati dei file
        cursor.close()

        # Converte i dati binari in base64
        modified_data = []  # Lista per contenere i dati modificati
        for dati in file_data:
            if dati[2]:  # Assicurati che i dati esistano prima di codificarli
                # Converto la tupla in lista per poterla modificare
                dati_list = list(dati)
                try:
                    # Codifica in base64
                    dati_list[2] = base64.b64encode(dati_list[2]).decode('utf-8')  
                except Exception as e:
                    print(f"Errore nella codifica dell'immagine: {e}")
                    dati_list[2] = ""  # Imposta una stringa vuota se c'è un errore
                modified_data.append(tuple(dati_list))  # Aggiungi la tupla modificata
            else:
                modified_data.append(dati)  # Se non ci sono dati, aggiungi la tupla originale

        if request.method == 'POST':
            id = request.form['id']  # Ottieni l'id del file selezionato dal form
            delete_file = "DELETE FROM panell WHERE id = %s" 
            cursor = mysql.connection.cursor() 
            cursor.execute(delete_file, (id,))
            mysql.connection.commit() 
            cursor.close() 
            return redirect(url_for('file_read'))  # Dopo aver eliminato, ricarica la pagina
        
        return render_template('file.html', data=modified_data)  # Passa i dati modificati al template
    
    except Exception as e:
        return f"Errore: {e}"



       






	 













if __name__ == '__main__':
    app.run(debug=True)
