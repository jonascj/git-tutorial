################################
Introduktion til versionsstyring
################################


***************
Kode ændrer sig
***************

Udviklingen af et computerprogram er en iterativ proces 
hvor de samme handlinger gentages igen og igen:


1. Identificer et krav til programmet 
   (noget programmet skal kunne).

2. Implementer kravet 
   (skriv kode som får programmet til at kunne det det skal kunne).

3. Test implementeringen 
   (kan programmet afvikles/køres og opfylder det kravet?)

   a. Hvis kravet er opfyldt: 
      gå til 1. for at find et nyt krav

   b. Krav er **ikke** opfyldt: 
      gå til 1. for at tjekke din forståelse af kravet
      og til 2. for at ændre implementeringen.


.. _fig-space-shooter-scene:
.. figure:: figs/space-shooter-scene.png
   :align: center 
   :scale: 120%

   Skitse af brugerfladen til et arkadespil i stil med Galaga eller Space Invaders.

Tag udviklingen af et arkadespil som eksempel.
:numref:`Figur %s <fig-space-shooter-scene>` viser et skitse af brugerfladen 
til et arkadespil i stil med Galaga eller Space Invaders, kald det **Space Shooter**.
Figuren viser allerede mange krav til hvad spillet skal indeholde:

* Et rumskib som kan skyde med laser eller missiler.
* Grønne aliens. 
* Scoreboard som viser hvor mange aliens man har skudt ned.

En programmør som skal udvikle spillet 
(specielt en programmør uden stor erfaring inden for spiludvikling)
vil gøre klogt i (eller ligefrem være nødsaget til)
at implementere bud på kravene ét ad gangen
og bruge flere itrationer på hvert krav.
Første version af spillet kunne være et program
som tegner rumskibet i bunden af skærmbilledet, 
anden version kunne være et program hvor 
den rumskibet kan flyttes med piletasterne osv.
Hvis programmøren tidligere har prøvet at tegne billeder på skærmen 
og flytte dem baseret på keyboardinput,
kan første og anden version måske skrives i én iteration i stedet for to.

Det er fristende at finde alle krav og påbegynde arbejdet på dem samtidigt,
mange krav hænger trods alt sammen med andre krav. 
Håbet kunne være, at programmet kunne skrives en gang for alle,
startende med linje 1, efterfulgt af linje 2 osv.
indtil arbejdet afsluttes med en enkelt test 
som bekræfter at alt virker som det skal.

Men i praksis kan det aldrig [#top-down-praksis]_ lade sig gøre. 
I praksis misforstås krav, der laves tastefejl, 
der kommer nye krav til efter projektet er startet,
du har som programmør ikke erfaring nok til at forudsige 
den bedste struktur af koden osv.

I praksis ændrer kode sig derfor i løbet af udviklingsprocessen.

*********************
Versioner og historik
*********************

Hver gang koden til et program ændres
opstår der en ny version af programmet (og koden).
Ofte gemmes dog kun den seneste version koden.

En Python-programmør som er i gang med at udvikle arkadespillet Space Shooter
har meget muligt kun én enkelt fil kaldet ``spaceshooter.py``
som indeholder nyeste version af koden.
Hver gang koden ændres overskrives filen ``spaceshooter.py``
således den forrige version forsvinder
og ``spaceshooter.py`` igen indeholder nyeste version.

Der er imidlertid mange situationer hvor det ville være en fordel 
at have gemt tidligere versioner af koden.
Et forsøg på at implementere et krav kan gå galt
og koden komme i en tilstand
hvor programmet slet ikke er funktionelt. 
Hvis arbejdet har stået på i flere timer
er det usandsynligt koden i sin tidligere funktionelle form
kan tilbagekaldes vha. editorens fortryd-/undo-funktion.

Manuel duplering eller backup, en simpel form for versionskontrol,
ses undertiden som vist på :numref:`figur %s <fig-filebrowser-backup>`.
Hver gang programmet har nået en milepæl eller før et eksperiment påbegyndes
gemmes en kopi af koden i en fil med et nyt filnavn 
(da to filer typisk ikke kan have samme navn).

 
.. _fig-filebrowser-backup:
.. figure:: figs/filebrowser-backup.png
   :align: center

   Grafisk visning af 8 filer som udgør forskellige version af et program.

En sådan løsning er bedre end ingen løsning,
men der er åbenlyse svagheder ved løsningen:

1. Det er svært at se hvilken fil som indeholder nyeste version af koden
   (filnavn og evt. tid/dato for redigering kan dog give en indikation).

2. Det er svært at gennemskue hvorfor en given version af koden er gemt,
   kun filnavnet indeholder et hint om årsagen.
  
3. Løsningen kan udvides til at virke for projekter som består af flere filer,
   f.eks. et spil med lydeffekter, billeder/textures og kode,
   ved at en helt projektmappe kopieres,
   men det forværrer typisk 1. og 2.


Derfor findes mere forfinede/avancerede systemer til *versionsstyring*.

***************
Versionsstyring
***************

Systemer til **verionsstyring** (engelsk: version control) 
systematiserer processen med at gemme og annoterer 
versioner af kode og softwareprojekter.

:numref:`Figur %s <fig-version-control-showcase>` viser hvorledes forskellige versioner
af et projekt/program/kode kan vises når det versionsstyres:

.. _fig-version-control-showcase:
.. figure:: figs/version-control-showcase.png
    :align: center
 
    Forskellige versioner af et projekt versionsstyret med *git* [#git]_ 
    og visualiseret vha. Visual Studio Code [#vscode]_ 
    med udvidelsen Git Graph [#gitgraph]_.

* :figroilbl:`A` Ét blandt en række af såkaldte *commits* i projektet
  (snapshots eller versioner af projektet)
  som det så ud på forskellige tidspunkter.

  Bemærk beskrivelsen af hvert commit, f.eks. ``Add multiple Aliens (no collision detection)``,
  som gør det let at identificere hvorfor en ændring er lavet.
   

* :figroilbl:`B` Indikation af at commit :guilabel:`Add multiple aliens ... (b0c7504f)`
  bestod af ændringer til filen ``game.py`` 
  (14 linjer tilføjet, 7 linjer fjernet).


* :figroilbl:`C` Visualisering af ændringer som er sket i ``game.py`` fra
  forrige version (7d9e2192) til denne version (b0c7504f).

  Linjer overstreget med rød er blevet fjernet
  og linjer overstreget med grøn tilføjet,
  f.eks. er linje 94 `screen.blit(alien...` blevet erstattet af
  linje 100-101 som indeholder et for-loop.


.. admonition:: Fortsæt ...

    Fortsæt nu til afsnittet :doc:`/ch-setup/setup`.


.. rubric:: Fodnoter

.. [#top-down-praksis] Uanset erfaringsniveau (bortset fra nul erfaring)
     kan det selvfølgelig lade sig gøre for en programmør at
     skrive et tilpas simpelt program lineært,
     med kun én successfuld test til slut.

     En programmør med timers erfaring kunne meget muligt
     skrive et program som spørger om brugerens navn 
     og outputter ``Hej <navn>`` 
     med brugerens navn indsat i stedet for ``<navn>``, lineært.

     Men på et tidspunkt holder teknikken op med at virke,
     uanset erfaringsniveau. 
     

.. [#git] https://git-scm.com/

.. [#vscode] https://code.visualstudio.com/

.. [#gitgraph] https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph


