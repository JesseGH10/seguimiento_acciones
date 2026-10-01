# 📈 AMZN Stock Pulse Dashboard

> **¡Bienvenido a AMZN Stock Pulse!** Una aplicación web interactiva y responsiva diseñada para rastrear, analizar y desglosar el comportamiento financiero de las acciones de Amazon (AMZN) en el periodo de 2020 a 2025. 

Este panel de control transforma datos históricos complejos (como precios de apertura, cierres, volúmenes de transacciones y tendencias de mercado) en información visual intuitiva y accionable para la toma de decisiones.

---

## 🚀 Características Clave

* **Análisis Multidimensional:** Filtra datos por año, tipos de tendencia (*Alcista*, *Bajista*, *Lateral*) o días específicos con ganancias netas.
* **Exploración de Datos Transparente:** Incluye un visor dinámico para auditar las primeras filas del dataset directamente desde la interfaz.
* **Métricas en Tiempo Real:** Tarjetas informativas con cálculos automatizados de volumen promedio y precios de cierre.
* **Visualizaciones de Alto Impacto:** Gráficos totalmente interactivos potenciados por Plotly Express optimizados para pantallas de cualquier tamaño.

---

## 🛠️ Tecnologías Utilizadas

El proyecto fue construido utilizando herramientas modernas del ecosistema de Ciencia de Datos en Python:

* **[Python](https://python.org):** Lenguaje principal para la manipulación y lógica de filtrado de datos.
* **[Streamlit](https://streamlit.io):** Framework de código abierto que nos permitió transformar scripts de datos en una aplicación web interactiva en minutos.
* **[Plotly Express](https://plotly.com):** Biblioteca de graficación interactiva para desplegar histogramas, diagramas de dona y gráficos de barras dinámicos.
* **[Pandas](https://pydata.org):** El motor principal para la carga, limpieza y segmentación eficiente de estructuras de datos financieras.

---

## 💻 Instalación y Uso en Local

Sigue estos sencillos pasos para clonar el repositorio y ejecutar el cuadro de mando en tu propia computadora:

### 1. Clonar el repositorio
Abre tu terminal y descarga los archivos del proyecto utilizando Git:
```bash
git clone https://github.com
cd AMZN-Stock-Pulse-Dashboard
```

### 2. Preparar el entorno e instalar dependencias
Es altamente recomendable utilizar un entorno virtual para mantener limpias tus librerías globales. Instala los requerimientos listados en el proyecto:
```bash
pip install -r requirements.txt
```

### 3. Asegurar la estructura de datos
Verifica que el archivo de datos históricos se encuentre guardado exactamente en la siguiente ruta relativa:
```text
📂 AMZN-Stock-Pulse-Dashboard
 ├── 📂 data
 │    └── 📄 datos.csv   <-- Tu archivo de datos aquí
 └── 📄 app.py
```

### 4. Lanzar la aplicación
Enciende el servidor local de Streamlit ejecutando:
```bash
streamlit run app.py
```
*¡Listo! Tu navegador web predeterminado abrirá automáticamente una pestaña en `http://localhost:8501` mostrando tu panel interactivo.*

---

## 📊 Vistas del Dashboard

El dashboard se compone de tres visualizaciones dinámicas integradas:
1. **Precio de Cierre Máximo por Trimestre:** Gráfico de barras verticales diseñado para identificar picos históricos del mercado.
2. **Proporción de Tendencias:** Gráfico de tipo dona (*Donut Chart*) para evaluar el sesgo de mercado general.
3. **Distribución del Volumen:** Un histograma enriquecido con un diagrama de caja (*box plot*) superior para rastrear anomalías o picos de volatilidad en las transacciones.

> 💡 **Nota para reclutadores y entusiastas:** Este repositorio forma parte de mi portafolio profesional de datos. Si encuentras útil este proyecto o te interesa colaborar en soluciones analíticas similares, ¡no dudes en conectar conmigo o dejar una ⭐️ al repositorio!
