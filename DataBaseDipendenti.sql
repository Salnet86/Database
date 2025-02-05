SELECT nome, cognome, età, , stipendio
FROM Dipendenti
WHERE età > 18;




SELECT MAX(stipendio) AS StipeMax
FROM Dipendenti
WHERE stipendio>= (SELECT MIN(stipendio) FROM Dipendenti);




CREATE DATABASE Dipen;


USE Dipen;


CREATE TABLE Dipendenti (
    id_dp INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(20),
    cognome VARCHAR(20),
    eta INT,
    stipendio DECIMAL(10, 2) -- Aggiungo il tipo di dato DECIMAL per il campo stipendio
);




INSERT INTO Dipendenti (nome, cognome, eta, stipendio)
VALUES 
('Maria', 'Bianchi', 28, 2300.00),
('Giulia', 'Verdi', 32, 2700.00),
('Francesca', 'Rossi', 25, 2100.00),
('Laura', 'Esposito', 40, 3000.00),
('Alessandra', 'Galli', 35, 2500.00),
('Silvia', 'Lombardi', 30, 2200.00),
('Elena', 'Martini', 29, 2400.00),
('Valentina', 'Ferrari', 33, 2600.00),
('Monica', 'Conti', 38, 2800.00),
('Anna', 'Ricci', 27, 2100.00),
('Giovanna', 'Pellegrini', 42, 2900.00),
('Paola', 'Gallo', 31, 2300.00),
('Irene', 'Martelli', 26, 2200.00),
('Marta', 'Barbieri', 34, 2700.00),
('Teresa', 'Giordano', 37, 2400.00),
('Caterina', 'Fontana', 28, 2600.00),

SELECT MAX(stipendio) AS StipeMax
FROM Dipendenti
WHERE stipendio >= (SELECT MIN(stipendio) FROM Dipendenti);




SELECT MAX(stipendio) AS StipeMax
FROM Dipendenti;


SELECT nome, eta, MAX(stipendio) AS StipeMax
FROM Dipendenti
WHERE nome = 'Maria' AND eta > 18 AND stipendio > (SELECT MIN(stipendio) FROM Dipendenti)
GROUP BY nome, eta;




SELECT nome, eta, MAX(stipendio) AS StipeMax
FROM Dipendenti
WHERE nome = 'Elisa' AND eta > 18 AND stipendio > (SELECT MIN(stipendio) FROM Dipendenti)
GROUP BY nome, eta;
