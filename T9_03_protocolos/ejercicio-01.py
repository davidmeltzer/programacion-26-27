# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2026/2027
# Archivo: T9_03_protocolos/ejercicio-01.py


# Cree una clase subscriptable que devuelva el cuadrado del índice cuando se utiliza notación con corchetes.

class SquareSubscriptable:
    # 👉 your code here
    def __getitem__(self, indice):
        return indice ** 2

# Sample uses
s = SquareSubscriptable()
print(s[3])   # Output: 9
print(s[5])   # Output: 25
print(s[10])  # Output: 100

# Iterate through the class using a for statement
for i in range(1, 6):
    print(f"{s[i]=}")