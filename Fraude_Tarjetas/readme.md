En el sector financiero, detectar una transacción fraudulenta a tiempo puede significar la diferencia entre recuperar o perder miles de pesos. Pero no todos los errores cuestan lo mismo: dejar pasar un fraude es mucho más costoso que bloquear por error una compra legítima. Este notebook aborda ese problema desde dos ángulos: el técnico y el de negocio. Se entrena y compara una Regresión Logística usada como benchmarkc contra un modelo XGBoost sobre un dataset de transacciones con tarjeta de crédito, evaluando no solo métricas estándar sino también el impacto económico real de cada tipo de error en el contexto argentino.

Flujo del análisis:

Limpieza y preparación de datos
Análisis exploratorio y correlaciones
Entrenamiento y comparativa de modelos
Ajuste de umbral de decisión
Matriz de impacto económico
Explicabilidad con SHAP
Análisis de errores (falsos negativos)
El dataset contiene registros de transacciones con variables como monto, saldo, distancia al comercio, hora de operación, antecedentes de fraude e indicador de operación internacional. Incluye ruido real: valores corruptos, nulos con distintos criterios de imputación etc.

<img width="1301" height="643" alt="image" src="https://github.com/user-attachments/assets/6ab591b6-f715-45a0-b14e-d794e7eb8fa3" />

<img width="1268" height="644" alt="image" src="https://github.com/user-attachments/assets/461a57b1-bd56-41d2-ab0a-bb0c77ab21f7" />

<img width="1306" height="409" alt="image" src="https://github.com/user-attachments/assets/6c191f4e-771d-4628-a31c-dd99eee7dbb2" />

<img width="1309" height="503" alt="image" src="https://github.com/user-attachments/assets/c057ad64-36a0-43bb-aadf-3481289f4a44" />
