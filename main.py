

datos_entrada = """fecha,producto,cantidad,precio_unitario
2026-01-01,Laptop,2,15000.00
2026-01-02,Mouse,10,250.00
2026-01-03,Laptop,1,14500.00
2026-01-04,Teclado,tres,800.00
2026-01-05,Mouse,8,abc.00"""

lineas = datos_entrada.strip().split('\n')

productos = {}

for linea in lineas[1:]:  # Desde la segunda linea
    partes = linea.split(',')
    
    #comprueba que haya cuatro columnas
    if len(partes) != 4:
        continue
    fecha = partes[0]
    producto = partes[1]
    #ignorando cantidades y precios invalidos
    try:
        cantidad = int(partes[2])
        precio = float(partes[3])
    except ValueError:
        continue
    if producto not in productos:
        productos[producto] = {
            "unidades": 0,
            "ingreso": 0.0
        }
    "Acumulando"
    productos[producto]["unidades"] += cantidad
    productos[producto]["ingreso"] += cantidad * precio

print(productos)


    
