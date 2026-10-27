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

## GitHub Actions: conceptos

- **Workflow:** proceso automatizado. Archivo YAML en `.github/workflows/`.
- **Evento (`on`):** qué lo dispara (push, PR, tag, botón manual).
- **Job:** grupo de pasos que corre en una máquina. Por defecto, los jobs corren **en paralelo**.
- **Step:** un paso. Puede ser un comando (`run`) o una action reutilizable (`uses`).
- **Runner:** máquina virtual limpia que GitHub crea para cada job y destruye al terminar.

## GitHub Actions: estructura de un workflow

```yaml
name: CI
on:
  pull_request:
    branches: [main]      # en cada PR hacia main
  push:
    branches: [main]      # cuando algo entra a main
    tags: ["v*.*.*"]      # cuando se pushea un tag de versión
  workflow_dispatch:      # botón para correrlo a mano

jobs:
  mi-job:
    runs-on: ubuntu-latest
    needs: otro-job       # espera a que otro job termine bien
    permissions:          # permisos mínimos del GITHUB_TOKEN
      contents: read
      packages: write
    env:
      VAR: ${{ secrets.MI_SECRETO }}
    steps:
      - uses: actions/checkout@v7     # bajar el código (el runner arranca vacío)
      - uses: actions/setup-python@v7
        with:
          python-version: "3.12"
      - name: Paso con nombre
        run: echo "hola"
      - run: |                        # comando de varias líneas
          linea 1
          linea 2
      - if: failure()                 # solo si algo falló
        run: docker compose logs
      - if: always()                  # siempre
        run: docker compose down -v
```

- `${{ ... }}`: expresión que GitHub reemplaza antes de ejecutar.
- `secrets.GITHUB_TOKEN`: token automático, vence al terminar el job. No hace falta crearlo.
- `github.actor`: el usuario que disparó el workflow.
- `echo "VAR=valor" >> "$GITHUB_ENV"`: deja una variable disponible para los pasos siguientes.
- `${VARIABLE#texto}` (bash): saca `texto` del principio del valor (ej.: `v1.1.0` → `1.1.0`).

Variables útiles: `GITHUB_RUN_NUMBER`, `GITHUB_WORKSPACE`, `GITHUB_WORKFLOW`, `GITHUB_SHA`, `GITHUB_REF_NAME`.

## GitHub: secrets y reglas

- Secrets: **Settings → Secrets and variables → Actions**. No se pueden volver a ver y en los logs aparecen como `***`.
- Checks obligatorios: **Settings → Rules → Rulesets → Require status checks to pass**.
  - El check tiene que haber corrido al menos una vez para aparecer en el buscador.
  - El nombre del check es el nombre del **job**.
- Un check que no es *Required* no bloquea el merge, aunque esté en rojo o en pending.

## Códigos de salida

- Todo comando devuelve un código al terminar: `0` = bien, cualquier otro = error.
- `echo $?`: muestra el código del último comando.
- Los pipelines marcan un paso como fallido si termina con código distinto de `0`.
- `curl -f`: devuelve error si la respuesta HTTP es un código de error (4xx, 5xx). **Imprescindible en tests.**
- `curl --retry 5 --retry-connrefused --retry-delay 2`: reintentar si la app todavía no arrancó.
- `comando || true`: si el comando falla, no cuenta como error.

## Ruff (linter de Python)

- `ruff check .`: revisar el código sin ejecutarlo.
- `docker run --rm -v .:/io ghcr.io/astral-sh/ruff check`: correrlo con Docker, sin instalar nada.
- `--fix`: aplicar las correcciones automáticas (las marcadas con `[*]`).
- `F401`: import que no se usa. `I001`: imports desordenados.
- Orden de imports: librería estándar → externas (pip) → propias, separados por línea en blanco.

## Tags y versiones

- `git tag -a v1.2.0 -m "mensaje"`: crear un tag anotado en el commit actual.
- `git tag`: listar tags. `git show v1.2.0`: ver un tag.
- `git push origin v1.2.0`: subir el tag (`git push` común **no** sube tags).
- `git tag -d v1.2.0`: borrar un tag local (solo si todavía no se pusheó).
- Un tag publicado **no se reutiliza**: si tiene un error, se publica la versión siguiente.
- Antes de taggear: `git switch main` y `git pull`, para que el tag incluya lo mergeado.
- Versionado semántico: MAYOR (rompe) . MENOR (agrega) . PARCHE (corrige o ajusta).
- GitHub → **Releases → Draft a new release → Generate release notes**: documenta la versión.
- `git commit --allow-empty -m "..."`: commit sin cambios, para volver a disparar los pipelines.

## Jenkins: conceptos

- **Controller:** servidor principal (interfaz web, configuración, coordina).
- **Agent:** máquina que ejecuta los builds. Buena práctica: los builds en agents, no en el controller.
- **Executor:** "lugar" para correr un build. Cantidad de builds simultáneos.
- **Job:** tarea configurada.
  - **Freestyle:** se configura con formularios. La configuración no queda en el repo.
  - **Pipeline:** definido en un `Jenkinsfile` en el repo.
  - **Multibranch Pipeline:** detecta solo las ramas y PRs con `Jenkinsfile`.
