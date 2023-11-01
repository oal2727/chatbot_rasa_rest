DUCKING HTTP > FECHAS,HORAS

componentes: https://rasa.com/docs/rasa/components/#spacytokenizer

# recordar definir los archivos a conexiones externas en el root
# nota en modificar el archiov actions.py no es necesario el train
# restantes archivos si es necesario el train

-salir del proyecto actual
deactivate
# enviroment:
1. crear directorio env
python -m venv env
2. ejecucion del proyecto actual:
.\env\Scripts\activate
3. descargar rasa
pip install rasa
4. instalar dependencias en tu proyecto
pip install -r requerimients.txt
5. descargar el modelo y adjuntarlo en la carpeta models
6. rasa run actions
7. rasa run --enable-api --port 5005

