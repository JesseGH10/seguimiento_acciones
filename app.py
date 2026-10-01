import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuración de la página del Dashboard (Ancho completo)
st.set_page_config(
    page_title="AMZN Tracker Dashboard",
    page_icon="📈",
    layout="wide"
)

# 2. Cargar los datos de manera eficiente con caché
@st.cache_data
def load_data():
    # Ruta solicitada: data/datos.csv
    df = pd.read_csv("data/datos.csv")
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    return df

try:
    df = load_data()

    # 3. Título y Subtítulo llamativos con Emojis 🚀
    st.title("📈 AMZN Stock Pulse Dashboard")
    st.subheader("Visualización Interactiva del Comportamiento de Amazon (2020 - 2025) 🛒📦")
    st.markdown("---")

    # 4. Barra Lateral (Sidebar) para los Filtros Interactivos
    st.sidebar.header("🎯 Panel de Filtros")

    # Filtro de Estilo Dropdown (Multiselect) para el Año
    anios_disponibles = sorted(df['Anio'].unique())
    anios_seleccionados = st.sidebar.multiselect(
        "Selecciona los Años:",
        options=anios_disponibles,
        default=anios_disponibles
    )

    # Filtro de Estilo Dropdown (Selectbox) para la Tendencia
    tendencias_disponibles = ["Todas"] + list(df['Tendencia'].unique())
    tendencia_seleccionada = st.sidebar.selectbox(
        "Selecciona la Tendencia del Mercado:",
        options=tendencias_disponibles
    )

    # Filtro de Estilo Checkbox para Días con Ganancia
    solo_ganancia = st.sidebar.checkbox("🚀 Mostrar solo días con Ganancia (Ganancia_Dia = True)", value=False)

    # Aplicación de los filtros al DataFrame original
    df_filtrado = df[df['Anio'].isin(anios_seleccionados)]

    if tendencia_seleccionada != "Todas":
        df_filtrado = df_filtrado[df_filtrado['Tendencia'] == tendencia_seleccionada]

    if solo_ganancia:
        df_filtrado = df_filtrado[df_filtrado['Ganancia_Dia'] == True]


    # 5. Checkbox para mostrar/ocultar vista previa del DataFrame (Directriz 3)
    if st.checkbox("🔍 Mostrar vista previa de los datos filtrados (Primeras 10 filas)"):
        st.write(f"Mostrando {min(10, len(df_filtrado))} de {len(df_filtrado)} registros encontrados:")
        st.dataframe(df_filtrado.head(10), use_container_width=True)
        st.markdown("---")


    # Validación en caso de que los filtros dejen vacío el DataFrame
    if df_filtrado.empty:
        st.warning("⚠️ No hay datos que coincidan con los filtros seleccionados. Intenta cambiarlos en la barra lateral.")
    else:
        # Métrica rápidas en la parte superior
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.metric("Total Registros Filtrados", f"{len(df_filtrado)}")
        with col_m2:
            st.metric("Precio Cierre Promedio", f"\${df_filtrado['Cierre'].mean():.2f}")
        with col_m3:
            st.metric("Volumen Promedio Total", f"{df_filtrado['Volumen_M'].mean():.2f}M")

        st.markdown("### 📊 Gráficos Interactivos")

        # 6. Distribución en columnas para los Gráficos (Directrices 5 y 6)
        col1, col2 = st.columns(2)

        with col1:
            # Gráfico 1: Barras Verticales - Precio de Cierre Máximo por Año/Trimestre
            st.markdown("#### 🔹 Precio de Cierre Máximo por Trimestre")
            # Agrupamos para que el gráfico sea limpio
            df_barras = df_filtrado.groupby(['Anio', 'Trimestre'])['Cierre'].max().reset_index()
            df_barras['Periodo'] = df_barras['Anio'].astype(str) + " - " + df_barras['Trimestre']
            
            fig_barras = px.bar(
                df_barras, 
                x="Periodo", 
                y="Cierre", 
                color="Trimestre",
                text_auto='.2f',
                labels={'Cierre': 'Precio de Cierre (\$)'},
                template="plotly_white"
            )
            fig_barras.update_layout(xaxis_title="Período", yaxis_title="Precio de Cierre (\$)")
            # use_container_width=True expande el gráfico al ancho completo de la columna
            st.plotly_chart(fig_barras, use_container_width=True)

        with col2:
            # Gráfico 2: Circular / Donut Chart - Proporción de Tipos de Tendencia
            st.markdown("#### 🔹 Proporción de Tendencias del Mercado")
            fig_pie = px.pie(
                df_filtrado, 
                names="Tendencia", 
                hole=0.4, # Convierte el Pie Chart en Donut Chart de estilo moderno
                color_discrete_sequence=px.colors.qualitative.Pastel,
                template="plotly_white"
            )
            fig_pie.update_traces(textinfo='percent+label')
            st.plotly_chart(fig_pie, use_container_width=True)

        # Gráfico 3: Histograma (Ocupa todo el ancho inferior)
        st.markdown("#### 🔹 Histograma: Distribución del Volumen de Transacciones (Millones)")
        fig_hist = px.histogram(
            df_filtrado, 
            x="Volumen_M", 
            nbins=20,
            color="Tendencia",
            marginal="box", # Agrega un diagrama de caja en la parte superior para detectar outliers
            labels={'Volumen_M': 'Volumen (Millones de Acciones)'},
            template="plotly_white"
        )
        fig_hist.update_layout(yaxis_title="Frecuencia de Días")
        st.plotly_chart(fig_hist, use_container_width=True)

except FileNotFoundError:
    st.error("❌ Error: No se encontró el archivo en la ruta `data/datos.csv`. Por favor asegúrate de crear la carpeta `data` y guardar el archivo CSV allí con el nombre correcto.")
except Exception as e:
    st.error(f"⚠️ Ocurrió un error inesperado al cargar la aplicación: {e}")