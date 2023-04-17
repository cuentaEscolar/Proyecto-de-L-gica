import expressionHandling  as eH
loop_acciones = True

def getVariables():

    loop_comp1 = True
    num_componentes = 0
    loop_agregar = True
    loop_comp = True
    while (loop_comp1 == True):
        print(f"Ingrese su componente nr. {num_componentes+1}")
        comp1 = input().upper()
        
        if (('A' <= comp1 and comp1 <='Z')) :
            loop_comp1 = False


        else:
            loop_comp1 = True



    num_componentes += 1
    lista_componentes = [comp1]         #La lista de componentes contiene 


    while (loop_agregar == True):

        try:    
            print("Desea agregar otro componente? yes or no")
            agregar = input().lower()

            num_componentes += 1
            
            if agregar == "yes":
            
                while (loop_comp == True):
                    print(f"Ingrese su componente nr. {num_componentes}")
                    comp = input().upper()

                    if (('A' <= comp and comp <= 'Z')):
                        lista_componentes.append(comp)
                        break

                    else:
                        loop_comp = False


            elif agregar == "no":
                loop_agregar = False

        
        except agregar != "yes" or agregar != "no":
                continue
    
    
    return lista_componentes

# lista_componentes = getVariables()

def generateExpresions(lista_componentes):
    lista_expresiones =[]
    while (loop_acciones == True):
        print(lista_componentes)
        print("\t1) Conjuncion ^\n"
            "\t2) Disyuncion V\n"
            "\t3) Implicacion ->\n"
            "\t4) Doble Implicacion <->\n"
            "\t5) Negacion ~\n"
            "\t6) Salir \n")


        print("Que desea hacer con sus componentes?\n")
        try:
            accion = int(input())
            if True:
                # if accion == 1:
                #     while True:
                #         print("Ingrese la posicion del componente al que quiere aplicar esta accion\n")
                #         indice = int(input()) - 1
                #         alteracion = lista_componentes[indice]
                #         #lista_componentes[indice] = ~ alteracion

                # elif accion == 2:
                #     while True:
                #         print("Ingrese la posicion del componente al que quiere aplicar esta accion\n")
                #         indice = int(input()) - 1
                #         alteracion = lista_componentes[indice]

                # elif accion == 3:
                #     while True:
                #         print("Ingrese la posicion del componente al que quiere aplicar esta accion\n")
                #         indice = int(input()) - 1
                #         alteracion = lista_componentes[indice]

                # elif accion == 4:
                #     while True:
                #         print("Ingrese la posicion del componente al que quiere aplicar esta accion\n")
                #         indice = int(input()) - 1
                #         alteracion = lista_componentes[indice]


                # elif accion == 5:
                #     while True:
                #         print("Ingrese la posicion del componente al que quiere aplicar esta accion\n")
                #         indice = int(input()) - 1
                #         alteracion = lista_componentes[indice]
                #         lista_expresiones.append(eH.expressionGenerator("", alteracion, eH.operatorStringGenerator(accion)))
                        
                # elif accion == 6:
                #     break
                pass
            if accion==6: return lista_expresiones
            if accion!=5 :
                print("Ingrese la posicion del primer componente\n")
                comp1In = int(input()) - 1
                comp1 = lista_componentes[comp1In]

                print("Ingrese la posicion del segundo componente\n")
                comp2In = int(input()) - 1
                comp2 = lista_componentes[comp2In]

                lista_expresiones.append(eH.expressionGenerator(comp1, comp2, eH.operatorStringGenerator(accion)))
            else:
                print("Ingrese la posicion del componente\n")
                indice = int(input()) - 1
                alteracion = lista_componentes[indice]
                lista_expresiones.append(eH.expressionGenerator("", alteracion, eH.operatorStringGenerator(accion)))
        except ValueError:
            continue

        # print(lista_expresiones)
    
    return lista_expresiones





