CREATE TABLE utenti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    cognome VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    codice_fiscale CHAR(16) NOT NULL UNIQUE,
    numero_telefono VARCHAR(15) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    data_registrazione TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE caricamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descrizione TEXT NOT NULL,
    file LONGBLOB NOT NULL
);