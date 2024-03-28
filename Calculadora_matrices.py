import numpy as np
import sys
print("¡BIENVENIDO A LA PRIMERA CALCULADORA PERFECTA PARA EL CBC (CALCULADORA CBCIANA)!")
print("")
print("Esta sección de la calculadora fue diseñada para poder verificar/corroborar tus resultados al escalonar matrices")
print("de sistemas lineales homogeneos de nxm.")
print("Su creador (SojoSam) no se hace responsable por el uso indebido de la misma.")
print("Ante cualquier problema en su utilización, advertencia de un mal cálculo realizado, ó simplemente desea compartir")
print("alguna sugerencia, por favor enviar mail a iamsamuelsojo@gmail.com")
print("")
print("Si deseas apoyarme te dejo mi alias: sojo.sam.mp")
print("")
print("Sin nada más que agregar, te dejo con la calculadora.")
print("")
print("Atte. su creador")
print("-SojoSam")
print("")
print("ACLARACIÓN:")
print("Para responder 'Sí' o  'No' a alguna pregunta, entonces debes presionar '1' para 'Sí' y cualquier otro NÚMERO para 'No")
print("")
while True:
      ecuaciones= int(input("ingresa cantidad de ecuaciones (en número y no en letras): "))
      incognitas= int(input("ingresa cantidad de incognitas (en número y no en letras): "))
      matriz= np.repeat(0,incognitas*ecuaciones)
      matriz=matriz.reshape(ecuaciones,incognitas)
      ordenar_matriz_cond=True

      for i in range(ecuaciones):
            for j in range(incognitas):
                  valor_incognita = float(input(f"Ingrese el valor del coeficiente de la incógnita {j + 1} en la ecuación {i + 1}: "))
                  matriz[i][j] = valor_incognita
      
      print(matriz)
      def multiplicar_por_un_escalar_fila():
            fila=int(input("ingrese la fila a multiplicar por un escalar: "))
            escalar=float(input("ingrese el escalar para multiplicar: "))
            for j in range (incognitas):
                  matriz[(fila-1,j)]=matriz[(fila-1,j)]*escalar
            return matriz

      def operar_una_fila_con_otra_fila():
            fila_principal=int(input("ingrese el número de fila a operar con otra: "))
            fila_secundaria=int(input("ingrese la fila con la que se va a operar: "))
            operacion=int(input("ingrese la operación a ser realizada entre ambas filas (presione 1 para 'suma' ó cualquier otro número para 'resta'): "))
            if (operacion==1):
                  for i in range(incognitas):
                        matriz[(fila_principal-1,i)]=matriz[(fila_principal-1,i)]+matriz[(fila_secundaria-1,i)]
            else:
                  for j in range(incognitas):
                        matriz[(fila_principal-1,j)]=matriz[(fila_principal-1,j)]-matriz[(fila_secundaria-1,j)]
            return matriz

      def restar_una_fila_con_otra_fila(fila_principal,fila_secundaria):
            for i in range(incognitas):
                  matriz[(fila_principal,i)]=matriz[(fila_principal,i)]-matriz[(fila_secundaria,i)]
            return matriz

      def multiplicar_fila_por_escalar(fila_principal,escalar):
            for j in range (incognitas):
                  matriz[(fila_principal,j)]=matriz[(fila_principal,j)]*escalar
            return matriz

      def dividir_una_fila_entre_un_escalar(fila_principal,escalar):
            fila_a_dividir = fila_principal  # Índice de la fila a dividir
            fila_dividida = [elemento / escalar for elemento in matriz[fila_a_dividir]]
            matriz[fila_a_dividir] = fila_dividida
            return matriz

      def ordenar_matriz():
            lista_incognitas_a_guardar=[]
            for i in range(ecuaciones):
                  if matriz[(i,0)]==1:
                        for j in range(incognitas):
                              lista_incognitas_a_guardar.append(matriz[(0,j)])
                              matriz[(0,j)]=matriz[(i,j)]
                              matriz[(i,j)]=lista_incognitas_a_guardar[0]
                              del lista_incognitas_a_guardar[0]
            return matriz

      while ordenar_matriz_cond!=False:
            condicion3=int(input("¿Deseas ordenar la matriz? (Sí/No): "))
            if (condicion3==1):
                  ordenar_matriz()
                  ordenar_matriz_cond=False
                  print(matriz)
            else:
                  ordenar_matriz_cond=False

      def corroborar_columna(incognita):
            posiciones_sin_ceros=[]
            ordenar_matriz()
            for i in range(ecuaciones):
                  if matriz[(i,incognita)]!=0:
                        posiciones_sin_ceros.append((i,incognita))
                  del posiciones_sin_ceros[0]
            return posiciones_sin_ceros

      def escalonar(fila,columna,fila_fija):
            escalonado=False
            ordenar_matriz()
            while (escalonado!=True):
                        for i in range(fila,ecuaciones):
                              for j in range (columna,incognitas):
                                    escalar_fila=matriz[(i,j)]
                                    escalar_fijo=matriz[(fila_fija,j)]
                                    if matriz[((i,j))]!=0:
                                          multiplicar_fila_por_escalar(fila_fija,escalar_fila)
                                          multiplicar_fila_por_escalar(i,escalar_fijo)
                                          restar_una_fila_con_otra_fila(i,fila_fija)
                                          dividir_una_fila_entre_un_escalar(fila_fija,escalar_fila)
                                          escalonado=True
                                          break
                                    else:
                                          escalonado=True
                                          break
            return matriz

      def escalonar_a_mano():
            if cond_esc_a_mano==True:
                  multiplicar_por_un_escalar=True
                  while multiplicar_por_un_escalar!=False:
                        condicion=int(input("¿Desea multiplicar una fila por algún escalar? (Sí/No): "))
                        if (condicion==1):
                                    multiplicar_por_un_escalar_fila()
                                    print(matriz)
                        else:
                              multiplicar_por_un_escalar=False

                        operar_una_fila_con_otra=True
                  while operar_una_fila_con_otra!=False:
                        condicion2=int(input("¿Desea operar una fila con otra? (solo es válida la suma y resta entre dos filas a la vez) (Sí/No): "))
                        if (condicion2==1):
                              operar_una_fila_con_otra_fila()
                              print(matriz)
                        else:
                              operar_una_fila_con_otra=False
            return matriz

      i=1
      j=0
      k=0
      cond_seguir2=True
      while i <= (ecuaciones-1) or j<=(incognitas-1):
            if i>(ecuaciones-1) or j>(incognitas-1):
                  print("La matriz ya está escalonada.")
                  print("")
                  i=1
                  j=0
                  k=0
                  break
            else:
                  condicion4=int(input("¿Desea escalonar en semiautomático? (Sí/No): "))
                  if (condicion4==1):
                        escalonar(i,j,k)
                        print(matriz)
                        i+=1
                        j+=1
                        k+=1
                        
                  else:
                        break
      cond_esc_a_mano=True
      while cond_esc_a_mano==True:
            condicion5=int(input("¿Deseas escalonar a mano? (Sí/No): "))
            if (condicion5==1):
                  escalonar_a_mano()
                  print(matriz)
            else:
                  break
            break

      print("")
      print("___________________________________________________________________________________")
      print("")
      print("Este programa ya no ofrece más opciones para escalonar :(")
      print("")
      print("¡Te invito a que utilices alguna de las opciones disponibles che!")
      print("")
      print("Tus opciones son:")
      print("")
      print("·)Escalonar alguna matriz.")
      print("·)salir del programa.")
      print("")
      cond_seguir1=int(input("¿Deseas escalonar alguna matriz? (Sí/No): "))
      if cond_seguir1==1:
            print("")
            print("¡Yay!")
            print("")
            print("¡Entonces sigamos! :)")
            print("")
            print("")
            print("Por favor introduce una matriz que desees escalonar.")
            print("")
      else:
            print("")
            print("Bueeeno ¡Muchas gracias por utilizar la calculadora Cbciana para matrices! :D")
            print("")
            print("Trataré de agregar más funciones con el paso del tiempo (cálculo de determinante, con parámetros, etc.).")
            print("")
            print("Te invito a que también utilices la sección de 'Calculadora resolvente' (perfecta para física).")
            print("")
            input("¡Un abrazo enorme! Puedes presionar cualquier tecla para cerrar el programa.")
            sys.exit()
