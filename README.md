# Evidencia Final - _El arte de Programar_

### Participantes


Ricardo Navarro Gómez - A01708825 - _Encargado de la modificación de Pacman_  
Fernando Josue Matute Soto - A00833375 - _Encargado de la modificación de Tic Tac Toe_

# Pacman


En primer lugar, tuve que comentar todo el código, por lo que investigué las funciones que habían dentro del mismo,
ya que realmente no tenía idea de las librerías que se estaban utilizan, ni de las funciones dentro de las mismas;
por lo que  llevé a cabo dicho proceso de investigación.

Una vez que tenía en claro esas funciones, fui comentando el código poco a poco, para entender de qué manera es que
estaba trabajando el mismo, encontrando así los puntos claves del mismo, como la velocidad de inicio y posición de los fantasmas
y pacman, a la par de la manera en la que se formaba el mapa. Una vez con todos los comentarios listos, fue que hice mi primer
commit con los mismos, para de ahí ya empezar las modificaciones que se nos pedían.

Ahora que tenía en claro la mayoría de las secciones del código claras gracias a los comentarios, me enfoqué en los puntos que se me pedían,
en primer lugar aumentar la velocidad de los fantasmas. Para ello, me di cuenta de que la velocidad de cualquier objeto está dividida en 2 partes:
la velocidad inicial, y la velocidad estándar después de el lanzamiento del juego; por lo que para afectar a la velocidad, debería de afectar ambos
parámetros. En segundo punto, también edbía de fijarme en el hecho de que el mapa estaba cuadriculado a 20 puntos, por lo que todos los
movimientos deberían de ser justamente múltiplos de su mínimo común divisor (en este caso el 5).

Por lo que finalmente lo último que debía de pensar para saber que tanto aumentar la velocidad de los fantasmas, fue basarme en el juego original
que me encontraba modificando. Ahí, encontré que los fantasmas justamente son más rápidos que pacman, pero no tanto, por lo que agarré la única velocidad
mínima posible que fuera mayor a la de el pacman del código (la cual era 5); y es así como les terminé colocando tanto de velocidad inicial,
como estándar dicho valor de movimiento en cualquier dirección.

En segunda instancia, tenía que trabajar en la modificación del mapa —el cual, perse a ser el punto más fácil de todos, decidí complicarlo
un poco más—, algo importante a recalcar del mismo, es que el mapa se encuentra en un formato binario, siendo los 1 los caminos, mientras
que los 0 serían las barreras. Es así como busqué el mapa original de pacman, y decidí hacer una versión similar al mismo (ya que no se
podía recrear totalmente al no tener el mapa dentro de este código y el del pacman original las mismas dimensiones. Así es como codifiqué de manera binaria
el mapa que formé y lo coloqué en la sección que le correspondía dentro del código.

Algo que también conllevó el cambio de mapa, era también la reposición de los personajes, ya que podría ser que ahora muchos de ellos aparecieran dentro
de las barreras, por lo que no podrían ni moverse; así que también llevé a cabo dichas modificaciones, para que los fantasmas y pacman tuvieran nuevas
posiciones dentro del nuevo mapa, y a continuación llevé a cabo el commit dentro de Github.

Como última parte de la modificación, ya solamente revisé que el código cumpliera con el estilo de PEP8 mediante el uso de flake8, y una vez
comprobé e hice las correcciones necesarias, subí el archivo final a la rama de pacman.

# Tic Tac Toe


En primera intsancia, cree una rama llamada Tictac, que es donde trabajé en mi parte del código de manera colaborativa con mi colega. Seguido de eso, comenté el código proporcionado de acuerdo a sus funcionalidades luego de haber comprendido que realiza cada línea.

Luego, fue la parte de la implementación de las dos nuevas funcionalidades del código. La primera funcionalidad nueva consistía en cambiar el color, tamaño y centrar las "X" y "O" que se utilizan en el juego. La segunda modificación consistía en validar si una casilla estába utilizada, de igual manera implementé otra funcionalidad para determinar un ganador del juego. 

Para finalizar, modifiqué el código de acuerdo a los estándares de codificación flake8 y los validamos para no tener errores. 

Todos estos pasos se pueden ver reflejados en los commits que se realizaron en la rama llamada Tictac.
