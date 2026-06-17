<img width="1206" height="660" alt="image" src="https://github.com/user-attachments/assets/5e9846b7-771e-4f50-8254-b7f377372c66" />

Las herramientas de fiscalización vinculadas a facturas apócrifas y registros asociados (como la Base APOC o “Base de Contribuyentes No Confiables”) se remontan a normativas internas de AFIP de los años ’90 y 2000, como la Instrucción General 326/1997 y posteriores (IG 748/05 y otras que evolucionaron ese registro).

Estas bases se usaban para identificar sujetos y documentos que presentaban irregularidades objetivas, como proveedores que simulaban operaciones o emitían facturas sin actividad económica real.

Dentro de este esquema de control, el CUIT funciona como el identificador principal de los contribuyentes, permitiendo distinguir y analizar a los sujetos fiscales de acuerdo con su naturaleza jurídica. El CUIT se encuentra conformado por 11 dígitos, distribuidos en tres partes:


1 - Primeros 2 dígitos (Indican qué tipo de persona o entidad es).

A-Personas humanas

20 → varón

27 → mujer

23 → asignación especial (cuando hay conflictos con DNI, duplicaciones, etc.)

B- Personas jurídicas

30 → sociedades comerciales (SA, SRL, SAS, etc.)

33 → asociaciones, fundaciones, cooperativas

34 → entidades del exterior / organismos especiales

2 - Bloque central (8 dígitos)

En personas humanas: el DNI (con ceros a la izquierda si hace falta)

En personas jurídicas: número interno asignado por AFIP/ARCA

3 - Último dígito (dígito verificador)

Se calcula con un algoritmo módulo 11 (método matemático clásico de control). Sirve para validar que el CUIT esté bien formado, si alguien se equivoca al tipear un número, el dígito verificador no coincide y el CUIT se invalida.

A partir de este identificador fiscal, se construye la base de análisis utilizada en este trabajo, la cual proviene de información de acceso público provista por AFIP/ARCA. Dicha base contiene únicamente cuatro campos: el campo “CUIT”, que identifica al contribuyente incorporado en el listado; “Fecha Condición Apócrifo”, que indica el momento en que se detecta la emisión de comprobantes no genuinos; “Fecha de Publicación”, que señala la fecha a partir de la cual el sujeto es publicado como no confiable; y un campo “Descripción”, sin información relevante para el análisis.

En el análisis se optó por enmascarar los números de CUIT y no publicar la base de datos, por razones de confidencialidad y protección de los datos.

<img width="1303" height="405" alt="image" src="https://github.com/user-attachments/assets/e54eb065-582e-4d69-a92d-69c18ba4dc9c" />

<img width="1275" height="344" alt="image" src="https://github.com/user-attachments/assets/1f653a44-9375-4e1b-b82f-fbbc3c1d41cf" />

<img width="1275" height="344" alt="image" src="https://github.com/user-attachments/assets/cb61cdb0-05b8-47f1-b0b9-2642aa104be6" />

<img width="1307" height="339" alt="image" src="https://github.com/user-attachments/assets/24f9e830-6c26-4ad9-aa92-a71657ba1073" />

## Créditos y autor
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Nestor_Diaz-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/contadornestordiaz/)


