# Descargar carpeta:

Para empezar, descargaremos la carpeta desde un fork, esto para que cuando lo hayas terminado, lo subas a tu perfil y te de las soluciones.

Rquesisitos: 

* Tener instalado git. Si aun no tienes git, sigue este [Tutorial](https://github.com/DanielCarmonaPhantom/Tutorial-Git-y-GitHub).

## Paso 1: Hacer Fork

En la parte superior derecha, hay un botón que dice Fork 

![](https://sammyk.s3.amazonaws.com/blog/images/2014-05-28/fork.png)

Le darás click y te llevará a crear un repositorio propio. Le darás `Create fork` y tendrás el repositorio en tu perfil. Cualquiera que entre a tu perfil vera que trabajaste en proyectos de Python.

## Paso 2: Clonar tu repositorio en tu computadora

Ya que tengas el proyecto en tu repositorios, lo abrirás y veras la misma pantalla pero ahora hay un botón verde que dice Code

![](https://www.freecodecamp.org/espanol/news/content/images/2020/12/clone.jpg)

Le darás click al botón verde y te abrirá unas opciones, ahora le daras click al de copiar para obtener la ruta de tu repositorio como en la imagen.

## Paso 3: Posicionarte en la carpeta donde clonarás el repo

Abriremos nuestra consola y automáticamente estaremos posicionados en la carpeta de usuario así que nos iremos a la carpeta Desktop con el comando:
```Bash
cd Desktop
```
Dependiendo tu sistema operativo podría ser en minúsculas, pero puedes poner `cd desk` y presionar `TAB` y completara por si solo.

Una vez estando en la carpeta escritorio en la terminal, procederemos a clonar el repositorio de GitHub colocando el comando `git clone` + la url que copiaste en el paso 2

**Windows**: Pondrás `git clone`, + 1 espacio y presionarás `control` + `c` para pegar la url

**Mac**: Pondrás `git clone`, + 1 espacio y  darás click derecho y presionarás pegar.

Debes tener algo así:

```Git
git clone https://github.com/TUUSUARIO/Python-Exercises-Easy.git
```
Le darás enter y automáticamente se te clonará el repositorio en tu escritorio. 

Para que puedas subir tus cambios, necesitaras trabajar en una nueva rama, solo debes usar el siguiente comando:

```Git
git chekout -b "exercises"
```

Ya teniendo la carpeta, abre tu editor de código y dale a Open Folder y seleccionamos la carpeta clonada.

Ya puedes continuar con las <a href='instructions.md'>Instrucciones del Notebook</a>
