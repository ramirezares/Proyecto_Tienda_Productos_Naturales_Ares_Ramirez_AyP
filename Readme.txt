Instrucciones del proyecto:

Proyecto: Tienda en línea de productos naturales 🌿

Te han contratado para el desarrollo de un nuevo proyecto, una tienda en línea de productos naturales. Este sistema servirá para la venta de productos, registro de clientes y más.

El sistema consta de seis (6) módulos fundamentales:
  1. Gestión de productos
  2. Gestión de ventas
  3. Gestión de clientes
  4. Gestión de pagos
  5. Gestión de envíos
  6. Indicadores de gestión (estadísticas)

Nota: Revise la información importante en observaciones

Gestión de productos
Este módulo permitirá a los usuarios administrar los productos que se venden en la tienda en línea. Para eso tendrás que tener en cuenta, que la información será dada a través de una API, (ver observaciones). Con esta información deberán desarrollar lo siguiente:

1. Agregar nuevos productos a la tienda con la siguiente información:
  Nombre del producto
  Descripción
  Precio
  Categoría (por ejemplo: alimentos, suplementos, cuidado personal, etc.)
  Inventario disponible

2. Buscar productos en función de los siguientes filtros:
  Categoría
  Precio
  Nombre
  Disponibilidad en inventario

3. Modificar la información de los productos existentes

4. Eliminar productos de la tienda

Gestión de venta
Este módulo permitirá a los usuarios administrar las ventas realizadas en la tienda en línea. Para ello, se deberá desarrollar lo siguiente:

1. Registrar las ventas con la siguiente información:
  - Cliente que realizó la compra
  - Productos comprados
  - Cantidad de cada producto
  - Método de pago
  - Método de envío
  - El desglose del total de compra
    i. Subtotal 
    ii. Descuentos
        1. 5% de descuento si el cliente es jurídico y paga de contado 
    iii. IVA (16%)
    iv. IGTF (3%) en caso de que pague en divisas
    v. Total

2. Generar facturas para cada compra
  - Si el cliente es jurídico se podrá realizar compras a crédito (pago en 15 o 30 días)

3. Buscar ventas en función de los siguientes filtros:
  - Cliente
  - Fecha de la venta	
  - Monto total de la venta

Gestión de clientes
Este módulo permitirá a los usuarios administrar la información de los clientes registrados en la tienda en línea. Para ello, se deberá desarrollar lo siguiente:

1. Registrar nuevos clientes con la siguiente información:
    - Nombre y Apellido o Razón Social
    - Tipo de cliente (Natural o Jurídico)
    - Cédula o RIF
    - Correo electrónico
    - Dirección de envío
    - Teléfono

2. Modificar la información de los clientes existentes

3. Eliminar clientes de la tienda

4. Buscar clientes en función de los siguientes filtros:
  - Cédula o RIF
  - Correo electrónico


Gestión de pagos
Este módulo permitirá a los usuarios administrar los pagos realizados por los clientes en la tienda en línea. Para ello, se deberá desarrollar lo siguiente:

1. Registrar los pagos con la siguiente información:
  - Cliente que realizó el pago
  - Monto del pago
  - Moneda del pago
  - Tipo de pago (e.g. PdV, PM, Zelle, Cash)
  - Fecha del pago
2. Buscar pagos en función de los siguientes filtros:
  - Cliente
  - Fecha
  - Tipo de pago
  - Moneda de pago


Gestión de envíos
Este módulo permitirá a los usuarios administrar los envíos realizados por la tienda en línea. Para ello, se deberá desarrollar lo siguiente:

1. Registrar los envíos con la siguiente información:
  - Order de compra
  - Servicio de envío (e.g. MRW, Zoom, Delivery)
  - En caso de que sea delivery agregar los datos del motorizado
  - Costo del servicio
2. Buscar envíos en función de los siguientes filtros:
  - Cliente
  - Fecha



Indicadores de gestión (Estadísticas)
Este módulo permitirá a los usuarios visualizar estadísticas sobre el desempeño de la tienda en línea. Para ello, se deberá desarrollar lo siguiente:

1. Generar informes de ventas con la siguiente información:
  - Ventas totales por día, semana, mes y año
  - Productos más vendidos
  - Clientes más frecuentes
2. Generar informes de pagos con la siguiente información:
  - Pagos totales por día, semana, mes y año
  - Clientes con pagos pendientes
3. Generar informes de envíos con la siguiente información:
  - Envíos totales por día, semana, mes y año
  - Productos más enviados
  - Clientes con envíos pendientes
4.Realizar gráficos con dichas estadísticas con las librerías de mathplotlib o Bokeh (Bono).

Observaciones
+ Posee una API en donde podrás obtener toda su información:
  - Documentación: 
		https://github.com/Algoritmos-y-Programacion-2223-3/api-proyecto
  - Endpoints:
   # Productos: https://github.com/Algoritmos-y-Programacion-2223-3/api-proyecto/blob/main/products.json

+ La API tiene que funcionar como una opción de pre-cargado de datos antes de empezar a usar el programa, es decir esta opción crea el estado inicial del programa, posteriormente no se debe usar la API a menos que se quiera borrar los datos y cargar su estado inicial

+ Se deben usar los conceptos de programación orientado a objetos

+ Antes de realizar el código, es imperante que realicen un diagrama de clases y que la implementación de su proyecto sea uno a uno con el diagrama

+ Se evaluará que el código este comentado (docstring)

+ Se evaluará que el sistema contenga validaciones

+ Se deberán guardar datos en un archivo TXT para preservar los datos

+ El proyecto deberá ser entregado a más tardar el XX de junio de 2023 a las 11:59PM



