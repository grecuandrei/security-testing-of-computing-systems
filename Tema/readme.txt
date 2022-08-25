---- TSSC Tema 1 ----

---- Task 1 ----

Prima data am descifrat hint-urile cu ajutorul lui rot7 si rot3

Buna gluma cu rick roll, dar stiam linkul deci nu v-a mers, avand
in vedere ca si eu fac asta altora xD

Am scos faptul ca se foloseste "RSA chosen chiper attack" si de
aici am inceput documentarea asupra algoritmului

Din puterea exemplului dat de voi, m-am gandit ca ar trb sa trimit
catre server sub forma unui json cu e, n si mesaj

Din message.txt mi-am dat seama de faptul ca ar trb sa fie encodat
in b64

Asa ca am decodat din b64 message.txt -> am luat msj, n si e =>
cipher_dash-ul conform formulei din algoritm

Am construit noul json de trimis catre server (cu cipher_dash-ul
encodat in base64 pt ca asa am observat si la flag-ul extras mai sus),

Am encodat json-ul, trimis la server, si salvat raspunsul

Raspunsul trebuia curatat cu decode unicode, l-am transformat
intr-un numar sa putem imparti la numarul random conform formulei si
am extras flagul transformandu-l inapoi in string

---- Task 2 ----

Am cautat initial hinturi, deci am dat comanda - find / -name '*hint*' -
si am dat un cat pe fisierul ascuns /var/.hints.txt

De la hintul cu hidden config am dat comanda - find / -perm -u=s -type f 2>/dev/null -
pt a cauta executabile sau configuri cu sticky bit

Am gasit exec-ul /usr/games/hunt/manele/th3bo55

Am dat un cat pe el, dar nu am aflat nimic

Am dat cu objdump pe el si am descoperit un strcmp in main pe la inceput

Am rulat exec-ul si nu mergea, si am zis sa ii dau un argument, dar nimic

Am dat ltrace pe exec (Try to ltrace the setuid binaries), si cu
si fara argument, si am observat ca atunci cand dau cu argument apare un strcmp

Am folosit al doilea argument al strcmp-ului ca argument si executabilul nu a mai dat Acces denied

In janitor_vacum.sh, vacum_control este rulat cu robot-sudo, robot-sudo care te face pe tine ownerul executabilului
(devi userul roombax care e in grupul bossel, acelasi grup cu userul bossel care are permisiuni de a rula execul)
si poti rula vacum_control ca ai permisiuni (euid > 7000)

Si deci am facut o copie la vacum_control ca nu pot sa il editez ca janitor si i-am adaugat inainte de echo Okay,
execul cu argumentul descoperit

Am modificat janitor_vacum.sh si am pus in schimb apelarea copiei vacum_control_cpy

Prin rularea ./janitor_vacum.sh am extras flagul

---- Task 3 ----

Am rulat de cateva ori pentru a observa comportamentul ./casino

Am utilizat Ghidra pentru a inspecta executabilul

Flow: main->loop-(posibil)->lose
                \
                 -(vrem)-> win

Am descoperit ca daca introduci numele Florin Salam, se afiseaza un easter egg cu un link =))

Am urmarit flow-ul si am descoperit ca in loop exista 3 variabile locale de 37, 3 si 1 in marime

Deci payloadul pana acum este "Florin Salam\n" + "1\n"*41 + "x\n" (x pt a termina scanf-ul)

Acum trb injectata functia de win pentru a reusi citirea flagului

Am pus adresa functiei win, insa nu am reusit sa trec de conditia
de verificare a numarului norocos, avand in vedere ca el se genereaza random la rulare

Asa ca am folosit adresa imediat urmatoare conditiei, si anume de la fopen 0x08048712 (in hex => in dec 134514450)

Deoarece am suprascris acele variabile locale prin primul scanf, al doilea necesita un input
si i se ofera un n pentru a incheia executia programului si a iesi cu succes (nu mai avem nevoie
de lucky number aflat pe else pt ca asa cum spuneam el este aleator la runtime si nu putem stii)

Comanda finala: python3 -c 'print("Florin Salam\n" + "1\n"*41 + "134514450\n" + "x\n" + "n\n")' | nc isc2022.1337.cx 10095

Pe local acest payload nu functioneaza, insa pe server se intoarce flagul corespunzator