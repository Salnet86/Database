package com.example;
import com.example.model.User;
import org.hibernate.Session;
import org.hibernate.Transaction;
import com.example.util.HibernateUtil;
import java.util.Scanner;
import org.hibernate.query.Query;  // Import per Hibernate Query
import java.util.List;             // Import per la lista di risultati

public class App 
{
    public static void main( String[] args ) 

        /*

       Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction transaction = null;

        try {
            transaction = session.beginTransaction();

            // Comando ALTER TABLE per aggiungere una colonna
            String sql = "ALTER TABLE User ADD COLUMN telefono VARCHAR(20)";
            session.createSQLQuery(sql).executeUpdate();  // Esegui il comando SQL

            transaction.commit();
            System.out.println("Colonna 'status' aggiunta con successo!");

        } catch (Exception e) {
            if (transaction != null) {
                transaction.rollback();  // Annulla la transazione in caso di errore
            }
            e.printStackTrace();
        } finally {
            session.close();
        }
   */

















     
        /*

       //Query delete
       // Avvia la sessione
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction transaction = null;

        try {
            // Inizia la transazione
            transaction = session.beginTransaction();
            
            // ID dell'utente da eliminare
            Long userIdToDelete = 1L; // Cambia con l'ID dell'utente da eliminare
            
            // Recupera l'utente
            User userToDelete = session.get(User.class, userIdToDelete);
            
            if (userToDelete != null) {
                // Elimina l'utente
                session.delete(userToDelete);
                System.out.println("Utente con ID " + userIdToDelete + " eliminato con successo.");
            } else {
                System.out.println("Utente con ID " + userIdToDelete + " non trovato.");
            }
            
            // Commit della transazione
            transaction.commit();
        } catch (Exception e) {
            if (transaction != null) {
                transaction.rollback(); // Annulla se c'è un errore
            }
            e.printStackTrace();
        } finally {
            session.close(); // Chiudi la sessione
        }

       */




















       /*
       //Query update 
       // Aprire una sessione
        Session session = HibernateUtil.getSessionFactory().openSession();

        // Creare una transazione
        Transaction transaction = session.beginTransaction();

        // Recuperare un utente tramite l'ID
        Long userId = 1L;   // Sostituisci con l'ID dell'utente che vuoi aggiornare
        User user = session.get(User.class, userId);
        
        if (user != null) {
            // Modificare il campo name dell'utente
            user.setName("Salvatore");

            // Hibernate aggiornerà automaticamente l'entità quando committi la transazione
            session.update(user);
            System.out.println("Utente aggiornato!");
        } else {
            System.out.println("Utente non trovato!");
        }

        // Completare la transazione
        transaction.commit();
        session.close();
        */





        /*

        //Query due
        Session session = HibernateUtil.getSessionFactory().openSession();

        // Creare una transazione
        Transaction transaction = session.beginTransaction();

        // Eseguire una query HQL per ottenere solo il nome degli utenti
        String hql = "SELECT u.name FROM User u";
        Query<String> query = session.createQuery(hql, String.class);
        List<String> userNames = query.list();

        // Visualizzare i risultati
        for (String userName : userNames) {
            System.out.println(userName);
        }

       */










      /*

       //Query una
       Session session = HibernateUtil.getSessionFactory().openSession();
        
        // Iniziare la transazione
        session.beginTransaction();

        // HQL: Seleziona tutti gli utenti
        String hql = "FROM User"; // Equivale a "SELECT * FROM User"
        Query<User> query = session.createQuery(hql, User.class);
        List<User> users = query.list();

        // Stampa gli utenti
        for (User user : users) {
           System.out.println(user.getName() + " - " + user.getEmail());

        }

        // Completare la transazione
        session.getTransaction().commit();
        session.close();
        */



          /*
        
         // Ottieni input dall'utente
        Scanner scanner = new Scanner(System.in);
        System.out.print("Inserisci il nome dell'utente: ");
        String name = scanner.nextLine();  // Legge il nome inserito
        System.out.print("Inserisci l'email dell'utente: ");
        String email = scanner.nextLine();  // Legge l'email inserita

        // Aprire una sessione
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction transaction = session.beginTransaction();

        // Creare un utente con i dati inseriti dall'utente
        User user = new User(name, email);
        session.save(user);

        // Completare la transazione
        transaction.commit();
        session.close();

        System.out.println("Utente salvato con successo!");
        HibernateUtil.shutdown();

        scanner.close(); // Chiudi lo scanner per evitare perdite di risorse




        
    

        // Aprire una sessione
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction transaction = session.beginTransaction();

        // Creare un utente
       // User user = new User("Salvo", "salvo@example.com");
        User donna = new User("Maria", "maria@example.com");
        session.save(donna);

        // Completare la transazione
        transaction.commit();
        session.close();

        System.out.println("Utente salvato con successo!");
        HibernateUtil.shutdown();
    */

    }
}
