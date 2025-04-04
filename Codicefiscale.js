function Codice(){
var vocali=0;
var consonanti=0;
var contatore=0;
var Vocali=new Array(50);
var Consonati=new Array(50);
var co_cognome=new Array(50);
var x=new Array(3);
var cognome=document.getElementById("cognome").value.toUpperCase();
var nome=document.getElementById("nome").value.toUpperCase();

var data=document.getElementById("d1").value;
var data=new Date(data);

  var dd = data.getDate(); 
        var mm = data.getMonth() + 1; 
  
        var yyyy = data.getFullYear(); 
        if (dd < 10) { 
            dd = '0' + dd; 
        } 
        if (mm < 10) { 
            mm = '0' + mm; 
        } 
        var data = dd + '/' + mm + '/' + yyyy; 
		
		 mese = data.substring(4, 5);
       anno = data.substring(8, 10);
       giorno = data.substring(0, 2);
   
var sesso= document.getElementById("mySelect").value;
 //var sesso="m";
var mese;
var anno;
var k=0;
var codice_fiscale=" ";
// controllo consonanti e vocali per cognome
for ( var i = 0; i < cognome.length; i++) {
if (contatore == 3)
break;
if (cognome.charAt(i) != 'A' && cognome.charAt(i) !=
'E'
&& cognome.charAt(i) != 'I' &&
cognome.charAt(i) != 'O'
&& cognome.charAt(i) != 'U') {
co_cognome[k] = cognome.charAt(i);
//console.log(co_cognome[k]);
codice_fiscale += co_cognome[k];
contatore++;
k++;
}
}
for (var j = 0; j< cognome.length; j++) {
if (contatore == 3)
break;
if (cognome.charAt(i) == 'A' || cognome.charAt(i) == 'E'
|| cognome.charAt(i) == 'I' || cognome.charAt(i)
== 'O'
|| cognome.charAt(i) == 'U') {
co_cognome[k] = cognome.charAt(i);
codice_fiscale += co_cognome[k];
contatore++;
k++;
}}
if (contatore != 3) {
while (contatore != 3) {
co_cognome[k] = 'X';
codice_fiscale+= co_cognome[k];
contatore++;
k++;
}
}
//controllo consonanti e vocali per nome
for (var i1 = 0; i1 < nome.length; i1++) {
if (nome.charAt(i1) != 'A' && nome.charAt(i1) != 'E'
&& nome.charAt(i1) != 'I' &&
nome.charAt(i1) != 'O'
&& nome.charAt(i1) != 'U') {
Consonati[j] = nome.charAt(i1);
consonanti++;
j++;
}
}
for (var i = 0; i < nome.length; i++) {
if (nome.charAt(i) == 'A' || nome.charAt(i) == 'E'
|| nome.charAt(i) == 'I' || nome.charAt(i) == 'O'
|| nome.charAt(i) == 'U') {
Vocali[j] = nome.charAt(i);
vocali++;
j++;
}
}
if (consonanti > 3) {
codice_fiscale+=Consonati[0];
codice_fiscale+=Consonati[2];
codice_fiscale+=Consonati[3];
}else if (consonanti == 3) {
codice_fiscale+=Consonati[0];
codice_fiscale+=Consonati[1];
codice_fiscale+=Consonati[2];
}else if (consonanti == 2 && vocali > 0) {
codice_fiscale+=Consonati[0];
codice_fiscale+=Consonati[1];
codice_fiscale+=Vocali[2];
} else if (consonanti == 1 && vocali > 1) {
codice_fiscale+=Consonati[1];
codice_fiscale+=Vocali[1];
codice_fiscale+=Vocali[2];
} else if (consonanti == 1 && vocali == 1) {
codice_fiscale+=Consonati[0];
codice_fiscale+=Vocali[1];
x[0] = 'X';
codice_fiscale+=x[0];
} else if (consonanti == 0 && vocali == 2) {
codice_fiscale+=Vocali[0];
codice_fiscale+=Vocali[1];
x[1] = 'X';
codice_fiscale+=x[1];
}
//anno di nascita
// anno di nascita prendo le utime cifre esempio 1986 uguale 86

for (var i = 0; i < data.length; i++) {
anno = data.substring(8, 10);
}
// trasformo in carrateri anno di nascita
for (var j = 0; j < anno.length; j++) {
codice_fiscale+=anno.charAt(j);
}

// codice controllo mese di nascita
switch (parseInt(mese)) {
case 1: {
ANN = 'A';
codice_fiscale+=ANN;
break;
} case 2: {
ANN = 'B';
codice_fiscale+=ANN;
break;
} case 3: {
ANN = 'C';
codice_fiscale+=ANN;
break;
} case 4: {
ANN = 'D';
codice_fiscale+=ANN;
break;
} case 5: {
ANN = 'E';
codice_fiscale+=ANN;
break;
} case 6: {
ANN = 'H';
codice_fiscale+=ANN;
break;
} case 7: {
ANN = 'L';
console.log(ANN);
break;
} case 8: {
ANN = 'M';
codice_fiscale+=ANN;
break;
} case 9: {
ANN = 'P';
codice_fiscale+=ANN;
break;
} case 10: {
ANN = 'R';
codice_fiscale+=ANN;
break;
} case 11: {
ANN = 'S';
codice_fiscale+=ANN;
break;
} case 12: {
ANN = 'T';
codice_fiscale+=ANN;
break;
}}
//giorno di nascita se uomo metto solo il giorno se donna sommo piu 40

var gg = parseInt(giorno);
var Giono = "" + gg;
if (sesso=="m") {
Giono = "0" + Giono;
//trsformo in carrateri GIO_UOMO
for (var i = 0; i < Giono.length; i++) {
GIO_UOMO = Giono.charAt(i);
codice_fiscale+=GIO_UOMO;
}
} else if (sesso=="f") {
gg = gg + 40;
GIO_DONNA = ""+gg+"";
//trsformo in carrateri GIO_DONNA
for(var i=0;i<GIO_DONNA.length;i++){
codice_fiscale+=GIO_DONNA.charAt(i);
}}
//codice controllo catastale comune
var comune=document.getElementById("catastale").value;
//var comune = "L219";
if (comune==comune) {
for (var i = 0; i < comune.length; i++) {
codice_fiscale+=comune.charAt(i);
}
}
 

//codice controllo sommo valori pari
				
				 var sommaPari1=0;
			        for (var i=0;i<codice_fiscale.length;i+=1) {
				    if(i%2==0)
			        switch (codice_fiscale.charAt(i)) {
			        case '0': {sommaPari1+=0;break;}
			        case '1': {sommaPari1+=1;break;}
			        case '2': {sommaPari1+=2;break;}
			        case '3': {sommaPari1+=3;break;}
			        case '4': {sommaPari1+=4;break;}
			        case '5': {sommaPari1+=5;break;}
			        case '6': {sommaPari1+=6;break;}
			        case '7': {sommaPari1+=7;break;}
			        case '8': {sommaPari1+=8;break;}
			        case '9': {sommaPari1+=9;break;}
			        case 'A': {sommaPari1+=0;break;}
			        case 'B': {sommaPari1+=1;break;}
			        case 'C': {sommaPari1+=2;break;}
			        case 'D': {sommaPari1+=3;break;}
			        case 'E': {sommaPari1+=4;break;}
			        case 'F': {sommaPari1+=5;break;}
			        case 'G': {sommaPari1+=6;break;}
			        case 'H': {sommaPari1+=7;break;}
			        case 'I': {sommaPari1+=8;break;}
			        case 'J': {sommaPari1+=9;break;}
			        case 'K': {sommaPari1+=10;break;}
			        case 'L': {sommaPari1+=11;break;}
			        case 'M': {sommaPari1+=12;break;}
			        case 'N': {sommaPari1+=13;break;}
			        case 'O': {sommaPari1+=14;break;}
			        case 'P': {sommaPari1+=15;break;}
			        case 'Q': {sommaPari1+=16;break;}
			        case 'R': {sommaPari1+=17;break;}
			        case 'S': {sommaPari1+=18;break;}
			        case 'T': {sommaPari1+=19;break;}
			        case 'U': {sommaPari1+=20;break;}
			        case 'V': {sommaPari1+=21;break;}
			        case 'W': {sommaPari1+=22;break;}
			        case 'X': {sommaPari1+=23;break;}
			        case 'Y': {sommaPari1+=24;break;}
			        case 'Z': {sommaPari1+=25;break;}
			        }
			        }


 
			      //codice controllo sommo valori dispari
			        
			        var sommaDispari=0;
			        for (var i=0;i<=codice_fiscale.length;i+=1) {
					if(i%2==1)	
			        switch (codice_fiscale.charAt(i)) {
			        case '0': {sommaDispari+=1;break;}
			        case '1': {sommaDispari+=0;break;}
			        case '2': {sommaDispari+=5;break;}
			        case '3': {sommaDispari+=7;break;}
			        case '4': {sommaDispari+=9;break;}
			        case '5': {sommaDispari+=13;break;}
			        case '6': {sommaDispari+=15;break;}
			        case '7': {sommaDispari+=17;break;}
			        case '8': {sommaDispari+=19;break;}
			        case '9': {sommaDispari+=21;break;}
			        case 'A': {sommaDispari+=1;break;}
			        case 'B': {sommaDispari+=0;break;}
			        case 'C': {sommaDispari+=5;break;}
			        case 'D': {sommaDispari+=7;break;}
			        case 'E': {sommaDispari+=9;break;}
			        case 'F': {sommaDispari+=13;break;}
			        case 'G': {sommaDispari+=15;break;}
			        case 'H': {sommaDispari+=17;break;}
			        case 'I': {sommaDispari+=19;break;}
			        case 'J': {sommaDispari+=21;break;}
			        case 'K': {sommaDispari+=2;break;}
			        case 'L': {sommaDispari+=4;break;}
			        case 'M': {sommaDispari+=18;break;}
			        case 'N': {sommaDispari+=20;break;}
			        case 'O': {sommaDispari+=11;break;}
			        case 'P': {sommaDispari+=3;break;}
			        case 'Q': {sommaDispari+=6;break;}
			        case 'R': {sommaDispari+=8;break;}
			        case 'S': {sommaDispari+=12;break;}
			        case 'T': {sommaDispari+=14;break;}
			        case 'U': {sommaDispari+=16;break;}
			        case 'V': {sommaDispari+=10;break;}
			        case 'W': {sommaDispari+=22;break;}
			        case 'X': {sommaDispari+=25;break;}
			        case 'Y': {sommaDispari+=24;break;}
			        case 'Z': {sommaDispari+=23;break;}
			        }
			        }     

                    var somma = sommaPari1+sommaDispari;;
			       
			        //codice controllo ultimo carratere somma%26
			        switch (somma%26) {
			    	case 0:{controllo='A';break;}
			    	case 1:{controllo='B';break;}
			    	case 2:{controllo='C';break;}
			    	case 3:{controllo='D';break;}
			    	case 4:{controllo='E';break;}
			    	case 5:{controllo='F';break;}
			    	case 6:{controllo='G';break;}
			    	case 7:{controllo='H';break;}
			    	case 8:{controllo='I';break;}
			    	case 9:{controllo='J';break;}
			    	case 10:{controllo='K';break;}
			    	case 11:{controllo='L';break;}
			    	case 12:{controllo='M';break;}
			    	case 13:{controllo='N';break;}
			    	case 14:{controllo='O';break;}
			    	case 15:{controllo='P';break;}
			    	case 16:{controllo='Q';break;}
			    	case 17:{controllo='R';break;}
			    	case 18:{controllo='S';break;}
			    	case 19:{controllo='T';break;}
			    	case 20:{controllo='U';break;}
			    	case 21:{controllo='V';break;}
			    	case 22:{controllo='W';break;}
			    	case 23:{controllo='X';break;}
			    	case 24:{controllo='Y';break;}
			    	case 25:{controllo='Z';break;}
			    	}

                   codice_fiscale+=controllo;
				   
   var txt=document.getElementById("codice");

for (var i= 0; i < codice_fiscale.length; i++) {

txt.innerHTML += codice_fiscale.charAt(i); 
}

}
function invia(){
Codice();
}