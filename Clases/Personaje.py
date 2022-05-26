class Personaje:
    # Se arranca con la definición del constructor, el cual es una función
    def __init__(self):
        # Definición del método
        # pass aveces se verá en los métodos y es un void, es un vacío, mientras se define todo
        # Atributos de la clase, se inician en la función por ejemplo self, nombre, edad
        self.__nombre=None
        self.__edad=None
        
    # Definiendo un método
    # def saludar(self):
    #     print("Hola", self.__nombre)

    # Llamar la clase o instanciar, los objetos son los elementos que usan la clase
    # esto se hace en el main.

    # 123.  En otros lenguajes se usa PROTECTED / PRIVATE / PUBLIC, que son modificadores
    # de acceso de una clase. para python, a continuación se pondrá entre el
    # self. y el atributo un __ y se iguala a None. También se edita el método. Algo
    # similar se requiere en el main .__nombre

    # Empezaremos a definir los encapsulamientos
    # Haremos el getter con @property. El .__ e spars definir privado
    @property
    def nombre(self):
        return(self.__nombre)

    @property
    def edad(self):
        return(self.__edad)
    
    # Haremos el SETTER. Se define con @nombre.setter
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    
    @edad.setter
    def edad(self,edad):
        if(edad<0):
            print("La edad no puede ser negativa")
        else:
            self.__edad=edad