- **Build:** cada ejecución (#1, #2...). **Workspace:** carpeta del job. A diferencia de Actions, **queda entre builds**.
- **Credentials:** donde se guardan secretos y tokens.

## Jenkins en Docker

```bash
docker build -t jenkins-docker:1.0 jenkins/
docker run -d --name jenkins \
  -p 8090:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --group-add $(getent group docker | cut -d: -f3) \
  --restart unless-stopped \
  jenkins-docker:1.0
```

- `jenkins_home`: volumen con toda la configuración. Si se pierde, se pierde Jenkins.
- `jenkins/Dockerfile`: imagen oficial + cliente de Docker y Compose.
- Contraseña inicial: `docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword`.
- Verificar que ve Docker: `docker exec jenkins docker ps`.
- `--restart unless-stopped`: arranca solo, salvo que lo pare yo.
- `--group-add`: suma al usuario de Jenkins al grupo `docker` de mi máquina.
- `getent group docker | cut -d: -f3`: número del grupo `docker`.
- Con el socket montado, Jenkins tiene control total de mi Docker: solo para laboratorio.
- Idioma: plugin **Locale** → Manage Jenkins → System → Default Language `en`.

## Jenkinsfile (declarativo)

```groovy
pipeline {
    agent any
    environment {
        IMAGE = "app:jenkins-${env.BUILD_NUMBER}"
    }
    stages {
        stage('Etapa') {
            environment {
                SECRETO = credentials('id-de-la-credencial')
            }
            steps {
                sh 'comando "$IMAGE"'
                sh '''
                    comando largo \
                      en varias líneas
                '''
            }
            post {
                failure { sh 'docker compose logs' }
                always  { sh 'docker compose down -v' }
            }
        }
    }
    post {
        always { sh 'docker rmi "$IMAGE" || true' }
    }
}
```

- Las etapas son **secuenciales**: si una falla, las siguientes se saltean (`parallel { }` para correrlas juntas).
- `sh '...'` con **comillas simples**: las variables las resuelve la shell, no Groovy (más seguro con secretos).
- `credentials('id')`: trae una credencial. En los logs aparece como `****`.
- `post`: `always`, `failure` y `success`. Puede ir en el pipeline o en una etapa.
- Variables útiles: `BUILD_NUMBER`, `WORKSPACE`, `JOB_NAME`, `GIT_COMMIT`, `GIT_BRANCH`.

## Docker desde Jenkins (trampas)

- `-v "$WORKSPACE":/ruta` **no funciona**: la ruta la interpreta el Docker de mi máquina, no Jenkins.
  → Usar `--volumes-from jenkins -w "$WORKSPACE"`.
- `--user "$(id -u):$(id -g)"`: correr la herramienta con el usuario de Jenkins (si no, deja archivos de root).
- `curl localhost` desde Jenkins apunta al propio Jenkins.
  → Usar `docker run --rm --network <proyecto>_default curlimages/curl -f http://app:8000/...`.
- Compose para CI:
  - `-p jenkins-ci`: nombre de proyecto propio, separado del stack local.
  - `-f compose.yaml -f compose.ci.yaml`: combinar archivos (el segundo pisa al primero).
  - `ports: !reset []`: vaciar los puertos heredados.
  - `profiles: ["herramientas"]`: el servicio solo arranca si se pide su profile.

## Jenkins: Multibranch y GitHub

- Credencial `github-token` (*Username with password*): token clásico con `repo:status` y `public_repo`.
- Branch Sources → GitHub → Behaviors:
  - Discover branches: *Exclude branches that are also filed as PRs*.
  - Discover PRs from origin: *Merging the pull request with the current target branch revision*.
- Scan Repository Triggers: *Periodically*, cada 1 minuto (GitHub no puede avisarle a un Jenkins en localhost).
- Checks en GitHub:
  - `continuous-integration/jenkins/pr-merge`: PRs (este va como obligatorio).
  - `continuous-integration/jenkins/branch`: ramas, como `main`.
- Executors del controller en 1 (Manage Jenkins → Nodes → Built-In Node), para que los builds no se pisen.

## Cron (Poll SCM)

- 5 campos: minuto, hora, día del mes, mes, día de la semana. `*` = cualquiera.
- `H/2 * * * *`: cada 2 minutos. `H` reparte los horarios entre jobs.

## GitHub Actions vs Jenkins

| | Actions | Jenkins |
|---|---|---|
| Infraestructura | La pone GitHub | La administro yo |
| Ejecución | Runner limpio cada vez | Workspace que queda |
| Jobs / etapas | En paralelo por defecto | Secuenciales por defecto |
| Secretos | Secrets del repo | Credentials |
| Integración con GitHub | Nativa | Plugin + token + polling o webhook |
| Conviene cuando | El código está en GitHub y no quiero mantener servidores | Varias plataformas, redes internas, mucha personalización |

## Errores que me aparecieron

- **El workflow no corre / no aparecen los checks:** el archivo estaba vacío (`ls -la` mostraba 0 bytes) o nunca se le hizo `git add`.
- **Los checks no aparecen en el ruleset:** tienen que haber corrido al menos una vez. Hay que escribir el nombre del job en el buscador.
- **`smoke-test` en *skipped*:** su `needs` (el lint) falló.
- **Merge habilitado con checks en rojo:** ese check no estaba como *Required*.
- **`I001` / `F401` en Ruff:** imports desordenados / import que no se usa.
- **Checks de Jenkins en pending para siempre:** el build se canceló al cambiar la configuración → commit vacío para que el PR tome los checks nuevos.
- **`denied` / `403` al publicar en GHCR desde Actions:** el repo no tiene permiso sobre el paquete → paquete → Manage Actions access → Write.
- **`HCS_E_HYPERV_NOT_INSTALLED` al instalar WSL:** virtualización apagada en el BIOS (*SVM Mode* en AMD, *VT-x* en Intel) + `wsl.exe --install --no-distribution`.
- **Ruff en Jenkins ve una carpeta vacía:** usé `-v "$WORKSPACE"` → hay que usar `--volumes-from jenkins`.
- **Mergeé sin que Jenkins revise:** Jenkins no informaba a GitHub → Multibranch + check obligatorio.