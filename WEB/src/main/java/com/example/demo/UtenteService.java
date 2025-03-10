package com.example.demo.service;

import com.example.demo.model.Utente;
import com.example.demo.repository.UtenteRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UtenteService {

    @Autowired
    private UtenteRepository utenteRepository;

    public List<Utente> getAllUtenti() {
        return utenteRepository.findAll();
    }

    public void aggiungiUtente(Utente utente) {
        utenteRepository.save(utente);
    }

    public void cancellaUtente(Long id) {
        utenteRepository.deleteById(id);
    }
}
