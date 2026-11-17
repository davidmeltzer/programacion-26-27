# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2026/2027
# Archivo: T9_03_modelo_datos/01-objeto.caracterizacion.py


class clase_privada:
    pass

obj_1 = clase_privada()
obj_2 = clase_privada()

# Identidad de objeto
print( f"{id(obj_1)=} ({hex(id(obj_1))})" )  # Entero que define identidad (instancia)
print( f"Representación textual: {obj_1=}" )
print( f"{id(obj_2)=} ({hex(id(obj_2))})" )  # Entero que define identidad (instancia)
print( f"Representación textual: {obj_2=}" )

print( f"\n¿Son la misma instancia? {id(obj_1) == id(obj_2)}" )
print( f"¿Son la misma instancia? {obj_1 is obj_2}" )  # El operador 'is' compara identidad

# Tipo de objeto
print( f"\ntype(obj_1) = {type(obj_1)}" )  # Tipo de objeto (clase)
print( f"type(obj_2) = {type(obj_2)}" )  # Tipo de objeto (clase)