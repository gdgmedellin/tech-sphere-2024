# Creando un producto de IA Generativa

1. Creamos un ambiente virtual de python.
```sh
python -m venv venv
```

2. Activamos el ambiente virtual de python 

En linux:
```sh
source venv/bin/activate
```

En windows:
```sh
source venv/Scripts/activate
```

3. Corremos nuestra aplicación

```sh
streamlit run src/app.py
```

4. Copiar el API Key
```sh
https://docs.google.com/document/d/1I9kT-aRjyRW6-I6SoTlA4HmD1UA7w6LA5I-QXmhdypk/edit?usp=sharing
```

5. Si queremos crear la imagen de docker
```sh
docker build -t app1 .
```

6. Ejecutamos la imagen de Docker
```sh
docker run -p 8501:8501 app1
```