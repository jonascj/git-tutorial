#################
Grundlæggende Git
#################

************
Repositories
************

Et Git-\ **repository** er en mappe i et filsystem, f.eks. på din harddisk, 
som indeholder et projekts filer
og som er under versionsstyring af Git.
Det letteste sted at møde repositories for første gang er https://github.com:

Repositores på GitHub
=====================

Åbn https://github.com/jonascj/space-shooter-python-git i en webbrowser.

Websiden viser det repository som vil blive brugt i denne tutorial.
Repository'et som kaldes *jonascj/space-shooter-python-git*
og det indeholder kode og andre filer som udgør spillet.

.. figure:: figs/github-space-shooter.png
    :align: center
    :class: with-border

    GitHubs visning af et repository.


.. admonition:: Aktivitet
    
    Udforsk repository'et på GitHub.
    Du kan trygt navigere rundt på siden, 
    du har kun læseadgang til repository'et og kan ikke ændre noget.


Fork et repository 
==================

For at videreudvikle på projektet repræsenteret ved  repository'et 
`github.com/jonascj/space-shooter-python-git
<https://github.com/jonascj/space-shooter-python-git>`_
vha. både Git og GitHub laves en såkaldt **fork** af repository'et.
En fork er en kopi af et repository som ejes af din GitHub-bruger.

#. Vælg :guilabel:`Create a new fork`  

   .. figure:: figs/github-fork.png
       :align: center
       :class: with-border

#. Navn og beskrivelse af repositoriet kan ændres hvis det ønskes.

   Opret din fork ved at klikke :guilabel:`Create fork`.

   .. figure:: figs/github-fork-create.png
       :align: center
       :class: with-border


Din nyligt oprettede fork er et nyt Git-repository (hosted af GitHub)
som kaldes **<username>/space-shooter-python-git**,
hvor `<username>` er dit GitHub-brugernavn.



Klon et repository
==================

At skaffe en lokal kopi af et repository, 
som du kan arbejde på fra en given computer,
kaldes at **klone** et repository (engelsk: **clone** a repository).

#. Kopier URL'en til dit repository fra browserens adressebar:

   .. figure:: figs/github-repo-url.png
       :align: center
       :class: with-border

#. Klon repository'et fra VS Code: 

   * Vælg :guilabel:`Source Ctrl` :figroilbl:`1` eller tryk :kbd:`Ctrl+Shift+G`
     (macOS: :kbd:`Cmd+Shift+G`).
   
   * Vælg :guilabel:`Clone Repository` :figroilbl:`2` .
   
   * Indtast URL'en til dit repository :figroilbl:`3` og afslut med :kbd:`Enter`.

   .. figure:: figs/vscode-clone-github-repo.png
      :align: center

#. Vælg en mappe / placering hvor du ønsker din klon af repository'et placeret.

   Hvis du vælger en mappe kaldet ``projects`` 
   vil der under den mappe blive lavet en mappe med navnet på repository'et:
   ``projects/space-shooter-python-git``.

   .. figure:: figs/vscode-clone-select-repo-location.png
      :align: center

#. Vælg :guilabel:`Open` når du bliver spurgt om du ønsker at åbne 
   det netop klonede repository.

   .. figure:: figs/vscode-clone-open-cloned-repo.png
      :align: center

#. VS Code spørger om du stoler ophavsmanden til filerne i den mappe som åbnes.
   VS Code kan nemlig eksekvere programmer fra mappen automatisk,
   hvilket kan være uheldigt/farligt hvis mappen indeholder ondsindet kode.

   I dette tilfælde kan du stole på indholdet af Space Shooter-projektet.
   Vælg derfor :guilabel:`Yes, I trust the authors`.

   .. figure:: figs/vscode-open-trust-author.png
      :align: center

#. Filerne som udgør Space Shooter-projektet, 
   og som hører til Git-repository'et,
   kan nu ses i din computers filsystem:

   .. _fig-filebrowser-repo-working-tree:
   .. figure:: figs/filebrowser-repo-working-tree.png
      :align: center

      Grafisk visning af filerne som verstionsstyres i repository'et.

   * :figroilbl:`A` Mappen med samme navn som repository'et 
     ``space-shooter-python-git``
     kan nu ses i mappen, som blev valgt som placering til klonen.

   * :figroilbl:`B` Skjult mappe med navn ``.git``
     som indeholder al information om repository'et.
     Slettes denne mappe er mappen ``projects/space-shooters-python-git``
     ikke længere et Git-repository.
   
   Mappen og alle filer under den (bortset fra ``.git``-mappen)
   kaldes repository'ets **working tree**\ :footcite:p:`git-scm-glossary`.

   .. admonition:: Aktivitet
      
      Undersøg filerne som udgør projektet i dit operativsystems filbrowser.


