## Forecasting de series temporales sobre acciones de APPLE con ARIMA

En los mercados financieros actuales, la capacidad de anticipar—aunque sea con un horizonte reducido—la dirección del precio de un activo es una ventaja competitiva significativa. Apple Inc. (AAPL), al ser uno de los valores con mayor capitalización bursátil y liquidez global, concentra un volumen de operaciones diario que supera los miles de millones de dólares.

Sin embargo, su precio no es un proceso aleatorio puro; presenta componentes estacionales, tendencias de largo plazo y efectos de memoria (autocorrelación) que pueden ser capturados mediante modelos estadísticos.

El modelo ARIMA (AutoRegressive Integrated Moving Average) es uno de los métodos más consolidados en la literatura de series temporales financieras por su robustez, interpretabilidad y bajo coste computacional en comparación con redes neuronales profundas. Su aplicación aquí no busca "adivinar" el precio exacto—algo imposible bajo la Hipótesis del Mercado Eficiente sino generar señales de probabilidad que puedan mejorar el ratio de Sharpe de una cartera (entender si una estrategia de inversión es realmente buena o solo es suerte).

>ARIMA  
-AR (AutoRegresivo) : La variable se explica por sus propios valores pasados. Ejemplo: el precio de hoy depende del precio de ayer. (-p-)  
-I (Integrado) : Es la diferenciación que aplicamos para hacer la serie estacionaria. Corresponde al número de veces que diferenciamos los datos. (-d-)  
-MA (Media Móvil) : Modela el error del pronóstico como combinación de errores pasados. (-q-)  

Serie de tiempo de la acción:  
<img width="1311" height="348" alt="image" src="https://github.com/user-attachments/assets/8b1a9cfc-c84b-49e9-9ad7-ddb0f895e6df" />

<img width="758" height="408" alt="image" src="https://github.com/user-attachments/assets/78073fec-93e7-4a19-9f1d-0469f998c267" />

El histograma de residuos presenta una forma que se aproxima a una distribución normal, evidenciando una clara simetría alrededor del valor central. Se observa una concentración mayor de residuos en las cercanías del cero, con una disminución gradual y progresiva hacia ambos extremos. Esta configuración en forma de campana sugiere que los errores del modelo siguen un comportamiento cercano al esperado bajo el supuesto de normalidad
<img width="1281" height="392" alt="image" src="https://github.com/user-attachments/assets/1d2296a6-5a78-445a-9a15-691f620ad850" />


Predicción:  
<img width="1318" height="420" alt="image" src="https://github.com/user-attachments/assets/ef28d058-4997-46a0-8f75-216f5f8e1c2b" />

Conclusiones: El modelo ARIMA(0,1,0) con deriva genera predicciones que forman una línea recta, con pendiente constante igual al coeficiente de deriva. Esto es matemáticamente correcto según la estructura del modelo, pero implica que la serie no presenta patrones adicionales (estacionalidad, autocorrelación, etc.) que permitan enriquecer el pronóstico.  
Se implementaron modelos ARIMA y SARIMA sin obtener mejoras significativas en la capacidad predictiva, ningun modelo probado mejora al modelo mas simple, evidenciando que la serie presenta un comportamiento cercano a ruido o caminata aleatoria. En función de ello, se propone la utilización de modelos otros modelos.

## Créditos y autor
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Nestor_Diaz-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/contadornestordiaz/)
