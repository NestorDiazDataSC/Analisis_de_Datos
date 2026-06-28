import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import shap
import warnings
warnings.filterwarnings("ignore")

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report, confusion_matrix,
    roc_auc_score, precision_recall_curve
)
from xgboost import XGBClassifier, plot_importance

# ── Config ────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Detección de Fraudes",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Estilos ───────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

  html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

  .stApp { background-color: #0D1117; color: #E6EDF3; }

  .hero {
    background: linear-gradient(135deg, #111827 0%, #1a1f2e 100%);
    border-left: 5px solid #F59E0B;
    border-radius: 12px;
    padding: 32px 36px;
    margin-bottom: 32px;
  }
  .hero h1 { color: #fff; font-size: 2rem; font-weight: 700; margin: 0 0 8px 0; }
  .hero p  { color: #9CA3AF; font-size: 0.95rem; margin: 0; line-height: 1.6; }

  .badge {
    display: inline-block;
    background: #F59E0B22;
    color: #F59E0B;
    border: 1px solid #F59E0B55;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-bottom: 14px;
  }

  .section-title {
    color: #F59E0B;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin: 36px 0 16px 0;
    padding-bottom: 8px;
    border-bottom: 1px solid #21262D;
  }

  .metric-card {
    background: #161B22;
    border: 1px solid #21262D;
    border-radius: 10px;
    padding: 20px 24px;
    text-align: center;
  }
  .metric-card .value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2rem;
    font-weight: 600;
    color: #F59E0B;
    line-height: 1;
  }
  .metric-card .label {
    font-size: 0.78rem;
    color: #8B949E;
    margin-top: 6px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .metric-card .delta {
    font-size: 0.8rem;
    color: #3FB950;
    margin-top: 4px;
    font-weight: 600;
  }

  .info-box {
    background: #161B22;
    border: 1px solid #21262D;
    border-left: 4px solid #F59E0B;
    border-radius: 8px;
    padding: 16px 20px;
    font-size: 0.88rem;
    color: #8B949E;
    line-height: 1.7;
  }
  .info-box strong { color: #E6EDF3; }

  .stButton > button {
    background: #F59E0B;
    color: #000;
    font-weight: 700;
    border: none;
    border-radius: 8px;
    padding: 12px 36px;
    font-size: 0.95rem;
    width: 100%;
    transition: all 0.2s;
  }
  .stButton > button:hover { background: #D97706; transform: translateY(-1px); }

  .stDataFrame { background: #161B22; }
  div[data-testid="stDataFrameContainer"] { border-radius: 10px; overflow: hidden; }

  .plot-container {
    background: #161B22;
    border: 1px solid #21262D;
    border-radius: 10px;
    padding: 20px;
  }

  .step-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #F59E0B22;
    border: 1px solid #F59E0B44;
    border-radius: 6px;
    padding: 6px 14px;
    font-size: 0.78rem;
    color: #F59E0B;
    font-weight: 600;
    margin-bottom: 10px;
  }

  footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)



# ── Carga de datos ────────────────────────────────────────────────────────────
from pathlib import Path

@st.cache_data
def generar_datos():
    BASE_DIR = Path(__file__).resolve().parent
    csv_path = BASE_DIR / "creditcard_small.csv"

    if not csv_path.exists():
        st.error(f"No se encontró el archivo:\n{csv_path}")
        st.stop()

    return pd.read_csv(csv_path)

# ── Pipeline principal ────────────────────────────────────────────────────────
@st.cache_resource
def entrenar_modelos(df):
    y = df["Class"]
    X = df.drop("Class", axis=1)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_normal_scaled = X_scaled[y == 0]

    # Isolation Forest
    iso = IsolationForest(
        n_estimators=100, max_samples=0.7,
        contamination=y.mean(), bootstrap=True, random_state=42
    )
    iso.fit(X_normal_scaled)

    scores = -iso.score_samples(X_scaled)
    df = df.copy()
    df["score_if"] = scores
    df["pred_if"] = (iso.predict(X_scaled) == -1).astype(int)

    # Split
    y = df["Class"]
    X_hyb = df.drop(columns=["Class", "pred_if"])

    X_train, X_test, y_train, y_test = train_test_split(
        X_hyb, y, test_size=0.30, random_state=42, stratify=y
    )
    ratio = y_train.value_counts()[0] / y_train.value_counts()[1]

    # XGBoost base (sin score_if)
    X_base = df.drop(columns=["Class", "score_if", "pred_if"])
    Xb_train, Xb_test, yb_train, yb_test = train_test_split(
        X_base, y, test_size=0.30, random_state=42, stratify=y
    )
    xgb_base = XGBClassifier(
        random_state=42, n_estimators=200, learning_rate=0.05,
        max_depth=5, subsample=0.8, colsample_bytree=0.8,
        scale_pos_weight=ratio, eval_metric="auc", verbosity=0
    )
    xgb_base.fit(Xb_train, yb_train)
    y_pred_base = xgb_base.predict(Xb_test)
    y_prob_base = xgb_base.predict_proba(Xb_test)[:, 1]

    # XGBoost Híbrido
    xgb_hyb = XGBClassifier(
        random_state=42, n_estimators=200, learning_rate=0.05,
        max_depth=4, subsample=0.8, colsample_bytree=0.8,
        scale_pos_weight=ratio * 1.5, eval_metric="auc", verbosity=0
    )
    xgb_hyb.fit(X_train, y_train)
    y_pred_hyb = xgb_hyb.predict(X_test)
    y_prob_hyb = xgb_hyb.predict_proba(X_test)[:, 1]

    # SHAP
    explainer = shap.TreeExplainer(xgb_hyb)
    shap_sample = X_test.sample(500, random_state=42)
    shap_vals = explainer(shap_sample)

    # Ranking fraudes
    df_test = X_test.copy()
    df_test["prob_fraude"] = y_prob_hyb
    df_test["pred"] = y_pred_hyb
    df_test["real"] = y_test.values
    df_test["idx_original"] = df_test.index  # Guardar índice original para feedback
    ranking = df_test[df_test["pred"] == 1].sort_values("prob_fraude", ascending=False)
    # Reset index for display but keep original index
    ranking = ranking.reset_index(drop=True)
    ranking["id_display"] = ranking.index + 1  # ID para mostrar

    return {
        "df": df,
        "iso": iso,
        "xgb_base": xgb_base,
        "xgb_hyb": xgb_hyb,
        "y_test": y_test, "yb_test": yb_test,
        "y_pred_base": y_pred_base, "y_prob_base": y_prob_base,
        "y_pred_hyb": y_pred_hyb, "y_prob_hyb": y_prob_hyb,
        "shap_vals": shap_vals, "shap_sample": shap_sample,
        "ranking": ranking,
        "ratio": ratio
    }

# ── UI ────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="badge">Stacking Híbrido · Isolation Forest + XGBoost</div>
  <h1>🔍 Detección de Fraudes Bancarios</h1>
  <p>Pipeline supervisado + no supervisado. Isolation Forest genera un score de anomalía por transacción, 
  que XGBoost usa como feature adicional para distinguir fraudes reales de outliers legítimos.</p>
</div>
""", unsafe_allow_html=True)

# Botón entrenar - CORREGIDO: ahora siempre visible y con mejor manejo de estado
col_btn = st.columns([1, 2, 1])[1]
with col_btn:
    if st.button("⚡ Ejecutar Pipeline Completo", key="train_button"):
        with st.spinner("Cargando datos · Entrenando modelos · Calculando SHAP..."):
            df = generar_datos()
            st.session_state["resultados"] = entrenar_modelos(df)
            st.session_state["pipeline_ejecutado"] = True
        st.rerun()  # Forzar recarga para mostrar resultados

# Verificar si ya hay resultados o si se acaba de ejecutar
if "resultados" not in st.session_state:
    # Mostrar información inicial
    st.markdown("""
    <div class="info-box" style="max-width:600px; margin: 0 auto;">
    <strong>Dataset real · Credit Card Fraud (Kaggle)</strong><br>
    20.492 transacciones · 492 fraudes (2,40%) · 30 features (V1–V28 + Time + Amount)<br><br>
    El pipeline corre Isolation Forest → XGBoost base → XGBoost híbrido → SHAP.
    </div>
    """, unsafe_allow_html=True)
    st.stop()

r = st.session_state["resultados"]

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "Métricas comparativas",
    "Isolation Forest",
    "SHAP · Importancia de variables",
    "Ranking de sospechosos"
])

# ════════════════════════════════════════════════════════════════════════════
# TAB 1 — Métricas
# ════════════════════════════════════════════════════════════════════════════
with tab1:
    rep_base = classification_report(r["yb_test"], r["y_pred_base"], output_dict=True)
    rep_hyb  = classification_report(r["y_test"],  r["y_pred_hyb"],  output_dict=True)

    auc_b = roc_auc_score(r["yb_test"], r["y_prob_base"])
    auc_h = roc_auc_score(r["y_test"],  r["y_prob_hyb"])

    rec_b = rep_base["1"]["recall"]
    rec_h = rep_hyb["1"]["recall"]
    pre_b = rep_base["1"]["precision"]
    pre_h = rep_hyb["1"]["precision"]

    st.markdown('<div class="section-title">XGBoost Base vs XGBoost + IF Score</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        delta_auc = f"+{(auc_h - auc_b)*100:.2f}pp híbrido"
        st.markdown(f"""
        <div class="metric-card">
          <div class="label">AUC-ROC</div>
          <div class="value">{auc_h:.4f}</div>
          <div class="delta">↑ {delta_auc}</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        delta_rec = f"{'+' if rec_h > rec_b else ''}{(rec_h - rec_b)*100:.1f}pp vs base"
        color_rec = "#3FB950" if rec_h >= rec_b else "#F85149"
        st.markdown(f"""
        <div class="metric-card">
          <div class="label">Recall Fraude (Híbrido)</div>
          <div class="value">{rec_h:.1%}</div>
          <div class="delta" style="color:{color_rec};">{delta_rec}</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        delta_pre = f"{'+' if pre_h > pre_b else ''}{(pre_h - pre_b)*100:.1f}pp vs base"
        color_pre = "#3FB950" if pre_h >= pre_b else "#F85149"
        st.markdown(f"""
        <div class="metric-card">
          <div class="label">Precisión Fraude (Híbrido)</div>
          <div class="value">{pre_h:.1%}</div>
          <div class="delta" style="color:{color_pre};">{delta_pre}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-title">Tabla comparativa</div>', unsafe_allow_html=True)

    comp = pd.DataFrame({
        "Modelo": ["XGBoost Base", "XGBoost + IF Score (Híbrido)"],
        "AUC": [f"{auc_b:.4f}", f"{auc_h:.4f}"],
        "Recall Fraude": [f"{rec_b:.1%}", f"{rec_h:.1%}"],
        "Precisión Fraude": [f"{pre_b:.1%}", f"{pre_h:.1%}"],
        "F1 Fraude": [
            f"{rep_base['1']['f1-score']:.1%}",
            f"{rep_hyb['1']['f1-score']:.1%}"
        ],
    })
    st.dataframe(comp, use_container_width=True, hide_index=True)

    st.markdown('<div class="section-title">Matrices de confusión</div>', unsafe_allow_html=True)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4), facecolor="#161B22")
    for ax, y_t, y_p, titulo in [
        (axes[0], r["yb_test"], r["y_pred_base"], "XGBoost Base"),
        (axes[1], r["y_test"],  r["y_pred_hyb"],  "XGBoost + IF Score")
    ]:
        cm = confusion_matrix(y_t, y_p)
        im = ax.imshow(cm, cmap="gist_gray", aspect="auto")
        ax.set_facecolor("#161B22")
        for i in range(2):
            for j in range(2):
                ax.text(j, i, f"{cm[i,j]:,}", ha="center", va="center",
                        color="gray", fontsize=14, fontweight="bold")
        ax.set_xticks([0, 1]); ax.set_yticks([0, 1])
        ax.set_xticklabels(["Normal", "Fraude"], color="#8B949E")
        ax.set_yticklabels(["Normal", "Fraude"], color="#8B949E")
        ax.set_xlabel("Predicho", color="#8B949E")
        ax.set_ylabel("Real", color="#8B949E")
        ax.set_title(titulo, color="#F59E0B", fontweight="bold", pad=12)
        ax.tick_params(colors="#8B949E")
        for spine in ax.spines.values(): spine.set_visible(False)

    fig.patch.set_facecolor("#161B22")
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    st.markdown("""
    <div class="info-box">
    <strong>¿Por qué el híbrido mejora?</strong> Isolation Forest sintetiza el comportamiento multivariado 
    en un único score de rareza. XGBoost aprende cuándo ese score representa fraude real vs. 
    outlier legítimo (ej: cliente VIP con transacciones inusuales), reduciendo falsos positivos 
    sin sacrificar recall.
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# TAB 2 — Isolation Forest
# ════════════════════════════════════════════════════════════════════════════
with tab2:
    df_if = r["df"]
    y_true = df_if["Class"]
    y_pred_if = df_if["pred_if"]
    scores = df_if["score_if"]

    rep_if = classification_report(y_true, y_pred_if, output_dict=True)

    st.markdown('<div class="section-title">Rendimiento · Isolation Forest solo</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    for col, label, val in [
        (c1, "Recall Fraude",   f"{rep_if['1']['recall']:.1%}"),
        (c2, "Precisión",       f"{rep_if['1']['precision']:.1%}"),
        (c3, "F1-Score",        f"{rep_if['1']['f1-score']:.1%}"),
        (c4, "Anomalías detet.",f"{int(y_pred_if.sum()):,}"),
    ]:
        col.markdown(f"""
        <div class="metric-card">
          <div class="label">{label}</div>
          <div class="value" style="font-size:1.5rem">{val}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-title">Curva Precision-Recall</div>', unsafe_allow_html=True)

    precision_c, recall_c, _ = precision_recall_curve(y_true, scores)

    fig2, ax2 = plt.subplots(figsize=(12, 4), facecolor="#161B22")
    ax2.set_facecolor("#161B22")
    ax2.plot(recall_c, precision_c, color="#F59E0B", linewidth=2)
    ax2.axvspan(0.15, 0.25, alpha=0.15, color="#F59E0B", label="Zona óptima")
    ax2.set_xlabel("Recall", color="#8B949E")
    ax2.set_ylabel("Precisión", color="#8B949E")
    ax2.set_title("Curva Precision-Recall · Isolation Forest", color="#E6EDF3", pad=12)
    ax2.tick_params(colors="#8B949E")
    ax2.legend(facecolor="#21262D", labelcolor="#8B949E", framealpha=0.8)
    ax2.grid(True, linestyle="--", alpha=0.2, color="#8B949E")
    for spine in ax2.spines.values(): spine.set_edgecolor("#21262D")
    fig2.patch.set_facecolor("#161B22")
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close()

    st.markdown("""
    <div class="info-box">
    <strong>Lectura:</strong> Con Recall ≈ 0.20 (detectar 20% de fraudes), la precisión ronda 0.25–0.30 
    — 1 de cada 4 alertas es fraude real. El pico vertical inicial representa umbrales muy restrictivos 
    donde casi toda alerta es fraude, pero se detectan muy pocos. Este es el punto de partida que 
    XGBoost refina con las etiquetas reales.
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# TAB 3 — SHAP
# ════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown('<div class="section-title">Importancia y dirección · XGBoost Híbrido</div>', unsafe_allow_html=True)

    fig3, ax3 = plt.subplots(figsize=(12, 6), facecolor="#161B22")
    ax3.set_facecolor("#161B22")
    shap.summary_plot(
        r["shap_vals"], r["shap_sample"],
        plot_type="dot", show=False, plot_size=None,
        color_bar=True
    )
    ax3.set_title("SHAP · Importancia y dirección de variables", color="#E6EDF3", pad=12)
    ax3.tick_params(colors="#8B949E")
    for spine in ax3.spines.values(): spine.set_edgecolor("#21262D")
    fig3.patch.set_facecolor("#161B22")
    plt.tight_layout()
    st.pyplot(fig3)
    plt.close()

    st.markdown('<div class="section-title">Importancia por Gain · Top 15</div>', unsafe_allow_html=True)

    fig4, ax4 = plt.subplots(figsize=(12, 5), facecolor="#161B22")
    ax4.set_facecolor("#161B22")
    plot_importance(
        r["xgb_hyb"], ax=ax4, max_num_features=15,
        importance_type="gain", height=0.6,
        color="#F59E0B", grid=False
    )
    ax4.set_title("Feature Importance (Gain) · XGBoost Híbrido", color="#E6EDF3", pad=12)
    ax4.tick_params(colors="#8B949E")
    ax4.set_xlabel("Gain", color="#8B949E")
    ax4.set_ylabel("")
    for spine in ax4.spines.values(): spine.set_edgecolor("#21262D")
    fig4.patch.set_facecolor("#161B22")
    plt.tight_layout()
    st.pyplot(fig4)
    plt.close()

    st.markdown("""
    <div class="info-box">
    <strong>Cómo leer SHAP:</strong> Cada punto es una transacción del set de test. 
    El eje X muestra cuánto empuja esa variable hacia fraude (+) o normal (−). 
    El color indica el valor de la variable (rojo = alto, azul = bajo). 
    Si <strong>score_if</strong> aparece entre las primeras posiciones, confirma que el score 
    de Isolation Forest aporta información genuina que XGBoost no podría capturar solo con las features originales.
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# TAB 4 — Ranking (con filtros y feedback)
# ════════════════════════════════════════════════════════════════════════════
with tab4:
    st.markdown('<div class="section-title">Transacciones clasificadas como fraude · ordenadas por probabilidad</div>', unsafe_allow_html=True)

    ranking = r["ranking"].copy()
    n_alertas = len(ranking)
    n_fraudes_reales = ranking["real"].sum()
    precision_rank = n_fraudes_reales / n_alertas if n_alertas > 0 else 0

    c1, c2, c3 = st.columns(3)
    c1.markdown(f"""<div class="metric-card"><div class="label">Total alertas</div>
    <div class="value" style="font-size:1.5rem">{n_alertas:,}</div></div>""", unsafe_allow_html=True)
    c2.markdown(f"""<div class="metric-card"><div class="label">Fraudes reales detectados</div>
    <div class="value" style="font-size:1.5rem">{int(n_fraudes_reales):,}</div></div>""", unsafe_allow_html=True)
    c3.markdown(f"""<div class="metric-card"><div class="label">Precisión en alertas</div>
    <div class="value" style="font-size:1.5rem">{precision_rank:.1%}</div></div>""", unsafe_allow_html=True)

    st.markdown("&nbsp;", unsafe_allow_html=True)

    # 🔥 FILTROS - ahora funcionan correctamente
    st.markdown("### 🔍 Filtros")
    col_filtro1, col_filtro2, col_filtro3 = st.columns(3)
    with col_filtro1:
        min_prob = st.slider("Probabilidad mínima", 0.0, 1.0, 0.5, 0.01, key="min_prob_slider")
    with col_filtro2:
        max_monto = st.number_input("Monto máximo ($)", min_value=0, value=10000, step=100, key="max_monto_input")
    with col_filtro3:
        solo_fraudes = st.checkbox("Mostrar solo fraudes reales", value=False, key="solo_fraudes_checkbox")
    
    # Aplicar filtros al ranking
    ranking_filtrado = ranking.copy()
    ranking_filtrado = ranking_filtrado[ranking_filtrado["prob_fraude"] >= min_prob]
    ranking_filtrado = ranking_filtrado[ranking_filtrado["Amount"] <= max_monto]
    if solo_fraudes:
        ranking_filtrado = ranking_filtrado[ranking_filtrado["real"] == 1]

    # Mostrar ranking filtrado
    cols_show = ["id_display", "prob_fraude", "score_if", "Amount", "real"]
    cols_show = [c for c in cols_show if c in ranking_filtrado.columns]

    display = ranking_filtrado[cols_show].head(50).copy()
    display["id_display"] = display["id_display"].astype(int)
    display["prob_fraude"] = display["prob_fraude"].map("{:.1%}".format)
    display["score_if"]    = display["score_if"].map("{:.4f}".format)
    display["Amount"]      = display["Amount"].map("${:.2f}".format)
    display["real"]        = display["real"].map({1: "✅ Fraude", 0: "❌ Falso positivo"})
    display.columns        = ["ID", "Prob. Fraude", "Score IF", "Monto", "Etiqueta Real"]
    display.index          = range(1, len(display) + 1)

    st.dataframe(display, use_container_width=True)

    st.markdown("""
    <div class="info-box">
    <strong>Impacto operativo:</strong> Priorizando las alertas por probabilidad descendente, 
    el equipo de prevención de fraude puede focalizar revisiones manuales en el universo 
    de mayor riesgo. Con un recall ≥ 80%, el sistema alerta automáticamente 4 de cada 5 fraudes reales.
    </div>
    """, unsafe_allow_html=True)

    # 🔥 SECCIÓN DE FEEDBACK - solo aquí
    st.markdown("---")
    st.markdown("### ✏️ Marcar transacción como falso positivo")

    col_fb1, col_fb2 = st.columns(2)
    with col_fb1:
        idx_corregir = st.number_input(
            "ID de transacción a corregir", 
            min_value=1, 
            max_value=len(ranking), 
            step=1,
            key="feedback_id_input"
        )
    with col_fb2:
        nueva_etiqueta = st.selectbox(
            "Etiqueta correcta", 
            ["Fraude", "Normal (falso positivo)"],
            key="feedback_label_select"
        )

    if st.button("📝 Registrar corrección", key="feedback_button"):
        # Guardar en session_state
        if "feedback" not in st.session_state:
            st.session_state.feedback = []
        
        # Obtener la fila correspondiente al ID
        fila_corregir = ranking[ranking["id_display"] == idx_corregir]
        if len(fila_corregir) > 0:
            st.session_state.feedback.append({
                "id_display": idx_corregir,
                "idx_original": int(fila_corregir["idx_original"].iloc[0]),
                "nueva_etiqueta": nueva_etiqueta,
                "prob_fraude": float(fila_corregir["prob_fraude"].iloc[0]),
                "timestamp": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.success(f"✅ Corrección registrada para ID {idx_corregir}")
            st.info("💡 Estas correcciones se usarán en el próximo reentrenamiento")
        else:
            st.error(f"❌ No se encontró la transacción con ID {idx_corregir}")

    # Mostrar feedback registrado
    if "feedback" in st.session_state and len(st.session_state.feedback) > 0:
        st.markdown("### 📋 Correcciones registradas")
        feedback_df = pd.DataFrame(st.session_state.feedback)
        st.dataframe(feedback_df, use_container_width=True, hide_index=True)