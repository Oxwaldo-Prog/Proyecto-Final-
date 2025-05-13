#Definimos mostar estado, este consiste en los datos que se mostraran dependiendo el nivel, palabra o errores segun el avanze del juego, asi como el dibujo grafico de nuetsro juego;
#utilize funciones como capitalize para agregar mayusculas y que tenga mejor presentacion y el join para unir todas las letras que se van descartando segun los errores, y en la palabra oculta para que tambien agrege las letras que se han adivinado 
def mostrar_estado(intentos, letras_descartadas, palabra_oculta, dibujo_ahorcado, dificultad):
    print(f'\nNivel de dificultad: {dificultad.capitalize()}')
    print(f'Intentos restantes: {intentos}')
    print(f'Letras descartadas: {", ".join(letras_descartadas)}')
    print(f'Palabra: {" ".join(palabra_oculta)}\n')
    print(dibujo_ahorcado[6 - intentos])
#Esta funcion de usa return ya que se actualiza conforme se la da uso

#Definimos todo el abesedario para que pueda ser usado mas adelante
lista_abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#Definimos la letra valida la cual mediante if y elif nos da varias respuestas dependiendo el uso incorrectoque se le podria dar el usuario, regresandolo hasta que conteste correctamente lo que se requiere 
def letra_valida(letra, lista_abecedario, palabra_oculta, letras_descartadas):
    if len(letra) != 1:
        print('Has puesto más de una letra, inténtalo de nuevo.')
        return False
    elif letra not in lista_abecedario:
        print('No has introducido una letra del abecedario.')
        return False
    elif letra in palabra_oculta:
        print('La letra ya la has acertado. Intenta con otra.')
        return False
    elif letra in letras_descartadas:
        print('Esa letra ya fue descartada. Intenta con otra.')
        return False
    return True
#Se define la actualizacion de palabra, esta funcion es usada para ir cambiando la palabra oculta con las letras que se van acertando por el usuario, usando a len para devolver el numero de caracteres a la palabra oculta 
def actualizar_palabra(letra, palabra_secreta, palabra_oculta):
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_oculta[i] = letra
#Esta funcion de usa return ya que se actualiza conforme se la da uso

#Definimos la seleccion de dificultad, con la cual se de un menu de eleccion y con elif´s, segun la respuesta del usuario nos manda la informacion correcta al juego, 
#En este caso selecciona un numero de intentos 
def seleccionar_dificultad():
    print("Selecciona nivel de dificultad:")
    print("1. Fácil (8 intentos, palabras cortas)")
    print("2. Medio (6 intentos, palabras normales)")
    print("3. Difícil (4 intentos, palabras largas)")
    print("4. Imposible (2 intentos, palabras complicadas)")
    opcion = input("Introduce 1, 2, 3 o 4: ")
    while opcion not in ["1", "2", "3", "4"]:
        opcion = input("Opción inválida. Introduce 1, 2, 3 o 4: ")

    if opcion == "1":
        dificultad = "facil"
        intentos = 8
    elif opcion == "2":
        dificultad = "medio"
        intentos = 6
    elif opcion == "3":
        dificultad = "dificil"
        intentos = 4
    else:
        dificultad = "imposible"
        intentos = 2

    return dificultad, intentos

#Importamos la libreria de random para que cada que se ejecute el programa se encargue de cambiar la palabra usada 
import random
#Definimos obtener palabra, funcion en la cual dependiendo la dificultad elegida anteriormente saca las palabras de la categoria adecuada
#Estas se separan definidas segun su longitud, y despues se eligen mediante elif´s
def obtener_palabra(dificultad):
    palabras_faciles = ["git", "sql", "php", "css", "html", "web", "api", "dns", "log", "try",
     "java", "perl", "dart", "tipo", "dato", "nulo", "texto", "lista", "tupla"
        ]
    palabras_medias = [
      "funcion", "objeto", "bucle", "ciclo", "decimal", "caracter", "booleano",
     "cadena", "conjunto", "estructura", "logica", "google", "compilar", "python",
     "colab", "cookie", "sesion", "modulo", "binario", "github", "commit", "rama",
     "merge", "clone", "debug", "error", "dominio", "consola", "terminal", "script",
     "backend", "frontend"  
    ]
    palabras_dificiles = [
     "algoritmo", "variable", "operador", "condicional", "retorno", "parametro",
     "argumento", "enumeracion", "herencia", "abstraccion", "interfaz", "libreria",
     "framework", "repositorio", "excepcion", "fullstack", "webservice", "refactorizar",
     "compiladores","optimizacion"   
    ]
    palabras_imposibles = [
     "diccionario", "comparacion", "ejecutar", "javascript", "recursividad",
     "polimorfismo", "encapsulamiento", "autenticacion", "desarrolladora",
     "implementacion", "configuracion", "transcompilador", "infraestructura",
     "serializacion", "multiprocesador"
    ]

    if dificultad == "facil":
        return random.choice(palabras_faciles)
    elif dificultad == "medio":
        return random.choice(palabras_medias)
    elif dificultad == "dificil":
        return random.choice(palabras_dificiles)
    else :
        return random.choice(palabras_imposibles)

#En esta definicion guardamos el dibujo grafico del juego ahorcado para darle mas interes al juego. hice uso de una triple comilla para poder usal mas lineas sin problema, asi como separe cada dibujo con comas 

def jugar_ahorcado():
    dibujo_ahorcado = [
        '''
           +---+
           |   |
               |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
        '''
    ]
#Esta funcion de usa return ya que se actualiza conforme se la da uso
