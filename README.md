# Proyecto final
## Requisitos
Para poder ejecutar este proyecto tienes que tener instalado:
- Docker ([instalación](https://docs.docker.com/engine/install/))

## Ejecución del proyecto en local
Nosotros usamos Docker Compose para desarrollar localmente. Al ejecutar por primera vez el proyecto con Docker Compose se construirá una imagen de Docker para local. El Dockerfile que usará es `Dockerfile.development`

El comando para ejecutar el proyecto es:
```bash
docker compose up
```

### Primera vez que se ejecute el proyecto
Si es la primera vez que ejecutamos el proyecto tendrás que inicializar la base de datos ejecutando el archivo manage.py de la siguiente forma:
```bash
./run.sh python3 manage.py
```
Lo que hace el comando es entrar dentro del contenedor de nombre `proyecto_final_app` y ejecuta el comando `python3 manage.py`

Con esto ya tendremos inicializada la base de datos con las tablas creadas.

### Actualizar archivos del contenedor de nuestra aplicación
Cada vez que hagas un cambio en la aplicación Docker Compose se actualizará para servir los nuevos ficheros ya que montamos un volumen de la carpeta local con la carpeta /app dentro del contenedor de Docker
> [!WARNING]
> Sí después de cambiar los archivos del proyecto no se ve reflejado en el contenedor de Docker, entonces tendrás que parar la ejecución y reconstruir la imagen de Docker para desarrollo con el comando:

```
docker compose up --build
```

El argumento `--build` forzará a recontruir las imágenes de Docker que usa nuestro fichero `docker-compose.yaml`

## Tests
Nuestra aplicación utiliza pytest para lanzar los tests unitarios que prueban los endpoints de nuestra API. Para ejecutarlos puedes usar el siguiente comando:
```
./run pytest
```

Si quieres crear un reporte de covertura de tests tienes que lanzar los siguientes comandos:
```
./run coverage run -m pytest
./run coverage report
```

El primer comando crea un fichero `.coverage` que contiene los resultados de lanzar el primero comando. El segundo comando lo que hace es leer de este fichero para mostrar una tabla con todos los archivos de nuestro código, excluyendo los archivos de tests, para mostrar que porcentaje de código nuestros tests cubre que contiene los resultados de lanzar el primero comando. El segundo comando lo que hace es leer de este fichero para mostrar una tabla con todos los archivos de nuestro código, excluyendo los archivos de tests, para mostrar que porcentaje de código nuestros tests cubren.
