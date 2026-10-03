import streamlit as st
import pandas as pd
import plotly.express as px


# 1. Configuración de la página
st.set_page_config(
    page_title="AMZN Tracker Dashboard",
    page_icon="📈",
    layout="wide"
)


# 2. Cargar los datos
@st.cache_data
def load_data():
    df = pd.read_csv("data/datos.csv")
    df["Fecha"] = pd.to_datetime(df["Fecha"])
    return df


df = load_data()


# 3. Título y subtítulo
st.title("📈 AMZN Stock Pulse Dashboard")
st.subheader(
    "🛒📦 Explorando el comportamiento de las acciones de Amazon"
)
st.markdown("---")


# 4. Filtros en la barra lateral
st.sidebar.header("🎯 Panel de Filtros")


# Filtro por año
anios_disponibles = sorted(df["Año"].unique())

anios_seleccionados = st.sidebar.multiselect(
    "📅 Selecciona los años:",
    options=anios_disponibles,
    default=anios_disponibles
)


# Filtro por tendencia
tendencias_disponibles = ["Todas"] + sorted(
    df["Tendencia"].unique().tolist()
)

tendencia_seleccionada = st.sidebar.selectbox(
    "📊 Selecciona la tendencia:",
    options=tendencias_disponibles
)


# Filtro para días con ganancia
solo_ganancia = st.sidebar.checkbox(
    "🚀 Mostrar solo días con ganancia",
    value=False
)


# Aplicar filtros
df_filtrado = df[df["Año"].isin(anios_seleccionados)]


if tendencia_seleccionada != "Todas":
    df_filtrado = df_filtrado[
        df_filtrado["Tendencia"] == tendencia_seleccionada
    ]


if solo_ganancia:
    df_filtrado = df_filtrado[
        df_filtrado["Ganancia_Dia"] == True
    ]


# 5. Vista previa del DataFrame
mostrar_datos = st.checkbox(
    "🔍 Mostrar vista previa de los datos filtrados"
)


if mostrar_datos:
    st.write(
        f"Mostrando las primeras {min(10, len(df_filtrado))} "
        f"filas de {len(df_filtrado)} registros."
    )

    st.dataframe(
        df_filtrado.head(10),
        use_container_width=True
    )

    st.markdown("---")


# 6. Validar que existan datos después de aplicar los filtros
if df_filtrado.empty:

    st.warning(
        "⚠️ No hay datos que coincidan con los filtros seleccionados."
    )

else:

    # 7. Métricas principales
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📊 Registros filtrados",
            len(df_filtrado)
        )

    with col2:
        st.metric(
            "💰 Precio de cierre promedio",
            f"${df_filtrado['Cierre'].mean():.2f}"
        )

    with col3:
        st.metric(
            "📦 Volumen promedio",
            f"{df_filtrado['Volumen_M'].mean():.2f} M"
        )


    st.markdown("### 📊 Gráficos interactivos")


    # =========================================================
    # GRÁFICO 1 - BARRAS
    # =========================================================

    st.markdown(
        "#### 🔹 Precio de cierre máximo por trimestre"
    )

    df_barras = (
        df_filtrado
        .groupby(["Año", "Trimestre"])["Cierre"]
        .max()
        .reset_index()
    )

    df_barras["Periodo"] = (
        df_barras["Año"].astype(str)
        + " - "
        + df_barras["Trimestre"]
    )

    fig_barras = px.bar(
        df_barras,
        x="Periodo",
        y="Cierre",
        color="Trimestre",
        text_auto=".2f",
        labels={
            "Periodo": "Período",
            "Cierre": "Precio de cierre ($)",
            "Trimestre": "Trimestre"
        },
        title="Precio de cierre máximo por período",
        template="plotly_white"
    )

    fig_barras.update_layout(
        xaxis_title="Período",
        yaxis_title="Precio de cierre ($)"
    )

    st.plotly_chart(
        fig_barras,
        use_container_width=True
    )


    # =========================================================
    # GRÁFICO 2 - DISPERSIÓN
    # =========================================================

    st.markdown(
        "#### 🔹 Relación entre volumen y precio de cierre"
    )

    fig_scatter = px.scatter(
        df_filtrado,
        x="Volumen_M",
        y="Cierre",
        color="Tendencia",
        hover_data=[
            "Fecha",
            "Año",
            "Trimestre",
            "Ganancia_Dia"
        ],
        labels={
            "Volumen_M": "Volumen (Millones)",
            "Cierre": "Precio de cierre ($)",
            "Tendencia": "Tendencia",
            "Ganancia_Dia": "Ganancia del día"
        },
        title="Volumen de transacciones vs. precio de cierre",
        template="plotly_white"
    )

    st.plotly_chart(
        fig_scatter,
        use_container_width=True
    )


    # =========================================================
    # GRÁFICO 3 - HISTOGRAMA
    # =========================================================

    st.markdown(
        "#### 🔹 Distribución del volumen de transacciones"
    )

    fig_hist = px.histogram(
        df_filtrado,
        x="Volumen_M",
        color="Tendencia",
        nbins=20,
        labels={
            "Volumen_M": "Volumen (Millones)",
            "Tendencia": "Tendencia"
        },
        title="Distribución del volumen de transacciones",
        template="plotly_white"
    )

    fig_hist.update_layout(
        yaxis_title="Número de registros",
        xaxis_title="Volumen (Millones)"
    )

    st.plotly_chart(
        fig_hist,
        use_container_width=True
    )