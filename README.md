tp: crear repositorio y subir script en python (libros) en la branch "dev"

El programa permite llevar una "biblioteca" de libros, cuyos datos (por cada ejemplar) son: título, autor, género y puntuación.

A través de funciones y POO, se crean acciones para:
cargar libros existentes desde un archivo csv
agregar libros a la biblioteca
buscar libros por género
buscar libros por género, mostrando la puntuación más alta
crear dataframe con la "biblioteca" de libros
crear gráfico de género/puntuación (histograma)
mostrar al usuario las listas de títulos, autores y géneros (valores únicos)

en la carga de Libro se verifica que cada dato esté completo y sea del tipo correcto
se verifica, también, que el título no se duplique

las clases Lista y Libro son para la creación de una lista de Python que contendrá objetos del tipo Libro

al salir del programa, se guardan los Libros contenidos en Lista en el archivo "biblioteca.csv"

no se agregan más funcionalidades por falta de tiempo. Lo más eficiente sería cargar "biblioteca.csv" a
un dataframe y desde ahí continuar, especialmente en lo que refiere a la modificación de datos ya
existentes (poco práctico en la lectura secuencial de un csv/txt), al margen de agilizar la búsqueda de
datos y/o creación de informes.
