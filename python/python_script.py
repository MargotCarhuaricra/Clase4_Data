import os
###### carpeta dataset #######

location = "C:/Users/Margot/Documents/proyecto_parcial/python/dataset"

### validar si existe la carpeta ###

if not os.path.exists(location): ## carperta no existe
    os.mkdir(location) ## crear carpeta

else :  ##carpeta existe 
    ##borrar contenido
    for root, dirs, files in os.walk(location,topdown=False):
        for name in files:
            os.remove(os.path.join(root,name)) ## eliminar los archivos
        for name in dirs:
            os.rmdir(os.path.join(root,name)) ##eliminar las carpetas

##Importar libreria API kagle ###

from kaggle.api.kaggle_api_extended import KaggleApi  

api = KaggleApi()
api.authenticate()

##decargar dataset ###

##print(api.dataset_list(search="")) ##nos aparece en listado la data sate

##api.dataset_download_file('rahulvyasm/netflix-movies-and-tv-shows','netflix_titles.csv',path=location,force=True,quiet=False)
api.dataset_download_files('rahulvyasm/netflix-movies-and-tv-shows',path=location,force=True,quiet=False,unzip=True)

