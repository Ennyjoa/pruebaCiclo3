#--------------- RETO # 3 ---------------------
import os
import time

# -----------------VARIABLES GLOBALES----------

    #------ Reto2 ------

opc1 = "Cambiar contraseña"
opc2 = "Ingresar coordenadas actuales "
opc3 = "Ubicar zona wifi más cercana" 
opc4 = "Guardar archivo con ubicación cercana" 
opc5 = "Actualizar registros de zonas wifi desde archivo" 
opc6 = "Elegir opción de menú favorita"
opc7 = "Cerrar sesión."

contador = 0   # inicia contador de errores 
listaMenu = [opc1, opc2, opc3, opc4, opc5, opc6, opc7]

    #------ Reto1 -------

usuarioGuardado= '52209' #Codigo Grupo de fundamentos de programación
ContrasenaGuardada = 90225
captcha1 = 209
captcha2 = 5+2+2-9 #Operacion del con los numeros del codigo
captcha = captcha1 - captcha2

#---------------END REGION------------------------------

#..... Funciones......

def borrar_pantalla():
    if os.name == 'nt' or os.name == 'ce' or os.name == 'dos':
        os.system('cls')
    if os.name == 'posix':
        os.system('clear')

def listaOriginal():    
    for x in range(len(listaMenu)):
        #f = formato especial - {} = variables
        print(f"{x+1}. {listaMenu[x]}") # Imprime el menú

def ValidacionDatos(dato1, dato2):
    # dato1 = usuario guardado
    # dato2 = usuario ingresado
    if dato1 == dato2:
        return True
    else:
        return False    
    pass

def ReordenarFavorito(posicion):
    mover = listaMenu[posicion - 1]
    listaMenu.remove(mover)
    listaMenu.insert(0, mover)
#.....................



print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

usuarioIngresado = input('Ingrese su Nombre: ')

if ValidacionDatos(usuarioIngresado, usuarioGuardado):

    # Funcion (ContraseñaIngresada, Contraseña Guardada)
    ContrasenaIngresada = int(input('Ingrese su Contraseña: '))
    if ValidacionDatos(ContrasenaIngresada, ContrasenaGuardada):

        revision = int(input(f"Ingrese el resultado de la operación {captcha1} - {captcha2}: ")) # Formato para imprimir un input con valores
        
        if ValidacionDatos (revision, captcha): # revisión del el valor que ingresa el usuarion con el captcha guardado.
            
            borrar_pantalla()
            #os.system("cls")
            print("Sesión Iniciada.")
            time.sleep(2)

#----------------------- Programa principal-----------------------------------------------------------

            
            while contador < 3:    
                
                borrar_pantalla()
                #os.system("cls")
                
                listaOriginal() # Imprime la Lista original de opciónes del Menú
                
                opcionSelecionada = int(input("Elija una opción: ")) #El usuario debe selecionar una opción del Menú
                
                if opcionSelecionada > 0 and opcionSelecionada < 8:
                    
                    opcionElegida = listaMenu[opcionSelecionada - 1]

                    if opcionElegida == opc1:
                        print(f" Usted ha elegido la opción 1")
                        #print(opc1)
                        time.sleep(1)
                        break
                           
                    elif opcionElegida == opc2:
                        print(f" Usted ha elegido la opción 2")
                        #print(opc2)
                        time.sleep(1)
                        break
                        
                    elif opcionElegida == opc3:
                        #print(opc3)
                        print(f" Usted ha elegido la opción 3")
                        time.sleep(1)
                        break
                        
                    elif opcionElegida == opc4:
                        print(f" Usted ha elegido la opción 4")
                        #print(opc4)
                        time.sleep(1)
                        break

                    elif opcionElegida == opc5:
                        print(f" Usted ha elegido la opción 5")
                        #print(opc5)
                        time.sleep(1)
                        break

                    elif opcionElegida == opc6:
                        print(opc6)
                    
                        nuevofavorito = int(input("Seleccione opción favorita: "))
                        borrar_pantalla()
                        if nuevofavorito == 1 or nuevofavorito == 2 or nuevofavorito == 3 or nuevofavorito == 4 or nuevofavorito == 5: 
                            if int(input(f'Para confirmar por favor responda: Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es: ')) == 0 :
                                if int(input(f'Para confirmar por favor responda: Me separaron de mi hermano siamés, antes era un ocho y ahora soy un… la respuesta es: ')) == 9:
                                    
                                    ReordenarFavorito(nuevofavorito)

                                else:
                                    borrar_pantalla()
                                    print("Error") # Error de 2da Adivinanza
                                    quit()

                            else:
                                borrar_pantalla()
                                print("Error") # Error de 1era Adivinanza
                                quit()
                        
                        else:
                            borrar_pantalla()
                            print("Error") # Error de diferente favorito
                            quit()


                    elif opcionElegida == opc7:
                        print(f" Usted ha elegido la opción 7")
                        #print(opc7)
                        time.sleep(1)
                        print("Hasta pronto")
                        quit() # break
                        
                
                else:
                    contador +=1
                    borrar_pantalla()
                    print("Error") # Error de mas de 3 veces
                    continue   

        else:
            print("Error")  # Error de Captcha  
    else:
        print("Error")      # Error de la contraseña Incorrecta
else:
    print("Error")          # Error del Usuario Incorrecta  
    

