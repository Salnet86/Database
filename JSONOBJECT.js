var count = 0;
var vector = [];

function aggiungi() {

  var Persona = {   // <-- creato ogni volta
    nome: 'maria',
    cognome: 'pozzato',
    eta: 34
  };

  var arra = new Array();

  count++;
  arra[count] = Persona;

  vector.push(arra[count]);

  for (var i = 0; i < vector.length; i++) {
    console.log(vector[i]);
  }
}
