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
docker container exec -it proyecto_final_app sh -c "python3 manage.py"
```
Lo que hace el comando es entrar dentro del contenedor de nombre `proyecto_final_app` y ejecuta el comando `python3 manage.py`

Con esto ya tendremos inicializada la base de datos con las tablas creadas.

### Actualizar archivos del contenedor de nuestra aplicación
Cada vez que hagas un cambio en la aplicación tendrás que parar los contendores de Docker de la aplicación haciendo `Control+C` en la terminal donde tengas el docker compose en ejecución.

Después levanta el proyecto con:
```
docker compose up --build
```

El argumento `--build` forzará a recontruir las imágenes de Docker que usa nuestro fichero `docker-compose.yaml`
