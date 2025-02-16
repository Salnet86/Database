
import java.sql.*;
import java.util.ArrayList;

// Modello Commessa
class Commessa {
    String nome, cognome, dataNascita, codiceFiscale;
    int eta;

    public Commessa(String nome, String cognome, int eta, String dataNascita, String codiceFiscale) {
        this.nome = nome;
        this.cognome = cognome;
        this.eta = eta;
        this.dataNascita = dataNascita;
        this.codiceFiscale = codiceFiscale;
    }

    @Override
    public String toString() {
        return nome + " " + cognome + ", Età: " + eta + ", Data di nascita: " + dataNascita + ", CF: " + codiceFiscale;
    }
}

// Gestione del database
class DatabaseManager {
    private static final String URL = "jdbc:mysql://localhost:3306/tua_database";
    private static final String USER = "root";
    private static final String PASSWORD = "password";

    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }

    public static void inserisciCommessa(Commessa c) {
        String sql = "INSERT INTO commesse (nome, cognome, eta, data_nascita, codice_fiscale) VALUES (?, ?, ?, ?, ?)";
        try (Connection conn = getConnection(); PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, c.nome);
            stmt.setString(2, c.cognome);
            stmt.setInt(3, c.eta);
            stmt.setString(4, c.dataNascita);
            stmt.setString(5, c.codiceFiscale);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static ArrayList<Commessa> getListaCommesse() {
        ArrayList<Commessa> lista = new ArrayList<>();
        String sql = "SELECT * FROM commesse";
        try (Connection conn = getConnection(); Statement stmt = conn.createStatement(); ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                lista.add(new Commessa(
                    rs.getString("nome"),
                    rs.getString("cognome"),
                    rs.getInt("eta"),
                    rs.getString("data_nascita"),
                    rs.getString("codice_fiscale")
                ));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return lista;
    }
}

// Esecuzione
public class Main {
    public static void main(String[] args) {
        ArrayList<Commessa> commesse = new ArrayList<>();
        commesse.add(new Commessa("Maria", "Rossi", 28, "1996-03-15", "MRARSS96C55H501X"));
        commesse.add(new Commessa("Giulia", "Bianchi", 25, "1999-07-20", "GLABNC99L60H501Z"));
        commesse.add(new Commessa("Elena", "Verdi", 30, "1994-11-10", "ELVVRD94T50H501Y"));
        
        for (Commessa c : commesse) {
            DatabaseManager.inserisciCommessa(c);
        }
        
        ArrayList<Commessa> lista = DatabaseManager.getListaCommesse();
        for (Commessa c : lista) {
            System.out.println(c);
        }
    }
}
