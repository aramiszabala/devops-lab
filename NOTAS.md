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
