def operaciones_matematicas(a,b):
    def suma(a,b):
        """
        Returns:
            La suma de a y b
        """
        return a+b
    
    def resta(a,b):
        """
        Returns:
            La resta de a y b
        """
        return a-b
    
    def multiplicacion(a,b):
        """
        Returns:
            La multiplicacion de a y b
        """
        return a*b
    
    def division(a,b):
        """
        Returns:
            La division de a y b
        """
        return a/b
    
    
    print ("El resultado de la suma es", suma(a,b))
    print ("El resultado de la resta es", resta(a,b))
    print ("El resultado de la multiplicacion es", multiplicacion(a,b))
    print ("El resultado de la division es", division(a,b))   