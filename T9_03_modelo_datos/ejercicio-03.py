# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2026/2027
# Archivo: T9_03_modelo_datos/ejercicio-03.py


# Cree la clase MiEnumerador que imite el comportamiento de la función incorporada enumerate().


class MiEnumerador:
    def __init__(self, objeto_iterable, *, inicio_numeracion=0):
        pass
    
    # Añadir los métodos que proceda para que la clase sea iterable y
    # devuelva tuplas (indice, valor) al iterar sobre ella.
    

# Uso explícito del iterador
lista = ['a', 'b', 'c']
enumerador = MiEnumerador(lista, inicio_numeracion=1)
it = iter(enumerador)
print(next(it))  # (1, 'a')
print(next(it))  # (2, 'b')
print(next(it))  # (3, 'c')
# print(next(it))  # Levantaría StopIteration

# Uso con un bucle for
for indice, valor in MiEnumerador(['x', 'y', 'z'], inicio_numeracion=10):
    print(indice, valor)