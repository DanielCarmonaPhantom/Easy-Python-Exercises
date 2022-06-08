# Descargar carpeta:

Para empezar, descargaremos la carpeta desde un fork, esto para que cuando lo hayas terminado, lo subas a tu perfil y te de las soluciones.

Rquesisitos: 

* Tener instalado git. Si aun no tienes git, sigue este [Tutorial](https://github.com/DanielCarmonaPhantom/Tutorial-Git-y-GitHub).

## Paso 1: Hacer Fork

En la parte superior derecha, hay un botón que dice Fork 

![](https://sammyk.s3.amazonaws.com/blog/images/2014-05-28/fork.png)

Le darás click y te llevará a crear un repositorio propio. Le darás `Create fork` y tendrás el repositorio en tu perfil. Cualquiera que entre a tu perfil vera que trabajaste en proyectos de Python.

## Paso 2: Descargar la carpeta en tu computadora

Este paso puedes realizarlo de 2 maneras:

1. Clonando el repositorio
2. Descargando el zip

### Clonar el repositorio

Ya que tengas el proyecto en tu repositorios, lo abrirás y veras la misma pantalla pero ahora hay un botón verde que dice Code

![](https://www.freecodecamp.org/espanol/news/content/images/2020/12/clone.jpg)

Le darás click al botón verde y te abrirá unas opciones, ahora le daras click al de copiar para obtener la ruta de tu repositorio como en la imagen.

Aquí estaremos utilizando la consola de la computadora, ya sea el cdm de windows o la terminal de Mac/Linux. 

**Para Windows**: Presionamos la tecla Windows + R y escribimos CMD

**Mac/Linux**: Abrimos la aplicación de la terminal.

Abriremos nuestra terminal en la computadora y automáticamente estaremos posicionados en la carpeta de usuario. Para verificar que estamos en usuario podemos utilizar los comandos `dir` en Windows y `pwd` en Mac/linux.

Así que nos iremos a la carpeta Desktop u Escritorio con el comando:
```Bash
cd Desktop
```
Dependiendo tu sistema operativo podría ser en minúsculas, pero puedes poner `cd Desk` y presionar `TAB` y completara por si solo.

Una vez estando en la carpeta escritorio en la terminal, procederemos a clonar el repositorio de GitHub colocando el comando `git clone` + la url que copiaste en el paso 2

**Windows**: Pondrás `git clone`, + 1 espacio y presionarás `control` + `c` para pegar la url

**Mac**: Pondrás `git clone`, + 1 espacio y  darás click derecho y presionarás pegar.

Debes tener algo así:

```Git
git clone https://github.com/TUUSUARIO/Python-Exercises-Easy.git
```
Le darás enter y automáticamente se te clonará el repositorio en tu escritorio. 

### Descargar el zip

En vez de darle al boton copiar, abajo dice `Download ZIP`

## Paso 3: Crear una rama donde estaras trabajando

Ya teniendo la carpeta, abre tu editor de código y dale a Open Folder y seleccionamos la carpeta. 

Para que puedas subir tus cambios, necesitaras trabajar en una nueva rama.

### Si clonaste el repo, en la misma consola haz:

```Git
git chekout -b "exercises"
```

### Si lo descargaste.
Tendras que abrir la terminal de visual code. Hasta arriba en las opciones de ventan, dice `Terminal` y en `Nueva terminal`.


Ya puedes continuar con las <a href='instructions.md'>Instrucciones del Notebook</a>
