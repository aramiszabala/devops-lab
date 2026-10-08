## Linux básico

- `cd ~`: ir a mi carpeta personal.
- `cd <carpeta>`: entrar a una carpeta.
- `ls`: listar archivos. Con `-a` incluye los ocultos.
- `mkdir <carpeta>`: crear una carpeta.
- `touch <archivo>`: crear un archivo vacío.
- `cat <archivo>`: mostrar el contenido de un archivo.
- `echo "texto" > archivo`: escribir en un archivo (reemplaza todo el contenido).
- `echo "texto" >> archivo`: agregar al final del archivo.
- `code .` / `code <archivo>`: abrir VS Code en la carpeta actual / en ese archivo.
- `python3 app.py`: ejecutar un script de Python. Se corta con `Ctrl+C`.
- `curl localhost:8000/health`: hacer un pedido HTTP desde la terminal. Con `-i` muestra los encabezados.
- `q`: salir del paginador (cuando abajo aparece `:` o `(END)`).

## Git: configuración (una sola vez)

- `git config --global user.name "Nombre"`: nombre que queda en cada commit.
- `git config --global user.email "email"`: email que queda en cada commit (el mismo de GitHub).
- `git config --global init.defaultBranch main`: la primera rama de cada repo nuevo se llama `main`.
- `git config --global --list`: ver la configuración guardada.

## Git: crear un repo

- `git init`: convierte la carpeta actual en un repo (crea la carpeta oculta `.git`).

## Git: ciclo básico

Carpeta de trabajo --`git add`--> Staging --`git commit`--> Repositorio

- `git status`: estado de cada archivo (untracked, modified, staged).
- `git diff`: cambios que todavía no pasé a staging.
- `git add <archivo>` / `git add .`: pasar cambios a staging (uno / todos).
- `git commit -m "mensaje"`: guardar lo que está en staging como un commit.
- `git commit --amend --reset-author --no-edit`: corregir el autor del último commit. Solo si todavía no lo pusheé.

## Git: historial

- `git log`: historial completo, con autor y fecha.
- `git log --oneline`: un commit por línea (hash corto + mensaje).
- `git log --oneline --graph`: igual, con el dibujo de las ramas.
- `HEAD`: dónde estoy parado ahora.

## Git: remotos (GitHub)

- `git remote add origin <url>`: conectar el repo local con GitHub. `origin` es el nombre del remoto.
- `git remote -v`: ver los remotos configurados.
- `git push -u origin <rama>`: primer push de una rama. `-u` la vincula con la de GitHub.
- `git push`: los pushes siguientes.
- `git pull`: bajar cambios de GitHub y unirlos a mi rama.
- `git fetch --prune`: consultar GitHub sin tocar mis archivos y borrar referencias a ramas que ya no existen allá.
- "ahead of 'origin/main' by N commits": tengo N commits locales que no están en GitHub.

## Git: ramas

- `git branch`: listar ramas locales (`*` = la actual).
- `git branch -a`: listar ramas locales y remotas.
- `git switch <rama>`: cambiar de rama.
- `git switch -c <rama>`: crear una rama desde donde estoy parado y cambiarme a ella.
- `git branch -d <rama>`: borrar una rama ya mergeada. `-D` la borra a la fuerza.

## Git: merge y conflictos

- `git merge <rama>`: unir esa rama a la rama actual.
- Fast-forward: si la rama actual no cambió, Git solo la mueve hacia adelante, sin commit de merge.
- Conflicto: dos ramas cambiaron la misma línea. Git marca el archivo así:
  - `<<<<<<< HEAD`: arriba, lo que tiene mi rama actual.
  - `=======`: separador.
  - `>>>>>>> rama`: arriba, lo que trae la otra rama.
- Para resolverlo: editar, borrar los marcadores, `git add <archivo>` y `git commit --no-edit`.
- `git merge --abort`: cancelar el merge y volver a como estaba antes.

## Flujo de trabajo con main protegida

1. `git switch main` y `git pull`: arrancar desde main actualizada.
2. `git switch -c tipo/descripcion`: crear la rama de trabajo.
3. Hacer cambios, `git add` y `git commit -m`.
4. `git push -u origin tipo/descripcion`.
5. En GitHub: crear PR → Merge → Delete branch.
6. `git switch main`, `git pull`, `git branch -d tipo/descripcion` y `git fetch --prune`.

