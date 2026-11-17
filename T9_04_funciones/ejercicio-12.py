# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2026/2027
# Archivo: T9_04_funciones/ejercicio-12.py


# Create a decorator 'timer' that measures how long a function takes to run using time.time()

def timer(func):
    import time
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultados = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo transcurrido={fin-inicio}")
        return resultados
    return wrapper

@timer
def do_work(maximum):
    return sum( (x ** 2 for x in range(maximum)) )

print(do_work(100000))
