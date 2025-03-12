package com.example.demo;
import com.example.demo.model.Utente;
import com.example.demo.service.UtenteService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class MyController {

    @Autowired
    private UtenteService utenteService;

    // Visualizza il form per inserire dati
    @GetMapping("/")
    public String showForm(Model model) {
        model.addAttribute("utente", new Utente());
        return "index"; // Assicurati di avere un file index.html in src/main/resources/templates
    }

    // Visualizza la lista degli utenti
    @GetMapping("/utenti")
    public String showUtenti(Model model) {
        model.addAttribute("utenti", utenteService.getAllUtenti());
        return "utenti"; // Assicurati di avere un file utenti.html in src/main/resources/templates
    }



  
    // Aggiungi un nuovo utente
    @PostMapping("/add")
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
