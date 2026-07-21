## Estudio de Forecasting con Prophet (Meta) aplicado a pagos QR

Este notebook presenta un estudio de **pronóstico de series temporales** utilizando **Prophet**, la librería desarrollada por Meta, con el objetivo de proyectar el volumen de pagos realizados mediante plataformas **QR** para un horizonte de **90 días**.

El modelo se construye a partir de un **dataset sintético/simulado**, diseñado con fines exclusivamente educativos y de experimentación, permitiendo reproducir un escenario similar al que podría encontrarse en una entidad financiera o empresa del sector de medios de pago.

Además de la información histórica de transacciones, el modelo incorpora **regresores externos** que pueden influir en el comportamiento de la serie, entre ellos un calendario de **feriados nacionales argentinos** y un **calendario personalizado de eventos comerciales**, incluyendo fechas de alta actividad como Hot Sale, CyberMonday, Black Friday y otras jornadas especiales que suelen impactar en el volumen de operaciones.

A lo largo del notebook se desarrolla el flujo completo de trabajo, incluyendo la preparación y exploración de los datos, el entrenamiento del modelo, la incorporación de variables exógenas, la generación de pronósticos, el análisis de los componentes de la serie (tendencia y estacionalidades) y la evaluación del desempeño mediante **validación cruzada para series temporales**, utilizando métricas como **MAE**, **RMSE** y **MAPE**.

El propósito de este trabajo es demostrar una metodología práctica para la construcción y evaluación de modelos de forecasting aplicados al ámbito financiero, mostrando cómo la incorporación de información contextual puede contribuir a mejorar la calidad de las predicciones y facilitar la toma de decisiones basada en datos.

Ejemplos del EDA:  
<img width="978" height="422" alt="image" src="https://github.com/user-attachments/assets/4d87ec80-f09b-4154-a293-5ce4f9a52249" />

<img width="1054" height="326" alt="image" src="https://github.com/user-attachments/assets/a77f9ba6-2437-49bc-b27d-f1c883769d35" />

<img width="1284" height="345" alt="image" src="https://github.com/user-attachments/assets/7d476a03-0775-490c-acc7-5ac0dd1c4bbb" />

Componentes del modelo:  
- Tendencia (trend): Muestra la dirección general de los datos a largo plazo, quitando el ruido de los días o los meses. En este caso muestra una tendencia general al alza desde finales de 2023 hasta principios de 2027. No es una línea recta, tiene fluctuaciones y luego se estabiliza subiendo. Al final de la linea (en abril 2027) se ven los intervalos de incertidumbre de la predicción a futuro.
- Estacionalidad Semanal (weekly): Muestra el comportamiento o patrón que se repite cada semana según el día. El grafico dice que los fines de semana (domingo y sábado) tienen un impacto altísimo y positivo en la métrica, en cambio durante los días de semana (lunes a viernes), la actividad cae drásticamente y se mantiene en negativo respecto a la media.
- Estacionalidad Anual (yearly): Muestra cómo varían los datos a lo largo de los meses de un año completo (de enero a enero). Hay una estacionalidad anual muy marcada. El pico más alto ocurre en los primeros meses del año y a partir de mayo, empieza a caer en hasta tocar fondo aproximadamente en agosto, para luego volver a recuperarse con fuerza hacia el fin de año.
- Regresores Extra Aditivos (extra_regressors_additive): Estos son eventos o variables externas que fueron agregados al modelo (feriados, días de promociones especiales, eventos tipo Black Friday, etc). Esos picos o líneas verticales muestran momentos exactos en el tiempo donde ocurrió un evento especial que le sumó un valor fijo (cercano a 2.500) a la predicción general.
<img width="637" height="819" alt="image" src="https://github.com/user-attachments/assets/027fe34c-9214-401d-88c8-daea8c0c63a5" />

Metricas: MAPE  
<img width="607" height="387" alt="image" src="https://github.com/user-attachments/assets/161caab7-5a85-46a2-b8cc-4c37dff72d67" />

Grafico de historicos, pronostico + 90 dias  
<img width="713" height="439" alt="image" src="https://github.com/user-attachments/assets/fec24dae-13e0-441b-9be3-79ff6ca8932a" />


## Créditos y autor
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Nestor_Diaz-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/contadornestordiaz/)
