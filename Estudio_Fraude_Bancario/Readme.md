El fraude bancario se refiere a cualquier acción intencional destinada a obtener un beneficio económico indebido perjudicando a una entidad financiera o a sus clientes.
El objetivo del análisis con Machine Learning es detectar patrones anómalos o sospechosos en los datos transaccionales o crediticios antes de que el fraude ocurra o se concrete.

Los tipos más comunes de fraude:

- Fraude con tarjetas de crédito/débito: Transacciones no autorizadas, uso de datos robados o clonados, compras online con tarjetas comprometidas.

- Fraude de identidad: Solicitudes de crédito o préstamos con documentación falsificada, suplantación de identidad de clientes reales.

- Fraude interno: Manipulación de datos o procesos por parte de empleados, acceso indebido a cuentas o registros.

- Fraude en transferencias electrónicas: Desvío de fondos a cuentas no autorizadas, phishing, smishing o ingeniería social.

- Lavado de dinero: Uso del sistema bancario para legitimar fondos ilícitos mediante múltiples transacciones pequeñas.

Estas tipologías permiten entender los distintos patrones de fraude que los modelos deben aprender a detectar.
Para ello, se emplean indicadores operativos y financieros que ayudan a identificar operaciones anómalas o perfiles de riesgo dentro de las transacciones bancarias.

Entre los más comunes se encuentran:

**a) Ratio de Transacción Sospechosa (RTS):**

$$
RTS = \frac{\text{Monto de transacciones sospechosas}}{\text{Monto total de transacciones del cliente}}
$$

Este indicador mide qué proporción del volumen total del cliente corresponde a operaciones marcadas como sospechosas.
Cuando el valor de RTS supera cierto umbral (por ejemplo, 0.05 o 0.10 según la política interna de cada entidad), puede reflejar una actividad irregular a revisar.

**b) Variación de Monto Transaccional (VMₜ):**

$$
VM_t = \frac{|M_t - M_{hist}|}{M_{hist}}
$$
Donde:

$M_t$: monto total de transacciones en el período actual

$M_{hist}$: promedio histórico de montos del cliente


Aqui se compara el monto actual de una transacción con el promedio histórico del cliente.
Un VMₜ elevado indica operaciones atípicas respecto al comportamiento habitual.

c) **Frecuencia de Transacciones (Fᵢ):**

$$F_i = \frac{\text{Días del período analizado}}{\text{N° de transacciones en el período}}$$

Permite detectar incrementos súbitos en la frecuencia de operaciones, lo que puede sugerir automatización o uso indebido de credenciales.

d) **Ratio de Ubicación Atípica (RL):**

$$ RL = \frac{\text{N° de operaciones fuera del país habitual}}{\text{Total de operaciones}}$$

Un valor alto puede señalar movimientos inusuales en regiones donde el cliente no opera habitualmente, alertando sobre posibles fraudes geográficos.

Estas fórmulas permiten cuantificar el comportamiento de los clientes y traducirlo en variables numéricas que luego sirven como entradas del modelo predictivo. En este sentido, el fraude, desde el enfoque del Machine Learning, se aborda como un problema de clasificación binaria, donde el objetivo es distinguir entre operaciones legítimas y operaciones fraudulentas. En este tipo de análisis, suele presentarse un fuerte desbalance de clases, ya que de miles de registros disponibles, solo una pequeña proporción corresponde efectivamente a casos de fraude.

Debido a esta característica, los modelos más utilizados para este tipo de problemas suelen ser aquellos capaces de manejar bases de datos desbalanceadas, tales como:

- Regresión Logística

- Árboles de Decisión y Random Forest

- XGBoost o LightGBM

- Redes Neuronales (en escenarios más complejos)

Estos modelos se complementan con técnicas específicas para equilibrar las clases, como oversampling (SMOTE), undersampling o el uso de ponderación de clases (class weights).

Como los casos de fraude son muy pocos en comparación con los casos legítimos, las métricas tradicionales como la exactitud (accuracy) pueden resultar engañosas. Por ejemplo, un modelo que clasifica todo como “no es fraude” podría tener una precisión del 99 %, pero en realidad no estaría detectando ningún caso fraudulento.

Por este motivo, se utilizan métricas específicas que permiten evaluar mejor el rendimiento del modelo frente a este tipo de situaciones:

- Precisión: mide qué proporción de las operaciones que el modelo predijo como fraude realmente lo son. Es clave cuando se busca reducir los falsos positivos (casos legítimos marcados erróneamente como fraude).

- Recall o Sensibilidad: indica qué porcentaje de los fraudes reales fueron correctamente detectados por el modelo. Es fundamental cuando la prioridad es no dejar escapar fraudes verdaderos.

- F1-Score: combina precisión y recall en una sola métrica, siendo útil para encontrar un equilibrio entre ambos.

- AUC-ROC (Área bajo la curva ROC): evalúa la capacidad del modelo para distinguir entre clases en distintos umbrales de decisión. Cuanto más se acerque a 1, mejor es la capacidad discriminante.

- Matriz de confusión: muestra de forma detallada cuántas predicciones fueron verdaderas o falsas para cada clase, permitiendo identificar el tipo de error que más comete el modelo (falsos positivos o falsos negativos).


En este notebook aplico técnicas de Machine Learning orientadas a la detección de fraude bancario, con el objetivo de identificar transacciones potencialmente fraudulentas a partir de patrones en los datos.
El proceso incluye la preparación y normalización del dataset, análisis exploratorio para evaluar distribuciones y desequilibrio de clases, y la implementación comparativa de modelos utilizados.
Finalmente, se evalúa el rendimiento de cada modelo mediante métricas como Precision, Recall y F1-Score, priorizando la capacidad de detección de fraudes minimizando falsos negativos.

Distribución de la variable objetivo
<img width="1333" height="444" alt="image" src="https://github.com/user-attachments/assets/0140d2f7-57f4-4acb-ac4a-44c09a185270" />

Matriz de correlación (mas correlacionadas)  
<img width="447" height="317" alt="image" src="https://github.com/user-attachments/assets/1e3201ad-9957-4a27-8caf-68cf9f0ec5b1" />

Metricas de los modelos de ML estudiados
<img width="1376" height="624" alt="image" src="https://github.com/user-attachments/assets/94befa8b-9e1d-4653-beae-e5ecfe5e38d9" />