Projektet i VS Code
===================

Filerne fra :numref:`figur %s <fig-filebrowser-repo-working-tree>`,
kan også ses i VS Code og programmet/spillet kan også eksekveres fra VS Code.
Det var hele pointen med at forke og klone:
at blive i stand til at arbejde på koden!

* Vælg :guilabel:`Explorer` :figroilbl:`1` eller tryk :kbd:`Ctrl+Shift+E`
  (macOS: :kbd:`Cmd+Shift+E`).

* Åbn filen ``game.py`` :figroilbl:`2` ved at klikke på den i EXPLORER-panelet.

* Kør programmet ved at klikke på play-knappen i øverste højre hjørne :figroilbl:`3`. 

.. figure:: figs/vscode-file-explorer.png
   :align: center


Spillet skulle gerne starte og se således ud:

.. figure:: figs/space-shooter-showcase.png
   :align: center
   :scale: 50%

.. admonition:: Fejlsøgning

   * Hvis spillet ikke starter (men en fejl vises i VS Codes indbyggede terminal) 
     kan det skyldes *pygame* modulet ikke er installeret.

     Se installationsinstruktionen her: :ref:`sec-pygame-install`.
 
   * Hvis play-knappen :figroilbl:`3` mangler i øverste højre hjørne
     kan det skyldes en eller flere VS Code Extensions mangler at blive installeret.

     Se installationsinstruktionen her: :ref:`sec-vscode-extensions`.

   
************************
Ændringer i kode/projekt
************************

Git kan detektere ændringer i projektets filer 
og visualisere dem for programmøren. 
Hvis ændringerne er uønskede kan Git også kassere ændringerne
(engelsk: discard changes).
Det vigtigt at kunne orientere sig om ændringer til projektet
og det er nyttigt at kunne kassere uønskede ændringerne 
(f.eks. resultatet af et uheld eller et kort, fejlslagent eksperiment).

Vi vil nu lave en ændring til koden i ``game.py``
for at se hvordan Git viser disse ændringer
og vi vil bede Git kassere ændringerne igen.


#. Slet ``()`` fra ``pg.time.Clock()`` i linje 9 :figroilbl:`1`
   og gem filen med :kbd:`Ctrl+S` (macOS: :kbd:`Cmd+S`).

   .. figure:: figs/vscode-explorer-modified-error.png
      :align: center

Når programmet nu køres vha. play-knappen :figroilbl:`2`
fejler programmet med en ``AttributeError`` fra linje 179 :figroilbl:`A`.

VS Code og Git gør opmærksom på ``game.py`` er ændret
i forhold til sidste *commit* (snapshot af projektet)
med et :guilabel:`M` ud for filnavnet :figroilbl:`B`. 
I alt én fil er ændret, indikeret med :guilabel:`1` :figroilbl:`C`.

Hvis ændringen var lavet ved et uheld
kunne man selvfølgelig finde frem til linje 9 ud fra fejlmeddelelsen,
men det er hurtigere at bede Git kassere ændringen.


Status og diff
==============

Git kan vise et repository's status, 
en liste af alle ændringer foretaget i working tree
som endnu ikke er comitted.

#. Åbn SOURCE CONTROL-panelet ved at klikke på :figroilbl:`1`, 
   eller brug genvejen :kbd:`Ctrl+Shift+G` (macOS: :kbd:`Cmd+Shift+G`),
   og klik på filen ``game.py`` :figroilbl:`2`.

   .. figure:: figs/vscode-git-diff-side-by-side.png
      :align: center
   
   * :figroilbl:`A` En tab som viser ændringerne til ``game.py``.
     Visningen kaldes et **diff**, en forkortelse for *difference*.

   * :figroilbl:`B` Linje 9 er markeret i begge filer.
     Linjen markeret med rød er fjernet
     og linjen markeret med grøn er tilføjet.

