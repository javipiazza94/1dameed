class circulo():
    def __init__(self,radio):
        self.radio=radio

    @property
    def radio(self):
        print("Estoy dando el radio")
        return self._radio    

    @radio.setter
    def radio(self,radio):
        if radio>=0:
            self._radio = radio
        else:
            raise ValueError("Radio positivo")
            self._radio = 0
            
    @radio.deleter
    def radio(self):
        del self._radio
        
    def __str__(self):
        clase = type(self).__name__
        msg = "{0} de radio {1}"
        return msg.format(clase, self.radio)

    def __repr__(self):
        clase = type(self).__name__
        msg = "{0}({1})"
        return msg.format(clase, self.radio)
                          
    def __eq__(self,otro):
        return self.radio==otro.radio
    
    def __add__(self,otro):
        self.radio+=otro.radio

    def __sub__(self,otro):
        if self.radio-otro.radio>=0:
            self.radio-=otro.radio
        else:
            raise ValueError("No se pueden restar")
    
        """La clase circulo define un objeto que representa un círculo y tiene las siguientes características:
            El constructor de la clase __init__ recibe un parámetro radio y lo asigna a un atributo de instancia self.radio.
            La propiedad radio permite acceder al atributo de instancia _radio y añade una función que imprime "Estoy dando el radio" cada vez que se accede a ella.
            El decorador @radio.setter define un método que se ejecuta cada vez que se intenta asignar un valor al atributo de instancia self.radio. En este caso, comprueba que el valor sea mayor o igual a cero y, en caso contrario, lanza una excepción ValueError.
            El decorador @radio.deleter define un método que se ejecuta cada vez que se llama a la función del para eliminar el atributo radio.
            El método __str__ devuelve una cadena de texto que indica el tipo de objeto y su radio.
            El método __repr__ devuelve una cadena de texto que permite representar al objeto de forma unívoca.
            El método __eq__ permite comparar dos objetos de tipo circulo y devuelve True si tienen el mismo radio.
            El método __add__ permite sumar el radio de dos objetos de tipo circulo.
            El método __sub__ permite restar el radio de dos objetos de tipo circulo siempre y cuando el resultado sea mayor o igual a cero. Si el resultado es negativo, lanza una excepción ValueError.
                    """