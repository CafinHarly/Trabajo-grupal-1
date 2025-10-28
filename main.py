import pandas as pd

# Clases

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

    def resumen(self):
        print(f"\n📈 Estadísticas descriptivas para '{self.columna}':")
        print(f"Media: {round(self.media(),2)}")
        print(f"Mediana: {round(self.mediana(),2)}")
        print(f"Varianza: {round(self.varianza(),2)}")
        print(f"Desviación estándar: {round(self.desviacion_estandar(),2)}")

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


# Cargar archivo a analizar
url = "https://raw.githubusercontent.com/RaulAM22/TED-XD/refs/heads/main/paises1957.csv"
df_general = pd.read_csv(url) # La variable df almacena la tabla csv

# Filtrar por tipos de categorias
lista_cuantitativas = df_general.select_dtypes(include=['float64', 'int64']).columns.tolist() #Filtra los nombres de las columnas con variables cuantitativas
lista_cualitativas = df_general.select_dtypes(include=['object', 'category']).columns.tolist() #Filtra los nombres de las columnas con variables cualitativas
print("Las columnas se dividen entre las variables:")
print("📊 Cuantitativas:", lista_cuantitativas)
print("🏷️ Cualitativas:", lista_cualitativas)


# Subconjunto con las variables cuantitativas
df_cuantitativas = df_general[lista_cuantitativas]

# Subconjunto con las variables cualitativas
df_cualitativas = df_general[lista_cualitativas]

