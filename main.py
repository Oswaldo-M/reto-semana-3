import sys


def main():
    productos = {}
    primera_linea = True

    for linea in sys.stdin:  
        linea= linea.strip()
        if primera_linea:
            primera_linea = False
            continue

        if not linea:
            continue

        partes = linea.split(',')

        #ingorando lineas invalidas    
        if len(partes) != 4:
            continue
        #parseando la linea
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

        #Calculando el precio promedio por producto
    for producto in productos:
        unidades = productos[producto]["unidades"]
        ingreso = productos[producto]["ingreso"]
        productos[producto]["promedio"] = ingreso/unidades if unidades > 0 else 0
        
    #Ordenando por ingreso descendente
    productos_ordenados = sorted(
        productos.items(),
        key=lambda x: x[1]["ingreso"],
        reverse=True
    )

    print("producto,unidades_vendidas, ingreso_total, precio_promedio")
    for nombre, datos in productos_ordenados:
        print(f"{nombre},{datos['unidades']},{datos['ingreso']:.2f},{datos['promedio']:.2f}")


if __name__ == "__main__":
    main()

    
