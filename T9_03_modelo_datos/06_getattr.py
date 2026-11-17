# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2026/2027
# Archivo: T9_03_modelo_datos/06_getattr.py


class SecureData:
    def __init__(self):
        self.public = "Public Info"
        self._secret = "Sensitive Data"

    def __getattr__(self, name):  # Se ejecuta solo si el atributo no existe
        if name.startswith("_"):
            raise AttributeError(f"Access to private attribute '{name}' is denied")
        raise AttributeError(f"Attribute '{name}' does not exist")
    def _do_something_private(self):
        return "Doing something private"


obj = SecureData()

print(obj.public)  # Se obtiene el valor del atributo
print(obj._secret)  # __getattr__ no se ejecuta: el atributo existe
# print(obj._missing)  # __getattr__ se ejecuta y deniega el acceso
# print(obj.unknown)  # __getattr__ se ejecuta e indica que el atributo no existe
