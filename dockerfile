# Usa un'immagine base di Python
FROM python:3.9-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file necessari
COPY requirements.txt requirements.txt
COPY db_conv.py db_conv.py
COPY Db_example.xml Db_example.xml

# Installa le dipendenze Python
RUN pip install --no-cache-dir -r requirements.txt

# Esegui lo script Python
CMD ["python", "db_conv.py"]







