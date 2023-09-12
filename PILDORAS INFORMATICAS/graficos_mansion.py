import pandas as pd

# Datos del préstamo
monto_prestamo = 150000  
tasa_interes_anual = 4.0  
plazo_anios = 30          

def calcular_amortizacion(monto_prestamo, tasa_interes_anual, plazo_anios):
    # Convertir la tasa de interés anual a tasa mensual
    tasa_interes_mensual = tasa_interes_anual / 12 / 100
    
    # Calcular el número total de pagos mensuales
    numero_pagos = plazo_anios * 12
    
    # Calcular la mensualidad usando la fórmula
    mensualidad = monto_prestamo * (tasa_interes_mensual * (1 + tasa_interes_mensual)**numero_pagos) / ((1 + tasa_interes_mensual)**numero_pagos - 1)
    
    # Inicializar listas para almacenar los años y montos pagados
    anos = []
    montos_pagados = []
    
    # Inicializar el saldo restante al monto del préstamo
    saldo_restante = monto_prestamo
    
    # Calcular los montos pagados año por año
    for anio in range(1, plazo_anios + 1):
        for mes in range(1, 13):
            interes_mes = saldo_restante * tasa_interes_mensual
            principal_mes = mensualidad - interes_mes
            saldo_restante -= principal_mes
            if saldo_restante <= 0:
                saldo_restante = 0
            montos_pagados.append(monto_prestamo - saldo_restante)
            anos.append(anio)
            if saldo_restante <= 0:
                break
    
    # Crear un DataFrame
    df = pd.DataFrame({'Año': anos, 'Monto Pagado': montos_pagados})
    
    return df

# Calcular la amortización
amortizacion_df = calcular_amortizacion(monto_prestamo, tasa_interes_anual, plazo_anios)

# Imprimir el DataFrame
print(amortizacion_df)


def calcular_mensualidad(monto_prestamo, tasa_interes_anual, plazo_anios):
    # Convertir la tasa de interés anual a tasa mensual
    tasa_interes_mensual = tasa_interes_anual / 12 / 100
    
    # Calcular el número total de pagos mensuales
    numero_pagos = plazo_anios * 12
    
    # Calcular la mensualidad usando la fórmula
    mensualidad = monto_prestamo * (tasa_interes_mensual * (1 + tasa_interes_mensual)**numero_pagos) / ((1 + tasa_interes_mensual)**numero_pagos - 1)
    
    return mensualidad

# Calcular la mensualidad
mensualidad = calcular_mensualidad(monto_prestamo, tasa_interes_anual, plazo_anios)

# Imprimir el resultado
print(f"La mensualidad a pagar es de: ${mensualidad:.2f} por mes")


