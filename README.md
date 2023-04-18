# Safe Browsing Flask Alkalmazás

A Safe Browsing Flask alkalmazás egy egyszerű webalkalmazás, amely lehetővé teszi a felhasználók számára, hogy ellenőrizzék egy domain fertőzöttségét a Google Safe Browsing API segítségével. A projekt Docker és docker-compose segítségével könnyen futtatható és skálázható.

## Funkciók

- Domain fertőzöttségének ellenőrzése a Google Safe Browsing API segítségével
- Eredmények mentése SQLite adatbázisba
- Dockerizált alkalmazás
- Gunicorn alkalmazásszerver

## Követelmények

- Docker
- docker-compose
- Google Safe Browsing API kulcs

## Projektstruktúra

```
.
├── app
│   ├── data
│   ├── main.py
│   └── requirements.txt
├── config
│   └── Dockerfile
├── templates
│   └── index.html
├── docker-compose.yml
└── .env
```

- `app`: Az alkalmazás fő mappája, amely tartalmazza a Python kódot, a függőségek listáját és az adatbázis fájlt.
- `config`: A konfigurációs mappa, amely tartalmazza a Dockerfile-t.
- `templates`: A sablonok mappája, amely az `index.html` fájlt tartalmazza.
- `docker-compose.yml`: A docker-compose konfigurációs fájl, amely definiálja az alkalmazás szolgáltatásait.
- `.env`: Az API kulcs tárolására szolgáló környezeti változók fájlja.

## Telepítés és futtatás

1. Győződjön meg róla, hogy telepítette a Docker-t és a docker-compose-t a számítógépén.
2. Klónozza a projektet a számítógépére.
3. Hozzon létre egy `.env` fájlt a projekt gyökérkönyvtárában a következő tartalommal (cserélje le a `YOUR_GOOGLE_API_KEY` értékét a saját API kulcsával):

```
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

4. Építse és futtassa az alkalmazást a következő parancsokkal:

```sh
docker-compose build
docker-compose up
```

Az alkalmazás most elérhető lesz a http://localhost:8000 címen.

## Használat
1. Nyissa meg a http://localhost:8000 címet a böngészőjében.
2. Írja be a domain nevét, amelyet ellenőrizni szeretne, és kattintson az "Ellenőriz" gombra.
3. A rendszer piros színnel jelzi, ha a weboldal fertőzött, zöld színnel, ha nem fertőzött. Az eredményt és az ellenőrzés dátumát elmenti az SQLite adatbázisba.

## Licenc és közreműködés
A Safe Browsing Flask alkalmazás MIT licenc alatt áll, amely lehetővé teszi a szabad felhasználást, módosítást és terjesztést a megfelelő forrásmegjelölés mellett. Kérjük, hogy a módosításokat és az új funkciókat ossza meg a közösséggel, hogy elősegítse a projekt fejlődését és a hasznosságát.

## Közreműködés
A közösségi közreműködés nagyra értékelendő. Ha hibát talál az alkalmazásban vagy javaslatokkal rendelkezik új funkciókra, nyugodtan nyisson egy hibajegyet vagy küldjön be egy pull request-et a projekt GitHub tárhelyén. Az alkalmazás fejlesztése során örömmel vesszük a visszajelzéseket és a javaslatokat.

## Támogatás
Ha kérdése van az alkalmazás használatával vagy fejlesztésével kapcsolatban, kérjük, vegye fel a kapcsolatot a projekt szerzőjével vagy a közösséggel a megfelelő csatornákon (pl. GitHub, Stack Overflow, e-mail).

## Köszönetnyilvánítás
Köszönjük a közösségnek és a hozzájárulóknak, akik segítettek az alkalmazás létrehozásában és fejlesztésében. Külön köszönet illeti a Google Safe Browsing API-t és a kapcsolódó technológiákat, amelyek lehetővé teszik ezt az alkalmazást.

Köszönöm a ChatGPT-nek, az OpenAI-nak és a ChatGPT magyarul csoportnak, hogy ezt az anyagot elkészíthettük.
