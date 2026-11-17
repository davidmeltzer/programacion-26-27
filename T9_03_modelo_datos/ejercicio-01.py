# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2026/2027
# Archivo: T9_03_modelo_datos/ejercicio-01.py


# Dada la codificación incial de la clase Complejo de un ejemplo anterior: 
# 1. añada los métodos __repr__ y __str__ para que las instancias de la clase
# tengan una representación adecuada tanto para desarrolladores como para 
# usuarios finales. 
# 2. Añada también el método que permita usar el operador de suma (+) 
# entre dos números complejos.

class NumeroComplejo:
    pass

a = NumeroComplejo( (1, 2) )
b = NumeroComplejo( (3, -4) )

c = a + b  # Implementa la suma de números complejos
print(f"a = {a}")  # Muestra el valor de a usando __str__
print(f"b = {b}")  # Muestra el valor de b usando __str__
print(f"a + b = {c}")  # Muestra el resultado de la suma usando __str__

repr_objeto = repr(c)
d = eval( repr_objeto ) # La representación devuelta por __repr__ debe permitir (si es posible) recrear el objeto.
print(f"d == c: {d == c}")  # Comprueba que d y c son iguales