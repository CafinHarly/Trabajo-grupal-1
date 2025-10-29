import pandas as pd
import matplotlib.pyplot as plt
from harlybreria import Cuantitativa, Cualitativa, menu

url = "https://raw.githubusercontent.com/RaulAM22/TED-XD/refs/heads/main/paises1957.csv"
df = pd.read_csv(url)

menu(df)