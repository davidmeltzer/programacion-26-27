# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2026/2027
# Archivo: T9_04_funciones/ejercicio-15.py
+

# Create a decorator 'access_control' that only allows a function to run 
# if a global variable user_logged_in = True. Otherwise, print "Access Denied".


def access_control(func):
    # 👉 Your code here
    # Para verificar si una variable existe en el contexto global del script
    # se puede usar la función globals(). Ver: https://docs.python.org/3/library/functions.html#globals
    def wrapper(*args, **kwargs):
        if globals().get('user_logged_in') == True:
            resultados = func(*args, **kwargs)
        else:
            print("Acceso denegado")
    return wrapper


@access_control
def get_safe_box_content():
    print("Safe box content: [Top Secret Data]")

print("Trying to access safe box content without user_logged_in being defined")
get_safe_box_content()

print("Trying to access safe box content with user_logged_in = False")
user_logged_in = False
get_safe_box_content()

print("Trying to access safe box content with user_logged_in = True")
user_logged_in = True
get_safe_box_content()