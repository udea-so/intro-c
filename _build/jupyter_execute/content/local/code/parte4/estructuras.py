#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dannymrock/UdeA-SO-Lab/blob/master/lab0/lab0b/parte4/estructuras.ipynb)

# In[ ]:


get_ipython().system('pip3 install tutormagic')


# In[20]:


get_ipython().run_line_magic('load_ext', 'tutormagic')


# # Estructuras en C
# 
# 

# ---
# > **Objetivos**
# > * xxx.
# > * yyy
# 
# ---

# ## 1. Conceptualizacion
# 
# Anteriormente vimos que los **arrays** esta una coleccion de datos de un mismo tipo agrupados bajo un mismo nombre. C, pese a no ser un lenguaje de programacion orientado a objetos maneja un tipo de dato compuesto conocido como **estructura**. En si, una estructura es lo mas cercano a la definición que conocemos de **clase** en los lenguajes de programación, la unica diferencia respecto a las clases (sin hablar en el sentido estricto de la palabra), es que una estructura es como una clase con miembros pero sin metodos.
# 
# La mayor ventaja de estas, es que permiten la creacion de **nuevos tipos de datos**, liberando al programador de tener que restringirse 
# al uso de los tipos de datos tipicos ofrecidos por el lenguaje como tal (int, double, float, etc.) lo cual hace posible organizar datos complicados, particularmente en largos programas.
# 
# Una **estructura**, es una coleccion de uno o más tipos de datos denominados **miembros**, cada uno de los cuales (como se dijo antes) puede ser de un tipo diferente. 
# 
# ## 2. Trabajando con estructuras
# 
# ### 2.1. Declaración de una estructura
# 
# La declaración de una estructura tiene la siguiente sintaxis:
# 
# ```C
# struct nombre-estructura {
#   tipo_1 miembro_1;
#   tipo_2 miembro_2;
#   tipo_3 miembro_3;
#   ...
#   tipo_N miembro_N;
# };
# ```
# 
# 

# **Ejemplos**
# 
# 1. Definir una estructura asociada a un punto en el plano cartesiano.
# 
# ![fig1](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte4/imagenes/punto.png?raw=true)
# 
# **Figura 1**. Punto.
# 
# ```C
# struct Punto2D {
#   float x;
#   float y;
# };
# ```
# 
# 2. Definir una estructura asociada a una fecha.
# 
# ![fig2](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte4/imagenes/fecha.png?raw=true)
# 
# **Figura 2**. Fecha.
# 
# ```C
# struct Date {
#   unsigned year;
#   unsigned month;
#   unsigned day;
# };
# ```
# 
# 3. Definir una estructura asociada a una hora.
# 
# ![fig3](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte4/imagenes/hora.png?raw=true)
# 
# **Figura 3**. Tiempo
# 
# ```C
# struct Tiempo {
#   unsigned int hr;
#   unsigned int min;
#   unsigned int sec;
# };
# ```
# 
# 4. Definir una estructura asociada a un album musical
# 
# ![fig4](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte4/imagenes/album.png?raw=true)
# 
# **Figura 4**. Album
# 
# ```C
# struct Album {
#   char titulo[64];
#   char artista[32];
#   char genero[32];
#   char *canciones;
# };
# ```
# 
# 5. Definir una estructura asociada a una cancion.
# 
# ![fig5](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte4/imagenes/cancion.png?raw=true)
# 
# **Figura 5**. Cancion.
# 
# ```C
# struct Cancion {
#   char titulo[64];
#   char artista[32];
#   char compositor[32];
#   short duracion;
#   struct fecha f_publicacion;
# };
# ```
# 
# 6. Definir una estructura asociada a un libro.
# 
# ![fig6](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte4/imagenes/libro.png?raw=true)
# 
# **Figura 6**. Libro.
# 
# ```C
# struct Book  {
#    int  book_id;
#    char title[50]; 
#    char author[40]; 
#    int pages;
#    float price;
# };
# 
# ```
# 

# ### 2.2. Definición de variables tipo struct
# 
# Las variables de estructuras se pueden definir de dos formas:
# 1. Listándolas inmediatamente después de la llave de cierre de la llave de cierre de la declaración de la estructura, algo como esto tal y como se muestra en el siguiente codigo en el cual se declaran dos variables (**book1** y **book2**) tipo **struct Book**:

# In[21]:


get_ipython().run_cell_magic('tutor', '-l c -k', 'struct Book  {\n   int  book_id;\n   char title[30]; \n   char author[20]; \n   int pages;\n   float price;\n} book1, book2;\n\nint main() {\n  return 0;\n}')


# 2. Listando el tipo de la estructura seguida por las variables correspondientes en cualquier lugar del programa antes de utilizarlas, así, asumiendo que la estructura está declarada. El siguiente codigo muestra esto, notese que la declaración de las variables (**book1** y **book2**)  es similar a la declaración para datos no estructurados (**int**, **double**, etc), aquí, la unica difetencia es que estas serán para el caso datos tipo **struct Book**:
# 

# In[22]:


get_ipython().run_cell_magic('tutor', '-l c -k', 'struct Book  {\n   int  book_id;\n   char title[30]; \n   char author[20]; \n   int pages;\n   float price;\n};\n\nstruct Book book1, book2;\n\nint main() {\n  return 0;\n}')


# La salida sea para uno u otro caso se muestra a continuación:
# 
# 
# ![fig7](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte4/imagenes/declaracion_books.png?raw=true)
# 
# **Figura 7**. Estructuras tipo libro.
# 
# 
# Adicionalmente, los conceptos aplicados para los tipos de datos simples aplican para estructuras tambien; esto es, es posible crear variables normales, arrays, matrices y apuntadores de estructuras entre otros. Veamos:

