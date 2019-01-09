### Cambios servicio meteorológico v2:

- Se han quitado todas las variables globales excepto listaMeteo, apiKey, weatherCity, units y BASE_URI. De estas globales, apiKey, weatherCity, units y BASE_URI se leen para saber que preguntar al servicio rest, pero solo se puede modificar desde el código. Solo listaMeteo es modificada con cada actualización de la página:

        - listaMeteo se puede modificar de varias formas, cada vez que se entra a la página o 
          se accede a la posicion 0 de la página, o que siempre se vaya actualizando 
          cada vez que entre actualice la página al entrar a cada posición. En este 
          caso he usado la ultima opción, pero no estoy seguro de si habra algún error 
          si muchas personas actualizan al mismo tiempo la página, dando asi un gran 
          problema a los demas si mientras uno vacia la lista, otro lee
        
- Se ha introducido en la url para ver el tiempo y pasar de una fecha a la siguentes o anteriores, la "posición" que debe visitar a continuación (se puede ver en la url que el valor de posición actua para paginar la lista de 10 en 10). Teniendo asi la url, se evita tener de variable global la posicion y resuelve el problema de que cada vez que un usuario vea una página de la lista, al resto le afectaba si recargaba la página y veían lo mismo que el otro.

### Cambios respecto a la rama master:

- Nueva clase Meteo en models.py para guardar los datos meteorológicos en una fecha concreta

- Nuevo botón en modules.html llamado "Ver el tiempo"

- Nueva pagina llamada verTiempo.html donde se mostrará en una tabla los datos meteorológicos de 10 en 10, junto a 3 botones, "Fechas anteriores", "Fechas posteriores" y "Atras"

- Nuevo archivo viewsMeteo.py donde se enviará la lista de objetos Meteo necesaria para verTiempo.html y gestionará las peticiones relacionadas con el servicio meteorológico, como:

       - Acceder a él desde la pagina principal al darle al botón "Ver el tiempo" y 
         redirigir a la página verTiempo.html

       - Realizar un par de funciones que devuelve un booleano diciendo si puede 
         ver los siguientes datos de la tabla o los anteriores (se pasarán a la pagina 
         estos booleanos para luego renderizar o no, los botones para poder ver los 
         siguientes o anteriores datos)

       - Una función next y back que darán la función a los botones para ver los 
         siguientes o anteriores datos y actualizara la tabla como corresponde

- Se ha añadido al main.py las correspondientes líneas para que importe las nuevas clases y use los nuevos métodos en viewsMeteo.py para las nuevas redirecciones
