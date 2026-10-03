# 📈 AMZN Stock Pulse Dashboard

> 🚀 **Dashboard interactivo para explorar y visualizar el comportamiento de las acciones de Amazon (AMZN).**

Este proyecto presenta un **panel de control interactivo** desarrollado con Python, Streamlit y Plotly Express, diseñado para explorar diferentes dimensiones del comportamiento histórico de las acciones de Amazon.

A través de filtros dinámicos y visualizaciones interactivas, el usuario puede analizar los datos por **año, tendencia del mercado y días con ganancia**, así como explorar indicadores como el precio de cierre y el volumen de transacciones.

🎯 **Objetivo:** transformar un conjunto de datos financieros en una experiencia visual e interactiva que facilite la exploración y comprensión de los datos.

---

## 🌐 Ver el Dashboard en línea

🚀 **¡Explora la aplicación directamente desde tu navegador!**

👉 **[Visitar AMZN Stock Pulse Dashboard en Render](https://seguimiento-acciones-wls6.onrender.com/)**



---

## 📊 ¿Qué encontrarás en el Dashboard?

La aplicación cuenta con diferentes herramientas para explorar el comportamiento de las acciones:

* 📅 **Filtro por año** para seleccionar los periodos de interés.
* 📈 **Filtro por tendencia** para analizar comportamientos alcistas, bajistas o laterales.
* 🚀 **Filtro de días con ganancia**.
* 🔍 **Vista previa interactiva** de los datos filtrados.
* 📊 **Gráfico de barras** para visualizar el precio máximo de cierre por periodo.
* 🔵 **Gráfico de dispersión** para explorar la relación entre volumen de transacciones y precio de cierre.
* 📦 **Histograma** para analizar la distribución del volumen de operaciones.
* 🖱️ **Visualizaciones interactivas** que se actualizan de acuerdo con los filtros seleccionados.

---

## 🛠️ Tecnologías utilizadas

Este proyecto fue desarrollado utilizando:

| Tecnología            | Uso en el proyecto                                 |
| --------------------- | -------------------------------------------------- |
| 🐍 **Python**         | Lenguaje principal de programación                 |
| 🐼 **Pandas**         | Carga, transformación y filtrado de datos          |
| 📊 **Plotly Express** | Creación de visualizaciones interactivas           |
| 🎈 **Streamlit**      | Desarrollo del dashboard y la interfaz web         |
| 📁 **CSV**            | Fuente de datos del proyecto                       |
| 🌐 **Render**         | Despliegue de la aplicación web                    |
| 🔧 **Git / GitHub**   | Control de versiones y almacenamiento del proyecto |

---

## 💻 Instalación y ejecución local

Si quieres ejecutar el proyecto en tu propio equipo, sigue estos pasos.

### 1️⃣ Clona el repositorio

Abre una terminal y ejecuta:

```bash
git clone https://github.com/JesseGH10/seguimiento_acciones.git
```

Después, entra a la carpeta del proyecto:

```bash
cd seguimiento_acciones
```

---

### 2️⃣ Crea y activa un entorno virtual

Se recomienda utilizar un entorno virtual para mantener aisladas las dependencias del proyecto.

En Windows:

```bash
python -m venv .venv
```

Activa el entorno virtual:

```bash
.venv\Scripts\activate
```

Si la activación fue correcta, verás `(.venv)` al inicio de la línea de comandos.

---

### 3️⃣ Instala las dependencias

Con el entorno virtual activo, ejecuta:

```bash
pip install -r requirements.txt
```

Esto instalará las librerías necesarias para ejecutar la aplicación.

---

### 4️⃣ Inicia el Dashboard

Finalmente, ejecuta:

```bash
streamlit run app.py
```

Streamlit iniciará la aplicación y mostrará una dirección similar a:

```text
Local URL: http://localhost:8501
```

Abre esa dirección en tu navegador para comenzar a explorar el dashboard. 🚀

---

## 📂 Estructura del proyecto

El proyecto está organizado de la siguiente manera:

```text
seguimiento_acciones/
│
├── 📁 data/
│   └── datos.csv
│
├── 📁 notebooks/
│   └── EDA.ipynb
│
├── 📄 app.py
├── 📄 README.md
├── 📄 requirements.txt
└── 📄 .gitignore
```

### 📌 Componentes principales

* **`app.py`** → contiene la aplicación desarrollada con Streamlit.
* **`data/datos.csv`** → conjunto de datos utilizado por el dashboard.
* **`notebooks/EDA.ipynb`** → notebook utilizado para la exploración y análisis inicial de los datos.
* **`requirements.txt`** → lista de dependencias necesarias para ejecutar el proyecto.
* **`.gitignore`** → especifica archivos y carpetas que no deben incorporarse al repositorio.

---

## 📈 Visualizaciones

El dashboard utiliza **Plotly Express** para generar visualizaciones interactivas:

> 🔹 **Precio de cierre máximo por trimestre**
> Permite comparar el comportamiento del precio máximo de cierre entre diferentes periodos.

> 🔹 **Volumen vs. precio de cierre**
> Explora visualmente la relación entre el volumen de transacciones y el precio de cierre, diferenciando los registros según su tendencia.

> 🔹 **Distribución del volumen de transacciones**
> Permite identificar la concentración y distribución de los volúmenes registrados.

Todas las visualizaciones responden dinámicamente a los filtros seleccionados por el usuario. 🎯

---

## 🚀 Despliegue

La aplicación está preparada para ejecutarse en **Render**, permitiendo acceder al dashboard desde cualquier navegador sin necesidad de instalar Python o Streamlit localmente.

🌐 **Dashboard público:**

**[🔗 Abrir AMZN Stock Pulse Dashboard](https://seguimiento-acciones-wls6.onrender.com/)**

---

## 🎯 Propósito del proyecto

Este proyecto forma parte de un proceso de aprendizaje y práctica en **Data Science**, con énfasis en:

* 🐍 Programación con Python.
* 🧹 Manipulación y filtrado de datos.
* 📊 Visualización de datos.
* 🌐 Desarrollo de aplicaciones interactivas con Streamlit.
* 📈 Exploración de datos financieros.
* 🚀 Despliegue de aplicaciones de datos en la nube.

> 💡 **Del dato a la decisión:** este proyecto busca demostrar cómo Python puede transformar datos estructurados en una herramienta interactiva para explorar información de manera clara y visual.

---

## ⭐ Gracias por visitar el proyecto

Si este proyecto te resulta interesante, puedes explorar el código, probar el dashboard y seguir el proceso de desarrollo.

**¡Gracias por visitar y explorar el AMZN Stock Pulse Dashboard! 🚀📈**