# **Ejemplo**:
# Empleando la estructura tipo Punto2D crear las siguientes variables:
# * Dos variables llamadas p1 y p2 (local).
# * Un array de 3 elementos llamado vP (local).
# * Un apuntador llamado *ptrP que apunte a p[1] (global).
# * Una matrix de 2x2 llamada mP (global).
# 
# La solución se muestra a continuación:
# 

# In[23]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nstruct Punto2D {\n  float x;\n  float y;\n};\n\nstruct Punto2D vP[3];\nstruct Punto2D mP[2][2];\nint main() {\n  // Los datos tipo Punto2D seran locales\n  struct Punto2D p1, p2;  \n  struct Punto2D *ptrP = &vP[1];  \n  return 0;\n}')


# A continuacion se muestra el resultado en memoria de la ejecución del codigo anterior:
# 
# ![fig8](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte4/imagenes/declaracion_point.png?raw=true)
# 
# **Figura 8**. Estructuras tipo punto.
# 

# ### 2.3. Inicializacion de variables tipo struct
# 
# Al igual que para el caso de las variables simples, las estructuras pueden tener valores iniciales una vez se declaran. Como estas con estructuras compuestas, lo que se hace para inicializar estas, es inicializar miembro por miembro. A continuacion se describen las dos formas de llevar a cabo esto:
# 
# #### 2.3.1. Usando una lista de inicialización
# Esta es similar a la empleada para los arrays, y lo que se hace es inicializar cada miembro de la estructura con el correspondiente valor inicial asociado. Cada valor inicial es separado por coma (,). Veamos.
# 
# **Ejemplo** 
# Iniciar la estructura Cancion con la siguiente informacion asociada a una cancion de [Billie Holiday](https://es.wikipedia.org/wiki/Billie_Holiday). A continuacion se muestra el codigo:
# 

# In[24]:


get_ipython().run_cell_magic('tutor', '-l c -k', '\n// Declaracion de la estructura\nstruct Cancion {\n  char titulo[20];\n  char artista[32];\n  char compositor[32];\n  short duracion;\n  char URL[32];\n};\n                         \n// Funcion main                         \nint main() {\n  // Inicializacion de la variable (sadSong) tipo struct Cancion \n  struct Cancion sadSong = {\n                              "Strange fruit",\n                              "Billie Holiday",\n                              "Abel Meeropol",\n                              164,\n                              "http://bit.ly/1mU1gBT"\n                           }; \n  return 0;\n}')


# A continuacion se muestra como quedan las estructura tipo Cancion (sadSong) al ejecutarse el codigo:
# 
# ![fig9](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte4/imagenes/var_song1.png?raw=true)
# 
# **Figura 9**. Estructuras tipo cancion (variable sadSong).
# 

# #### 2.3.2. Inicialización específica de cada uno de los miembros
# Básicamente, consiste en la designación de cada uno de los miembros siguiendo la siguiente forma.
# 
# ```C
# .miembro = valor; // designador
# ```

# **Ejemplo** 
# Realizar la misma inicilizacion del caso anterior, pero en este caso emplear la inicializacion especifica de miembros:
# 

# In[25]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n// Declaracion de la estructura\nstruct Cancion {\n  char titulo[20];\n  char artista[32];\n  char compositor[32];\n  short duracion;\n  char URL[32];\n};\n                         \n// Funcion main                         \nint main() {\n  // Inicializacion de la variable (sadSong) tipo struct Cancion \n  struct Cancion sadSong = {\n                             .titulo = "Strange fruit",\n                             .artista = "Billie Holiday",\n                             .compositor = "Abel Meeropol",\n                             .duracion = 164,\n                             .URL = "http://bit.ly/1mU1gBT"\n                           };\n  return 0;\n}')


# El resultado de ejecutar el codigo anterior, es el mismo que el mostrado en la **figura 9**.

# #### 2.3.3. Caso en el que no se inicializan todos lo miembros
# Ya sea que se emplee una u otra de las formas anteriormente mencionadas, es posible inicializar parcialmente una variable tipo estructura, para ello, basta con no pasar todos los elementos que puede contener la lista de inicialización. A continuación se muestra un ejemplo:
# 
# **Ejemplo**
# Crear dos variables tipo struct Cancion, estas variables no tendran todos los parametros inicialidos:

# In[26]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n// Declaracion de la estructura\nstruct Cancion {\n  char titulo[20];\n  char artista[32];\n  char compositor[32];\n  short duracion;\n  char URL[32];\n};\n\n// Variables globales tipo struct Cancion\nstruct Cancion song1 = {"Mi cerebro esta boca abajo"};\nstruct Cancion song2 = { \n                         .titulo = "Noches de Hungria",\n                         .compositor = "Julio Jaramillo",\n                         .duracion = 127\n};\n\n// Funcion main                         \nint main() {\n  return 0;\n}')


# En la siguiente figura se muestra el resultado del codigo anterior, notese lo que sucede como quedan los miembros que no fueron inicializados.
# 
# ![fig10](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte4/imagenes/var_song2.png?raw=true)
# 
# **Figura 10**. Variables tipo cancion sin inicializar todos sus miembros.
# 

# ### 2.4. Empleo de la palabra clave typedef para crear alias (tocayos)
# La palabra reservada ```typedef``` permite a un programador crear un sinónimo de un tipo de dato definido por el usuario o de un tipo ya existente. La sintaxis para usar esta palabra clave es la siguiente:
# 
# ```C
# tipo_dato typedef nombre_alias;
# ```
# 
# **Ejemplo**
# Dada la siguiente declaracion de variables:
# 
# ```C
# double alto, ancho;
# ```
# 
# Teniendo en cuenta que **alto** y **ancho** son medidas de longitud, podemos crear un alias para una variable tipo double llamado **longitud** y el efecto será el mismo que el del caso anterior, el código para el caso sera el siguiente:
# 
# ```C
# typedef double longitud;
# longitud alto, ancho;
# ```
# 
# El resultado se muestra a continuacion:
# 
# ![fig11](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte4/imagenes/type_def1.png?raw=true)
# 
# **Figura 11**. Uso de typedef para la creacion de alias.

