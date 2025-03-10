package com.example.demo.controller;

import com.example.demo.model.Utente;
import com.example.demo.service.UtenteService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class UtenteController {

    @Autowired
    private UtenteService utenteService;

    // Visualizza il form per inserire dati
    @GetMapping("/")
    public String showForm(Model model) {
        model.addAttribute("utente", new Utente());
        return "index";
    }

    // Visualizza la lista degli utenti
    @GetMapping("/utenti")
    public String showUtenti(Model model) {
        model.addAttribute("utenti", utenteService.getAllUtenti());
        return "utenti";
    }

    // Aggiungi un nuovo utente
    @PostMapping("/do")
    public String addUtente(@ModelAttribute Utente utente) {
        utenteService.aggiungiUtente(utente);
        return "redirect:/utenti";
    }

    // Cancella un utente
    @PostMapping("/delete")
    public String deleteUtente(@RequestParam("id") Long id) {
        utenteService.cancellaUtente(id);
        return "redirect:/utenti";
    }
}
