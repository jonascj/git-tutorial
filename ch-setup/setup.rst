
#########################
Installation og opsætning
#########################

Udviklingsmiljøet som bliver opsat i afsnittet her benytter sig af 
fire komponenter som alle virker på de tre store platforme
(Windows, macOS og Linux):

**Visual Studio Code (VS Code)** (Microsoft [#msvscode]_) benyttes som 
integrated development environment (IDE).


**Git** (free/libre, open source [#foss]_) er det versionsstyringssytem
som betjenes grafisk VS Code og github.com.


**GitHub** (Microsoft [#msgithub]_) er en webbaseret hosting-service
for såkaldte *git repositories* som tilbyder backup af
repositories og tilbyder brugere at samarbejde om et repository.


**Python** er benyttet som programmeringssprog i alle eksempler 
og tutorials. 
VS Code, Git og github.com kan selvfølgelig bruges med et hvilket som helst
andet programmeringssprog.


.. _sec-git-install:

*******************
Installation af Git
*******************

.. tabs::

   .. group-tab:: Linux
      #. Test om *Git* allerede er installeret (det kan det meget vel være).
   
         Åbn en terminal og kør kommandoen ``git --version``.
   
         Hvis du får output ala ``git version 2.x`` så er Git allerede installeret
         og du behøver ikke gøre mere.
   
      #. Hvis Git ikke er installeret så kan du finde 
         en installationsvejledning til de fleste store Linux-distributioner her:
   
         https://git-scm.com/download/linux
   
         .. admonition:: Ubuntu
   
            I Ubuntu 16, 18, 20 og 22 kan Git installeres fra kommandolinjen 
            med en enkelt kommando:
   
               .. code-block:: console
         
                  sudo apt install git
   
   .. group-tab:: macOS
      #. Åbn en terminal (:kbd:`Cmd+Space` og søg efter ``terminal``)
         og skriv kommandoen :code:`git --version` efterfulgt af :kbd:`Enter`.
         
         .. image:: figs/git-install-xcode-macos.png
            :align: center
      
      #. Hvis der fremkommer et popupvindue som vist på skærmbilledet ovenfor
         er Git ikke installeret og du kan installere det ved at vælge
         :guilabel:`Install`.
      
         Hvis der i stedet for et popupvindue blot fremkommer teksten
         ``git version 2.x`` i terminalvinduet så er Git installeret
         og du behøver ikke gøre mere.

         Hvis der hverken fremkommer teksten ``git version 2.x``
         eller et popupvindue
         kan du prøve kommandoen ``xcode-select --install``.


   .. group-tab:: Windows

      #. Download :guilabel:`64-bit Git for Windows Setup` fra
         https://git-scm.com/download/win

         .. image:: figs/git-install-download-win.png
             :align: center

         -----

      #. Kør installationsprogrammet :program:`Git-2.x.y-64-bit.exe` 
         som netop er downloadet og gennemfør installationen.

         Alle forvalgte indstillinger (defaults) er som de skal være,
         du behøver ændre noget.
      

.. _sec-python-install:

**********************
Installation af Python
**********************

.. tabs::

   .. group-tab:: Linux

      #. Test om Python 3.7 eller nyere er installeret.
      
         Kør kommandoen ``python3 --version`` i en terminal.
      
         a. Hvis outputtet er ``Python 3.x.y`` (og x er 7 eller større)
            så er Python 3 installeret og du behøver ikke gøre mere.
      
         b. Hvis Python ikke er installeret (output a la ``Command not found``)
            kan Python med stor sandsynlighed installeres vha. din distributions
            package manager.
      
            Lav en internetsøgning efter :samp:`{<distro name>} install python 3`,
            e.g. ``ubuntu 16 install python 3``.
         
      
      #. Test om Pythons package installer *pip* er installeret. 
      
         Kør kommandoen `pip --version` i en terminal.
      
         a. Hvis outputtet er ``pip x.y.z from ...`` så er *pip* installeret
            og du behøver ikke gøre mere.
      
         b. Hvis *pip* ikke er installeret (output a al ``Command not found``)
            kan *pip* med stor sandsynlighed installeres vha. din distributions
            package manager.
      
            Lav en internetsøgning efter :samp:`{<distro name>} install python pip`,
            e.g. ``ubuntu 16 install python pip``.

      .. admonition:: Ubuntu
         
          Hvis du bruger Ubuntu 18, 20 eller 22 er Python 3.7 eller nyere installeret,
          men du mangler Pythons package installer *pip*.
         
          *pip* kan installeres fra kommandolinjen:
         
          .. code-block:: console
         
              sudo apt update
              sudo apt install python3-pip 


   .. group-tab:: macOS
   
      #. Download seneste version af Python fra
         https://www.python.org/downloads/
      
         .. image:: figs/python-install-download-macos.png
            :align: center
      
      #. Kør installationsprogrammet :program:`python-3.x.y-macos11.pkg`
         som netop er downloadet.
      
         Gennemfør installationen ved at trykke :guilabel:`Continue`, 
         acceptér licensbetingelserne osv.
      
         Ingen særlige indstillinger er nødvendige undervejs.

   .. group-tab:: Windows

      #. Download seneste version af Python fra
         https://www.python.org/downloads/
      
         .. image:: figs/python-install-download-win.png
            :align: center
      
      #. Kør installationsprogrammet :program:`python-3.x.y-amd64.exe` 
         som netop er downloadet.
      
         .. image:: figs/python-install-win.png
            :align: center
      
         .. important::
      
            Sæt flueben ved :guilabel:`[x] Add python.exe to path`.
      
            Fjern fluebenet ved 
            :guilabel:`[ ] Use admin privileges when install py.exe`.


.. _sec-vscode-install:

***********************
Installation af VS Code
***********************

.. note::
   
   Koden til VS Code er open source\ :footcite:p:`github-vscode`, 
   men programmet som kan downloades fra https://code.visualstudio.com/
   består af mere end blot open source koden til VS Code.
   Det indeholder også proprietære komponenter til telemetri/tracking. 

   Ønskes disse features ikke har du to muligheder: 
   
   1. Slå dem fra i VS Code 
      som beskrevet i afsnittet :ref:`sec-vscode-telemetry`.

   2. Installér VSCodium i stedet for VS Code: https://vscodium.com/#install

      VSCodium er en udgave af VS Code, baseret på samme open source kode,
      men med telemetri/tracking deaktiveret.

.. tabs::

   .. group-tab:: Linux

      I de fleste moderne Linux-distributioner (Ubuntu, Debian, Fedora, CentOS m.f.)
      vil det nemmeste være at installere **Visual Studio Code** via *snap*-systemet.

      #. Besøg denne side https://snapcraft.io/code.

      #. Scroll til bunden af siden, vælg din distribution fra listen 
         og følg instruktionerne i den guide du videresendes til.

         .. admonition:: Ubuntu

            Hvis du bruger Ubuntu 16, 18, 20 eller 22 kan **Visual Studio Code** 
   	      installeres fra kommandolinjen med en enkelt konmando:

            .. code-block:: console
         
                     sudo snap install code --classic


   .. group-tab:: macOS

      #. Åbn https://code.visualstudio.com/Download 
         og download *.zip Universal*
   
         .. image:: figs/download-vscode-macos.png
            :align: center
   
   
      #. Applikationen **Visual Studio Code** kan nu startes ved at dobbeltklikke på
         applikationen **Visual Studio Code** som findes i mappen *Downloads* 
         (*Overførsler*).
   
         Overvej at flytte applikationen til mappen *Applications* 
         (vha drag and drop / træk og slip).
   
   .. group-tab:: Windows

      #. Åbn https://code.visualstudio.com/Download 
         og download *User Installer*
   
         .. image:: figs/download-vscode-win.png
            :align: center
   
         .. note::
            Vælg *System Installer* hvis programmet skal installeres 
            for flere brugere af en PC,
            denne installer placere programfilerne i ``c:\program files\`` 
            og dette kræver administratorrettigheder.
   
   
      #. Start installationsprogrammet ved at dobbeltklikke på den netop 
         downloadede fil (i skrivende stund ``VSCodeUserSetup-x64-1.72.0.exe``)
   
      #. Gennemfør installationsproceduren, der er ingen særlige indstillinger 
         som skal laves under vejs. 
   
      #. Programmet **Visual Studio Code** kan nu startes fra startmenuen 
         eller genvej på skrivebordet.


.. _sec-vscode-setup:

********************
Opsætning af VS Code
********************

Opsætningen af VS Code er den samme på alle tre platforme 
(Windows, macOS, Linux).

Første start
============

Første gang VS Code startes ser du følgende skærmbillede:

.. image:: figs/vscode-config-first-start0.png
     :align: center

#. Du kan skifte farvetema, f.eks. til et lyst farvetema (light mode).

#. Tryk på :guilabel:`< Get Started` for at komme tilbage til startskærmen
   som vil møde dig næste gang du åbner VS Code.

VS Code ser nu ud som nedenfor. 

.. image:: figs/vscode-config-first-start1.png
     :align: center


.. _sec-vscode-telemetry:

Telemetridata og online services (valgfrit)
===========================================

Hvis du ikke ønsker at VS Code sender data om din brug af VS Code
tilbage til Microsoft kan du slå *telemetry* fra:

#. Vælg menupunkt :menuselection:`File --> Preferences --> Telemetry` 
   
   (macOS: :menuselection:`Code --> Preferences --> Telemetry`)

#. Vælg :guilabel:`Off` fra drop-down-listen:

    .. image:: figs/vscode-config-telemetry.png
        :align: center

Hvis du ikke ønsker VS Code skal benytte forskellige Microsoft online services, 
f.eks. Bing til at søge blandt indstillinger [#vscodebing]_,
så kan du slå dem fra:


#. Vælg menupunkt 
   :menuselection:`File --> Preferences --> Online Services Settings`
   
   (macOS: :menuselection:`Code --> Preferences --> Online Services Settings`)

#. Vælg :guilabel:`Off` fra drop-down-listen:


.. _sec-vscode-extensions:

Udvidelser/extensions
=====================

#. Åbn Extensions-panelet.

#. Søg efter ``ms-python.python``.

#. Klik :guilabel:`Install`.

.. image:: figs/vscode-extensions-python.png
     :align: center

Installér på samme måde følgende udvidelser:

* ``donjayamanne.githistory``

* ``mhutchie.git-graph``



    
.. _sec-gitconfig:

****************
Opsætning af Git
****************

Git konfigureres med dit navn og din email-adrese,
som du ønsker de skal fremgå af Gits log over hændelser i dine repositories.

#. Vælg menupunkt :menuselection:`Terminal --> New Terminal`

   .. figure:: figs/vscode-terminal-gitconfig.png
        :align: center
	
        :figroilbl:`a` :guilabel:`>` kaldes en prompt
        og :figroilbl:`b` er navnet på det program som modtager kommandoerne fra terminalen.
        Promptens udseende og programmets navn varierer fra system til system. 

#. Indtast kommandoen ``git config --global user.name "Your Name"``, 
   erstat ``Your Name`` med dit ønskede navn 
   (husk citationstegn hvis dit navn indeholder mellemrum),
   og tryk :kbd:`Enter`.

   Udfør på samme måde måde kommandoen ``git config --global user.email "your@email.com"``.


#. Tjek om konfigurationen lykkedes ved at køre kommandoen ``git config user.name``
   og ``git config user.email``. 

   De to kommandoer skulle gerne outputte det navn og den email-adresse du netop har indtastet.



.. _sec-pygame-install:

**********************
Installation af pygame 
**********************

Introduktionen til versionsstyring med Git, GitHub og VS Code
er bygget omkring et simpelt arkadespil,
som benytter sig af Python-modulet *pygame*.

#. Genbrug en allerede åbn terminal i VS Code 
   eller åbn en :menuselection:`Terminal --> New Terminal`

#. Kør kommandoen ``pip3 install pygame``.

   .. image:: figs/vscode-terminal-pippygame.png
        :align: center

   .. note:: 
       Hvis kommandoen ``pip3 install pygame`` giver en fejl a la ``Command not found``
       og du benytter Windows så har du måske glemt at sætte fluebenet
       :guilabel:`[x] Add python.exe to path` 
       fra afsnit :ref:`sec-python-install`.

       Ret fejlen ved at geninstallere Python (og sætte fluebenet).


************
GitHub-konto
************

#. Udfyld oprettelsesformularen på https://github.com/signup 

   .. note::

      Det brugernavn du vælger under oprettelsen 
      kommer til at være synligt for andre.
      
      URL's til repositories har formatet 
      ``https://github.com/<username>/<repository name>``
      f.eks. https://github.com/user1234/cool-tool-x.

      Repositories omtales også som ``<username>/<repository name>``,
      f.eks. ``user1234/cool-tool-x``.


#. Ved første har du mulighed for at personalisere din GitHub-konto.
   
   Jeg vil anbefale at vælge :guilabel:`Skip personalization`.

   .. image:: figs/github-signup-skip.png
        :align: center
        :scale: 50%

#. Din GitHub-konto er nu klar til brug 

   .. image:: figs/github-signup-first-login.png
        :align: center
        :scale: 50%

.. seealso::
    
    Git er uafhængigt af GitHub og man behøver således ikke en konto hos GitHub
    for at bruge Git til versionsstyring. 

    Skulle man imidlertid ønske sig et webbaseret sted at dele git-repositories,
    f.eks. for at have backup af sine repositories eller for at samarbejde,
    kan man selv hoste et github-lignende system kaldet *GitLab*:

    https://about.gitlab.com/install/?version=ce




.. rubric:: Fodnoter

.. [#msvscode] https://en.wikipedia.org/wiki/Visual_Studio_Code

.. [#foss] https://en.wikipedia.org/wiki/Free_and_open-source_software

.. [#msgithub] https://en.wikipedia.org/wiki/GitHub

.. [#vscodebing] https://code.visualstudio.com/blogs/2018/04/25/bing-settings-search
