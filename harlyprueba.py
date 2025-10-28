import pandas as pd
from Harlybreria import Cuantitativa, Cualitativa

url = "https://raw.githubusercontent.com/RaulAM22/TED-XD/refs/heads/main/paises1957.csv"
df = pd.read_csv(url)

analisis_cuanti = Cuantitativa(df, "esperanza_de_vida")
analisis_cuanti.resumen()

analisis_cuali = Cualitativa(df, "continente")
analisis_cuali.tabla_frecuencia()