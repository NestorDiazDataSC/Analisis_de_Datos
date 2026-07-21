## Estudio de Forecasting con Prophet (Meta) aplicado a pagos QR

Este notebook presenta un estudio de **pronóstico de series temporales** utilizando **Prophet**, la librería desarrollada por Meta, con el objetivo de proyectar el volumen de pagos realizados mediante plataformas **QR** para un horizonte de **90 días**.

El modelo se construye a partir de un **dataset sintético/simulado**, diseñado con fines exclusivamente educativos y de experimentación, permitiendo reproducir un escenario similar al que podría encontrarse en una entidad financiera o empresa del sector de medios de pago.

Además de la información histórica de transacciones, el modelo incorpora **regresores externos** que pueden influir en el comportamiento de la serie, entre ellos un calendario de **feriados nacionales argentinos** y un **calendario personalizado de eventos comerciales**, incluyendo fechas de alta actividad como Hot Sale, CyberMonday, Black Friday y otras jornadas especiales que suelen impactar en el volumen de operaciones.

A lo largo del notebook se desarrolla el flujo completo de trabajo, incluyendo la preparación y exploración de los datos, el entrenamiento del modelo, la incorporación de variables exógenas, la generación de pronósticos, el análisis de los componentes de la serie (tendencia y estacionalidades) y la evaluación del desempeño mediante **validación cruzada para series temporales**, utilizando métricas como **MAE**, **RMSE** y **MAPE**.

El propósito de este trabajo es demostrar una metodología práctica para la construcción y evaluación de modelos de forecasting aplicados al ámbito financiero, mostrando cómo la incorporación de información contextual puede contribuir a mejorar la calidad de las predicciones y facilitar la toma de decisiones basada en datos.