Prefijos de ramas: `feature/` (funcionalidad), `fix/` (corrección), `docs/` (documentación), `chore/` (mantenimiento).


## Stash

Cajón temporal para guardar cambios sin commitear y dejar la carpeta limpia.
Sirve para cambiar de rama sin commitear trabajo a medias.

### Guardar

- `git stash push -m "mensaje"`: guarda los cambios (en staging o no) de archivos que Git ya sigue.
- `git stash push -u -m "mensaje"`: incluye también archivos nuevos (untracked).

### Ver

- `git stash list`: lista lo guardado. `stash@{0}` es el más reciente.
- `git stash show -p`: muestra las líneas del último stash sin aplicarlo.
- `git stash show -p stash@{1}`: lo mismo con un stash específico.

### Recuperar

- `git stash pop`: aplica el último stash y lo saca del cajón.
- `git stash apply`: aplica el último stash y deja una copia en el cajón.
- `git stash pop stash@{1}`: aplica un stash específico (también funciona con `apply`).

### Descartar

- `git stash drop`: tira el último stash sin aplicarlo.
- `git stash drop stash@{1}`: tira uno específico.
- `git stash clear`: tira **todos**. No se recupera fácil.

### A tener en cuenta

- Los cambios sin commitear no pertenecen a ninguna rama: te siguen si cambiás de rama.
- Sin `-u`, los archivos nuevos no se guardan en el stash y quedan en la carpeta.
- Si al hacer `pop` hay conflicto, se resuelve como en un merge y el stash **no** se borra del cajón: después de resolverlo, hacé `git stash drop`.

## Docker: conceptos

- **Imagen:** plantilla de solo lectura (como un ISO). Se construye con un Dockerfile.
- **Contenedor:** una imagen corriendo. De una imagen salen muchos contenedores.
- **Registry:** donde se guardan las imágenes (Docker Hub, GHCR).
- **Capas:** cada instrucción del Dockerfile es una capa. Si no cambió, se reutiliza de caché.
- Lo que se cambia **adentro** de un contenedor se pierde al borrarlo. Lo que tiene que perdurar va en un volumen.

## Docker: contenedores

- `docker run -d --name web -p 8080:80 nginx`: crear y arrancar un contenedor.
  - `-d`: en segundo plano.
  - `--name`: nombre para referirse a él.
  - `-p <puerto-mi-máquina>:<puerto-del-contenedor>`: publicar un puerto. El de la derecha lo define la app.
  - `-v <carpeta-mía>:<carpeta-contenedor>:ro`: bind mount (`:ro` = solo lectura).
  - `--rm`: borrar el contenedor al terminar (para herramientas de un solo uso).
- `docker ps`: contenedores corriendo. Con `-a`, también los detenidos.
- `docker logs <contenedor>`: ver logs. Con `-f`, en vivo (`Ctrl+C` para salir).
- `docker exec -it <contenedor> bash`: entrar al contenedor (`exit` para salir).
- `docker stop` / `docker start <contenedor>`: detener / volver a arrancar.
- `docker rm <contenedor>`: borrar. Con `-f`, lo para y lo borra.
- `docker port <contenedor>`: ver los puertos publicados.
- `docker container prune`: borrar todos los contenedores detenidos.

## Docker: imágenes

- `docker images`: listar imágenes. `docker images <nombre>` filtra.
- `docker pull <imagen>`: descargar sin correr.
- `docker build -t <nombre>:<tag> .`: construir (`.` = contexto de build).
- `docker tag <imagen> <nombre-nuevo>`: otro nombre para la misma imagen (mismo ID).
- `docker history <imagen>`: ver las capas.
- `docker inspect --format '{{ json .Config.Labels }}' <imagen>`: ver datos internos (acá, los labels).
- `docker rmi <imagen>`: borrar una imagen (no se puede si un contenedor la usa).
- `docker image prune`: borrar imágenes `<none>` que quedan de builds anteriores.

## Dockerfile

- `FROM python:3.12-slim`: imagen base. Preferir variantes chicas (`-slim`).
- `LABEL clave=valor`: metadatos. `org.opencontainers.image.source` vincula la imagen al repo en GHCR.
- `RUN <comando>`: se ejecuta **durante el build**.
- `WORKDIR /app`: crear la carpeta y pararse ahí.
- `COPY <origen> <destino>`: copiar archivos de mi máquina a la imagen.
- `USER appuser`: a partir de acá, ejecutar sin privilegios de root.
- `EXPOSE 8000`: documenta el puerto (no lo publica).
- `CMD ["python", "app.py"]`: comando que se ejecuta al **arrancar** el contenedor.

