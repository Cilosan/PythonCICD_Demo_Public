# Verwende das offizielle Python-Image als Basis
FROM python:3.10

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die lokalen Dateien in das Container-Verzeichnis
COPY . /app

# Installiere Python-Abhängigkeiten
RUN pip install

# Definiere den Befehl, der beim Starten des Containers ausgeführt wird
CMD ["python", "python_app.py"]