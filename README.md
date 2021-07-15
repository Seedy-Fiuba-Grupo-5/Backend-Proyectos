# Seedy Fiuba Backend-Proyectos
[![Main](https://github.com/Seedy-Fiuba-Grupo-5/Backend-Proyectos/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/Seedy-Fiuba-Grupo-5/Backend-Proyectos/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/Seedy-Fiuba-Grupo-5/Backend-Proyectos/branch/main/graph/badge.svg)](https://codecov.io/gh/Seedy-Fiuba-Grupo-5/Backend-Proyectos/branch/main)

[![Develop](https://github.com/Seedy-Fiuba-Grupo-5/Backend-Proyectos/actions/workflows/develop.yml/badge.svg?branch=develop)](https://github.com/Seedy-Fiuba-Grupo-5/Backend-Proyectos/actions/workflows/develop.yml)
[![codecov](https://codecov.io/gh/Seedy-Fiuba-Grupo-5/Backend-Proyectos/branch/develop/graph/badge.svg)](https://codecov.io/gh/Seedy-Fiuba-Grupo-5/Backend-Proyectos/branch/develop)

## Tecnologias
- Flask (framework del servicio web)
- Postgres (Base de datos)

## Entorno Local

### Construccion
```
docker-compose build --remove-orphans
```

### Levantar servicios
```
docker-compose up
```

### Pruebas: pytest & flake8
pytest: libreria de python para 'testing'.
pytest-cov: plugin de pytest para medir porcentaje de cobertura de las pruebas.
flake8: 'linter' de python, basado en los lineamientos de pep8.

2) Pytest + Flake8:
```
./run_tests.sh
```
Nota 1: Este script requiere que los servicios se encuetren levantados.
Nota 2: Este script esperara hasta que la base de datos se haya inicializado.

3) Se pueden realizar cambios en el codigo y los servicios (en ejecucion), los detectaran y se actualizaran, permaneciendo en ejecucion.

### Autopep8
autopep8: Formatea el codigo de python para que se adecuado a los
lineamientos de pep8.
```
./run_autopep8.sh
```
Nota: Este script requiere que los servicios se encuetren levantados.

### Postgres psql
```
docker exec -it -u postgres container_projects_db psql
```

### Detener servicios
```
docker-compose stop
```
Nota: Mantiene el estado de la base de datos.

### Destruir contenedores
```
docker-compose down -v
```

## Entorno Heroku
## Informacion
Nombre de la aplicacion Heroku (App): seedy-fiuba-backend-projects
Nombre del repositorio Heroku: https://git.heroku.com/seedy-fiuba-backend-projects.git

Heroku Postgres (BDD): postgresql-corrugated-25619
(La aplicación desplegada en Heroku utiliza una base de datos Postgres propia de
la plataforma, agregada como add-on de la aplicacion)

URL de la aplicacion: https://seedy-fiuba-backend-projects.herokuapp.com/

## Despliegue
Conectarse a Heroku:
```
heroku login
```

Agregar repositorio remoto de Heroku
```
heroku git:remote -a seedy-fiuba-backend-projects
```
Nota: El creador del repositorio de Heroku deberia hacer colaborado a quienes quieren pushear al mismo.

Conectarse al contenedor de Heroku:
```
heroku container:login
```

Construir imagen de la aplicacion y pushear a heroku:
```
heroku container:push web --app seedy-fiuba-backend-projects
```

Ejecutar la imagen subida en la instancia de heroku
```
heroku container:release web --app seedy-fiuba-backend-projects
```

## Prendido y apagado del servicio
Prendido del servicio :
```
heroku ps:scale web=1 --app seedy-fiuba-backend-projects
```

Apagado del servicio :
```
heroku ps:scale web=0 --app seedy-fiuba-backend-projects
```

## Postgres psql
```
heroku pg:psql --app seedy-fiuba-backend-projects
```

## Migraciones (ambos entornos)
### Crear carpeta migrations/
Crear carpeta migrations:
```
docker-compose exec service_projects_web flask db init
```

### Agregar nueva migración
```
docker-compose exec service_projects_web flask db migrate -m "descripción de la migración"
```

### Actualizar la base de datos con las nuevas migraciones
```
docker-compose exec service_projects_web flask db upgrade
```
Nota 1: Manualmente, se debe agregar las nuevas migraciones
a traves del comando `flask db migrate` descrito en la sección
anterior. Esto es gran importancia antes de subir la nueva
instancia de la aplicacion a Heroku.

Nota 2: Este comando ya es invocado desde el archivo
docker-entrypoint.sh antes de invocar a la aplicación web.


