class Calculadora:
    def __init__(self, numero1, numero2):
         self.num1 = numero1
         self.num2 = numero2
         
    def suma(self):
         return self.num1 + self.num2
     
    def resta(self):
         return self.num1 - self.num2
     
    def mutiplicacion(self):
        mul= self.num1 * self.num2
        return mul
     
    def división(self):
         return self.num1 / self.num2
     
class calEstandar(Calculadora):
    def __init__(self, num1, num2):
        super().__init__(num1,num2)
    def mutiplicacion(self):
         return self.num1*self.num2
    def exponente(self, base, exp):
        resp = 1
        while exp > 0:
            resp = resp*base
            exp -= 1
        return resp
        
    def valorAbsoluto(self,numero):
        if numero < 0:
            numero = numero * -1
        return numero
    
class calCientifica(Calculadora):
    def __init__(self, numero1, numero2):
        super().__init__(numero1,numero2)
    def  circunferencia(self, radio):
        PI = 3.1416
        cif = 2 * radio * PI 
        return cif
    def areaCirculo(self, radio):
        PI = 3.1416
        area = PI * radio ** 2 
        return area
    
    def areaCuadrado(self, lado):
        area = lado * lado
        return area
        
        



