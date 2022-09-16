trivia = True
import time
import random
nombre = ""
puntaje = 0
puntajeTotal = 0
pregunta = 0
intentos = 0
 
while nombre == "":
  print("╭━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮")
  print("┃╭╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃")
  print("┃╰╯╰┳┳━━┳━╮╭╮╭┳━━┳━╮╭┳━╯┣━━╮")
  print("┃╭━╮┣┫┃━┫╭╮┫╰╯┃┃━┫╭╮╋┫╭╮┃╭╮┃")
  print("┃╰━╯┃┃┃━┫┃┃┣╮╭┫┃━┫┃┃┃┃╰╯┃╰╯┃")
  print("╰━━━┻┻━━┻╯╰╯╰╯╰━━┻╯╰┻┻━━┻━━╯")
  nombre_mst = input ("Indique un sobrenombre antes de iniciar: ")
  nombre = str(nombre_mst.title())
else:
  print("↣ ¡Bienvenido a la prueba de conocimiento, " + nombre + "!")
  time.sleep(2)
  print ("↣ Ganarás puntos aleatorios a medida que vayas respondiendo correctamente.")
  time.sleep(2)
  print ("↣ Recuerda solo escribir la letra de la respuesta que consideres correcta.")
  time.sleep(2)
  print("↣ ¡Empecemos!")
  time.sleep(2)

