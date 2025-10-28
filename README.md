# 📊 Librería de Análisis Estadístico (POO en Python)

Este proyecto es una **librería en Python** que realiza análisis estadístico básico de **variables cualitativas y cuantitativas** usando **Programación Orientada a Objetos (POO)**.  
Desarrollado como parte del curso de **Programación II**.

---

## 🚀 Características

### 🔸 Variables Cualitativas
- Cálculo de **moda**
- Generación de **tabla de frecuencias** con porcentajes

### 🔸 Variables Cuantitativas
- **Media**
- **Mediana**
- **Varianza**
- **Desviación estándar**

---

## 🧱 Estructura del Proyecto

- `Estadistica`: clase padre base
- `Cualitativa`: clase para variables categóricas
- `Cuantitativa`: clase hija para variables numéricas

---

## 🧠 Ejemplo de Uso

```python
# Ejemplo de uso de la librería estadística

from estadistica import Cualitativa, Cuantitativa

# --- Análisis cualitativo ---
datos_cuali = ["A", "B", "A", "C", "A", "B"]
analisis_cuali = Cualitativa(datos_cuali)
moda, frec = analisis_cuali.moda()
print("📍 Moda:", moda)
analisis_cuali.tabla_frecuencia()

# --- Análisis cuantitativo ---
datos_cuanti = [5, 7, 8, 5, 10, 9, 8]
analisis_cuanti = Cuantitativa(datos_cuanti)
print("📏 Media:", analisis_cuanti.media())
print("📐 Desviación estándar:", analisis_cuanti.desviacion())
```

---

## 📂 Archivos Principales

- `estadistica.py`: contiene las clases principales  
- `main.ipynb`: cuaderno donde se prueban las clases  
- `README.md`: documentación del proyecto  

---

## 👥 Integrantes del Grupo

| Nombre | Usuario de GitHub |
|--------|--------------------|
| Fabricio Barrientos | [@fabriciobarrientos26](https://github.com/fabriciobarrientos26) |
| Harley Puma | [@CafinHarly](https://github.com/CafinHarly) |
| Maria Montero | [@usuario3](https://github.com/usuario2) |
| Raul Anton | [@usuario3](https://github.com/usuario3) |

---

## 🧰 Tecnologías Usadas
- Python 3.x  
- Programación Orientada a Objetos (POO)

---

## 📄 Licencia
Proyecto académico con fines educativos.
