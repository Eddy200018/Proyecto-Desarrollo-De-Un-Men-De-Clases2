class Cadena:
    def __init__(self,cadena):
        self.cad = cadena

    def recorrerCadena(self):
        for ele in self.cad:
            print(ele)
            
    def  buscarCaracter(self,buscado):
            for pos,ele in enumerate(self.cad):
                if ele == buscado: return pos

            

    def  listaPosiciones(self,caracter):
        lista=[]
        for pos, ele in enumerate(self.cad):
            if ele == caracter:
                lista.append(pos)
        return lista

    def listaPalabras(self):
        return self.cad.split(" ")

    
    def cadenaLista(self):
        cadena=""
        for ele in self.cad:
            cadena+=ele+" "
        return cadena


    def insertarDato(self,buscado,posicion):
        auxcadena=""
        auxcadena2=" "+buscado
        for pos in enumerate(self.cad):
            if posicion < pos+1:
                auxcadena= buscado + " "
                break
        if auxcadena != "":
            self.cad = self.cad[0:pos]+ auxcadena + self.cad[pos:]
        else :
            self.cad= self.cad[0:]+auxcadena2
        return self.cad

        
    def eliminarOcurrencias(self,buscado):
        self.cad = self.cad.lower().replace(buscado,"")
        return self.cad


    def retornaValor(self,posicion):
        cadena2=self.cad
        cadena2=self.cad.replace(self.cad[posicion],"",1)
        print("La cadena sin el valor eliminado es {}".format(cadena2))
        return self.cad[posicion]


    def concatenarCadena(self,dato):
        self.cad = self.cad + " " + dato
        return self.cad






# cad=input("Ingrese la frase: ")
# busca=input("Ingrese la frase que desea concatenar: ")
# n=Cadena(cad)
# print("La frase completa de la cadena es {}".format(n.concatenarCadena(busca)))
     

# rec=input("ingrese la cadena xd:")
# bus=input("ingrrese la variables: ")
# cad = Cadena(rec)
# cad.buscarCaracter(bus)