# **Ejemplo**
# La mayor ventaja del uso de esta palabra clave se ve con las estructuras. A continuación se muestra el resultado:
# 
# 1. Cree dos variables tipo Punto2D llamadas P1 y P2 con valores (2,3) y (-1,6). No emplee typedef:

# In[27]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n// Declaracion de las estructura\nstruct Punto2D {\n  float x;\n  float y;\n};\n\n\n// Funcion main                         \nint main() { \n  // Declaracion de variables\n  struct Punto2D P1 = {\n                        2,\n                        3\n                      };\n\n  struct Punto2D P2 = {\n                        .x = -1,\n                        .y = 6\n                      };\n  return 0;\n}')


# La salida del programa anterior es:
# 
# ![fig12](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte4/imagenes/point_sin_typedef.png?raw=true)
# 
# **Figura 11**. Uso variables tipo struct Punto2D sin usar typedef.
# 

# 2. Realice lo mismo que en el punto anterior, pero esta vez haga uso de la palabra clave **typedef** para crear un alias son **struct Punto2d** llamado **Punto2D**:

# In[28]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n// Declaracion de las estructura\nstruct Punto2D {\n  float x;\n  float y;\n};\n\n// Creacion del alias\ntypedef struct Punto2D Punto2D;\n\n// Funcion main                         \nint main() { \n  // Declaracion de variables\n  Punto2D P1 = {\n                        2,\n                        3\n                      };\n\n  Punto2D P2 = {\n                        .x = -1,\n                        .y = 6\n                      };\n  return 0;\n}')


# La salida del programa anterior (observe en que se diferencia respecto al anterior) es:
# 
# ![fig12](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte4/imagenes/point_con_typedef.png?raw=true)
# 
# **Figura 12**. Uso variables tipo struct Punto2D usando typedef.

# ### 2.5. Manipulando estructuras
# Por manipulacion de la estructuras (dentro de este contexto) nos queremos referir al acceso a los miembros de esta, tal y como sucede cuando se accede a los miembros de un objeto en el caso de la POO. Para el caso de las estructuras en particulas, existen dos formas de acceder:
# * Empleando el operador punto (.)
# * Emplenando el operador flecha (->)
# 
# #### 2.5.1 Usando el operador punto (.)
# Usado cuando se definen variables del tipo de la estructura. Básicamente tiene la siguiente sintaxis:
# 
# ```C
# <nombre_variable_estructura>.<nombre_miembro> = datos;
# ```

# **Ejemplos**
# 1. Crear dos puntos P1 y P2. Luego de su declaracion inicialicelos con los siguientes valores: (1,1) y (10,3). En el siguiente [enlace](https://goo.gl/XzWLMR) se encuentra el codigo.
# 
# ```
# // Declaracion de las estructura
# struct Punto2D {
#   ...
# };
# 
# // Creacion del alias
# struct Punto2D Punto2D;
# 
# // Declaracion de los puntos
# Punto2D P1, P2;
# 
# // Manipulacion (acceso a los miembros)
# P1.x = 1;
# P1.y = 1;
# P2.x = 10, P2.y = 3;
# ```
# 
# Observe como quedan los campos de las variables P1 y P2 despues de la ejecucion del codigo anterior.
# 
# ![fig13](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte4/imagenes/acceso_struct_punto.png?raw=true)
# 
# **Figura 13**. Manipulando variables tipo Punto2D.
# 
# 2. Crear una estructura asociada a un libro y porteriormente declarar dos libros (como un array) con la siguiente informacion.
# 
# ![fig13](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte4/imagenes/libros.png?raw=true)
# 
# **Figura 13**. Libros.
# 
# <table style="width: 91px;">
# <tbody>
# <tr>
# <td style="width: 15px;">#</td>
# <td style="width: 15px;">BookID</td>
# <td style="width: 15px;">Title</td>
# <td style="width: 15px;">Author</td>
# <td style="width: 15px;">Pages</td>
# <td style="width: 15px;">Price</td>
# </tr>
# <tr>
# <td style="width: 15px;">1</td>
# <td style="width: 15px;">1211</td>
# <td style="width: 15px;">C Primer Plus</td>
# <td style="width: 15px;">Stephen Prata</td>
# <td style="width: 15px;">984</td>
# <td style="width: 15px;">585.00</td>
# </tr>
# <tr>
# <td style="width: 15px;">2</td>
# <td style="width: 15px;">1212</td>
# <td style="width: 15px;">The ANSI C Programming</td>
# <td style="width: 15px;">Dennis Ritchie</td>
# <td style="width: 15px;">214</td>
# <td style="width: 15px;">125.00</td>
# </tr>
# </tbody>
# </table>
# 
# El [código](https://goo.gl/dbjcTF) solucion se muestra a continuación, note que la forma como se accede a la variable tipo ```Book``` en el correspondiente arreglo es ```book[i]``` para el caso, por ende la forma de acceder a cada uno de los miembros del array en cuestion será ```book[i].miembro```
# 
# ```C
# #include <stdio.h>
# #include <string.h>
# 
# // Declaracion de las estructura
# struct Book  {
#    int  book_id;
#    char title[24]; 
#    char author[20]; 
#    int pages;
#    float price;
# };
# 
# // Creacion del alias
# typedef struct Book Book;
# 
# // Declaracion del array de libros
# Book books[2];
# 
# int main() {
#   // Manipulacion (acceso a los miembros)
# 
#   // Libro # 1
#   books[0].book_id = 1211;
#   //OJO: books[0].title = "C Primer Plus" es un ERROR 
#   strcpy(books[0].title,"C Primer Plus");    
#   strcpy(books[0].author,"Stephen Prata"); 
#   books[0].pages = 984;
#   books[0].price = 585.00;
# 
#   // Libro #2
#   books[1].book_id = 1212;
#   strcpy(books[1].title,"The ANSI C Programming"); 
#   strcpy(books[1].author,"Dennis Ritchie"); 
#   books[1].pages = 214;
#   books[1].price = 125.00;
# 
#   return 0;
# }
# ```
# 
# A continuacion se muestra el resultado en memoria.:
# 
# ![fig14](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte4/imagenes/declaracion_books.png?raw=true)
# 
# **Figura 14**. Resultado en memoria para variables asociadas a los libros.

