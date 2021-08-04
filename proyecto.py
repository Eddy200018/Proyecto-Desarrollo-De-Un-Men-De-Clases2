from menuTratamientoLista import Lista
from menu import Menu
import os
from menuOperacionNumeros import Basico, Intermedio
from menuOperacionCadena import Cadena
from menuCalculadora import calEstandar, calCientifica


opcion=1
while opcion != 5:
    men= Menu("Menú Principal",["1) Calculadora","2) Operación Números", "3) Tratameinto de Listas", "4) Operaciones de Cadenas", "5) Salir"])
    opcion= men.menus()
    os.system ("cls")

    if opcion == 1:
        opc1=1
        while opc1 != 10:
            men= Menu("Menú Calculadora", ["1) Suma", "2) Resta", "3) Multiplicación", "4) División", "5) Exponente", "6) Valor Absoluto", "7) Circunferencia", "8) Área Círculo", "9)Área Cuadrado", "10) Salir"])
            opc1= men.menus()
            os.system ("cls")
            if opc1 == 1:
                n1=int(input("ingrese el numero:"))
                n2=int(input("ingrese el numero:"))
                calc = calCientifica(n1,n2)
                print("{} + {} = {}".format(n1,n2,calc.suma()))
                input("Presione ¨ENTER¨ para volver al menú Calculadora")
                os.system ("cls")
            elif opc1 == 2:
                n1=int(input("ingrese el numero:"))
                n2=int(input("ingrese el numero:"))
                calc = calCientifica(n1,n2)
                print(" {} - {} = {}".format(n1,n2,calc.resta()))
                input("Presione ¨ENTER¨ para volver al menú Calculadora")
                os.system ("cls")
            elif opc1 == 3:
                n1=int(input("ingrese el numero:"))
                n2=int(input("ingrese el numero:"))
                calc = calCientifica(n1,n2)
                print("{} * {} = {}".format(n1,n2,calc.mutiplicacion()))
                input("Presione ¨ENTER¨ para volver al menú Calculadora")
                os.system ("cls")  
            elif opc1 == 4:
                n1=int(input("ingrese el numero:"))
                n2=int(input("ingrese el numero:"))
                calc = calCientifica(n1,n2)
                print("{} / {} = {}".format(n1,n2,calc.división()))
                input("Presione ¨ENTER¨ para volver al menú Calculadora")
                os.system ("cls")
            elif opc1 == 5:
                n1=int(input("ingrese la base:"))
                n2=int(input("ingrese el exponente:"))
                est = calEstandar(0,0)
                print("{}^{} = {}".format(n1,n2,est.exponente(n1,n2)))
                input("Presione ¨ENTER¨ para volver al menú Calculadora")
                os.system ("cls")  
            elif opc1 == 6:
                n1=int(input("ingrese el numero:"))
                est = calEstandar(0,0)
                print("El valor absoluto de {} = {}".format(n1,est.valorAbsoluto(n1)))
                input("Presione ¨ENTER¨ para volver al menú Calculadora")
                os.system ("cls")
            elif opc1 == 7:
                radio=int(input("ingrese el Radio:"))
                calc = calCientifica(0,0)
                print("La circunferencia de {} = {}".format(radio,calc.circunferencia(radio)))
                input("Presione ¨ENTER¨ para volver al menú Calculadora")
                os.system ("cls")
            elif opc1 == 8:
                R=float(input("ingrese el radio:"))
                un=input("ingrese la únidad en la que esté expresa el radío: ")
                calc = calCientifica(0,0)
                area = calc.areaCirculo(R)
                print("El área del circulo es de {0:.2f}".format(area),un,"al cuadrado")
                input("Presione ¨ENTER¨ para volver al menú Calculadora")
                os.system ("cls")
            elif opc1 == 9:
                lado=int(input("ingrese un lado del cuadrado: "))
                un=input("ingrese la únidad en la que esté expresa el cuadrado: ")
                calc = calCientifica(0,0)
                print("El área del cuadrado es {0:.2f}".format(calc.areaCuadrado(lado)),un,"al cuadrado")
                input("Presione ¨ENTER¨ para volver al menú Calculadora")
                os.system ("cls")      

    elif opcion == 2:
        opc1=1
        while opc1 != 11:
            men= Menu("Menú Operación Números", ["1) Presentar los números del 1 a n", "2) Sumar los Números del 1 al n", "3) Múltiplo de un Número", "4 )Presentar los Divisores de un Número", "5) Número Primo", "6) Factorial de un Número", "7) Fibonacci de una Serie de n Números", "8) Perfecto", "9) Primos Gemelos", "10) Número Amigos", "11) Salir" ])
            opc1= men.menus()
            os.system ("cls")
            n=Intermedio()
            if opc1 == 1:
                n1=int(input("Ingrese el número límite a presentar: "))
                n = Basico()
                n.numerosN(n1)
                input("Presione ¨ENTER¨ para volver al menú Operación Números")
                os.system ("cls")
            elif opc1 == 2:
                n1= int(input("Ingrese el número límite de la sumatoria: "))
                n.numerosN(n1)
                input("Presione ¨ENTER¨ para volver al menú Operación Números ")
                os.system ("cls")
            elif opc1 == 3:
                n1= int(input("Ingrese el número del que desea obtener sus múltiplos: "))
                print("Los múltiplos de {} son: ".format(n1),end="")
                n.multiplo(n1)
                input("Presione ¨ENTER¨ para volver al menú Operación Números ")
                os.system ("cls")
            elif opc1 == 4:
                n1= int(input("Ingrese el número del que desea obterner sus divisores: "))
                print("Los divisores de {} son: ".format(n1),end="")
                for ele in n.divisoresNumeros(n1):
                    print(ele,end="  ")
                print("")
                input("Presione ¨ENTER¨ para volver al menú Operación Números ")
                os.system ("cls")
            elif opc1 == 5:
                n1= int(input("Ingrese el número a verificar: "))
                if n.primo(n1) == 2: print("El {} es un número primo".format(n1))
                else: print("El {} no es un número primo".format(n1))
                input("Presione ¨ENTER¨ para volver al menú Operación Números ")
                os.system ("cls")
            elif opc1 == 6:
                n1= int(input("Ingrese el número del que desea obtener el factorial: "))
                print("{}! = {}".format(n1,n.factorial(n1)))
                input("Presione ¨ENTER¨ para volver al menú Operación Números ")
                os.system ("cls")
            elif opc1 == 7:
                n1= int(input("Ingrese el límite de la serie: "))
                for ele in n.fibonacci(n1):
                    print (ele,end="  ")
                print("")
                input("Presione ¨ENTER¨ para volver al menú Operación Números ")
                os.system ("cls")
            elif opc1 == 8:
                n1= int(input("Ingrese el número a verificar: "))
                n.perfercto(n1)
                input("Presione ¨ENTER¨ para volver al menú Operación Números ")
                os.system ("cls")
            elif opc1 == 9:
                n1= int(input("Ingrese el primer número: "))
                n2= int(input("Ingrese el segundo número: "))
                n.primosGemelos(n1,n2)
                input("Presione ¨ENTER¨ para volver al menú Operación Números ")
                os.system ("cls")
            elif opc1 == 10:
                n1= int(input("Ingrese el primer número: "))
                n2= int(input("Ingrese el segundo número: "))
                n.amigos(n1,n2)
                input("Presione ¨ENTER¨ para volver al menú Operación Números ")
                os.system ("cls")
                
    elif opcion == 3:
        opc1=1
        while opc1 != 11:
            men = Menu("Menú Tratamiento Listas", ["1) Recorrer y Presentar los Datos de una Lista", "2) Buscar un Valor en una Lista", "3) Retomar una Lista con los Factoriales", "4) Retomar una Lista de Número Primos", "5) Recorrer una lista de Diccionario con notas de Alumnos", "6) Insertar un Dato en una Lista Dada la Posición", "7) Eliminar Todas las Ocurrencias en una Lista", "8) Retomar Cualquier Valor de una Lista Eliminándolo", "9) Copiar Cada Elemeto de una Tupla a una Lista", "10) Dar el Vuelto a Varios Clientes", "11) Salir"])
            opc1= men.menus()
            os.system ("cls")
            if opc1 != 5 and opc1 != 9 and opc1 != 10 and opc1 != 11:
                list= []
                cont=1
                longitud =int(input("Ingrese de cuantos elementos consta su lista: "))
                while cont <= longitud:
                    ele = int(input("Ingrese el elemento {} de su lista: ".format(cont)))
                    list.append(ele)
                    cont+=1
                n = Lista(list)
            if opc1 == 1:
                n.PresentarLista()
                input("Presione ¨ENTER¨ para volver al menú Tratamiento Listas ")
                os.system ("cls")
            elif opc1 == 2:
                buscado=input("Ingrese el valor a buscar: ")
                if buscado in list: print("El caracter {} se encuentra en la pocición {}".format(buscado,n.buscarlista(buscado)))
                else: print("El caracter ingresado no se encuentra en la lista")
                input("Presione ¨ENTER¨ para volver al menú Tratamiento Listas ")
                os.system ("cls")
            elif opc1 == 3:
                print("Factoriales de la lista : {}".format(n.listafactorial()))
                input("Presione ¨ENTER¨ para volver al menú Tratamiento Listas ")
                os.system ("cls")
            elif opc1 == 4:
                print("Los números primos de la listas son: {}".format(n.listaPrimo()))
                input("Presione ¨ENTER¨ para volver al menú Tratamiento Listas ")
                os.system ("cls")
            elif opc1 == 5:
                list= []
                cont=1
                longitud =int(input("Ingrese de cuantos elementos consta su lista: "))
                while cont <= longitud:
                    dicci={}
                    cont2=1
                    longitud2 =int(input("Ingrese de cuantas notas tiene el diccionario número {}: ".format(cont)))
                    while cont2 <= longitud2:
                        if cont2 == 1:
                            nombre=input("Ingrese nombre: ")
                            dicci["nombre"]= nombre
                        n1=int(input("Ingrese la nota numero {}: ".format(cont2)))
                        dicci["n"+str(cont2)]=n1
                        cont2+=1
                    list.append(dicci)
                    cont+=1
                n=Lista(0)
                n.listaNotas(list)
                input("Presione ¨ENTER¨ para volver al menú Tratamiento Listas ")
                os.system ("cls")
            elif opc1 == 6:
                val=int(input("Ingrese el valor a insertar: "))
                pos=int(input("Ingrese la pocición en la que quiere insertar: "))
                print(n.insertarLista(val,pos))
                input("Presione ¨ENTER¨ para volver al menú Tratamiento Listas ")
                os.system ("cls")
            elif opc1 == 7:
                val=int(input("Ingrese la ocurrecia que desea eliminar: "))
                print("Lista sin ocurrencias: ",n.eliminarLista(val))
                input("Presione ¨ENTER¨ para volver al menú Tratamiento Listas ")
                os.system ("cls")
            elif opc1 == 8:
                val=int(input("ingrese la posición del valor a eliminar: "))
                print("Valor eliminado: {}\nLista restante: {}".format(n.retornarValorLista(val)[0],format(n.retornarValorLista(val)[1])))
                input("Presione ¨ENTER¨ para volver al menú Tratamiento Listas ")
                os.system ("cls")
            elif opc1 == 9:
                list= []
                cont=1
                longitud =int(input("Ingrese de cuantos elementos consta su tupla: "))
                while cont <= longitud:
                    ele = int(input("Ingrese el elemento {} de su tupla: ".format(cont)))
                    list.append(ele)
                    cont+=1
                tup= tuple(list)
                n = Lista(0)
                print("Tupla Ingresada: {} \nLista salinte: {}".format(tup,n.copiarTuplaLista(tup)))
                input("Presione ¨ENTER¨ para volver al menú Tratamiento Listas ")
                os.system ("cls")
            elif opc1 == 10:
                list= []
                cont=1
                longitud =int(input("Ingrese la cantidad de clientes: "))
                while cont <= longitud:
                    dicci={}
                    cont2=1
                    longitud2 = 1
                    while cont2 <= longitud2:
                        nombre=input("Ingrese nombre del Cliente: ")
                        dicci["nombre"]= nombre
                        n1=int(input("Ingrese el valor a pagar: "))
                        dicci["costo"]=n1
                        n2=int(input("Ingrese el pago: "))
                        dicci["pago"]=n2
                        cont2+=1
                    list.append(dicci)
                    cont+=1
                n = Lista(0)
                n.vueltoLista(list)
                input("Presione ¨ENTER¨ para volver al menú Tratamiento Listas ")
                os.system ("cls")
                 
    elif opcion == 4:
        opc1=1
        while opc1 != 10:
            men= Menu("Menú Operaciones de Cadenas", ["1) Recorrer y Presentar los Datos de una Cadena", "2) Buscar un Caracter en una Cadena", "3) Retomar una Lista con las Posiciones Dado un Carácter de la Cadena", "4) Retomar una Lista con Todas las Palabras de una Cadena", "5) Retomar una Cadena a Partir de una Lista", "6) Insertar un Dato en una Cadena Dada la Posición", "7) Eliminar Todas las Ocurrencias en una Cadena", "8) Retomar Cualquier Valor de una Cadena Eliminándolo", "9) Concatenar Cadenas", "10) Salir"])
            opc1= men.menus()
            os.system ("cls")
            if opc1 == 1:
                cad=input("Ingrese la cadena: ")
                n = Cadena(cad)
                n.recorrerCadena()
                input("Presione ¨ENTER¨ para volver al menú Operaciones de Cadenas ")
                os.system ("cls")
            elif opc1 == 2:
                cade=input("Ingrese la cadena: ")
                buscado=input("Ingrese el valor a buscar: ")
                n = Cadena(cade)
                if buscado in cade:
                    print("El caracter {} se encuentra en la pocición {}".format(buscado,n.buscarCaracter(buscado)))
                else: print("El caracter ingresado no se encuentra en la cadena")
                input("Presione ¨ENTER¨ para volver al menú Operaciones de Cadenas ")
                os.system ("cls")
            elif opc1 == 3:
                cad=input("Ingrese la cadena: ")
                caract=input("Ingrese el caracter a buscar: ")
                n=Cadena(cad)
                print(n.listaPosiciones(caract))
                input("Presione ¨ENTER¨ para volver al menú Operaciones de Cadenas ")
                os.system ("cls")
            elif opc1 == 4:
                cad=input("Ingrese la cadena: ")
                n=Cadena(cad)
                print(n.listaPalabras())
                input("Presione ¨ENTER¨ para volver al menú Operaciones de Cadenas ")
                os.system ("cls")
            elif opc1 == 5:
                lista= []
                cont=1
                longitud =int(input("Ingrese cuantos elementos consta en su lista: "))
                while cont <= longitud:
                    ele = input("Ingrese el elemento {} de su lista: ".format(cont))
                    lista.append(ele)
                    cont+=1
                n=Cadena(lista)
                print(lista, "=", n.cadenaLista())
                input("Presione ¨ENTER¨ para volver al menú Operaciones de Cadenas ")
                os.system ("cls")
            elif opc1 == 6:
                caden=input("Ingrese la cadena principal: ")
                buscar=input("Ingrese lo que desee insertar: ")
                posi= int(input("Ingrese la pocición en la que desee insertar: "))
                n=Cadena(caden)
                print(n.insertarDato(buscar,posi))
                input("Presione ¨ENTER¨ para volver al menú Operaciones de Cadenas ")
                os.system ("cls")
            elif opc1 == 7:
                cad=input("Ingrese la frase: ")
                busca=input("Ingrese las ocurrencias: ")
                n=Cadena(cad)
                print(n.eliminarOcurrencias(busca))
                input("Presione ¨ENTER¨ para volver al menú Operaciones de Cadenas ")
                os.system ("cls")
            elif opc1 == 8:
                cad=input("Ingrese la frase: ")
                busca=int(input("Ingrese la posición: "))
                n=Cadena(cad)
                print("El valor eliminado de la cadena es [{}]".format(n.retornaValor(busca)))
                input("Presione ¨ENTER¨ para volver al menú Operaciones de Cadenas ")
                os.system ("cls")
            elif opc1 == 9:
                cad=input("Ingrese la frase: ")
                busca=input("Ingrese la frase que desea concatenar: ")
                n=Cadena(cad)
                print("La frase completa de la cadena es {}".format(n.concatenarCadena(busca)))
                input("Presione ¨ENTER¨ para volver al menú Operaciones de Cadenas ")
                os.system ("cls")


    else: print("Gracias por su visita")