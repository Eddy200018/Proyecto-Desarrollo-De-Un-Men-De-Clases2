class Basico:

    def numerosN(self,n1):
        for valor in range(1,n1+1):
            print(valor,end="  ")
        print()


    def multiplo(self, numero):
        for multiplo in range(numero,101):
            if multiplo % numero == 0: print(multiplo,end="  ")
        print()

    
    def divisoresNumeros(self,numero):
        lista=[]
        for divisor in range(1,numero+1):
            if numero % divisor== 0: lista.append(divisor)
        return lista

    
    def primo(self,numero):
        cont=0
        for valor in range(1,numero+1):
            if numero % valor == 0: cont+=1
        return cont


    def perfercto(self,numero):
        cont=0
        for valor in range(1,numero):
            if numero % valor == 0: cont+=valor
        if cont == numero: print("El {} es un número perfecto".format(numero))
        else: print("El {} no es un número perfecto".format(numero))


class Intermedio(Basico):

    def numerosN(self,n):
        acu=0
        for valor in range(1,n+1):
            acu+= valor
        print("La suma de los número del 1 al {} es igual a {}".format(n,acu))


    def factorial(self,numero):
        acu=1
        for valor in range(1,numero+1):
            acu*= valor
        return acu


    def fibonacci(self,n):
        g=[1]
        acu1=0
        acu2=1
        for valor in range(int(n/2)):
            acu1+=acu2
            acu2+=acu1
            if len(g) < n: g.append(acu1)
            if len(g) < n: g.append(acu2)
        return g


    def primosGemelos(self,num1,num2):
        if self.primo(num1) == 2 and self.primo(num2) == 2:
            if num1 - num2 == 2 or num2 - num1 == 2: print("{} y {} son primos gemelos".format(num1,num2))
            else: print("{} y {} no son primos gemelos".format(num1,num2))
        else: print("{} y {} no son primos gemelos".format(num1,num2))


    def amigos(self,num1,num2):
        acu1=0
        acu2=0
        for ele in self.divisoresNumeros(num1):
            acu1+=ele
        for ele in self.divisoresNumeros(num2):
            acu2+=ele
        if (acu1-num1)==num2 and (acu2-num2)==num1: print("Los números {} y {} son números amigos".format(num1,num2))
        else: print("Los números {} y {} no son números amigos".format(num1,num2))




if __name__ == "__main":

    n=Basico()
    n.numerosN(12)

    n=Intermedio()
    n.multiplo(12)

    for ele in n.divisoresNumeros(12):
        print(ele,end="  ")
    print("")

    num=int(input("Ingrese el número a verificar: "))
    if n.primo(num) == 2: print("El {} es un número primo".format(num))
    else: print("El {} no es un número primo".format(num))


    n.primo(12),n.primo(7)
    n.perfercto(12),n.perfercto(28)
    n.numerosN(12)
    n.factorial(5)

    for ele in n.fibonacci(8):
        print (ele,end="  ")
    print("")

    a=11
    b=13
    n.primosGemelos(a,b)
    n.amigos(200,58),n.amigos(220,284)