# #### 2.5.2 Usando el operador flecha (->)
# 
# Es empleado cuando se hace uso de punteros a estructuras, su sintaxis es de la siguiente forma:
# 
# ```C
# <puntero_estructura>-><nombre_miembro> = datos;
# ```
# 

# **Ejemplos**
# 1. Suponga que se tiene una estructura asociada a las fechas. Tambien, suponga que tiene una variable llamada diaDestino cuyo valor asociado es el 5 de noviembre de 1955 (primer viaje en el tiempo de Marty MacFly). Luego cree una variable tipo apuntador a esta este tipo de estructura y modifique a traves de este el valor de diaDestino al 21 de octubre de 2015 (fecha a la cual viaja Marty MacFly al futuro). Imprima los valores en cada caso.
# 
# El código solucion se muestra a continuacion:
# 

# In[29]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nstruct Date {\n  unsigned year;\n  unsigned month;\n  unsigned day;\n};\n\ntypedef struct Date Fecha;\n\nint main() {\n  /* Declaracion de variables */\n  Fecha diaDestino; // Varible tipo fecha\n  Fecha *diaPtr;    // Variable tipo apuntador a fecha\n  diaPtr = &diaDestino;  // Inicializacion del apuntador\n  \n  /* Viaje al pasado */\n  // Fijando por medio del operador punto (.) los valores \n  // de dia destino al 5 de noviembre de 1955 \n  diaDestino.year = 1955;\n  diaDestino.month = 11;\n  diaDestino.day = 5;\n  printf("Destination time: %d/%d/%d\\n", \n         diaDestino.day, diaDestino.month, diaDestino.year);\n  \n  /*Viaje al futuro */\n  // Fijando por medio del operador flecha (->) los valores \n  // de dia destino al 21 de octubre de 2015\n  diaPtr->year = 2015;\n  diaPtr->month = 10;\n  diaPtr->day = 21;\n  printf("Destination time: %d/%d/%d\\n", \n         diaPtr->year, diaPtr->month, diaPtr->year);\n  return 0;\n}')


# Hay que aclarar que el uso del operador punto (.) tambien puede ser empleado con variables tipo apuntador, para ello se sigue la siguiente forma:

# **Ejemplos**
# 1. Implemente el mismo ejemplo anterior, pero esta vez use el operador punto (.) para modificar los miembros de la variable tipo Date a traves del apuntador.
# 
# El codigo solución se muestra a continuacion:

# In[30]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nstruct Date {\n  unsigned year;\n  unsigned month;\n  unsigned day;\n};\n\ntypedef struct Date Fecha;\n\nint main() {\n  /* Declaracion de variables */\n  Fecha diaDestino; // Varible tipo fecha\n  Fecha *diaPtr;    // Variable tipo apuntador a fecha\n  diaPtr = &diaDestino;  // Inicializacion del apuntador\n  \n  /* Viaje al pasado */\n  // Fijando por medio del operador punto (.) los valores \n  // de dia destino al 5 de noviembre de 1955 \n  diaDestino.year = 1955;\n  diaDestino.month = 11;\n  diaDestino.day = 5;\n  printf("Destination time: %d/%d/%d\\n", \n         diaDestino.day, diaDestino.month, diaDestino.year);\n  \n  /*Viaje al futuro */\n  // Fijando por medio del operador flecha (->) los valores \n  // de dia destino al 21 de octubre de 2015\n  (*diaPtr).year = 2015;\n  (*diaPtr).month = 10;\n  (*diaPtr).day = 21;\n  printf("Destination time: %d/%d/%d\\n", \n         diaPtr->year, diaPtr->month, diaPtr->year);\n  return 0;\n}')


# Si lo simula, podrá notar que la salida es exactamente la misma que la del ejemplo anterior.

# ### 2.6. Estructuras anidadas
# Una estructura puede tener a su vez otra estructura como miembro. A continuacion se muestra un ejemplo para ello.
# 

# **Ejemplos**
# 1. Suponga que se tiene la siguiente tabla asociada a personajes historicos.
# 
# ![fig16](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte4/imagenes/personajes.png?raw=true)
# 
# **Figura 16**. Personajes
# 
# <table>
# <tbody>
# <tr>
# <td>Nombre</td>
# <td>Nacimiento</td>
# <td>Muerte</td>
# <td>Profesion</td>
# </tr>
# <tr>
# <td>Ernest Hemingway</td>
# <td>21/07/1899</td>
# <td>02/07/1961</td>
# <td>Escritor</td>
# </tr>
# <tr>
# <td>Albert Einstein</td>
# <td>14/03/1879</td>
# <td>18/04/1955</td>
# <td>Fisico</td>
# </tr>
# </tbody>
# </table>
# 
# Note que para el problema podemos crear dos estructuras, una asociada al personaje y otra asociada a las fechas. Asi mismo, podemos ver que las fechas pueden ser tratadas como estructuras del personaje. A continuacion vamos a mostrar el código que define ambas estructuras:
# 
# ```C
# struct date {
#   unsigned year;
#   unsigned month;
#   unsigned day;
# };
# 
# typedef struct date fecha;
# 
# struct personajeHistorico {
#   char nombre[21];
#   fecha nacimiento;
#   fecha muerte;
#   char profesion[21];
# };
# 
# typedef struct personajeHistorico personaje;
# 
# 
# int main() {
#   
#   personaje per1 = {
#                      .nombre = "Ernest Hemingway",
#                      .nacimiento = {
#                        .year = 21, 
#                        .month = 07,
#                        .day =  1899,
#                       },
#                      .muerte = { 02, 07, 1961 },
#                      .profesion = "Escritor"                  
#                    };
#   personaje per2, *ptr;
#   fecha d = {14, 03, 1879};  
#   ptr = &per2;
#   strcpy(per2.nombre,"Albert Einstein");
#   strcpy(ptr->profesion,"Fisico");
#   (*ptr).nacimiento = d;
#   per2.muerte.year = 1955;
#   per2.muerte.month = 4;
#   per2.muerte.day = 18;
#   return 0;
# }
# ```
# 
# Notese que en el anterior [ejemplo](https://goo.gl/wFkkgf), se combinan varias de las cosas que hemos discutido previamente. El resultado en memoria se muestra a continuacion:
# 
# ![fig17](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte4/imagenes/struct_personajes.png?raw=true)
# 
# **Figura 17**. Resultado en memoria cuando existen estructuras anidadas.

