## Analisis sobre riesgo crediticio

> En el negocio financiero, el crédito es un activo que genera ingresos, pero también riesgos. La gestión del riesgo crediticio busca cuantificar y mitigar las pérdidas derivadas del incumplimiento de los clientes, utilizando modelos estadísticos y métricas regulatorias.  
> En el marco de los acuerdos de Basilea II y III, el riesgo crediticio se mide a través de tres componentes fundamentales: [PD], [LGD] y [EAD], que permiten estimar la Pérdida Esperada [Expected Loss]. Luego se complementa con ejercicios de Stress Testing para medir la capacidad del portafolio de préstamos o inversiones de un banco de resistir shocks adversos sin generar pérdidas críticas o incumplimientos regulatorios.

> | Concepto | Significado | Resumen |
> |---|---|---|
> | **PD** | Probability of Default | Probabilidad de que el cliente entre en default. |
> | **LGD** | Loss Given Default | Porcentaje de pérdida si ocurre el default, considerando recuperos y garantías. |
> | **EAD** | Exposure at Default | Monto de exposición que tendrá el banco al momento del default. |
> | **EL** | Expected Loss | Pérdida esperada del crédito. Combina PD, LGD y EAD. |
> | **Default** | Incumplimiento | Situación en la que el deudor no cumple con sus obligaciones de pago. |

El proyecto partió de datos no anonimizados de clientes bancarios. Tras la carga y control de calidad de los datos, se realizó un análisis exploratorio (EDA) para identificar patrones. Sobre esta base, se aplicaron múltiples algoritmos de machine learning. Finalmente, se calculó el Expected Loss para esos datos.

EDA
<img width="1289" height="466" alt="image" src="https://github.com/user-attachments/assets/94534cf7-7a27-4b4d-aef3-82e9e7566ac4" />

<img width="1286" height="464" alt="image" src="https://github.com/user-attachments/assets/a9f03448-a01d-4a17-ba45-d6a5e099d4c5" />

<img width="1289" height="495" alt="image" src="https://github.com/user-attachments/assets/82f7a2af-8ccc-42cf-8a34-428a456cefe6" />

<img width="1289" height="497" alt="image" src="https://github.com/user-attachments/assets/4e836699-f4ba-4622-9906-9aa90cd84c07" />

<img width="1284" height="469" alt="image" src="https://github.com/user-attachments/assets/b58f9249-da4c-4cc0-9859-d172330b5452" />

Distribucion de la perdida esperada (Expected Loss)  
Es una métrica central en riesgo crediticio, estima la pérdida promedio esperada por incumplimiento de los clientes.  
<img width="1287" height="340" alt="image" src="https://github.com/user-attachments/assets/e4560377-7efe-4798-95b8-999645ffe453" />
Los montos bajos corresponden a clientes con una exposición monetaria reducida, por lo que representan un menor riesgo de pérdida. En cambio, los montos más elevados suelen estar asociados a clientes con una mayor exposición y, por ende, con una mayor probabilidad de incumplimiento (default). Por ello, cuando las barras de mayor altura se concentran hacia la izquierda del gráfico, significa que la mayor parte de los clientes presenta pérdidas esperadas bajas. Las barras ubicadas hacia la derecha representan a un grupo más reducido de clientes, pero con pérdidas esperadas considerablemente mayores.

## Créditos y autor
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Nestor_Diaz-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/contadornestordiaz/)
