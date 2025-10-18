---
Comparación de algoritmos de regresión y mejora del ajuste predictivo en el análisis de precios de vehículos en Argentina
---
Análisis aplicado a un conjunto de datos obtenidos de Kaggle, los cuales fueron recopilados mediante un web scraping realizado en un sitio Argentino de clasificados. El dataset incluye múltiples características de automóviles correspondientes a enero de 2023, como marca, modelo, año, kilometraje, tipo de motor, versión, y otras especificaciones técnicas y comerciales relevantes.


Ejemplo del analisis exploratorio de los datos:
<img width="1008" height="423" alt="image" src="https://github.com/user-attachments/assets/0e93381b-9d6e-4ec9-97a4-e7aa99fdda68" />

<img width="1005" height="432" alt="image" src="https://github.com/user-attachments/assets/414c1eb1-dbee-4bae-80f7-090a82eb9955" />

<img width="1006" height="420" alt="image" src="https://github.com/user-attachments/assets/dd7b45c8-b669-4693-963a-b5926b7fdf05" />

<img width="1005" height="435" alt="image" src="https://github.com/user-attachments/assets/64a87e9c-2b0e-44b5-8566-3d232dd2f83a" />


A continuación los modelos de regresión utilizados:

Regresión Lineal

<img width="516" height="350" alt="image" src="https://github.com/user-attachments/assets/785c0712-a0d3-47c1-b4ac-44b1e5122502" />

Regresión Polinomica

<img width="640" height="387" alt="image" src="https://github.com/user-attachments/assets/5fef0a82-f558-4243-b07d-9b872aa93d8d" />

Gradient Boosting

<img width="981" height="451" alt="image" src="https://github.com/user-attachments/assets/62c2c33e-ef1e-49cd-a9fa-35ccaa0ab0b4" />

XGBoost

<img width="997" height="473" alt="image" src="https://github.com/user-attachments/assets/30f59cff-8d03-4562-8eda-7537a3c71d3c" />


Finalmente, se realiza un análisis comparativo de los diferentes modelos de regresión empleados, evaluando su desempeño en función del Error Cuadrático Medio (MSE). Este enfoque permite determinar cuál de los modelos logra predecir los precios de los automóviles con mayor precisión, ya que a medida que el valor del MSE disminuye, el modelo se aproxima de manera más exacta a los valores reales, reflejando un mejor ajuste y capacidad predictiva


<img width="766" height="440" alt="image" src="https://github.com/user-attachments/assets/11614f2c-de52-4e47-8e79-ca2d4fc3a04b" />
