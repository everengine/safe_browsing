# Prompts

## Dokumentáció készítése

Nem tudom, hogy ti hogy vagytok vele, de nekem mindig nyűg, általában nincs rá igazán időm, és ezt az ügyfelek sem szeretik megfizetni. Ugyanakkor ez az egyik leghasznosabb dolog, ha új kollégának a rendszert meg kell mutatni, illetve akkor, amikor ritkán használunk egy kódot, és vissza kell rá térni, illetve közösségi használat esetén különösen hasznos.

A dokumentáció fontos eleme a szoftverfejlesztésnek, hiszen segít abban, hogy az új fejlesztők könnyen megértsék a rendszert, és elősegíti a hosszú távú karbantartást és fejlesztést. A dokumentáció készítése közben érdemes odafigyelni a részletekre, és folyamatosan frissíteni azt a rendszer változásaival együtt. Emellett a jól megírt és átgondolt dokumentáció hozzájárul a projekt sikerességéhez és a csapat hatékonyságának növeléséhez.

## Kód generálás
Tudnál írni egy rövid Python flask kódot, ami annyit csinál, hogy lekéri a Google safe browsing apibol, hogy az adot oldal fertőzött-e, a domaint html form segítségével lehet megadni egy index.html fájlban az oldal bootstrap alapú legyen és az index oldalra pirossal írja ki ha fertőzött a domain, zölddel ha nem fertőzött. A domaint, az eredményt és a dátumot mentse el egy sqlight adatbázisba.

## Dockerizálás
Készíts kérlek egy docker-compose.yml fájlt és dockerizáld a kódot.  Alpinista Linuxot használj legyen app könyvtár, amiben a kód van és a requiermets.txt azon belül legyen egy data mappa, ahol az sqlight fálj van. Legyen egy config mappa az app mellett, ahol Dockerfile van. A yml fájl mellett legyen egy .env fájl, ahol a Google api kulcsot tároljuk. Ennek megfelelően módosítsd a kódot is. Használj gunicorn-t.

## Dokumentáció
Készítenél egy teljeskörű dokumentációt a fenti programhoz

## Markdown formátum
Leírnád markdown formátumba, hogy be tudjam majd illeszteni a readme.md fájlba?

Kérlek magyar nyelven írd és ne Google Safe Browsing Flask Application legyen a neve, hanem  Safe Browsing Flask Application

