CREATE DATABASE Supermercato;


USE Supermercato;


CREATE TABLE utente (
  cod_fisc CHAR(16) NOT NULL, -- Codice fiscale, che dovrebbe essere un identificatore unico
  nome VARCHAR(20) NOT NULL, -- Nome dell'utente
  cognome VARCHAR(20) NOT NULL, -- Cognome dell'utente
  eta INT NOT NULL, -- Età dell'utente
  data_nascita DATE, -- Data di nascita dell'utente
  N_Carta_edentita VARCHAR(30) NOT NULL, -- Numero della carta d'identità
  email VARCHAR(50) NOT NULL, -- Indirizzo email dell'utente
  telefono VARCHAR(20), -- Numero di telefono dell'utente
  PRIMARY KEY (cod_fisc) -- Definisce cod_fisc come chiave primaria
);


CREATE TABLE ordini (
  id_prodotto INT NOT NULL AUTO_INCREMENT, -- ID prodotto, auto-incrementato
  tipo_prodotto VARCHAR(20) NOT NULL, -- Tipo del prodotto
  prezzo DECIMAL(10, 2) NOT NULL, -- Prezzo del prodotto con 2 decimali
  cod_fisc CHAR(16) NOT NULL, -- Codice fiscale dell'utente
  PRIMARY KEY (id_prodotto), -- Imposta id_prodotto come chiave primaria
  FOREIGN KEY (cod_fisc) REFERENCES utente(cod_fisc) -- Chiave esterna che fa riferimento alla tabella 'utente'
);








INSERT INTO utente (cod_fisc, nome, cognome, eta, data_nascita, N_Carta_edentita, email, telefono)
VALUES
('RSSMRA85M01H501Z', 'Maria', 'Rossi', 30, '1994-05-01', '123456789012345', 'maria.rossi@email.com', '3331234567'),
('BNCLSN95S60H501Y', 'Sofia', 'Bianchi', 25, '1999-03-15', '987654321098765', 'sofia.bianchi@email.com', '3332345678'),
('MZZNDR87S50A123B', 'Ana', 'Mendez', 28, '1996-11-07', '567890123456789', 'ana.mendez@email.com', '3333456789'),
('LDNSRA85M01D501P', 'Lina', 'De Luca', 35, '1989-07-21', '123456789012346', 'lina.deluca@email.com', '3334567890'),
('SMNGRG92C50H501F', 'Ines', 'Garcia', 22, '2002-12-05', '234567890123457', 'ines.garcia@email.com', '3335678901'),
('LOPFRN80R50B123S', 'Francesca', 'Loppi', 33, '1991-06-30', '345678901234568', 'francesca.loppi@email.com', '3336789012');




INSERT INTO ordini (tipo_prodotto, prezzo, cod_fisc)
VALUES
('Pane', 1.50, 'RSSMRA85M01H501Z'),
('Latte', 1.00, 'BNCLSN95S60H501Y'),
('Pasta', 2.00, 'MZZNDR87S50A123B'),
('Pomodoro', 1.80, 'LDNSRA85M01D501P'),
('Olio', 3.50, 'SMNGRG92C50H501F'),
('Riso', 2.40, 'LOPFRN80R50B123S'),
('Caffè', 4.00, 'RSSMRA85M01H501Z'),
('Zucchero', 1.20, 'BNCLSN95S60H501Y'),
('Sale', 0.90, 'MZZNDR87S50A123B'),
('Frutta', 5.00, 'LDNSRA85M01D501P');





INSERT INTO utente (cod_fisc, nome, cognome, eta, data_nascita, N_Carta_edentita, email, telefono)
VALUES
('RSSMRA85M01H501Z', 'Maria', 'Rossi', 30, '1994-05-01', '123456789012345', 'maria.rossi@email.com', '3331234567'),
('BNCLSN95S60H501Y', 'Sofia', 'Bianchi', 25, '1999-03-15', '987654321098765', 'sofia.bianchi@email.com', '3332345678'),
('MZZNDR87S50A123B', 'Ana', 'Mendez', 28, '1996-11-07', '567890123456789', 'ana.mendez@email.com', '3333456789'),
('LDNSRA85M01D501P', 'Lina', 'De Luca', 35, '1989-07-21', '123456789012346', 'lina.deluca@email.com', '3334567890'),
('SMNGRG92C50H501F', 'Ines', 'Garcia', 22, '2002-12-05', '234567890123457', 'ines.garcia@email.com', '3335678901'),
('LOPFRN80R50B123S', 'Francesca', 'Loppi', 33, '1991-06-30', '345678901234568', 'francesca.loppi@email.com', '3336789012'),
('MRTLCT90R50B123X', 'Martina', 'Lombardi', 27, '1997-08-12', '456789012345679', 'martina.lombardi@email.com', '3337890123'),
('ZNRVNC88F50D501T', 'Giulia', 'Vincenzi', 24, '2000-09-10', '567890123456780', 'giulia.vincenzi@email.com', '3338901234'),
('PNMSRT83D55L123K', 'Elena', 'Martini', 32, '1992-11-22', '678901234567891', 'elena.martini@email.com', '3339012345'),
('FNNLDN85B12A123J', 'Chiara', 'Fornari', 26, '1998-04-04', '789012345678902', 'chiara.fornari@email.com', '3330123456'),
('SMNDRN90F10L123A', 'Sara', 'Andrei', 29, '1995-01-15', '890123456789013', 'sara.andrei@email.com', '3332346789'),
('TSPFNS92G50P123B', 'Valentina', 'Tosi', 31, '1993-02-02', '901234567890124', 'valentina.tosi@email.com', '3333457890'),
('PNTMNN93S50A123C', 'Alessandra', 'Pinto', 30, '1994-07-25', '012345678901235', 'alessandra.pinto@email.com', '3334568901'),
('ZNSRLL90F60B123D', 'Gabriella', 'Neri', 33, '1991-03-14', '123456789012347', 'gabriella.neri@email.com', '3335679012');





