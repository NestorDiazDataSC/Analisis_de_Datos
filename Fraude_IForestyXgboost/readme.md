## XGBoost con Score de Anomalía de Isolation Forest para Detección de Fraudes

>Isolation Forest es un algoritmo de detección de anomalías basado en árboles aleatorios que parte de la premisa de que las observaciones anómalas son más fáciles de aislar que las normales, ya que requieren un menor número de particiones para quedar separadas del resto de los datos. Al aplicar este algoritmo sobre el conjunto de transacciones, se obtiene para cada observación un score de anomalía, que refleja el grado de rareza o desviación respecto al comportamiento habitual. Este score se incorpora posteriormente como una nueva característica de entrada para entrenar el modelo XGBoost, dando lugar a un enfoque de Stacking Híbrido. De esta manera, XGBoost puede aprender a interpretar la información proporcionada por Isolation Forest y determinar, en combinación con el resto de las variables, si una transacción corresponde o no a un fraude.

Contenido del notebook:

EDA.
Isolation Forest.
Aplicación de XGBoost con Score de Isolation Forest.
SHAP para el modelo supervisado.

EDA  
<img width="1291" height="648" alt="image" src="https://github.com/user-attachments/assets/a79a2092-cac2-4df3-a659-f603601af10d" />

<img width="1277" height="596" alt="image" src="https://github.com/user-attachments/assets/246e86bc-34c6-4bc4-ab7b-37d5719f8e58" />

<img width="1290" height="384" alt="image" src="https://github.com/user-attachments/assets/391f4a62-56a1-4df9-9249-e0c3c75f496b" />

Explicabilidad del modelo elegido.  
<img width="525" height="677" alt="image" src="https://github.com/user-attachments/assets/c943c70c-918f-4725-807f-1dc17cbfde50" />

Cada punto representa una observación.
El eje X muestra el valor SHAP:
Derecha (+): aumenta la probabilidad de fraude.
Izquierda (-): disminuye la probabilidad de fraude.
El color indica el valor de la variable:
Azul = valor bajo.
Rosa/Rojo = valor alto.
Las variables están ordenadas por importancia global (de arriba hacia abajo)
Se logró un modelo híbrido con Isolation Forest + XGBoost optimizado mediante cambios en los hiperparametros, alcanzando un Recall del 84% en el set de test. El impacto operativo es que de cada 100 casos de anomalías/fraudes reales, el sistema alerta automáticamente 84. Esto reduce el riesgo fiscal y financiero, tambien permite focalizar esfuerzos en un universo delimitado de alertas."

## Créditos y autor
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Nestor_Diaz-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/contadornestordiaz/)


