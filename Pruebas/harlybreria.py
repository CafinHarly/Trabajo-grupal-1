import pandas as pd
import matplotlib.pyplot as plt
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

    def graficar(self):
        #Histograma
        plt.figure(figsize=(6,4))
        plt.hist(self.datos, bins=10, edgecolor='black')
        plt.title(f"Histograma de {self.columna}")
        plt.xlabel(self.columna)
        plt.ylabel("Frecuencia")
        plt.show()
        #Boxplot
        plt.figure(figsize=(6,4))
        plt.boxplot(self.datos)
        plt.title(f"Boxplot de {self.columna}")
        plt.ylabel(self.columna)
        plt.show()

    def matriz_correlacion(self):
        print("\n Matriz de correlaciones entre variables cuantitativas:\n")
        df_num = self.df.select_dtypes(include=['float64', 'int64']).copy()
        df_num = df_num.loc[:, ~df_num.columns.str.contains("Unnamed")]
        df_num = df_num.loc[:, df_num.apply(lambda x: x.nunique() > 1)]
        corr = df_num.corr()
        print(corr.round(3))

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
        print(f"Cantidad de datos: {self.cantidad()}\n")
        print
        
    def generar_reporte(self, nombre_archivo="reporte.txt"):
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(f"Análisis de la variable: {self.columna}\n")
            f.write(f"Cantidad de datos: {self.cantidad()}\n")
            f.write(f"Media: {round(self.media(),2)}\n")
            f.write(f"Mediana: {round(self.mediana(),2)}\n")
            f.write(f"Varianza: {round(self.varianza(),2)}\n")
            f.write(f"Desviación estándar: {round(self.desviacion_estandar(),2)}\n")
            f.write(f"Rango: {round(self.rango(),2)}\n")
            f.write(f"N° de valores atípicos: {len(self.outliers())}\n")
            f.write(f"Percentil 25: {round(self.percentiles(25),2)}\n")
            f.write(f"Percentil 75: {round(self.percentiles(75),2)}\n")
            #Para la matriz de correlación
            df_num = self.df.loc[:, ~self.df.columns.str.contains("^Unnamed")]
            corr = df_num.corr(numeric_only=True)
            f.write("Matriz de correlaciones entre variables cuantitativas:\n")
            f.write(corr.to_string())  
            f.write("\n")
        print(f"Reporte guardado en '{nombre_archivo}'")
    
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
        tabla = pd.Series(self.datos).value_counts()
        total = len(self.datos)

        df_freq = pd.DataFrame({
            "Frecuencia": tabla,
            "Frecuencia Relativa": round(tabla / total, 3),
            "Frecuencia Acumulada": round((tabla / total).cumsum(), 3)
        })

        print(f"\n📊 Tabla de frecuencias para '{self.columna}':\n")
        print(df_freq)

        moda, frec_moda = self.moda()
        print("\n🔹 Moda:")
        if moda is None:
            print(" → No hay moda (todas las frecuencias son iguales)")
        else:
            print(f" → {moda} (frecuencia: {frec_moda})")
    
    def graficar(self):
        tabla = pd.Series(self.datos).value_counts()
        plt.figure(figsize=(6,4))
        tabla.plot(kind='bar')
        plt.title(f"Distribución de {self.columna}")
        plt.ylabel("Frecuencia")
        plt.xlabel("Categorías")
        plt.show() 


def menu(df):
    cuantis = df.select_dtypes(include=['float64', 'int64']).columns.tolist() #Filtra los nombres de las columnas con variables cuantitativas
    cualis = df.select_dtypes(include=['object', 'category']).columns.tolist() #Filtra los nombres de las columnas con variables cualitativas

    print("Variables cuantitativas:", cuantis)
    print("Variables cualitativas:", cualis)
    tipo = input("¿Qué tipo de variable deseas analizar? (cuantitativa/cualitativa): ")
    col = input("Escribe el nombre de la columna: ")
    if tipo == "cuantitativa":
        analisis_cuanti = Cuantitativa(df, col)
        analisis_cuanti.resumen()
        analisis_cuanti.graficar()
        analisis_cuanti.generar_reporte()
        analisis_cuanti.matriz_correlacion()
    elif tipo == "cualitativa":
        analisis_cuali = Cualitativa(df, col)
        analisis_cuali.tabla_frecuencia()
        analisis_cuali.graficar()
    else:
        print(" Tipo inválido.")          