#Inicio del juego
while trivia == True:
  intentos += 1
  puntaje = 0
  input ("➜ Presiona la tecla Enter para continuar... ")
  time.sleep (1)
  print ("Llevas: ", intentos , " intentos.")
  time.sleep (1)
  
  #Pregunta 1
  pregunta += 1
  print (f'\n {pregunta}. ¿Cuál es la red social más utilizada en todo el mundo? \na) Youtube \nb) Twitter \nc) Facebook \nd) LinkedIn')
  respuesta1 = input ("⇢ Indique su respuesta: ")
  while respuesta1 not in ("a", "b", "c", "d"):
    respuesta1 = input ("✖ Por favor, solo escribe una letra: ")
  if respuesta1 == 'c':
    puntaje = random.randint(0, 50)
    puntajeTotal = puntaje
    print ("✅ ¡Respuesta correcta! Obtienes +", puntaje , " puntos.")
    time.sleep (2)
    print ("🔘 Dato: Facebook tiene más de 2,500 millones de usuarios y sigue creciendo diariamente.")
  else:
    print("❌ ¡Respuesta incorrecta! Sigue intentándolo.")
    
  #Pregunta 2
  pregunta += 1
  time.sleep(2)
  print (f'\n {pregunta}. ¿Quién es actualmente (2022) el presidente del Perú? \na) Pedro Castillo \nb) Ollanta Humala \nc) Alan García \nd) Pedro Pablo Kuczynski')
  respuesta2 = input ("Indique su respuesta: ")
  while respuesta2 not in ("a", "b", "c", "d"):
    respuesta2 = input ("Por favor, solo escribe una letra: ")
  if respuesta2 == 'a':
    puntaje = random.randint(0, 50)
    puntajeTotal = puntajeTotal + puntaje
    print ("✅ ¡Respuesta correcta! Obtienes +", puntaje , " puntos.")
    time.sleep (2)
    print ("🔘 Dato: Pedro Castillo se desempeña como presidente del Perú desde el 28 de julio de 2021 luego de resultar ganador en las elecciones del año 2021.")
  else:
    print("❌ ¡Respuesta incorrecta! Sigue intentándolo.")

  #Pregunta 3
  pregunta += 1
  time.sleep(2)
  print (f'\n {pregunta}. ¿A cuánto equivale 1kg en gramos? \na) 10000g \nb) 10g \nc) 100000g \nd) 1000g')
  respuesta3 = input ("Indique su respuesta: ")
  while respuesta3 not in ("a", "b", "c", "d"):
    respuesta3 = input ("Por favor, solo escribe una letra: ")
  if respuesta3 == 'd':
    puntaje = puntaje + random.randint(0, 50)
    puntajeTotal = puntajeTotal + puntaje
    print ("✅ ¡Respuesta correcta! Obtienes +", puntaje , " puntos.")
    time.sleep (2)
    print ("🔘 Dato: El kilogramo es la unidad básica de masa del Sistema Internacional de Unidades. Es una medida ampliamente utilizada en la ciencia, la ingeniería y el comercio en todo el mundo, y a menudo simplemente se le llama kilo en el habla cotidiana.")
  else:
    print("❌ ¡Respuesta incorrecta! Sigue intentándolo.")
    
  #Pregunta 4
  pregunta += 1
  time.sleep(2)
  print (f'\n {pregunta}. ¿Quién fundó la empresa Microsoft? \na) Bill Gates \nb) Steve Jobs \nc) Richard Stallman \nd) Elon Musk')
  respuesta4 = input ("Indique su respuesta: ")
  while respuesta4 not in ("a", "b", "c", "d"):
    respuesta4 = input ("Por favor, solo escribe una letra: ")
  if respuesta4 == 'a':
    puntaje = puntaje + random.randint(0,50)
    puntajeTotal = puntajeTotal + puntaje
    print("✅ ¡Correcto! \n🔘 Dato: Bill Gates fundó, junto a su compañero, Paul Allen, la gigante empresa Microsoft en el año 1975.")
    print("Obtienes +", puntaje, " puntos.")
  elif respuesta4 == 'b':
    print("❌ ¡Incorrecto! Steve Jobs fundó la conocida empresa Apple.")
  elif respuesta4 == 'c':
    print("❌ ¡Incorrecto! Richard Stallman es creador del proyecto GNU y presidente de la Free Software Foundation.")
  elif respuesta4 == 'd':
    print("❌ ¡Incorrecto! Elon Musk es fundador de varias empresas conocidas en el sector tecnológico, como Tesla.")
    
 #Pregunta para duplicar o perder totalmente los puntos
    
  time.sleep (2)
  print("\n🔔 ¡ATENCIÓN! 🔔")
  time.sleep(2)
  print("\nEstás a punto de finalizar la trivia, pero antes, ¿quiseras dublicar todo tu   puntaje (o perderlo totalmente) con una pregunta más?")
  time.sleep(2)
  resdupli = input ("\n⚠ Solamente responde si o no: ")
  while resdupli not in ("si", "no"):
      resdupli = input ("❗❗ Indique solamente si o no: ") 
  if resdupli == "si":
    print ("\n🌟 ¡Excelente decisión! Presta atención a la pregunta.")
    time.sleep (2)
    pregunta += 1
    print (f'\n {pregunta}. ¿En qué año empezó la Primera Guerra Mundial?')
    respuesta5 = input ("Escriba solamente con números: ")
    if respuesta5 == '1914':
       puntajeTotal = puntajeTotal * 2
       print("\n🎉 ¡Es la respuesta correcta! 🎉")
       time.sleep(2)
       print("💰 ¡FELICIDADES! Acabas de duplicar todo tu puntaje. 💰")
       time.sleep(2)
    else:
       puntajeTotal = puntajeTotal * 0
       print("\n❌ La respuesta es incorrecta.")
       time.sleep(2)
       print("❌ Acabas de perder totalmente tus puntos. Lo siento :(")
       time.sleep(2)
  else:
    print ("💡 Es una buena decisión. ¡Gracias por participar!")
    time.sleep(2)
    
  print("\n▸ Agradezco el tiempo que te tomaste para realizar esta prueba de conocimientos.")
  time.sleep (3)
  print("\n💰 Lograste: ", puntajeTotal , " puntos en total.")
  time.sleep (3)
  print("\n▸ ¿Deseas intentarlo nuevamente?")
  pregunta = 0
  time.sleep (2)
  repetirTrivia = input("\n▸ Escribe si para iniciar nuevamente o, de lo contrario, no para finalizar: ").lower()
  if repetirTrivia != "si":
    time.sleep(2)
    print("\n▸ Gracias por participar, ",nombre,", espero que lo hayas pasado bien, hasta pronto!")
    trivia = False