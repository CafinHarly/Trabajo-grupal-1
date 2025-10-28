import pandas as pd
# ----------------------------- #
# 🧩 CLASE PADRE
# ----------------------------- #
class VariableEstadistica:
    def __init__(self, df, columna):
        self.df = df
        self.columna = columna
        # elimina valores nulos y los guarda como lista
        self.datos = df[columna].dropna().tolist()


    def cantidad(self):
        return len(self.datos)


    def mostrar_datos(self, n=10):
        print(self.datos[:n])

# ----------------------------- #
# 🔵 CLASE HIJA: CUANTITATIVA
# ----------------------------- #
class Cuantitativa(VariableEstadistica):


    def media(self):
        return sum(self.datos) / len(self.datos)


    def mediana(self):
        datos_ordenados = sorted(self.datos)
        n = len(datos_ordenados)
        mitad = n // 2
        if n % 2 == 0:
            return (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2
        else:
            return datos_ordenados[mitad]
    def varianza(self):
        media = self.media()
        return sum((x - media) ** 2 for x in self.datos) / len(self.datos)


    def desviacion_estandar(self):
        return self.varianza() ** 0.5
    
    def rango(self):
        return max(self.datos) - min(self.datos)

    def percentiles(self, p):
        datos_ordenados = sorted(self.datos)
        k = (len(datos_ordenados) - 1) * (p / 100)
        f = int(k)
        c = k - f
        if f + 1 < len(datos_ordenados):
            return datos_ordenados[f] + c * (datos_ordenados[f + 1] - datos_ordenados[f])
        else:
            return datos_ordenados[f]
    
    def outliers(self):
        q1, q3 = self.percentiles(25), self.percentiles(75)
        iqr = q3 - q1
        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr
        outliers = [x for x in self.datos if x < limite_inferior or x > limite_superior]
        return outliers


    def resumen(self):
        print(f"\n📈 Estadísticas descriptivas para '{self.columna}':")
        print(f"Media: {round(self.media(),2)}")
        print(f"Mediana: {round(self.mediana(),2)}")
        print(f"Varianza: {round(self.varianza(),2)}")
        print(f"Desviación estándar: {round(self.desviacion_estandar(),2)}")
        print(f"Rango: {round(self.rango(),2)}")
        print(f"N° de valores atípicos: {len(self.outliers())}")
        print(f"Percentil 25: {round(self.percentiles(25),2)}")
        print(f"Percentil 75: {round(self.percentiles(75),2)}")
        
        
    def generar_reporte(self, nombre_archivo="reporte.txt"):
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(f"Análisis de la variable: {self.columna}\n")
            f.write(f"Cantidad de datos: {self.cantidad()}\n")
            f.write(f"Media: {round(self.media(),2)}\n")
            f.write(f"Mediana: {round(self.mediana(),2)}\n")
    
# ----------------------------- #
# 🟢 CLASE HIJA: CUALITATIVA
# ----------------------------- #
class Cualitativa(VariableEstadistica):


    def moda(self):
        max_frec = 0
        moda = None
        for valor in self.datos:
            frec = self.datos.count(valor)
            if frec > max_frec:
                max_frec = frec
                moda = valor
        return moda, max_frec


    def tabla_frecuencia(self):
        tabla = {}
        for valor in self.datos:
            tabla[valor] = tabla.get(valor, 0) + 1
        total = len(self.datos)
        print(f"\n📊 Tabla de frecuencias para '{self.columna}':")
        print("Valor\t\tFrecuencia\tPorcentaje")
        for valor, frec in tabla.items():
            porcentaje = round((frec / total) * 100, 2)
            print(f"{valor}\t\t{frec}\t\t{porcentaje}%")
            