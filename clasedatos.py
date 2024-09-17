class informacion:
    def milista(self):
        lista_noperros=["boby","dollar","fany"]
        for x in lista_noperros:
            print(x)
#creando el objeto
datos=informacion()
print("listado de nombres de perros:")
datos.milista()

class colors:
    def mitupla(self):
        arcoiris=("azul","verde","rojo","amarillo")
        print(arcoiris)
        for x in arcoiris:
            print(x)
#creando el objeto
datos=colors()
print("listado de colores: ")
datos.mitupla()

class datos:
    def midiccionario(self):
        yo = {
            "id" : 1234,
            "nombre": "diana",
            "edad": 16,
            "especialidad": "programacion"
        }
        for x, y in yo.items():
            print(x, y)
#creando el objeto
datos=datos()
print("listado informacion: ")
datos.midiccionario()

class numeros:
    def miconjunto(self):
        conjunto_numeros = {16, 17, 20}
        for x in conjunto_numeros:
            print(x)
#creando el objeto
datos=numeros()
print("listado de numeros: ")
datos.miconjunto()
