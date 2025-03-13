package com.example.demo;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import java.util.List;
public interface LibroRepository extends JpaRepository<Libro, Long> {

    @Query("SELECT l FROM Libro l JOIN FETCH l.utente WHERE l.utente.nome = :nome")
    List<Libro> findLibriByUtenteNome(@Param("nome") String nome);
}