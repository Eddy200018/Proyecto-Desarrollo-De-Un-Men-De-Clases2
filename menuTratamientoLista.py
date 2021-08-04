from menuOperacionNumeros import Intermedio

class Lista(Intermedio):

    def __init__(self,lista):
        self.lista=lista


    def PresentarLista(self):
        for dt in self.lista:
            print (dt)


    def buscarlista(self,buscado):
        for pos,ele in enumerate(self.lista):
            if ele == buscado: return pos

    def listafactorial(self):
        listfac=[]
        for ele in self.lista:
            listfac.append(self.factorial(ele))
        return listfac
    
    def listaPrimo(self):
        listprim=[]
        for ele in self.lista:
            if self.primo(ele) == 2:
                listprim.append(ele)
        return listprim

    def listaNotas(self,listaNotasDiccionario):
        for ele in listaNotasDiccionario:
            print (ele)


    def insertarLista(self,valor,pocision):
        auxlista=[]
        auxlista2=[valor]
        for pos,ele in enumerate(self.lista):
            if pocision < pos+1:
                auxlista.append(valor)
                break        
        if auxlista != []: self.lista=self.lista[0:pos]+auxlista +self.lista[pos:]
        else: self.lista=self.lista[0:]+auxlista2
        return self.lista


    def eliminarLista(self,valor):
        for i in range(len(self.lista)-1,-1,-1):
            if self.lista[i] == valor:
                self.lista.pop(i)
        return self.lista


    def retornarValorLista(self,posicion):
        auxlista=self.lista
        if posicion != 0: auxlista=self.lista[:posicion]+self.lista[posicion+1:]
        else: auxlista= self.lista[1:]
        return self.lista[posicion], auxlista
    
    def copiarTuplaLista(self,tupla):
        list=[]
        for ele in tupla:
            list.append(ele)
        return list





    def vueltoLista(self,listaClienteDiccionario):
        for ele in listaClienteDiccionario:
            ele["cambio"]=ele["pago"]-ele["costo"]
        print(listaClienteDiccionario)