# Adivina el número 

Mediante el desarrollo del siguiente **juego de adivinanza en Python** deberá utilizarse todo lo aprendido sobre lo básico de python, valorando la correcta decisión en el uso de los algoritmos.   

La estructura del juego será la siguente:

### Menú principal

Al comenzar el juego y durante el desarrollo del mismo, las opciones que se muestran hasta elegir la opción salir son:

1. **Partida modo solitario**
   *(Modo solitario supone que el número a adivinar es generado aleatoriamente por el ordenador).*
2. **Partida 2 Jugadores**
   *(Primero se escribe un número a adivinar y luego un segundo jugador intenta adivinarlo).*
3. **Estadística**
   *(Mostrará los datos almacenados en el fichero Excel, donde se podrá observar el historial de partidas jugadas).*
4. **Salir**

#### Submenú de dificultad

Tanto la opción 1 como la opción 2 tendrán un submenú para elegir la dificultad.     
En ambos menús debe chequearse que la opción elegida es válida y avisar en caso contrario.    

1. **Fácil** (20 intentos)
2. **Medio** (12 intentos)
3. **Difícil** (5 intentos)

### Reglas del juego
* El número a adivinar debe ser entre **1 y 1000**.
* Si se adivina el número, se gana la partida y se vuelve al menú principal.
* Si no se adivina, el programa debe indicar si el número buscado es **mayor o menor**.
* Si se supera el número de intentos, se pierde y se vuelve al menú principal.

### Registro de resultados

* Al finalizar cada partida (ya sea ganada o perdida), se pide el **nombre del jugador**.
* Se guarda esta información junto con el resultado de la partida en un **fichero Excel**.

### María Carolina González Bernal
