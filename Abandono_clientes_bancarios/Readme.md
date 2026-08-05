
## Machine Learning aplicado a la retención de clientes bancarios: Predicción de abandono

> El modelo XGBoost obtuvo el mejor Recall.Que es el abandono de clientes (Churn). Es la tasa de clientes que dejan de usar un servicio o producto durante un período de tiempo determinado.  
> Fórmula básica: (Clientes perdidos en un período / Total de clientes al inicio del período) × 100.
Ejemplo: si empiezo el mes con 1.000 clientes y pierdo 50, el churn mensual es del 5%.

## Tipos de Churn

| Tipo | Definición | Causas comunes | Estrategia recomendada |
|------|------------|----------------|------------------------|
| **Churn Voluntario** | El cliente toma la decisión activa de cancelar o abandonar el servicio. | - Insatisfacción con el producto/servicio <br> - Mejor oferta de la competencia <br> - Precio percibido como muy alto <br> - Mala experiencia de usuario <br> - Falta de valor percibido | - Mejorar la experiencia del cliente <br> - Programas de fidelización <br> - Personalización de ofertas <br> - Análisis de feedback y quejas <br> - Mejora continua del producto |
| **Churn Involuntario** | El cliente se pierde por razones ajenas a su voluntad, sin intención de cancelar. | - Tarjeta de crédito expirada <br> - Fondos insuficientes en la cuenta <br> - Error en el procesamiento de pago <br> - Cambio de correo electrónico sin actualizar <br> - Migración de cuenta fallida | - Automatizar recordatorios de pago <br> - Ofrecer múltiples métodos de pago <br> - Sistema de reintentos de cobro <br> - Notificaciones proactivas <br> - Facilitar la actualización de datos |
| **Churn Activo** | El cliente se da de baja formalmente y notifica su salida. | - Decisión consciente y documentada <br> - Suele ir precedida de señales de alerta | - Encuestas de salida para conocer motivos <br> - Ofertas de retención personalizadas <br> - Análisis de patrones previos a la baja |
| **Churn Pasivo** | El cliente deja de usar el servicio sin notificarlo formalmente (especialmente en modelos freemium o prueba gratuita). | - Falta de engagement <br> - No encuentra valor en el producto <br> - Olvido o abandono silencioso | - Campañas de reactivación <br> - Onboarding mejorado <br> - Análisis de comportamiento temprano <br> - Recordatorios y estímulos de uso |
| **Churn Total** | Cliente que cancela todos los servicios o productos contratados. | - Abandono completo de la relación comercial | - Estrategias de retención agresivas <br> - Análisis profundo del motivo de salida <br> - Ofertas de reincorporación |
| **Churn Parcial** | Cliente que reduce el nivel de gasto o servicios contratados sin llegar a cancelar todo. | - Ajuste de presupuesto <br> - Reducción de necesidad <br> - Prueba de alternativas sin abandonar del todo | - Upselling y cross-selling <br> - Demostrar valor adicional <br> - Planes flexibles según necesidades |

En este notebook aplico técnicas de Machine Learning para analizar y predecir la probabilidad de que los clientes de un banco abandonen el servicio. Comienzo con la preparación de los datos, incluyendo limpieza y escalado, seguida de un análisis exploratorio para entender la composición del dataset, presentando gráficos de las métricas clave.
Luego, implemento y comparo tres algoritmos comúnmente utilizados en problemas de predicción de abandono de clientes: Random Forest, XGBoost y una Red Neuronal, evaluando su desempeño a través de métricas relevantes como precisión, recall y exactitud. Finalmente, selecciono el modelo más adecuado para realizar predicciones de prueba y demostrar su aplicación práctica.

Analisis exploratorio de los datos:
<img width="1289" height="401" alt="image" src="https://github.com/user-attachments/assets/d62f5cf9-7fe2-48b8-80e2-122ee11c2d72" />

<img width="1096" height="423" alt="image" src="https://github.com/user-attachments/assets/5a413e31-a70a-4280-9d3e-580a80285092" />

<img width="1081" height="326" alt="image" src="https://github.com/user-attachments/assets/4b5027b3-bb1e-458a-8e14-4ea185df9834" />

<img width="1050" height="324" alt="image" src="https://github.com/user-attachments/assets/84ff433c-9350-443a-9ed5-1fea704a72d5" />  

En un problema de reducción de abandono de clientes, el objetivo principal no es maximizar la precisión global, sino identificar correctamente a los clientes que realmente van a abandonar (clase positiva, 1).

Esto se debe a que el costo de un falso negativo (no detectar a un cliente que se va a ir) es significativamente mayor que el de un falso positivo (gastar recursos en un cliente que finalmente no se iba). Por lo tanto, la métrica más relevante en este contexto es el Recall (sensibilidad) para la clase positiva, ya que mide la capacidad del modelo para capturar a los verdaderos clientes en riesgo de abandono.

Tras comparar los algoritmos evaluados, se observa que XGBoost ofrece el mejor equilibrio entre detección de abandonos y precisión:

Alto Recall (0.77): Detecta la mayor proporción de clientes que realmente abandonarán, minimizando los falsos negativos.

Buena Precisión (0.74): Aunque no es la más alta, mantiene un nivel aceptable de falsos positivos, lo que evita campañas de retención ineficientes.

Rendimiento general equilibrado: Supera por un margen muy ajustado a la Red Neuronal, pero con una ventaja clara en la detección de casos positivos, que es la prioridad del negocio.

 A continuación el grafico comparativo de las metricas obtenidas en cada algoritmo.  
<img width="1051" height="424" alt="image" src="https://github.com/user-attachments/assets/2f8890fc-c07b-418b-8ab8-fcf750f07512" />

Y las matrices de confusión de cada uno.
<img width="1302" height="367" alt="image" src="https://github.com/user-attachments/assets/0c691bb5-ae0e-4b10-b9ab-14ea8210400f" />

Por todo ello, XGBoost es el modelo seleccionado para implementar en el sistema de predicción de churn. 

## Créditos y autor
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Nestor_Diaz-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/contadornestordiaz/)
