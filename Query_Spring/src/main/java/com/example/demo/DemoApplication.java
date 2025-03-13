package com.example.demo;


import org.springframework.beans.factory.annotation.Autowired;
import java.util.List;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication implements CommandLineRunner {


    @Autowired
    private LibroRepository libroRepository;

    @Autowired
    private UtenteRepository utenteRepository;

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }


 @Override
    public void run(String... args) throws Exception {
        // Esegui una query per ottenere i libri di un utente con un nome specifico
        List<Libro> libri = libroRepository.findLibriByUtenteNome("Anna");
        
        // Stampa i risultati
        for (Libro libro : libri) {
            System.out.println("Titolo: " + libro.getTitolo() + ", Utente: " + libro.getUtente().getNome());
        }
    }






   
}
