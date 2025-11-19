cantidad = float(input("Cantidad de dinero invertido: "))
porcentajeInteres1 = float(input("Porcentaje de interés: "))
tiempo = float(input("Tiempo invertido (en días): "))

porcentajeInteres2 = porcentajeInteres1 / 100
valorIntereses = (cantidad * porcentajeInteres2 * tiempo) / 360
valorDescuento = valorIntereses * 0.07
valorTotal = cantidad + valorIntereses - valorDescuento

print("El valor de intereses es:", valorIntereses)
print("El valor del descuento es:", valorDescuento)
print("El valor a recibir es:", valorTotal)