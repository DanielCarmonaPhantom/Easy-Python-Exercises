# Subiendo tu trabajo a GitHub

Ya que has terminado los ejercicios, debes subirlos a tu github para que te cuente que has trabajado en proyectos de python. 

### Paso 1: Agregar los elementos a git
En nuestra consola posicionados en nuestra carpeta de trabajo, donde estan los ejercicios, ejecutaras el siguiente comando:

```Git
git add .
```

Esto subirá los elementos modificados.

### Paso 2: Realizar el commit

Describe tu proyecto ejecutando un commit y añadiendo **1 solo nombre tuyo** como: 

```Git
git commit -m "Ejercicios - NOMBRE"
```

Presionar enter y esto pondrá nombre a tu trabajo realizado.

### Paso 3: Hacer push

Ya que hayas hecho el commit, ahora subirás el proyecto.

```Git
git push origin exercises
```

Estamos subiendo la rama `exercises` que creamos cuando clonamos el repo.

### Paso 4: Hacer pull request

Entrarás a tu repositorio que hiciste fork, habrá un botón arriba a la izquierda que dice `main` y a lado te debe aparecer `2 branches`.

![](https://diarioinforme.com/wp-content/uploads/2022/01/Click-Branches..png)

Vas a darle click al boton main y seleccionamos la rama `exercises`

Ahora te aparecerá un recuadro que dice `Esta rama tiene una contribución de: TU NOMBRE` y a la derecha aparece `Contribute`.

<img src="https://www.earthdatascience.org/images/earth-analytics/git-version-control/github-create-new-pull-request.png" width="450">

Se desplegara unas opciones y darás click en `Open Pull Requests`.

Ya te abrirá una página para enviar tu trabajo y ya viene definido el nombre de tu trabajo. 

Le darás al botón verde que dice `Create pull request``

¡Listo! Ya subiste tus ejercicios ¡Felicidades! pronto te mandaré un mensaje comentando las respuestas.
