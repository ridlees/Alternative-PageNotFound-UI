# Alternative PageNotFound UI

Někdy je pro mě náročné přečist fonty, co PageNotFound používá, tak jsem napsal tento nástroj, co mi zobraazí pouze text (nedává dokonalý zažitek, protože neukazuje obrázky a některé věci nefungují, cílem tohoto projektu není nahradit PageNotFound, ale pouze pro mě zjednodušit čtení.)

Snad to redakci PageNotFound nebude vadit <3

## Dependencies
1. Python
2. Flask
3. requests
4. beautifulSoup4

## Instalace

* K použití potřebujete python (já to psal na python3.8). Nainstalujte si ho/stáhněte si ho z stránky [Pythonu](https://www.python.org/downloads/)

* Poté potřebujete nástroj pip (který se k Pythonu přidává) na stahovnání modulů. Mužete ho získat zavoláním `python get-pip.py`. Či se koukněte na [dokumentaci](https://pip.pypa.io/en/stable/installation/)

* Následně, se v terminálu přesuňte do složky Alternativního UI (`cd`) a zavolejte `pip install -r requirements.txt`. Tím se vám nainstalují všechny depencencies.

* Poté zavolejte `python main.py`. (Aplikace nemá WSGI, protože není myšlená jako produkční appka k hostování, ale jako malý nástroj k selfhostování)*

* Voilá, na localhostu http://127.0.0.1:80 je aplikace k použití. Vypnete ji v terminálu kombinací ctr + c.


\* Samozřejmě, můžete UI hostovat přes nástroje jako je `ngrok` či jinak. Ale nedělejte to. PageNotFound nedovoluje takovéto nakládání s texty.



## Použití

1. Na PageNotFound najděte **odemčený** článek.
2. Zkopírujte jeho URL adresu
3. Na localhostu ji dejte do políčka pro URL adresu.
4. Stiskněte Generovat. Po chvíli se objeví text (pokud jste dali správnou URL adresu.) Neklikejte vícekrát, jinak se Vám text objeví vícekrát.

