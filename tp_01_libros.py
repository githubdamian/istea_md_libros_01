import os #para el manejo de archivos
import pandas as pd
import matplotlib.pyplot as plt
#clase Libro
class Libro():
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo=titulo
        self.autor=autor
        self.genero=genero
        self.puntuacion=puntuacion
        
    def __str__ (self):
        #modifico el comportamiento del método __str__ de python, para indicarle cómo mostrar
        #la info cada vez que se imprime por pantalla un libro:
        return f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Puntuación: {self.puntuacion}"

#creo una clase para la lista que contrendrá los libros:
class Lista():
    def __init__(self):
        self.libros = [] #defino la lista
         
    def agregar(self, libro):
        self.libros.append(libro) #método para agregar un libro
    
    def mostrar_libros(self, recomendado=False):
        """
        aprovecho la misma función para codificar la búsqueda por género
        o bien recomendar de acuerdo a la puntuación.
        al final realizo un ternario para mostrar el resultado
        """
        cantidad=0;
        puntua=0;
        valor=str(input("Ingrese el Género buscado: ")).upper()
        print(f"****** EL GENERO INGRESADO ES {valor} ******\n")
        for libro in self.libros:
            if not recomendado:
                if libro.genero == valor: #si concide el género c/el valor ingresado
                    print(libro, "\n", "=" * 50)    
                    cantidad = cantidad+1
            else:
                #si coinciden gener y valor, y la puntuación es más alta:
                if libro.genero == valor and libro.puntuacion > puntua:
                    libro_recomendado = libro #guardo el libro
                    puntua=libro.puntuacion #actualizo el valor más alto
        #operador ternario:
        print(f"{cantidad} de libros del Género {valor}"  \
              if not recomendado else f"Mejor puntuado del Génro {valor}:  {libro_recomendado}")
            
def opciones():
    """
    defino el menú de opciones con una función y la hago recursiva hasta que el usuario
    ingrese una opción correcta
    """
    opcion=str(input("""\n\nOPCIONES:
                     A-Agregar Libro
                     B-Buscar por Género
                     D-Mostrar datos en Tabla
                     R-Recomendar Libro
                     V-Visualizar datos
                     S-Salida\n""")).upper()
    if opcion not in ["A", "B", "D", "R", "V", "S"]:
        return opciones()
    else:
        return opcion

def pedir_datos():
    """
    creo una lista y en cada posición guardo un dato (título, autor, etc).
    voy validando cada ingreso, hasta que el dato sea correcto
    """
    datos=[]
    dato=str(input("Ingrese el Título del libro:\n")).upper()
    #que rechace la data si el Título ya existe o ingresó la data en blanco:
    while dato in titulos or dato == "":
        dato=str(input("Dato vacío o Título ya registrado. Ingrese el Título del libro:\n"))
    else:
            datos.append(dato)
    dato=str(input("Ingrese el Autor:\n")).upper().strip()
    while dato == "":
        dato=str(input("Ingrese el Autor:\n")).upper()
    datos.append(dato)
    dato=str(input("Ingrese el Género:\n")).upper().strip()
    while dato == "":
        dato=str(input("Ingrese el Género:\n")).upper().strip()
    datos.append(dato)
    datos.append(input("Ingrese la puntuación:\n"))
    #corroboro que que dato sea numérico:
    while not datos[3].replace(".","").replace(",", "").isdigit():
        print("****** LA PUNTUACION DEBE SER NUMÉRICA ******")
        datos[3] = input("Ingrese la puntuación:\n")
    return datos #devuelvo la lista con todos los datos del libro

def agregar_libro(nuevo_libro):
    #instancio a la clase, pasando los datos necesarios:
    libro = Libro(titulo=nuevo_libro[0], autor=nuevo_libro[1], genero=nuevo_libro[2], puntuacion=nuevo_libro[3])
    lista_libros.agregar(libro) #invoco al método "agregar" de la clase Lista

def cargar_txt(nombre_archivo):
    global titulos,autores, generos #lista para guardar los títulos de cada libro
    #si el archivo existe, lo abro. tengo que pasar a utf-8 por los acentos y caracteres especiales
    if os.path.exists(nombre_archivo): 
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines() #cargo todos los registros en una variable
            for linea in lineas: #y la recorro
                linea = linea.strip() #limpio espacios y tabulaciones
                campos = linea.split(",") #spliteo con la coma, separando cada campo
                #instancio  a Libro y le paso los datos:
                libro = Libro(titulo=str(campos[0]).upper(), autor=str(campos[1]).upper(),
                              genero=str(campos[2]).upper(), puntuacion=float(campos[3]))
                lista_libros.agregar(libro)
                #creo listas con los valores únicos de títulos, autor y género, para luego realizar
                #búsquedas más rápidas y mostrar la info respectiva:
                if not str(campos[0]).upper() in titulos:
                    titulos.append(str(campos[0]).upper())
                if not str(campos[1]).upper() in autores:
                    autores.append(str(campos[1]).upper())                
                if not str(campos[2]).upper() in generos:
                    generos.append(str(campos[2]).upper())

def guardar_txt(nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for libro in lista_libros.libros:
            linea = libro.titulo + "," + libro.autor + "," + libro.genero +"," +str(libro.puntuacion)
            archivo.write(linea + "\n")

            
def crear_dataframe(nombre_archivo):
    #con los datos en un data_frame, sería más sencillo y utilizaría menos recursos
    #para, por ejemplo, actualizar datos:
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_colwidth", 10)
    #si el archivo existe, lo abro. tengo que pasar a utf-8 por los acentos y caracteres especiales
    if os.path.exists(nombre_archivo): 
        data=pd.read_csv(file_name, sep=",", header=None)
        df = pd.DataFrame(data=data)
        df.columns=["TITULO", "AUTOR", "GENERO", "PUNTUACION"]
        df.plot(kind="bar", x="GENERO", y="PUNTUACION")
        plt.xlabel("Género")
        plt.ylabel("Puntuación")
        plt.show()
        return df
        
def visualizar_info():
    print(f"Títulos disponibles\n{titulos}\n", "X="*25)
    print(f"Autores\n{autores}\n", "X="*25)
    print(f"Géneros\n{generos}\n", "X="*25)
######################################################
#################   MAIN                                     #################
######################################################
global titulos, autores, generos, df
titulos=[]
autores=[]
generos=[]
lista_libros = Lista()
file_name="biblioteca.csv"
cargar_txt(nombre_archivo=file_name)

while True:
        op=opciones()
        if op=="S" :
            print("Ha salido del sistema")
            guardar_txt(file_name)
            break
        else:
            match op:
                case "A":
                    nuevo_libro = pedir_datos()
                    agregar_libro(nuevo_libro)
                case "B":
                    lista_libros.mostrar_libros()
                case "D":
                   df= crear_dataframe(nombre_archivo=file_name)
                   print(df['PUNTUACION'].describe())
                case "R":
                    lista_libros.mostrar_libros(recomendado=True)
                case "V":
                    visualizar_info()