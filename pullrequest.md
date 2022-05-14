# Subiendo tu trabajo a GitHub

Ya que has termino los ejercicios, deberas subirlos a tu github para que te cuente que has trabajado en proyectos de python. 

### Paso 1: Agregar los elementos a git
En nuestra consola posicionados en nuestra carpeta de trabajo, donde estan los ejercicios, ejecutaras el siguiente comando:

```Git
git add .
```

Esto subira los elementos modificados.

### Paso 2: Realizar el commit

Describe tu proyecto como: 

```Git
git commit -m "Ejercicios - SOLO 1 NOMBRE
```

### Paso 3: Hacer push

Ya que hayas hecho el commit, ahora subiras el proyecto.

```Git
git push origin exercises
```

Estamos subiendo la rama exercises que creamos cuando clonamos el repo.

### Paso 4: Hacer pull request

En tu repositorio que hiciste fork, donde hay un boton arriba a la izquierda que dice `main`, a lado te debe aparecer `2 branches`.

![](https://diarioinforme.com/wp-content/uploads/2022/01/Click-Branches..png)

Vas a darle click al boton main y seleccionaras la rama `exercises`
