## Proyecto Final
**Proyecto final para la clase de programacion**  
Nuestro proyecto muestra una version del juego ahorcado  
A la hora de ejecutarlo se muestras indicaciones en donde con numero se elijen los modos de juego y opciones  
Tiene la funcion de volver a ejecutar el codigo sin necesidad de cerrarlo, se usan muchas funciones definidas en el codigo antes de el inicio para asi ya solo llamarlas en la parte necesaria  

Equipo 3

Oxwaldo Lopez Diaz  
Aaron Becerra González

### **Variables y Funciones del Juego del Ahorcado**

#### **Variables:**
1. **`lista_abecedario`**  
   - **Uso**: Lista con todas las letras del abecedario en minúsculas.  
   - **Función**: Validar que el jugador ingrese solo letras válidas.

2. **`dibujo_ahorcado`** (dentro de `jugar_ahorcado()`)  
   - **Uso**: Lista de strings con dibujos ASCII del ahorcado.  
   - **Función**: Mostrar visualmente el estado del ahorcado en cada turno.

3. **`palabras_faciles`, `palabras_medias`, `palabras_dificiles`, `palabras_imposibles`**  
   - **Uso**: Listas de palabras clasificadas por dificultad.  
   - **Función**: Seleccionar la palabra secreta según la dificultad elegida.

---

#### **Funciones:**
1. **`mostrar_estado(intentos, letras_descartadas, palabra_oculta, dibujo_ahorcado, dificultad)`**  
   - **Uso**: Muestra el progreso del juego (intentos, letras incorrectas, palabra oculta y dibujo).  
   - **Detalle**: Usa `join()` para formatear la salida.

2. **`letra_valida(letra, lista_abecedario, palabra_oculta, letras_descartadas)`**  
   - **Uso**: Valida que la letra ingresada sea única, esté en el abecedario y no se haya usado antes.  
   - **Retorna**: `True` si es válida, `False` si no.

3. **`actualizar_palabra(letra, palabra_secreta, palabra_oculta)`**  
   - **Uso**: Reemplaza los `_` en `palabra_oculta` por la letra adivinada.  
   - **Detalle**: Modifica `palabra_oculta` directamente (no retorna nada).

4. **`seleccionar_dificultad()`**  
   - **Uso**: Pide al jugador elegir dificultad y asigna intentos correspondientes.  
   - **Retorna**: Tupla `(dificultad, intentos)`.

5. **`obtener_palabra(dificultad)`**  
   - **Uso**: Elige aleatoriamente una palabra de la lista según la dificultad.  
   - **Retorna**: La palabra secreta (string).

6. **`jugar_ahorcado()`**  
   - **Uso**: Función principal que orquesta el juego (bucle de turnos, mensajes, reinicio).  
   - **Detalle**: Llama a las demás funciones y maneja la lógica del juego.

