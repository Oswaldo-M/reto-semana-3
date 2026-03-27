# Reto Semana 3— Analizador de Ventas

Programa en **Python** que procesa un archivo CSV con registros de ventas, calcula estadísticas por producto y genera un resumen ordenado por ingreso total.

El programa:

* Lee datos desde **stdin**
* Escribe resultados en **stdout**
* Ignora automáticamente líneas inválidas

---

# Formato de Entrada

El programa recibe un **archivo CSV** con el siguiente formato:

```
fecha,producto,cantidad,precio_unitario
```

Columnas:

| Columna         | Descripción         | Ejemplo    |
| --------------- | ------------------- | ---------- |
| fecha           | Fecha de la venta   | 2026-01-01 |
| producto        | Nombre del producto | Laptop     |
| cantidad        | Unidades vendidas   | 2          |
| precio_unitario | Precio por unidad   | 15000.00   |

Ejemplo de entrada:

```
fecha,producto,cantidad,precio_unitario
2026-01-01,Laptop,2,15000.00
2026-01-02,Mouse,abc,250.00
2026-01-03,Teclado,5,invalid
2026-01-04,Laptop,1,14500.00
linea,incompleta
```

---

# Procesamiento

## Acumulación por producto

El programa agrupa los datos por producto y calcula:

* **Unidades vendidas** → suma de cantidades válidas
* **Ingreso total** → suma de (cantidad × precio)

---

## Cálculo de métricas

Para cada producto se calcula:

| Métrica         | Fórmula            |
| --------------- | ------------------ |
| ingreso_total   | cantidad × precio  |
| precio_promedio | ingreso / unidades |

---

## Manejo de líneas inválidas

El programa **ignora automáticamente** líneas que tengan:

* Cantidad no numérica (`abc`, vacío, etc.)
* Precio no numérico (`invalid`, vacío, etc.)
* Menos o más de 4 columnas
* Datos incompletos o mal formateados

---

## Ordenamiento

Los resultados se ordenan de forma descendente con base en su ingreso total:

---

# Formato de Salida

El programa genera un **CSV** con el siguiente formato:

```
producto,unidades_vendidas,ingreso_total,precio_promedio
```

Ejemplo de salida:

```
producto,unidades_vendidas,ingreso_total,precio_promedio
Laptop,3,44000.00,14666.67
Mouse,2,500.00,250.00
```

* `ingreso_total` se muestra con **2 decimales**
* `precio_promedio` se muestra con **2 decimales**

---

# Cómo ejecutar el programa

### Linux / Mac

```
python3 main.py < entrada.txt > salida.txt
```

### Windows (PowerShell)

```
Get-Content entrada.txt | python main.py > salida.txt
```

### Windows (CMD)

```
type entrada.txt | python main.py > salida.txt
```

---

# Ejemplo completo

Archivo `entrada.txt`:

```
fecha,producto,cantidad,precio_unitario
2026-01-01,Laptop,2,15000.00
2026-01-02,Mouse,1,250.00
2026-01-03,Teclado,abc,500.00
2026-01-04,Laptop,1,14000.00
```

Ejecución:

```
python3 main.py < entrada.txt > salida.txt
```

Salida:

```
producto,unidades_vendidas,ingreso_total,precio_promedio
Laptop,3,44000.00,14666.67
Mouse,1,250.00,250.00
```

---

# Autor

Oswaldo Morales
