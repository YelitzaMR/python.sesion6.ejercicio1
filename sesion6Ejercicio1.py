class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas

        
class Coche(Vehiculo):
    def __init__(self,color,ruedas, puertas,velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas, puertas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

miCoche = Coche('amarillo', 4, 5, 180, 6)
print ('Color del coche',miCoche.color)
print ('Tiene', miCoche.ruedas, 'ruedas y', miCoche.puertas, 'puertas')
print('Alcanza una velodidad de:',miCoche.velocidad)
print('Tiene', miCoche.cilindrada, 'cilindros')



    