# ### 2.6. Estructuras y funciones
# Los conceptos vistos hasta el momento sobre funciones tambien aplican a las estructuras ya que las estructuras pueden ser usadas como parametros y valores de retorno por citar unos cuantos casos. La unica cosa adicional, respecto a las funciones que trabajan con variables normales, es que las funciones con estructuras hacen uso de los operadores de acceso para la manipulacion y el procesamiento de los datos de acuerdo a lo que se desea que haga la funcion. Como en el caso tradicional, las funciones en las que se emplean estructuras pueden ser pasadas por valor y por referencia. A continuacion se describe cada caso:
# 
# ### 2.6.1. Paso de estructuras por valor
# En este caso la estructura pasada como argumento a la funcion es copiada al parametro de la funcion, de modo que el procesamiento se hace sobre la copia y no sobre la estructura pasada como argumento.
# 

# **Ejemplos**
# 1. Definir una estructura que este asociada a un numero completo. Luego haga una funcion que imprima el numero complejo en cuestion en la forma **parteReal + parteImaginaria*i**. Luego probar el programa para imprimir los numeros: 2, -3*i, -2.3 + 10.5*i, 1.23 - 3.67*i
# 
# El codigo solucion se muestra a continuación:

# In[31]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n/** Declaracion de  estructuras */\ntypedef struct complejo {\n  float re;\n  float im;\n} complejo;\n\n/** Declaracion de funciones */\nvoid imprimirComplejo(complejo); // void imprimirComplejo(complejo num)\n\n/** Funcion main */\nint main() {\n  /* Creando los numeros */\n  complejo n1 = {2, 0}; // 2\n  complejo n2 = {.re = 0, .im = -3}; // -3*i\n  complejo n3, n4;\n  n3.re = -2.3; // -2.3 + 10.5*i\n  n3.im = 10.5;\n  n4.re = 1.23; //  1.23 - 3.67*i\n  n4.im = -3.67;\n  /* Llamando las funciones para imprimir */\n  imprimirComplejo(n1);\n  printf("\\n");\n  imprimirComplejo(n2);\n  printf("\\n");\n  imprimirComplejo(n3);\n  printf("\\n");\n  imprimirComplejo(n4);\n  printf("\\n");\n  return 0;\n}\n\n/** Definicion de funciones */\nvoid imprimirComplejo(complejo num) {\n  if (num.im == 0) {\n    // Real puro\n    printf("%.2f",num.re);\n  }\n  else if (num.re == 0) {\n    // Imaginario puro\n    printf("%.2f*i",num.im);\n  }\n  else if (num.im < 0) {\n    // Complejo con parte imaginaria negativa\n    printf("%.2f - %.2f*i",num.re,(-1)*num.im);\n  }\n  else {\n    // Complejo con parte imaginaria positiva\n    printf("%.2f + %.2f*i",num.re,num.im);\n  }  \n}')


# Notese que en el anterior codigo se empleo ```typedef``` al declarar la estructura para definir de una vez el alias. La salida en pantalla y la representacion en memoria del programa anterior se muestra a continuacion.

# 2. En la anterior funcion se un numero complejo como parametro, sin embargo tambien es posible retornar otras estructuras variables de retorno. Para ello en el siguiente ejemplo:
# > * Hacer una funcion que sume dos numeros complejos y retorne el resultado de realizar la suma como otro complejo.
# > * Hacer un test sumando los numeros: 2 - 11*i y 8 + 9*i
# 
# A continuación se muestra el código solución:
# 

# In[32]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n/** Declaracion de  estructuras */\ntypedef struct complejo {\n  float re;\n  float im;\n} complejo;\n\n/** Declaracion de las funciones  */\nvoid imprimirComplejo(complejo);\ncomplejo sumarComplejos(complejo, complejo);\nvoid test(void); // Funcion para testing\n\n/** Funcion main */\nint main() {\n  /* Probando todo mediante la funcion test */\n  test();\n  return 0;\n}\n\n/** Definicion de funciones */\nvoid imprimirComplejo(complejo num) {\n  if (num.im == 0) {\n    // Real puro\n    printf("%.2f",num.re);\n  }\n  else if (num.re == 0) {\n    // Imaginario puro\n    printf("%.2f*i",num.im);\n  }\n  else if (num.im < 0) {\n    // Complejo con parte imaginaria negativa\n    printf("%.2f - %.2f*i",num.re,(-1)*num.im);\n  }\n  else {\n    // Complejo con parte imaginaria positiva\n    printf("%.2f + %.2f*i",num.re,num.im);\n  }  \n}\n\ncomplejo sumarComplejos(complejo c1, complejo c2) {\n    complejo solucion;\n    solucion.re = c1.re + c2.re;\n    solucion.im = c1.im + c2.im;\n    return solucion;\n}\n\nvoid test(void) {\n  complejo c1 = {2, -11}, c2 = {8, 9};\n  complejo c3 = sumarComplejos(c1,c2);\n  imprimirComplejo(c1);\n  printf("\\n");\n  imprimirComplejo(c2);\n  printf(" + \\n---------\\n");\n  imprimirComplejo(c3);\n}')