#. I stedet for at se de to versioner side om side 
   (engelsk: side-by-side diff)
   kan ændringen vises inline (engelsk: inline diff).

   Klik på menuen :guilabel:`...` :figroilbl:`1` 
   og vælg/marker :guilabel:`Inline View` :figroilbl:`2`.

   De to versioner af linje 9 :figroilbl:`A` viser over hinanden
   (kaldet inline view).

   .. figure:: figs/vscode-git-diff-inline.png
      :align: center


#. Ændringen til linje 9  kan kasseres ved at klikke på 
   :guilabel:`Discard Changes`-pilen :figroilbl:`1`
   ud for filen ``game.py``.

   Bekræft du vil kassere ændringerne ved at vælge :guilabel:`Discard changes` 
   fra dialogboksen som fremkommer.

   .. figure:: figs/vscode-sourcecontrol-discard.png
      :align: center

   ``game.py`` er nu ændret på harddisken,
   så filen igen er identisk med versionen af ``game.py`` fra sidste commit.
   
   Når der ingen ændringer er i working tree, 
   i forhold til sidste commit,
   kaldes working tree **clean**\ :footcite:p:`git-scm-glossary`.


.. Admonition:: Aktivitet

  Foretag ændringer i ``game.py`` og brug Git til at kassere ændringerne.
  Læg mærke til hvordan *diff*-visningen ser ud ved forskellige slags ændringer:

  * Linje tilføjet
  * Linje slettet
  * Linje ændret
  * Flere linjer ændret

  Foretag andre ændringer i projektet og brug Git til at kassere ændringerne:

  * Slet en fil fra projektmappen, f.eks. ``images/alien_1.png``.
  * Omdøb en fil.
  * Tilføj en fil


Tidligere versioner (checkout)
==============================

En af de primære årsager til at benytte versionsstyring er,
at forskellige versioner af et projekts filer kan gemmes
og genskabes senere.

At skifte version til et givent commit kaldes at foretage et **checkout**.
Ved checkout af et commit opdateres working tree
til at se ud som det gjorde da det pågældende commit blev lavet.
Fordi et checkout ændrer working tree kan man kun foretage checkouts
hvis working tree er clean
(ellers ville et checkout kassere ændringer foretaget i working tree).

1. Åbn fanen :guilabel:`Git Graph` ved at klikke på :figroilbl:`1`.

2. Højreklik på commit ``Initial commit ... (e267)`` :figroilbl:`2`,
   vælg :guilabel:`Checkout` :figroilbl:`3`.

3. Bekræft, at du vil lave et checkout af commit ``e267``
   ved at vælge :guilabel:`Yes, checkout` i den fremkomne dialog.

.. figure:: figs/vscode-gitgraph-checkout-commit.png
   :align: center

Projektet er nu i en tilstand kaldet **detached head**,
som dialogboksen informerede om.
Det betyde blot, at det ikke er nyeste commit som er checked out.


.. figure:: figs/vscode-detached-head.png
   :align: center

   VS Code viser projektet som det så ud da commit ``e267``
   blev lavet.

* :figroilbl:`A` Bemærk der står :guilabel:`e267 ..` 
  i stedet for :guilabel:`master` som der har gjort indtil nu.

* :figroilbl:`B` EXPLORER-panel viser working tree
  som det så ud i første version af spillet. 

* :figroilbl:`C` Fanen :guilabel:`game.py` viser filen ``game.py``
  som den så ud i commit ``e267``.

4. Afprøv spillet (kør programmet) vha. play-knappen :figroilbl:`1`.

.. admonition:: Aktivitet

   * Foretag et checkout af andre commits 
     og afprøv spillets forskellige versioner.

   * Foretag nogle ændringer i f.eks. ``game.py``
     mens et commit er checked out (detached head).
     Husk at kassere dine ændringer før du foretaget et nyt checkout.

5. Skift tilbage til nyeste version af projektet
   ved at højreklikke på :guilabel:`master` :figroilbl:`1`
   og vælge :guilabel:`Checkout Branch` :figroilbl:`2`.

   .. figure:: figs/vscode-checkout-master.png
      :align: center

.. 
 .. rubric:: Fodnoter

 .. [#git] https://git-scm.com/


**********************
Nye versioner (commit)
**********************

For at videreudvikle på 





