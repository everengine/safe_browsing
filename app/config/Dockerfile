# Alap Docker kép
FROM python:3.10-alpine

# Munkakönyvtár beállítása
WORKDIR /app

# Függőségek telepítése
COPY ./app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Az alkalmazás fájljainak másolása
COPY ./app /app

# Gunicorn konfiguráció
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:8000 --workers=2"

# Indítási parancs
CMD ["gunicorn", "main:app"]
