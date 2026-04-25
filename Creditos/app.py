import os
import streamlit as st

st.write("Directorio actual:", os.getcwd())

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
st.write("BASE_DIR:", BASE_DIR)

modelo_path = os.path.join(BASE_DIR, "modelo_credito.pkl")
scaler_path = os.path.join(BASE_DIR, "scaler.pkl")

st.write("Ruta modelo:", modelo_path)
st.write("Existe modelo:", os.path.exists(modelo_path))

st.write("Ruta scaler:", scaler_path)
st.write("Existe scaler:", os.path.exists(scaler_path))


import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

st.set_page_config(
    page_title="CreditRisk · Evaluador by Diaz Nestor",
    page_icon="-📊-",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─── CUSTOM CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');

  html, body, [class*="css"] {
    font-family: 'IBM Plex Sans', sans-serif;
  }

  /* Fondo oscuro industrial */
  .stApp {
    background-color: #0a0d12;
    color: #c9d1d9;
  }

  /* Sidebar */
  [data-testid="stSidebar"] {
    background-color: #0d1117;
    border-right: 1px solid #21262d;
  }

  /* Ocultar header de Streamlit */
  [data-testid="stHeader"] {
    background: transparent;
  }

  /* Inputs */
  .stNumberInput input, .stSlider .st-bx {
    font-family: 'IBM Plex Mono', monospace !important;
    background-color: #161b22 !important;
    border: 1px solid #30363d !important;
    color: #e6edf3 !important;
    border-radius: 4px !important;
  }

  .stNumberInput input:focus {
    border-color: #58a6ff !important;
    box-shadow: 0 0 0 2px rgba(88,166,255,0.15) !important;
  }

  /* Labels */
  .stNumberInput label, .stSlider label, .stRadio label {
    color: #8b949e !important;
    font-size: 11px !important;
    font-family: 'IBM Plex Mono', monospace !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
  }

  /* Radio buttons */
  .stRadio > div {
    background-color: #161b22;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 8px 12px;
  }

  /* Slider */
  .stSlider .st-bq { background-color: #30363d !important; }
  .stSlider .st-bt { background-color: #58a6ff !important; }

  /* Botón principal */
  .stButton > button {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    background-color: #1f6feb !important;
    border: none !important;
    border-radius: 6px !important;
    color: #ffffff !important;
    padding: 12px 24px !important;
    width: 100% !important;
    transition: background-color 0.2s ease !important;
  }

  .stButton > button:hover {
    background-color: #388bfd !important;
    box-shadow: 0 0 12px rgba(56,139,253,0.35) !important;
  }

  /* Métricas */
  [data-testid="stMetric"] {
    background-color: #161b22;
    border: 1px solid #21262d;
    border-radius: 8px;
    padding: 16px !important;
  }

  [data-testid="stMetricLabel"] {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 10px !important;
    color: #8b949e !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
  }

  [data-testid="stMetricValue"] {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 22px !important;
    color: #e6edf3 !important;
    font-weight: 600 !important;
  }

  /* Markdown separadores */
  hr { border-color: #21262d !important; }

  /* Expanders */
  .streamlit-expanderHeader {
    background-color: #161b22 !important;
    border: 1px solid #30363d !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 12px !important;
    color: #8b949e !important;
    letter-spacing: 0.05em !important;
  }

  /* Success / Error boxes */
  .stSuccess { background-color: #0d1f17 !important; border: 1px solid #238636 !important; }
  .stError   { background-color: #1a0d0d !important; border: 1px solid #da3633 !important; }

  /* Scrollbar */
  ::-webkit-scrollbar { width: 6px; }
  ::-webkit-scrollbar-track { background: #0a0d12; }
  ::-webkit-scrollbar-thumb { background: #30363d; border-radius: 3px; }
</style>
""", unsafe_allow_html=True)


# ─── HEADER ────────────────────────────────────────────────────────────────────
col_logo, col_title, col_ts = st.columns([1, 6, 2])

with col_logo:
    st.markdown("""
    <div style='padding-top:8px;'>
      <svg width="40" height="40" viewBox="0 0 40 40" fill="none">
        <rect width="40" height="40" rx="8" fill="#1f6feb"/>
        <path d="M10 28 L20 12 L30 28 Z" fill="none" stroke="white" stroke-width="2"/>
        <circle cx="20" cy="22" r="3" fill="white"/>
        <line x1="14" y1="28" x2="26" y2="28" stroke="white" stroke-width="1.5"/>
      </svg>
    </div>
    """, unsafe_allow_html=True)

with col_title:
    st.markdown("""
    <div style='padding-top:4px;'>
      <span style='font-family:"IBM Plex Mono",monospace; font-size:20px; font-weight:600; color:#e6edf3; letter-spacing:-0.02em;'>
        CREDITRISK 1.0
      </span>
      <span style='font-family:"IBM Plex Sans",sans-serif; font-size:13px; color:#8b949e; margin-left:12px;'>
        Motor de Evaluación Crediticia
      </span>
    </div>
    """, unsafe_allow_html=True)

with col_ts:
    now = datetime.now().strftime("%Y-%m-%d  %H:%M")
    st.markdown(f"""
    <div style='text-align:right; padding-top:10px;'>
      <span style='font-family:"IBM Plex Mono",monospace; font-size:11px; color:#484f58;'>{now}</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:2px; background:linear-gradient(90deg,#1f6feb,#21262d,transparent); margin:8px 0 24px;'></div>", unsafe_allow_html=True)


# ─── CARGA DE MODELO ───────────────────────────────────────────────────────────
@st.cache_resource
def cargar_modelo():
    modelo = joblib.load('modelo_credito.pkl')
    scaler = joblib.load('scaler.pkl')
    return modelo, scaler

try:
    modelo, scaler = cargar_modelo()
    modelo_cargado = True
except Exception:
    modelo_cargado = False
    st.markdown("""
    <div style='background:#161b22; border:1px solid #f0883e; border-radius:8px; padding:16px 20px; margin-bottom:24px;'>
      <span style='font-family:"IBM Plex Mono",monospace; font-size:12px; color:#f0883e;'>
        ⚠ MODO DEMO — Usando simulación.
      </span>
    </div>
    """, unsafe_allow_html=True)


# ─── PANEL DE INPUTS ───────────────────────────────────────────────────────────
st.markdown("""
<p style='font-family:"IBM Plex Mono",monospace; font-size:11px; color:#8b949e; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:16px;'>
  01 · Parámetros del solicitante
</p>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    score_credito = st.slider(
        "Score crediticio",
        min_value=300, max_value=850, value=620, step=5,
        help="300 = riesgo máximo · 850 = riesgo mínimo"
    )
    ingreso = st.number_input(
        "Ingreso mensual neto ($)",
        min_value=20_000, max_value=500_000,
        value=75_000, step=5_000
    )

with c2:
    monto_deuda = st.number_input(
        "Deudas vigentes totales ($)",
        min_value=0, max_value=500_000,
        value=18_000, step=1_000
    )
    deuda_ingreso = st.number_input(
        "Ratio deuda / ingreso (%)",
        min_value=0.0, max_value=200.0,
        value=24.0, step=0.5,
        help="DTI — Debt-to-Income ratio"
    )

with c3:
    empleo = st.radio(
        "Situación laboral",
        options=["Empleado en relación de dependencia", "Independiente / Monotributo", "Desempleado"],
        help="Afecta la ponderación del riesgo"
    )
    empleo_valor = 1 if "Desempleado" not in empleo else 0

    monto_solicitado = st.number_input(
        "Monto solicitado ($)",
        min_value=5_000, max_value=2_000_000,
        value=150_000, step=5_000
    )

st.markdown("<div style='height:24px;'></div>", unsafe_allow_html=True)

# ─── BOTÓN ─────────────────────────────────────────────────────────────────────
evaluar = st.button("▶  EJECUTAR EVALUACIÓN CREDITICIA", type="primary")

# ─── RESULTADO ─────────────────────────────────────────────────────────────────
if evaluar:
    datos_usuario = np.array([[score_credito, ingreso, monto_deuda, deuda_ingreso, empleo_valor]])

    if modelo_cargado:
        datos_escalados = scaler.transform(datos_usuario)
        probabilidad   = modelo.predict_proba(datos_escalados)[0][1]
        prediccion     = modelo.predict(datos_escalados)[0]
    else:
        # Simulación determinista para demo
        score_norm = (score_credito - 300) / 550
        dti_norm   = max(0, 1 - deuda_ingreso / 100)
        probabilidad = round(min(0.98, max(0.02, score_norm * 0.6 + dti_norm * 0.3 + empleo_valor * 0.1)), 4)
        prediccion   = 1 if probabilidad >= 0.5 else 0

    prob_pct    = probabilidad * 100
    riesgo_pct  = (1 - probabilidad) * 100

    # Clasificación de riesgo
    if prob_pct >= 75:
        nivel, nivel_color, nivel_bg = "BAJO RIESGO",   "#3fb950", "#0d1f17"
    elif prob_pct >= 50:
        nivel, nivel_color, nivel_bg = "RIESGO MODERADO","#d29922", "#1c1600"
    else:
        nivel, nivel_color, nivel_bg = "ALTO RIESGO",   "#f85149", "#1a0d0d"

    st.markdown("<div style='height:32px;'></div>", unsafe_allow_html=True)
    st.markdown("""
    <p style='font-family:"IBM Plex Mono",monospace; font-size:11px; color:#8b949e; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:16px;'>
      02 · Resultado del análisis
    </p>
    """, unsafe_allow_html=True)

    # ── Veredicto principal ──
    veredicto_texto = "APROBADO" if prediccion == 1 else "RECHAZADO"
    veredicto_color = "#3fb950" if prediccion == 1 else "#f85149"
    veredicto_bg    = "#0d1f17" if prediccion == 1 else "#1a0d0d"
    veredicto_icono = "✔" if prediccion == 1 else "✖"

    st.markdown(f"""
    <div style='
      background:{veredicto_bg};
      border:1px solid {veredicto_color};
      border-radius:8px;
      padding:24px 32px;
      display:flex;
      align-items:center;
      justify-content:space-between;
      margin-bottom:24px;
    '>
      <div>
        <div style='font-family:"IBM Plex Mono",monospace; font-size:11px; color:#8b949e; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:6px;'>
          Decisión crediticia
        </div>
        <div style='font-family:"IBM Plex Mono",monospace; font-size:32px; font-weight:600; color:{veredicto_color}; letter-spacing:-0.01em;'>
          {veredicto_icono} {veredicto_texto}
        </div>
      </div>
      <div style='text-align:right;'>
        <div style='font-family:"IBM Plex Mono",monospace; font-size:11px; color:#8b949e; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:6px;'>
          Clasificación de riesgo
        </div>
        <div style='font-family:"IBM Plex Mono",monospace; font-size:20px; font-weight:600; color:{nivel_color};'>
          {nivel}
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Gauge de probabilidad ──
    col_gauge, col_metricas = st.columns([2, 3])

    with col_gauge:
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=round(prob_pct, 1),
            number={
                'suffix': '%',
                'font': {'family': 'IBM Plex Mono', 'size': 36, 'color': '#e6edf3'},
            },
            title={
                'text': 'PROBABILIDAD DE APROBACIÓN',
                'font': {'family': 'IBM Plex Mono', 'size': 10, 'color': '#8b949e'}
            },
            gauge={
                'axis': {
                    'range': [0, 100],
                    'tickfont': {'family': 'IBM Plex Mono', 'size': 10, 'color': '#484f58'},
                    'tickcolor': '#30363d',
                    'tickwidth': 1,
                },
                'bar':          {'color': veredicto_color, 'thickness': 0.25},
                'bgcolor':      '#161b22',
                'borderwidth':  0,
                'steps': [
                    {'range': [0,  50], 'color': '#1a0d0d'},
                    {'range': [50, 75], 'color': '#1c1600'},
                    {'range': [75, 100],'color': '#0d1f17'},
                ],
                'threshold': {
                    'line': {'color': '#58a6ff', 'width': 2},
                    'thickness': 0.8,
                    'value': 50
                }
            }
        ))
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#c9d1d9',
            height=260,
            margin=dict(t=50, b=10, l=20, r=20)
        )
        st.plotly_chart(fig, use_container_width=True)

    with col_metricas:
        st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

        # Ratio cuota estimada / ingreso
        tasa_anual  = 0.55 if prediccion == 1 else 0.72   # estimación referencial
        plazo_meses = 24
        tasa_m      = tasa_anual / 12
        if tasa_m > 0:
            cuota = monto_solicitado * tasa_m * (1 + tasa_m)**plazo_meses / ((1 + tasa_m)**plazo_meses - 1)
        else:
            cuota = monto_solicitado / plazo_meses
        ratio_cuota_ingreso = cuota / ingreso * 100

        m1, m2 = st.columns(2)
        with m1:
            st.metric("Prob. aprobación",  f"{prob_pct:.1f}%")
            st.metric("Score crediticio",  f"{score_credito}")
            st.metric("Cuota est. mensual", f"${cuota:,.0f}")
        with m2:
            st.metric("Prob. rechazo",      f"{riesgo_pct:.1f}%")
            st.metric("DTI actual",         f"{deuda_ingreso:.1f}%")
            st.metric("Cuota / Ingreso",    f"{ratio_cuota_ingreso:.1f}%")

    # ── Radar de factores de riesgo ──
    st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)
    col_radar, col_tabla = st.columns([3, 2])

    with col_radar:
        # Normalizar cada factor entre 0 y 1 (mayor = más riesgo)
        r_score  = 1 - (score_credito - 300) / 550
        r_dti    = min(deuda_ingreso / 100, 1.0)
        r_empleo = 0.0 if empleo_valor == 1 else 1.0
        r_deuda  = min(monto_deuda / ingreso, 2.0) / 2.0
        r_cuota  = min(ratio_cuota_ingreso / 50, 1.0)

        categorias = ['Score<br>crediticio', 'DTI', 'Empleo', 'Carga<br>deuda', 'Cuota/<br>Ingreso']
        valores    = [r_score, r_dti, r_empleo, r_deuda, r_cuota]
        valores_pct = [round(v * 100, 1) for v in valores]

        fig2 = go.Figure()
        fig2.add_trace(go.Scatterpolar(
            r=valores_pct + [valores_pct[0]],
            theta=categorias + [categorias[0]],
            fill='toself',
            fillcolor='rgba(31,111,235,0.15)',
            line=dict(color='#1f6feb', width=2),
            name='Perfil de riesgo'
        ))
        fig2.update_layout(
            polar=dict(
                bgcolor='#161b22',
                radialaxis=dict(
                    visible=True, range=[0, 100],
                    tickfont=dict(family='IBM Plex Mono', size=9, color='#484f58'),
                    gridcolor='#21262d', linecolor='#30363d'
                ),
                angularaxis=dict(
                    tickfont=dict(family='IBM Plex Mono', size=10, color='#8b949e'),
                    gridcolor='#21262d', linecolor='#30363d'
                )
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            showlegend=False,
            height=300,
            margin=dict(t=30, b=30, l=50, r=50),
            title=dict(
                text='PERFIL DE RIESGO (0 = óptimo · 100 = crítico)',
                font=dict(family='IBM Plex Mono', size=9, color='#8b949e'),
                x=0.5
            )
        )
        st.plotly_chart(fig2, use_container_width=True)

    with col_tabla:
        st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
        st.markdown("""
        <p style='font-family:"IBM Plex Mono",monospace; font-size:10px; color:#8b949e; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:12px;'>
          Resumen de variables
        </p>
        """, unsafe_allow_html=True)

        def semaforo(valor, umbral_verde, umbral_amarillo):
            if valor <= umbral_verde:
                return "🟢"
            elif valor <= umbral_amarillo:
                return "🟡"
            return "🔴"

        tabla_data = {
            "Variable":  ["Score",  "DTI",         "Deuda/Ingreso",  "Empleo",                  "Cuota/Ingreso"],
            "Valor":     [str(score_credito), f"{deuda_ingreso}%", f"{monto_deuda/ingreso:.2f}x", empleo.split('/')[0].strip(), f"{ratio_cuota_ingreso:.1f}%"],
            "Estado":    [
                semaforo(850 - score_credito, 200, 400),
                semaforo(deuda_ingreso, 30, 50),
                semaforo(monto_deuda / ingreso, 0.3, 0.6),
                "🟢" if empleo_valor == 1 else "🔴",
                semaforo(ratio_cuota_ingreso, 25, 40)
            ]
        }
        df_tabla = pd.DataFrame(tabla_data)
        st.dataframe(
            df_tabla,
            use_container_width=True,
            hide_index=True,
            height=240
        )

    # ── Advertencia de política ──
    st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style='
      background:#161b22; border:1px solid #30363d; border-left:3px solid #58a6ff;
      border-radius:0 6px 6px 0; padding:12px 16px;
    '>
      <span style='font-family:"IBM Plex Mono",monospace; font-size:11px; color:#8b949e;'>
        ⓘ  Resultado generado por modelo de ML supervisado. Conforme al marco regulatorio BCRA (Com. "A" 6938 y concordantes), la decisión final debe contemplar análisis cualitativo del oficial de crédito y políticas internas de la entidad financiera. Este output no reemplaza el juicio crediticio institucional.
      </span>
    </div>
    """, unsafe_allow_html=True)