
Tarjetas de crédito: usando Machine Learning para predecir elegibilidad. Ejemplo de preparación y visualización de datos
---

En este proyecto, el objetivo principal es realizar un análisis exploratorio y de visualización de los datos de clientes, con el fin de preparar la información para su posterior uso en algoritmos de machine learning. Se busca identificar clientes potencialmente elegibles para recibir una tarjeta, generando así insights útiles y confiables para la toma de decisiones comerciales.

El análisis exploratorio de los datos arroja lo siguiente:

<img width="585" height="457" alt="image" src="https://github.com/user-attachments/assets/4d795a11-d84b-4c03-b20d-7a7b8d5873e4" />

<img width="1254" height="511" alt="image" src="https://github.com/user-attachments/assets/675e47ad-c1d3-4019-ab68-990660df1050" />

<img width="1233" height="367" alt="image" src="https://github.com/user-attachments/assets/0605d675-e9ba-4f79-9ce6-be387501f6e6" />

<img width="578" height="461" alt="image" src="https://github.com/user-attachments/assets/ce8ba461-0f02-493e-b2dc-bf8dbae74b63" />

Luego se aplicaran 3 modelos de clasificación para determinar si un cliente X puede ser o no aprobado para un producto financiero.

Modelos a usar:

- Regresión Logística (modelo clásico en el análisis de scoring crediticio, es el mas aceptado generalmente)
- Random Forest (mas robusto y con mejor balance entre potencia e interpretabilidad)
- XGBoost (Es el más preciso pero no tan interpretable).
  
Se evalúan utilizando métricas como:
- Accuracy (% de predicciones correctas sobre el total de los casos)
- Recall (Mide cuantos clientes que podrían ser aprobados fueron correctamente detectados).
- Auc (Mide como el modelo es capas de diferenciar entre aprobados y no aprobados, que tan bien los ordena de un lado y del otro).
