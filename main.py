BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

import random
puntaje = random.randint(0, 70)

import time
iniciar_trivia = True
intentos = 0

print("\033[33m¡BIENVENIDO A MI TRIVIA CINÉFILO!\033[39m")

time.sleep(1)
print("\033[31m\nPondremos a pruba tu SABIDURIA\n\033[39m")
time.sleep(1)
nombre=input("\033[34mEscribe tu nombre:\033[39m")
edad=input("\033[34mIngresa tu edad:\033[39m")
pelicula=input("\033[34m¿Cual es tu pelicula ó serie favorita?:\033[39m")

print("\033[32m\n¡Genial!\033[39m",nombre,"\033[39m\n")
time.sleep(1)
pelicula=input("\033[33m¿Estas listo para la aventura?:\033[39m")
print("\n")
print("\033[32mResponde las siguientes preguntas respondiendo con letra MINUSCULA de la alternativa correcta y presiona ENTER para enviar tu respuesta:\n\033[39m")
print("\n")
for numero_carga in range(3, 0, -1):
    print(numero_carga, "...")
    time.sleep(1)
while iniciar_trivia == True: 
   intentos += 1
   print("\n\033[33mIntento número:", intentos)
   input("Presiona Enter\033[39m")
   time.sleep(1)
   print("\n")
   print(GREEN + "comenzaras con :", puntaje, "puntos\n" + RESET)
   time.sleep(2)
   print(RED + "Pregunta 1\n")
   print("\033[36m1)¿Que pelicula gano el OSCAR el 2021? \033[39m\n")
  
   print("a) Nomadland")
   print("b) Sound of Metal")
   print("c) Mank")
   print("d) Minari")
   respuesta_1 = input(GREEN+"\nTu respuesta: "+RESET)
   time.sleep(1)
   while respuesta_1 not in ("a", "b", "c", "d"):
         respuesta_1 = input(
             "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
   if respuesta_1 == "a":
      puntaje += random.randint(5, 30)
      print("\n\033[33nMuy bien", nombre, "! Sigue asi!\033[39m")
   else:
        puntaje -= random.randint(1, 10)
        print(RED + "\nNo es la Respuesta correcta", nombre, "!" + RESET)
   print(YELLOW + "\nWow!", nombre, "vas obteniendo",
          puntaje, "puntos en mi trivia" + RESET)  

   time.sleep(3)
   print(RED + "\nPregunta 2\n")
   time.sleep(2)
   print("\033[36m\n2) ¿Cuál pelicula fue taquillera en el 2021?\033[39m\n")
   print("a) No Time to Die")
   print("b) Hi, Mom")
   print("c) Spider-Man: No Way Home")
   print("d) The Battle at Lake Changjin")
   respuesta_2 = input(GREEN+"\nTu respuesta: "+RESET)
   time.sleep(1)
   while respuesta_2 not in ("a", "b", "c", "d"):
         respuesta_2 = input(
             "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
   if respuesta_2 == "c":
      puntaje += random.randint(5, 30)
      print("\n\033[33nExcelente", nombre, "! Lo estas haciendo bien!\033[39m")
   else:
        puntaje -= random.randint(1, 10)
        print(RED + "\nNo es la Respuesta correcta", nombre, "!" + RESET)
   print(YELLOW + "\nWow!", nombre, "vas obteniendo",
          puntaje, "puntos en mi trivia" + RESET)
  
   time.sleep(3)
   print(RED + "\nPregunta 3\n")
   time.sleep(2)
   print("\033[36m\n3) ¿Cuál es la pelicula mas taquillera de la historia del cine?\033[39m\n")
   print("a) Star Wars: The Force Awakens")
   print("b) Avatar")
   print("c) Avengers: Endgame")
   print("d) Titanic")
   respuesta_3 = input(GREEN+"\nTu respuesta: "+RESET)
   time.sleep(1)
   while respuesta_3 not in ("a", "b", "c", "d"):
         respuesta_3 = input(
             "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
   if respuesta_3 == "d":
        puntaje -= random.randint(1, 10)
        print(RED + "Incorrecto!", nombre,
              "La pelicula Titanic recaudo 2202 millones de dolares hasta el dia de hoy."+RESET)
   elif respuesta_3 == "c":
        puntaje -= random.randint(1, 10)
        print(RED + "Incorrecto!", nombre,
              "La pelicula Avengers: Endgame recaudo 2797 millones de dolares."+RESET)
   elif respuesta_3 == "a":
        puntaje -= random.randint(1, 10)
        print(RED + "Incorrecto!", nombre,
              "La pelicula Star Wars:The Force Awakens recaudo 2066 millones de dólares."+RESET)
   elif respuesta_3 == "b":
        puntaje += 50
        print(GREEN + "Impresionante!: La pelicula mas taquillera y vista de la historia es AVATAR recaudando 2800 millones de dólares." + RESET)
   else:
        puntaje += random.randint(5, 20)
        print("Muy bien", nombre, "!" + RESET)
   print(YELLOW + "\nHola", nombre, "vas obteniendo",
          puntaje, "puntos en mi trivia" + RESET)

   print("\n\033[31mÚLTIMA PREGUNTA\033[329m,\033[33m ¡Tú puedes!\033[37m\n")
   time.sleep(3)
   print(RED + "\nPregunta 4\n")
   time.sleep(2)
   print("\033[36m\n4) ¿Quien es el actor que ha ganado más OSCARS en la historia del cine?\033[39m\n")
   print("a) Tom Cruise")
   print("b) Brad Pitt")
   print("c) Katharine Hepburn")
   print("d) Charlize Theron")
   respuesta_4 = input(GREEN+"\nTu respuesta: "+RESET)
   time.sleep(1)
   while respuesta_4 not in ("a", "b", "c", "d","z"):
         respuesta_4 = input(
             "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
   if respuesta_4 == "d":
        puntaje -= random.randint(1, 5)
        print(RED + "Incorrecto!", nombre,
              "uff casi cerca, pero THERON solo tiene UN OSCAR."+RESET)
   elif respuesta_4 == "b":
        puntaje -= random.randint(1, 5)
        print(RED + "Casi cerca pero es Incorrecto!", nombre,
              "Por que actualmente solo posee UN OSCAR."+RESET)
   elif respuesta_4 == "a":
        puntaje -= random.randint(1, 5)
        print(RED + "Incorrecto!", nombre,
              "TOM no posee ningún OSCAR hasta el momento."+RESET)
   elif respuesta_4 == "z":
        puntaje += 50
        print(GREEN + "Impresionante!: Hasta ahora no hay nadie que supere a Katharine Hepburn por que posee 4 OSCARS." + RESET)
   else:
        puntaje += random.randint(5, 45)
        print("Muy bien", nombre, "!" + RESET)
   print(YELLOW + "\nEres un Crack!", nombre, "has obteniendo",
          puntaje, "puntos en mi trivia" + RESET)
   time.sleep(2)
   print("\n¡Prueba tu SUERTE!\n")
   numero_usuario = int(input("Escriba un numero de 1 a 4:"+RESET))
  
   if numero_usuario == 1:
      puntaje = puntaje / 7

   elif numero_usuario == 2:
        puntaje = puntaje + 3

   elif numero_usuario == 3:
        puntaje = puntaje - 9
   else:
        numero_usuario == 4
        puntaje = puntaje * 5
   time.sleep(1)
   print(YELLOW + "\nImpresionante", nombre,
          "por jugar mi trivia, alcanzaste", puntaje, "puntos" + RESET)
  
   time.sleep(2)
   print("\033[33m\n¡POR TU SABIDURIA TE REGALAMOS UN PREMIO\n"+RESET)
   time.sleep(2)
   print(GREEN + "\4 DATOS CURIOSOS\n"+ RESET)
   print(CYAN+"Las estrellas de Hollywood son una caja de sorpresas. ¿Sabías que Tom Hanks es un pariente lejano de Abraham Lincoln?¿Que Robert Downey Jr. estudió ballet? y ¿Qué Jared Leto y Cameron Diaz estuvieron comprometidos? "+RESET)
   
   print(MAGENTA+"\n¿Deseas intentar nuevamente la trivia?")
   repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: "+RESET).lower()
   
   if repetir_trivia != "si":
        print("\nEspero", nombre,
              "que lo hayas pasado bien, hasta pronto!")
        iniciar_trivia = False
  
   




   
  
  
   


   
  


  







