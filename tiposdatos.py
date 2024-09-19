print("Clases v2 Camila Rodriguez")
# zona de clase
class Datos:
    # el constructor
    def __init__(self,estatura,peso):
        self.estatura=estatura
        self.peso=peso
    def mostrar_datos(self):
        print(f"Estatura: {self.estatura} mts,  Peso: {self.peso} Kg")
    def mi_lista(self):
        colores=["Morado","Amarillo","Rojo"]
        print(colores)
        for co in colores:
            print(co)
            
    def mi_tupla(self):
        dias=("viernes","sabado","domingo")
        print(dias)
        for d in dias:
            print(d)
            
    def mi_diccionario(self):
        pais = {
            "Nombre": "Mexico",
            "Idioma": "Español",
            "Continente": "America"
        }
        print(pais)
        for m, x in pais.items():
            print(m,x)
            
# creacion de objeto
info=Datos(1.75,70.5)

# utilizando el obj --> info
info.mostrar_datos()
print("Lista de colores Camila Rodriguez")
info.mi_lista()
print("Tupla de dias")
info.mi_tupla()
print("Diccionario de pais")
info.mi_diccionario()