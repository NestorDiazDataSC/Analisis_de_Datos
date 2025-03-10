
# Analisis-Data-Argentina

Algoritmos y graficos utilizados en este analisis:

* *Regresión Lineal*

* *Regresióm Lineal Multiples variables*

* *Heatmap*

Analisis de datos sociales de la Argentina, mediante el uso de Python me propuse analizar los datos de un dataframe disponible en Kaggle y tambien practicar realizando prediciones como ejemplo de tipo lineal de una y multiple variables. Primero se busco que datos estan mas correlacionados para hacer una predicción del tipo lineal con solo 2 variables, que determine mediante analisis que son las que mas correlación tenian entre ellas y luego analizarlo con el uso de multiples variables del set de datos. Busco predecir cuantas personas en el pais se encuentran "sin atención medica" por cada 30.000 personas que se consideran para la encuesta como "analfabetos" en la Argentina, la grafica de la relación entre estos datos es la que sigue:

![01](https://user-images.githubusercontent.com/94582879/162589689-112aaac2-4818-44b4-8037-007c722a73f6.jpg)

Luego utilice multiples variables para predecir: Cuantas personas hay "sin atención medica" cuando tenemos las siguientes caracteristicas: hay 30.000 "analfabetos" en la Argentina, "10.000" que sufren falta de infraestructura, "10.000" en la pobreza y "5000" personas que desertaron del colegio.

![02](https://user-images.githubusercontent.com/94582879/162589617-01513d0b-b466-40de-801d-4432139a60fe.jpg)

Por ultimo me centre en realizar una matriz de correlación para ver de este set de datos, cuales son los datos que tienen una mayor correlación entre ellos y que nivel de importancia tienen con respecto a otros datos, con esto genere un grafico "heatmap" que se puede ver en la imagen de abajo el cual detalla el orden de los datos desde los mas correlacionados hasta los menos, tomando los 5 mas correlacionados.

![03](https://user-images.githubusercontent.com/94582879/162589667-9dec59ca-8d15-4e25-8cea-367b9cd03630.jpg)

La conclución a la que llegue es que al PBI de cada provincia de la Argentina lo que mas lo afecta o lo hace variar es su cantidad de población, a mayor población mayor sera su PBI, si bien es algo obvio, estaban estos valores dentro del dataset, lo segundo que afecta al PBI de las provincias es la cantidad de doctores que hay por persona, entendiendose como cantidad de medicos por cada 100 habitantes, al haber mayor atención medica, el PBI de la provincia tiede a subir aunque este ultimo punto no es tan importante puesto que no es una correlación perfecta o cercana a 1 si no mas bien cerca del 0,22 por lo que tiene una importancia relativa.

## Créditos y autor
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Nestor_Diaz-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/contadornestordiaz/)
