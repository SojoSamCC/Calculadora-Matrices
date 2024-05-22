import numpy as np
import sys
print()
print("¡BIENVENIDO A LA PRIMERA CALCULADORA PERFECTA PARA EL CBC (CALCULADORA CBCIANA)!")
print()
print("Esta sección de la calculadora fue diseñada para poder verificar/corroborar tus resultados al escalonar matrices")
print("de sistemas lineales homogeneos de nxm.")
print("Su creador no se hace responsable por el uso indebido de la misma.")
print("Ante cualquier problema en su utilización, advertencia de un mal cálculo realizado, ó simplemente desea compartir")
print("alguna sugerencia, por favor enviar mail a academicsamuel02@gmail.com")
print()
print("Si deseas ver otros proyectos relacionados con la calculadora cbciana entra a:")
print()
print("https://github.com/SojoSamCC/CALCULADORA-CBCIANA.git")
print()
print()
print("Si deseas apoyarme te dejo mi link de cafecito: https://cafecito.app/teloexplicoencbc")
print()
print("Sin nada más que agregar, te dejo con la calculadora.")
print()
print("Atte. su creador")
print("-SojoSam")
print()
for i in range (100):
      print("-", end="")
print()
print()
while True:
      ecuaciones= int(input("Ingresa cantidad de ecuaciones (en número y no en letras): "))
      print()
      incognitas= int(input("Ingresa cantidad de incognitas (en número y no en letras): "))
      matriz= np.repeat(0,incognitas*ecuaciones)
      matriz=matriz.reshape(ecuaciones,incognitas)
      ordenar_matriz_cond=True

      for i in range(ecuaciones):
            for j in range(incognitas):
                  print()
                  valor_incognita = float(input(f"Ingrese el valor del coeficiente de la incógnita {j + 1} en la ecuación {i + 1}: "))
                  matriz[i][j] = valor_incognita
      
      print(matriz)
      def multiplicar_por_un_escalar_fila():
            print()
            fila=int(input("Ingrese la fila a multiplicar por un escalar: "))
            print()
            escalar=float(input("Ingrese el escalar para multiplicar: "))
            for j in range (incognitas):
                  matriz[(fila-1,j)]=matriz[(fila-1,j)]*escalar
            return matriz

      def operar_una_fila_con_otra_fila():
            print()
            fila_principal=int(input("Ingrese el número de fila que va a ser sumada o restada con otra fila: "))
            print()
            fila_secundaria=int(input("Ingrese el número de la otra fila que va a participar en la operación: "))
            print()
            print("- -")
            print("INSTRUCCIONES PARA ASIGNAR OPERADOR ENTRE LAS FILAS")
            print()
            print('·)SUMA: ingrese "SUMA" o "Suma" o "+"')
            print("·)RESTA: ingrese cualquier otro valor diferente a los de SUMA.")
            print("- -")
            print()
            operacion=input("Ingrese la operación a ser realizada entre ambas filas: ")
            if (operacion=="SUMA" or operacion=="Suma" or operacion=="+"):
                  for i in range(incognitas):
                        matriz[(fila_secundaria-1,i)]=matriz[(fila_secundaria-1,i)]+matriz[(fila_principal-1,i)]
            else:
                  for j in range(incognitas):
                        matriz[(fila_secundaria-1,j)]=matriz[(fila_secundaria-1,j)]-matriz[(fila_principal-1,j)]
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
            print()
            condicion3=input("¿Deseas ordenar la matriz? (Y/n): ")
            if (condicion3!="n"):
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
                  condicion_multiplicar_por_escalar=True
                  condicion_dividir_por_escalar=True
                  condicion_operar_una_fila_con_otra=True
                  while condicion_operar_una_fila_con_otra!=False:
                        while condicion_multiplicar_por_escalar==True or condicion_dividir_por_escalar==True:
                              print()
                              condicion_multiplicar_por_escalar=input("¿Desea multiplicar una fila por algún escalar? (Y/n): ")
                              if (condicion_multiplicar_por_escalar!="n"):
                                          print()
                                          multiplicar_por_un_escalar_fila()
                                          print(matriz)
                                          condicion_multiplicar_por_escalar=True
                              else:
                                    condicion_multiplicar_por_escalar=False

                              print()
                              condicion_dividir_por_escalar=input("¿Desea dividir una fila por algún escalar diferente de 0 (Y/n): ")
                              if (condicion_dividir_por_escalar!="n"):
                                    print()
                                    dividir_una_fila_entre_un_escalar()
                                    print(matriz)
                                    condicion_dividir_por_escalar=True
                              else:
                                    condicion_dividir_por_escalar=False
                  
                        print()
                        condicion2=input("¿Desea operar una fila con otra? (solo es válida la suma y resta entre dos filas a la vez) (Y/n): ")
                        if (condicion2!="n"):
                              operar_una_fila_con_otra_fila()
                              print(matriz)
                        else:
                              print()
                              condicion_continuar_operando=input("¿Deseas multiplicar o dividir alguna fila por algún escalar? (Y/n): ")
                              if condicion_continuar_operando=="n":
                                    condicion_operar_una_fila_con_otra=False
                              else:
                                    condicion_operar_una_fila_con_otra=True
                                    condicion_multiplicar_por_escalar=True
                                    condicion_dividir_por_escalar=True
            return matriz
      
      i=1
      j=0
      k=0
      while i <= (ecuaciones-1) or j<=(incognitas-1):
            if i>(ecuaciones-1) or j>(incognitas-1):
                  print()
                  print("La matriz ya está escalonada.")
                  print()
                  i=1
                  j=0
                  k=0
                  break
            else:
                  print()
                  condicion4=input("¿Desea escalonar en automatico? (Y/n): ")
                  if (condicion4!="n"):
                        escalonado=False
                        while escalonado==False:
                              escalonar(i,j,k)
                              i+=1
                              j+=1
                              k+=1
                              if i > (ecuaciones-1) or j>(incognitas-1):
                                    escalonado=True
                              else:
                                    escalonado=False
                        print()
                        print(matriz)
                  else:
                        while i <= (ecuaciones-1) or j<=(incognitas-1):
                              if i>(ecuaciones-1) or j>(incognitas-1):
                                    print()
                                    print("La matriz ya está escalonada.")
                                    print()
                                    i=1
                                    j=0
                                    k=0
                                    break
                              else:
                                    print()
                                    condicion4=input("¿Desea escalonar en semiautomático? (Y/n): ")
                                    if (condicion4!="n"):
                                          escalonar(i,j,k)
                                          print(matriz)
                                          i+=1
                                          j+=1
                                          k+=1
                                    else:
                                          cond_esc_a_mano=True
                                          while cond_esc_a_mano==True:
                                                print()
                                                condicion5=input("¿Deseas escalonar a mano? (Y/n): ")
                                                if (condicion5!="n"):
                                                      escalonar_a_mano()
                                                      print(matriz)
                                                else:
                                                      break
                                          break
                        break


      # while i <= (ecuaciones-1) or j<=(incognitas-1):
      #       if i>(ecuaciones-1) or j>(incognitas-1):
      #             print()
      #             print("La matriz ya está escalonada.")
      #             print()
      #             i=1
      #             j=0
      #             k=0
      #             break
      #       else:
      #             print()
      #             condicion4=input("¿Desea escalonar en semiautomático? (Y/n): ")
      #             if (condicion4!="n"):
      #                   escalonar(i,j,k)
      #                   print(matriz)
      #                   i+=1
      #                   j+=1
      #                   k+=1
                        
      #             else:
      #                   break
      
      # while cond_esc_a_mano==True:
      #       print()
      #       condicion5=input("¿Deseas escalonar a mano? (Y/n): ")
      #       if (condicion5!="n"):
      #             escalonar_a_mano()
      #             print(matriz)
      #       else:
      #             break
      #       break

      print()
      print("___________________________________________________________________________________")
      print()
      print("Este programa ya no ofrece más opciones para escalonar :(")
      print()
      print("¡Te invito a que utilices alguna de las opciones disponibles che!")
      print()
      print("Tus opciones son:")
      print()
      print("·)Escalonar alguna matriz.")
      print("·)salir del programa.")
      print()
      cond_seguir1=input("¿Deseas escalonar alguna matriz? (Y/n): ")
      if cond_seguir1!="n":
            print()
            print("¡Yay!")
            print()
            print("¡Entonces sigamos! :)")
            print()
            print()
            print("Por favor introduce una matriz que desees escalonar.")
            print()
      else:
            print()
            print("Bueeeno ¡Muchas gracias por utilizar la calculadora Cbciana para matrices! :D")
            print()
            print("Trataré de agregar más funciones con el paso del tiempo (cálculo de determinante, con parámetros, etc.).")
            print()
            print("Te invito a que también utilices la sección de 'Calculadora resolvente' (perfecta para física).")
            print()
            input("¡Un abrazo enorme! Puedes presionar cualquier tecla para cerrar el programa.")
            sys.exit()