# 3. Mejorar el codigo anterior agregando dos funciones que hagan lo siguiente:
# > * Calcule la magnitud de un numero complejo.
# > * Calcule el angulo de un numero complejo.
# 
# El codigo anterior se mejoro quedando de la siguiente manera:

# In[33]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n#include <math.h>\n\n/** Macros */\n#define PI 3.14\n\n// Converts degrees to radians.\n#define degreesToRadians(angleDegrees) (angleDegrees * PI / 180.0)\n\n// Converts radians to degrees.\n#define radiansToDegrees(angleRadians) (angleRadians * 180.0 / PI)\n\n/** Declaracion de  estructuras */\ntypedef struct complejo {\n  float re;\n  float im;\n} complejo;\n\n/** Declaracion de funciones */\nvoid imprimirComplejo(complejo); // void imprimirComplejo(complejo num)\ndouble calcularMagnitud(complejo);\ncomplejo sumarComplejos(complejo c1, complejo c2);\nvoid test1(void);\nvoid test2(void);\n\n/** Funcion main */\nint main() {\n  /* Creando los numeros */\n  // test1();  ---> Comentado por que ya se probo que dio bien\n  test2();\n  return 0;\n}\n\n/** Definicion de funciones */\nvoid imprimirComplejo(complejo num) {\n  if (num.im == 0) {\n    // Real puro\n    printf("%.2f",num.re);\n  }\n  else if (num.re == 0) {\n    // Imaginario puro\n    printf("%.2f*i",num.im);\n  }\n  else if (num.im < 0) {\n    // Complejo con parte imaginaria negativa\n    printf("%.2f - %.2f*i",num.re,(-1)*num.im);\n  }\n  else {\n    // Complejo con parte imaginaria positiva\n    printf("%.2f + %.2f*i",num.re,num.im);\n  }  \n}\n\ndouble calcularMagnitud(complejo num) {\n  return sqrt(pow(num.re,2) + pow(num.im,2));\n}\n\ndouble obtenerAngulo(complejo num) {\n  if (num.re >= 0 & num.im >= 0) {\n    // Cuadrante I\n    return radiansToDegrees(atan2(num.im,num.re));\n  }\n  else if(num.re < 0 & num.im >= 0) {\n    // Cuadrante II\n    return 180 - radiansToDegrees(atan2(-num.im,num.re));\n  }\n  else if(num.re < 0 & num.im < 0) {\n    // Cuadrante III\n    return 180 + radiansToDegrees(atan2(-num.im,-num.re));\n  }\n  else {\n    // Cuadrante IV\n    return 360 - radiansToDegrees(atan2(-num.im,num.re));\n  }  \n}\n\ncomplejo sumarComplejos(complejo c1, complejo c2) {\n    complejo solucion;\n    solucion.re = c1.re + c2.re;\n    solucion.im = c1.im + c2.im;\n    return solucion;\n}\n\nvoid test1(void) {\n  complejo c1 = {2, -11}, c2 = {8, 9};\n  complejo c3 = sumarComplejos(c1,c2);\n  imprimirComplejo(c1);\n  printf("\\n");\n  imprimirComplejo(c2);\n  printf(" + \\n-------------------\\n");\n  imprimirComplejo(c3);\n}\n\nvoid test2(void) {\n  complejo c1 = {sqrt(3),1};\n  complejo c2 = {-1,1};\n  complejo c3 = {-sqrt(3),-1};\n  complejo c4 = {1,-1};\n  printf("mag(c1) = %.1lf, ang(c1) = %.1lf\\n",calcularMagnitud(c1),obtenerAngulo(c1));\n  printf("mag(c2) = %.1lf, ang(c2) = %.1lf\\n",calcularMagnitud(c2),obtenerAngulo(c2));\n  printf("mag(c3) = %.1lf, ang(c3) = %.1lf\\n",calcularMagnitud(c3),obtenerAngulo(c3));\n  printf("mag(c4) = %.1lf, ang(c4) = %.1lf\\n",calcularMagnitud(c4),obtenerAngulo(c4));\n}')


# La salida en pantalla del programa anterior es:
# 
# ```
# mag(c1) = 2.0, ang(c1) = 30.0                                                                                                  
# mag(c2) = 1.4, ang(c2) = 315.1                                                                                                 
# mag(c3) = 2.0, ang(c3) = 210.0                                                                                                 
# mag(c4) = 1.4, ang(c4) = 315.0
# ```

# ### 2.6.2. Paso de estructuras por referencia
# En este caso, los parametros pasados a la funcion seran apuntadores a la estructura a pasar. El comportamiento es como el que se da en el caso de las funciones con datos tradicionales. 
# 

# **Ejemplos**
# 1. Tome la estructura asociada a los libros y realice una funcion que permita imprimir en pantalla la informacion asociada a un libro. El llamado para la funcion sera por referencia. A continuación se muestra el código solución:

# In[34]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n// Declaracion de las estructura\nstruct Book  {\n   int  book_id;\n   char title[24]; \n   char author[20]; \n   int pages;\n   float price;\n};\n\n/** Declaracion de funciones */\nvoid printBookInfo(struct Book *lptr);\n\n// Declaracion del array de libros\n// Notese que no se usaron alias\nstruct Book books[2];\n\n/** Funcion principal */\nint main() {\n  // Manipulacion (acceso a los miembros)\n\n  // Libro # 1\n  books[0].book_id = 1211;\n  //OJO: books[0].title = "C Primer Plus" es un ERROR \n  strcpy(books[0].title,"C Primer Plus");    \n  strcpy(books[0].author,"Stephen Prata"); \n  books[0].pages = 984;\n  books[0].price = 585.00;\n\n  // Libro #2\n  books[1].book_id = 1212;\n  strcpy(books[1].title,"The ANSI C Programming"); \n  strcpy(books[1].author,"Dennis Ritchie"); \n  books[1].pages = 214;\n  books[1].price = 125.00;\n  \n  // Imprimiendo la informacion de los libros\n  for(int i = 0; i < 2; i++) {\n    printBookInfo(&books[i]);\n    printf("\\n");\n  } \n  return 0;\n}\n\n/** Definicion de funciones */\nvoid printBookInfo(struct Book *lptr) {\n  printf("Book name: %s\\n", lptr->title);\n  printf("Author: %s\\n", lptr->author);\n  printf("Pages: %d\\n", lptr->pages);  \n}')


# La salida en pantalla se muestra a continuacion:
# 
# ```
# Book name: C Primer Plus
# Author: Stephen Prata
# Pages: 984
# 
# Book name: The ANSI C Programming
# Author: Dennis Ritchie
# Pages: 214
# ```

# 2. Hacer un programa que defina un vector tridimensional como una estructura. El programa tambien debera implementar las siguientes funciones para la manipulacion de vectores:
# * Imprimir vector.
# * Calcular suma.
# * Calcular resta.
# * Calcular producto escalar.
# 
# Una vez hecho lo anterior probar el programa con los vectores [1,3,0] y [2,5,-4].
# 
# El codigo solución se muestra a continuacion:

# In[35]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n/** Declaracion de  estructuras */\ntypedef struct vector3D {\n  float x;\n  float y;\n  float z;\n} vector3D;\n\n/** Declaracion de las funciones  */\nvoid imprimirVector3D(vector3D *vPrt); \nvector3D sumarVector3D(vector3D *v1P, vector3D *v2P);\nvector3D restarVector3D(vector3D *v1P, vector3D *v2P);\ndouble pEscalar(vector3D *v1P, vector3D *v2P);\nvoid test(void); // Funcion para testing\n\n/** Funcion main */\nint main() {\n  /* Probando todo mediante la funcion test */\n  test();\n  return 0;\n}\n\n/** Definicion de funciones */\nvoid imprimirVector3D(vector3D *vPtr) {\n   printf("[%.1f,%.1f,%.1f]",(*vPtr).x, (*vPtr).y, (*vPtr).z);   \n}\n\nvector3D sumarVector3D(vector3D *v1P, vector3D *v2P) {\n  vector3D r;\n  r.x = v1P->x + v2P->x;\n  r.y = v1P->y + v2P->y;\n  r.z = v1P->z + v2P->z;\n  return r;\n}\n\nvector3D restarVector3D(vector3D *v1P, vector3D *v2P) {\n  vector3D r;\n  r.x = v1P->x - v2P->x;\n  r.y = v1P->y - v2P->y;\n  r.z = v1P->z - v2P->z;\n  return r;\n}\n\ndouble pEscalar(vector3D *v1P, vector3D *v2P) {\n  return(v1P->x*v2P->x + v1P->y*v2P->y + v1P->z*v2P->z);\n}\n\n\nvoid test(void) {\n  vector3D v1 = {1,3,0}, v2 = {2,5,-4}, vSum, vRes;\n  double p_esc;\n  vSum = sumarVector3D(&v1,&v2);\n  vRes = restarVector3D(&v1,&v2);\n  p_esc = pEscalar(&v1,&v2); \n  printf("Suma -> \\n");\n  imprimirVector3D(&v1);\n  printf(" + ");\n  imprimirVector3D(&v2);\n  printf(" = ");\n  imprimirVector3D(&vSum);\n  printf("\\n\\n");\n  printf("Resta -> \\n");\n  imprimirVector3D(&v1);\n  printf(" - ");\n  imprimirVector3D(&v2);\n  printf(" = ");\n  imprimirVector3D(&vRes);\n  printf("\\n\\n");\n  printf("Producto escalar -> \\n");\n  imprimirVector3D(&v1);\n  printf(" * ");\n  imprimirVector3D(&v2);\n  printf(" = %.1f\\n",p_esc);  \n}')


# La salida del programa anterior se muestra a continuacion:
# ```
# Suma -> 
# [1.0,3.0,0.0] + [2.0,5.0,-4.0] = [3.0,8.0,-4.0]
# 
# Resta -> 
# [1.0,3.0,0.0] - [2.0,5.0,-4.0] = [-1.0,-2.0,4.0]
# 
# Producto escalar -> 
# [1.0,3.0,0.0] * [2.0,5.0,-4.0] = 17.0
# ```

# 3. Emplando llamados por referencia es posible pasar a funciones arreglos y matrices tal como se analizo en algun momento. Por ejemplo supongase que un caminante esta registrando las coordenadas (x,y) de diferentes puntos en los cuales realiza su caminata. Supongase, que el sistema de registro de datos registra 5 coordenadas. Teniendo en cuenta la siguiente estructura para las coordenadas:
# 
# ```C
# typedef struct coordenadas2D {
#   float x;
#   float y;
# } coord2D;
# ```
# 
# Implementar las siguientes funciones:
# * Una funcion para desplegar una coordenada, esta seguira el siguiente prototipo:
# 
# ```C
# void printCoord2D(coord2D *c);
# ```
# 
# * Una funcion para desplegar el contenido de un vector de coordenadas:
# 
# ```C
# void printCoord2DVector(coord2D *v, int tam);
# ```
# 
# * Una funcion que calcule la distancia entre dos coordenadas:
# 
# ```C
# double calcularDistancia(coord2D *pStart, coord2D *pEnd);
# ```
# 
# * Obtener la distancia total recorrida (suma de la distancia de todos lo puntos):
# 
# ```C
# double calcularDistanciaTotal(coord2D *vecPuntos, int N);
# ```
# 
# * Obtener la distancia del tramo mayor y la del tramo menor.
# 
# ```C
# void obtenerDistanciasExtremas(coord2D *vecPuntos, int N, double *disMin, double *disMax);
# ```
# 
# * Probar las funciones anteriores con una funcion llamada  ```caso_de_uso``` para la cual se definen las siguientes coordenadas: P1(0,0), P2(3,2), P3(-4,5), P4(-6,-2) y P5(-6,-3).

