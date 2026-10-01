#Notas de aprendizaje DevOps

## WSL
En PowerShell (Windows)

wsl --install

wsl: el programa de Windows que maneja los Linux instalados.
--install: instala WSL y, por defecto, Ubuntu.

wsl ~

Abre la distribución predeterminada.
~: arranca en tu carpeta personal de Linux, no en la carpeta donde estaba parado Windows.

wsl -l -v

-l (list): lista las distribuciones instaladas.
-v (verbose, detallado): agrega el estado (corriendo o detenida) y la versión de WSL de cada una.

wsl --set-default Ubuntu

--set-default: define qué distribución abre wsl cuando no le decís cuál.
Ubuntu: el nombre de esa distribución, tal como aparece en wsl -l -v.

wsl -d NombreDeLaDistro

-d (distribution): abre una distribución específica sin cambiar la predeterminada.

exit

Cierra la sesión de la terminal actual. Si estabas dentro de Linux desde PowerShell, volvés a PowerShell.

## En Ubuntu: navegación y sistema

cd ~

cd (change directory): te mueve a otra carpeta.
~: atajo de tu carpeta personal (/home/aramiszabala).

ls ~/.ssh

ls (list): muestra los archivos de una carpeta.
~/.ssh: la carpeta .ssh dentro de tu carpeta personal. El punto adelante indica que es una carpeta oculta: un ls común no la muestra, y para verla hay que usar ls -a.

cat ~/.ssh/id_ed25519.pub

cat: muestra en pantalla el contenido de un archivo.

sudo apt update, sudo apt upgrade -y, sudo apt install git -y

sudo (superuser do): ejecuta el comando como administrador (root). Hace falta para instalar programas o tocar archivos del sistema.
apt, update, upgrade, install y -y: ya los vimos.

apt --help y man apt

--help: muestra un resumen de las opciones del comando. Casi todos los comandos lo tienen.
man (manual): abre el manual completo del comando. Te movés con las flechas y salís con q.

## En Ubuntu: Git y VS Code

git --version

--version: muestra qué versión está instalada. Sirve para verificar que un programa existe.

code .

code: abre VS Code.
.: la carpeta actual. Abre VS Code con esa carpeta cargada.

git config --global user.name "Tu Nombre" (y lo mismo con user.email)

git config: lee o cambia la configuración de Git.
--global: la configuración se aplica a todos tus repos, no solo al actual. Se guarda en ~/.gitconfig.
user.name / user.email: el nombre y email que quedan registrados en cada commit.
Las comillas hacen falta porque el valor tiene espacios. Sin ellas, Git entendería "Tu" y "Nombre" como dos cosas separadas.

git config --global --list

--list: muestra toda la configuración guardada.

## En Ubuntu: SSH

ssh-keygen -t ed25519 -C "tu-email@ejemplo.com"

ssh-keygen (key generator): genera un par de claves.
-t (type): el algoritmo de la clave. ed25519 es el más moderno; el viejo es rsa.
-C (comment): un texto que queda al final de la clave pública para identificarla.

eval "$(ssh-agent -s)" es el más raro de todos, va por partes:

ssh-agent: arranca el programa que guarda tus claves desbloqueadas en memoria.
-s: le pide que, al arrancar, imprima unos comandos que definen variables de entorno. Son datos que la terminal guarda, en este caso dónde encontrar al agente.
$( ... ): ejecuta lo que está adentro y devuelve el texto que imprimió.
eval: toma ese texto y lo ejecuta como si fueran comandos.
En resumen: arranca el agente y le avisa a tu terminal dónde está, para que ssh-add y git lo encuentren.

ssh-add ~/.ssh/id_ed25519

ssh-add: le entrega una clave privada al agente. Te pide la passphrase una vez y, mientras la terminal siga abierta, no la vuelve a pedir.

ssh -T git@github.com

ssh: se conecta a otra máquina.
-T: no pide una terminal interactiva. GitHub igual no te la da; solo queremos probar que te reconoce.
git@github.com: el formato es usuario@servidor. En GitHub todos se conectan con el usuario git, y GitHub sabe quién sos por tu clave, no por el usuario.