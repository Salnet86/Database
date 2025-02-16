import sqlite3
from datetime import datetime

# Funzione per connettersi al database
def connessione_db():
    return sqlite3.connect('condominio.db')

# Creazione delle tabelle (se non esistono)
def crea_tabelle():
    conn = connessione_db()
    cursor = conn.cursor()

    # Creazione tabella ammiratori
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ammiratori (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cognome TEXT NOT NULL,
        tipo_lavoro TEXT,
        tasse_pagate REAL,
        assemblea_data_ora TEXT
    )''')

    # Creazione tabella utenti
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS utenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cognome TEXT NOT NULL,
        codice_fiscale TEXT NOT NULL,
        numero_telefono TEXT,
        email TEXT
    )''')

    conn.commit()
    conn.close()

# Funzione per inserire un ammiratore
def inserisci_ammiratore():
    nome = input("Nome ammiratore: ")
    cognome = input("Cognome ammiratore: ")
    tipo_lavoro = input("Tipo di lavoro: ")
    tasse_pagate = float(input("Tasse pagate: "))
    assemblea_data_ora = input("Data e ora assemblea (YYYY-MM-DD HH:MM:SS): ")

    conn = connessione_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO ammiratori (nome, cognome, tipo_lavoro, tasse_pagate, assemblea_data_ora)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, cognome, tipo_lavoro, tasse_pagate, assemblea_data_ora))
    conn.commit()
    conn.close()
    print("Ammiratore inserito con successo.")

# Funzione per inserire un utente
def inserisci_utente():
    nome = input("Nome utente: ")
    cognome = input("Cognome utente: ")
    codice_fiscale = input("Codice fiscale: ")
    numero_telefono = input("Numero di telefono: ")
    email = input("Email: ")

    conn = connessione_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO utenti (nome, cognome, codice_fiscale, numero_telefono, email)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, cognome, codice_fiscale, numero_telefono, email))
    conn.commit()
    conn.close()
    print("Utente inserito con successo.")

# Funzione per visualizzare gli ammiratori
def visualizza_ammiratori():
    conn = connessione_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ammiratori')
    ammiratori = cursor.fetchall()
    if ammiratori:
        for ammiratore in ammiratori:
            print(ammiratore)
    else:
        print("Nessun ammiratore trovato.")
    conn.close()

# Funzione per visualizzare gli utenti
def visualizza_utenti():
    conn = connessione_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM utenti')
    utenti = cursor.fetchall()
    if utenti:
        for utente in utenti:
            print(utente)
    else:
        print("Nessun utente trovato.")
    conn.close()

# Menu per l'interfaccia utente
def menu():
    while True:
        print("\nGestione Condominio")
        print("1. Inserisci un ammiratore")
        print("2. Inserisci un utente")
        print("3. Visualizza ammiratori")
        print("4. Visualizza utenti")
        print("5. Esci")
        
        scelta = input("Scegli un'opzione: ")
        
        if scelta == "1":
            inserisci_ammiratore()
        elif scelta == "2":
            inserisci_utente()
        elif scelta == "3":
            visualizza_ammiratori()
        elif scelta == "4":
            visualizza_utenti()
        elif scelta == "5":
            print("Uscita...")
            break
        else:
            print("Opzione non valida.")

# Esecuzione principale
def main():
    crea_tabelle()
    menu()

if __name__ == "__main__":
    main()