# **Solucion**: En el [codigo](https://onlinegdb.com/r13uPE9wM) mostrado abajo se definen los puntos anteriormente mostrados y se verifican que los resultados del programa sean los arrojados anteriormente de manera manual. Si todo esta bien se tendrán resultados simulares a los siguiente:
# 
# Distancia entre los puntos sera:
# * d(P1,P2) = 3.61
# * d(P2,P3) = 7.62
# * d(P3,P4) = 7.28
# * d(P4,P5) = 1
# 
# Salidas a desplegar:
# * d_total = 19.5
# * d_min = 1
# * d_max = 7.62
# 
# 
# A continuación se muestra el código:
# 
# ```
# #include <stdio.h>
# #include <math.h>
# 
# /** Declaracion de  estructuras */
# typedef struct coordenadas2D {
#   float x;
#   float y;
# } coord2D;
# 
# 
# /** Declaracion de las funciones  */
# void printCoord2D(coord2D *c);
# void printCoord2DVector(coord2D *v, int tam);
# double calcularDistancia(coord2D *pStart, coord2D *pEnd);
# double calcularDistanciaTotal(coord2D *vecPuntos, int N);
# void obtenerDistanciasExtremas(coord2D *vecPuntos, int N, double *disMin, double *disMax);
# void caso_de_uso(void);
# 
# /** Funcion main */
# int main() {
# 	caso_de_uso();
# 	return 0;
# }
# 
# /** Definicion de las funciones  */
# 
# void printCoord2D(coord2D *c) {
#     printf("(%.2f,%.2f)",(*c).x,(*c).y);
# }
# 
# void printCoord2DVector(coord2D *v, int tam) {
#     for(int i = 0; i < tam; i++) {
#         printCoord2D(v++);
#         printf("\n");
#     }
# }
# 
# double calcularDistancia(coord2D *pStart, coord2D *pEnd) {
#   double dist;
#   double dx = pEnd->x - pStart->x;
#   double dy = pEnd->y - pStart->y;  
#   dist = sqrt(pow(dx,2) + pow(dy,2));
#   return dist;
# }
# 
# 
# double calcularDistanciaTotal(coord2D *vecPuntos, int N) {
#   // Code
#   coord2D pIni, pFin;
#   double d_total = 0;
#   pIni = *vecPuntos; // *vecPuntos = vecPuntos[0];
#   for(int i = 1; i < N; i++) {
# 	pFin = *(vecPuntos + i); // *(vecPuntos + i) = vecPuntos[i];
# 	// printf("%.2lf\n",calcularDistancia(&pIni, &pFin));
# 	d_total +=  calcularDistancia(&pIni, &pFin); 
# 	pIni = pFin;
#   }
#   return d_total;  
# }
# 
# void obtenerDistanciasExtremas(coord2D *vecPuntos, int N, double *disMin, double *disMax) {
#   // Code
#   coord2D *pIni, *pFin;
#   pIni = &vecPuntos[0];
#   pFin = &vecPuntos[1];
#   double d = calcularDistancia(pIni, pFin);
#   double d_min = d, d_max = d;
#   calcularDistancia(pIni,pFin);
#   pIni = vecPuntos;
#   for(int i = 2; i < N; i++) {
# 	  pIni = pFin;
# 	  pFin = vecPuntos + i; // vecPuntos + i = &vecPuntos[i]; 
# 	  d = calcularDistancia(pIni, pFin);
# 	  if(d <= d_min) {
# 		  d_min = d;
# 	  }
# 	  else if(d >= d_max) {
# 		  d_max = d;
# 	  }	  
#   }
#   *disMin = d_min;
#   *disMax = d_max;
# }
# 
# void caso_de_uso(void) {
#     printf("Puntos registrados\n");
#     double m, M;
#     coord2D coords[5] = {
#                          {0,0},
#                          {3,2},
#                          {-4,5},
#                          {-6,-2},
#                          {-6,-3}
#                         };
#     printCoord2DVector(coords, 5);
#     printf("\n");
#     printf("-> Distancia total: %.2lf\n",calcularDistanciaTotal(coords,5));
#     obtenerDistanciasExtremas(coords, 5, &m, &M);
#     printf("-> Distancia minima: %.2lf\n",m);
#     printf("-> Distancia maxima: %.2lf\n",M);
# }
# ```
# 
# Para el cual la salida en pantalla del programa anterior es la siguiente:
# 
# ```
# Puntos registrados                                                                                                               
# (0.00,0.00)                                                                                                                      
# (3.00,2.00)                                                                                                                      
# (-4.00,5.00)                                                                                                                     
# (-6.00,-2.00)                                                                                                                    
# (-6.00,-3.00)                                                                                                                    
#                                                                                                                                  
# -> Distancia total: 19.50                                                                                                        
# -> Distancia minima: 1.00                                                                                                        
# -> Distancia maxima: 7.62  
# ```

# ## 3. Enlaces
# 
# * https://computer.howstuffworks.com
# * https://www.studytonight.com/c/structures-in-c.php
# * https://www.tutorialspoint.com/cprogramming/c_structures.htm
# * https://www.programiz.com/c-programming/c-structures
# * https://www.geeksforgeeks.org/structures-c/
# * https://github.com/fordea/c-programming-a-modern-approach
# 
