## Construcción de un Modelo de detección de Fraude

Construcción de un modelo predictivo para la detección de fraude a partir de un conjunto de datos de aproximadamente 250.000 registros. Se desarrollan etapas de ingeniería de características, reducción de dimensionalidad y entrenamiento de un modelo Random Forest

EDA
<img width="1304" height="547" alt="image" src="https://github.com/user-attachments/assets/2e442649-1ed4-4a7c-bcfd-f77961c4b3dc" />
En la columna de operaciones normales, se ve una concentración de puntos (mancha negra muy densa en la parte baja), eso indica que el grueso de transacciones legítimas son de montos pequeños o medianos, arriba marco que existen outliers de estas operaciones pero son totalmente autenticas.  

<img width="1307" height="285" alt="image" src="https://github.com/user-attachments/assets/d9ac8ad2-e3e2-4c2a-8db0-7a13195ea80a" />

| Tipo de Transacción | Descripción | Ilícitos más comunes |
|---------------------|-------------|----------------------|
| **P2M** (Person to Merchant) | Pagos de una persona a un comercio (ej. pagos con QR). | Abuso operativo y contracargos en pagos. |
| **P2P** (Person to Person) | Transferencias entre personas (ej. transferencias entre familiares). | Fraude de ingeniería social, uso de cuentas intermediarias, cuentas de terceros que prestan CBU/Alias, etc. |

<img width="1302" height="289" alt="image" src="https://github.com/user-attachments/assets/3670c15b-1aac-465b-a981-545718711878" />
Los rubros más utilizados corresponden, en primer lugar, a Grocery, asociado a la compra de alimentos y productos de consumo diario (almacenes y supermercados). Le sigue el rubro Food, también vinculado a la adquisición de alimentos. En tercer lugar se ubica Shopping que agrupa compras en comercios minoristas no esenciales, tales como indumentaria, calzado, electrónica, artículos para el hogar.  


Conclusiones:
<img width="1117" height="203" alt="image" src="https://github.com/user-attachments/assets/d4f8ca65-4543-43b7-81ae-7b3d8651e937" />


## Créditos y autor
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Nestor_Diaz-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/contadornestordiaz/)