Buenas prácticas:

- Una instrucción por línea.
- Lo que cambia seguido, al final (primero `requirements.txt` + `pip install`, después el código).
- No correr como root.
- Fijar versiones (`postgres:16`, `psycopg==3.2.*`).
- `.dockerignore` para no meter `.git`, `.env` ni basura en la imagen.

## Volúmenes

- **Bind mount** (`-v ~/carpeta:/ruta`): una carpeta mía. Los cambios se ven al instante.
- **Volumen con nombre** (`datos-db:/ruta`): lo administra Docker. Para datos de bases.
- `docker volume ls`: listar volúmenes.

## Registry (GHCR)

- Nombre completo: `registry/dueño/nombre:tag`, por ejemplo `ghcr.io/aramiszabala/devops-lab-app:1.0.0`. Sin registry, Docker asume Docker Hub.
- Versionado semántico: `MAYOR.MENOR.PARCHE`.
- `read -s CR_PAT`: guardar el token sin que se vea ni quede en el historial.
- `echo $CR_PAT | docker login ghcr.io -u <usuario> --password-stdin`: iniciar sesión.
- `unset CR_PAT`: borrar la variable con el token.
- `docker push <imagen>`: subir. `docker pull <imagen>`: bajar.
- `docker logout ghcr.io`: cerrar sesión.
- Los paquetes nuevos en GHCR son **privados** por defecto.

## Docker Compose

- `docker compose up -d`: levantar todo. Con `--build`, reconstruye antes.
- `docker compose ps`: estado de los servicios (y si están `healthy`).
- `docker compose logs <servicio>`: logs. Con `-f`, en vivo.
- `docker compose exec <servicio> <comando>`: ejecutar algo adentro de un servicio.
- `docker compose stop` / `start <servicio>`: detener / arrancar un servicio.
- `docker compose down`: borrar contenedores y red (los volúmenes quedan).
- `docker compose down -v`: también borra los volúmenes. **Se pierden los datos.**
- `docker compose config`: ver el archivo con las variables ya reemplazadas (muestra secretos).

En `compose.yaml`:

- `build: .` (construir, para desarrollo) vs `image: ...` (descargar, para producción).
- `environment`: variables de entorno. `${VAR}` se toma del `.env`.
- `depends_on` + `condition: service_healthy`: esperar a que otro servicio esté sano.
- `healthcheck`: comando que indica si el servicio está sano.
- Los servicios se encuentran por **nombre** (`db`), no por `localhost`.
- `.env` nunca al repo. Sí se sube `.env.example` con valores de ejemplo.
- La contraseña de `POSTGRES_PASSWORD` solo se aplica la **primera vez** que se crea el volumen.
- YAML: la sangría importa y se usan espacios, nunca tabs.

## Trivy

```bash
docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v trivy-cache:/root/.cache/ \
  aquasec/trivy \
  image --severity HIGH,CRITICAL --ignore-unfixed <imagen>
```

- `--severity`: filtrar por gravedad.
- `--ignore-unfixed`: ocultar las que todavía no tienen corrección.
- Priorizar: severidad, si tiene corrección y si la app usa ese paquete.

## Errores que me aparecieron

- `permission denied ... docker.sock`: mi usuario no está en el grupo `docker` → `sudo usermod -aG docker $USER` y `newgrp docker`.
- `port is already allocated`: ese puerto de mi máquina ya está en uso → elegir otro puerto (el de la izquierda en `-p`).
- `container name ... is already in use`: ya existe un contenedor con ese nombre → `docker rm -f <nombre>` u otro nombre.
- `Connection reset by peer`: el puerto del contenedor (el de la derecha en `-p`) no es donde escucha la app.
- `FROM requires either one or three arguments`: algo de más en la línea del `FROM` (otra instrucción en la misma línea, o espacios).
- `tag does not exist` en un push: no hay ninguna imagen local con ese nombre exacto → revisar con `docker images`.
- `error from registry: denied`: la imagen no existe con ese nombre, o es privada y no tengo sesión.
- `password authentication failed` en Postgres: contraseña distinta a la que tiene el volumen (o `.env` sin guardar).
- VS Code `No file system provider`: se cortó la conexión con WSL (por ejemplo, después de `wsl --shutdown`) → Reload Window o `code .` de nuevo.