#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dannymrock/UdeA-SO-Lab/blob/master/lab0/lab0b/parte3/matrices_ptr.ipynb)

# In[ ]:


get_ipython().system('pip3 install tutormagic')


# In[ ]:


get_ipython().run_line_magic('load_ext', 'tutormagic')


# # Apuntadores y arreglos multidimensionales
# 

# ---
# > **Objetivos**
# > * Introducir el concepto, manipulacion y uso de los arreglos multidimensionales.
# > * Tratar mas aplicaciones de los apuntadores
# 
# ---

# ## 1. Arreglos multidimensionales en C
# 
# A diferencia de los vectores, los arreglos multidimensionales (tambien conocidos como) se caracterizan por que manejan mas de un indice. Respecto a la manipulación, no existen considerables diferencias con java, sin embargo, a modo de repaso vamos a introducir algunos conceptos de repaso.
# 
# ### 1.1. Declaración
# Aqui se establecen ls dimensiones de cada componente, las formas mas comunes siguen una sintaxis como la siguiente:
# 
# **Caso para un arreglo de dos dimensiones**
# 
# ```C
# // Arreglo de dos dimensiones
# arrayType  arrayName[Rows][Columns];
# ```
# 
# **Caso para un arreglo de tres dimensiones**
# 
# ```C
# // Arreglo de tres dimensiones
# arrayType  arrayName[Planes][Rows ][Columns];
# ```
# 
# **Caso para un arreglo de N dimensiones**
# 
# ```C
# // Arreglo de N dimensiones
# arrayType  arrayName[Dim1][Dim2]...[DimN];
# ```
# 
# **Ejemplo**
# El siguiente codigo  muestra algunas declaraciones:
# 

# In[3]:


get_ipython().run_cell_magic('tutor', '-l c -k', 'int A[2][3];\nfloat B[3][1];\n\nint main() {\n  char C[2][3][4];\n  return 0;\n}')


# La salida es como se muestra a continuacion:
# 
# ![matrix_1](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/matriz1.png?raw=true)
# 
# **Figura 1**. Declaración de varios arreglos multidimensionales.
# 
# A veces, puede ser util **inicializar** una matrix al declararla, a continuacion se muestran algunos ejemplos:
# 
# **Ejemplo**
# El siguiente ćodigo muestra diferentes formas de declarar e inicializar matrices:
# 

# In[5]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nint matrix1[][4] = {\n                    {4, 2, 7, 3},\n                    {6, 1, 9, 5},\n                    {8, 5, 0, 1}  \n                  };\n\n\nint main() {\n  int matrix2[2][2] = {{1, 2}, {3, 4}};\n  int matrix3[2][2] = {{1}, {3, 4}}; \n  int matrix4[3][5]={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};\n  int matrix5[][3]={1, 2, 3, 4};\n  return 0;\n}')


# La representación en memoria de las matrices declaradas en el ejercicio anterior se muestra a continuación
# 
# ![matrix_2](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/matriz2.png?raw=true)
# 
# **Figura 2**. Declaración e inicialización de varios arreglos multidimensionales.
# 
# **Nota**: Al inicializar una matrix se debe pasar como minimo la dimension de las columnas (para el caso de dos dimensiones), si no se hace el compilador no sera capaz de deducir el tamaño de la matriz y se producira un error.
# 
# 

# ### 1.2. Procesamiento de los arreglos multimensionales
# 
# Como en java, el uso de ciclos anidados es fundamentar para el movimiento a traves de cada uno de los elementos de la matrix. Generalmente, las varibles que controlan los ciclos seran empleados como subindices para barrer las matrices. A continuación se muestra un código para refrescar el concepto:

# In[6]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n#define F 3\n#define C 4\n\n\nint main() {\n  int M[F][C] = {\n                  {4, 2, 7, 3},\n                  {6, 1, 9, 5},\n                  {8, 5, 0, 1}  \n                };\n  \n  printf("Barriendo por filas: \\n");\n  for(int i = 0; i < F; i++) {\n    printf("Fila %d: ",i);\n    for(int j = 0; j < C; j++) {\n      printf("%d ",M[i][j]);\n    }\n    printf("\\n");\n  }\n  printf("\\nBarriendo por columnas: \\n");\n  for(int i = 0; i < C; i++) {\n    printf("Columna %d: ",i);\n    for(int j = 0; j < F; j++) {\n      printf("%d ",M[j][i]);\n    }\n    printf("\\n");\n  }\n  return 0;\n}')


# En la siguiente figura se muestra el resultado del código anterior.
# 
# ![matrix_3](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/matriz3.png?raw=true)
# 
# **Figura 3**. Barriendo un array multidimensional.

# ### 1.3. Funciones y arreglos multidimensionales
# 
# Es posible pasar arreglos multidimensionales como parametros de funciones. Cuando se pasa un array multidimensional, la primera dimension del array no tiene que ser especificada pero la segunda dimension (y cualquier subsecuente) deberá ser dada. A continuacion se muestran diferentes casos de uso cuando se emplean funciones con arreglos multidimensionales.
# 
# **Caso 1 - Cuando las dimensiones de la matrix estan disponibles globalmente**: las dimensiones pueden ser constantes globales o macros. A continuación se muestra en caso específico en el que se crea una función para imprimir una matrix 2D. Veamos el código asociado:

# In[7]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n#define M 3\n#define N 3\n \nvoid print(int arr[M][N]);\n \nint main()\n{\n    int arr[][N] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};\n    print(arr);\n    return 0;\n}\n\nvoid print(int arr[M][N]) {\n    int i, j;\n    for (i = 0; i < M; i++) {\n      printf("[ ");\n      for (j = 0; j < N; j++) {\n        printf("%d ", arr[i][j]);\n      }\n      printf("]\\n");\n    }\n}')


# **Caso 2 - Cuando solo la segunda dimension de la matrix esta disponible globalmente**: esta puede ser un constante global o una macro. Pese a que se omite la primera dimension de la matrix, esta debe ser usada como un parametro formal de la función con el objetivo de conocer la expención de la primera dimensión. Veamos el mismo ejemplo anterior teniendo en cuenta este caso:

# In[8]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n#define N 3\n \nvoid print(int arr[][N], int m); \n \nint main()\n{\n    int arr[][N] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};\n    print(arr,3);\n    return 0;\n}\n\nvoid print(int arr[][N], int m) {\n    int i, j;\n    for (i = 0; i < m; i++) {\n      printf("[ ");\n      for (j = 0; j < N; j++) {\n        printf("%d ", arr[i][j]);\n      }\n      printf("]\\n");\n    }\n}')


# **Caso 3 - Pasando matrices de cualquier dimension**: 
# Notese que una de las limitaciones de los dos metodos anteriores, es que el tamaño de ambas (caso 1) o al menos una de las dimensiones de la matrix es fijo (columnas de la matrix para el caso 2). Sin embargo desde C99, C soporta que matrices de tamaño variable puedan ser pasadas al especificar las dimensiones de la variable. A continuacion de muestra el caso para el mismo ejemplo analizado (ver el siguiente código):
# 

# In[9]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nvoid print(int m, int n, int arr[][n]);\n \nint main()\n{\n    int arr[][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};\n    int F = 3, C = 3;\n    print(F, C, arr);\n    return 0;\n}\n\nvoid print(int m, int n, int arr[][n]) {\n    int i, j;\n    for (i = 0; i < m; i++) {\n      printf("[ ");\n      for (j = 0; j < n; j++) {\n        printf("%d ", arr[i][j]);\n      }\n      printf("]\\n");\n    }\n}')


# Como anotación importante, de todos los parámetros pasados a la función el último debe ser la matriz, pues como usa como dimensión para las columnas otra variable, si esta no esta previamente declarada se generara un error; de este modo poner la matrix de último evita este problema.
# 
# Finalmante, para todos los casos anteriormente expuestos, la salida es la siguiente:
# 
# ![matrix_4](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/matriz4.png?raw=true)
# 
# **Figura 4**. Salida del programa.
# 
# Otra forma de pasar matrices a funciones es empleando apuntadores, pero esto ser visto posteriormente.
# 

# ## 2. Apuntadores y matrices
# 
# Así como en el caso de los arreglos de una dimensión, es posible representar los arreglos multidimensionales con una notación de punteros equivalente. 
# 
# En el caso de las matrices de dos dimensiones, cuando estas se almacenan en memoria, la forma como la memoria se llena es fila por fila, es decir si se tiene una matriz de n filas por m columnas las primeras n posiciones en memoria corresponden a los n elementos de la primera fila, las n posiciones siguientes corresponden a los n elementos de la siguiente fila y así sucesivamente hasta que todas las filas son ocupadas (n*m posiciones de memoria). La siguiente figura muestra esto:
# 
# 
# <table>
# <tbody>
# <tr>
# <td><b>Representacion de la matrix</b></td>
# <td><b>Representacion en memoria</b></td>
# </tr>
# <tr>
# <td><img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/a1.png?raw=true" alt="a"><br>
# <br>
# short a[3][2] = {<br>
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{101,51},<br>
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{102,67},<br>
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{103,76}<br>
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;};<br><br>
# Para el caso vamos a suponer que cada dato tipo short ocupa 2 bytes.  
# </td>
# <td>
# <img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/mem_a1.png?raw=true" alt="mem_a">  
# </td>    
# </tr>  
# <tbody>  
# </table>
# 
# A continuación se muestra otro ejemplo para reforzar el concepto. Para el caso, dato el siguiente código.

# In[10]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nint main() {\n  int matrix[2][5] = {\n                       {1,2,3,4,5},\n                       {6,7,8,9,10}\n                     };\n\n  for(int i = 0; i < 2; i++) {\n    for(int j = 0; j < 5; j++) {\n      printf("matrix[%d][%d] -> Address: %p, Value: %d\\n",\\\n             i,j,&matrix[i][j],matrix[i][j]);\n    }    \n  }\n  return 0;\n}')


# La salida del programa se muestra a continuación:
# 
# ![matrix_5](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/matrix_output.png?raw=true)
# 
# **Figura 5**. Salida del programa.
# 
# De modo que segun lo anterior, la representacion en memoria de la matrix será:
# 
# ![matrix_6](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/matrix_mem.png?raw=true)
# 
# **Figura 6**. Representación de la matrix en memoria.
# 
# Así mismo, un arreglo de dos dimensiones puede ser tratado como un arreglo de una dimensión cuyos elementos son arreglos de una dimensión (las filas). Esto es resaltado en la siguiente figura para la matrix anteriormente definida:
# 
# ![matrix_7](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/matrix_vector.png?raw=true)
# 
# **Figura 7**. Representación de la matrix como arreglos de una dimension asociada a  cada una de las filas.
# 
# **Ejemplo**: Se tiene el siguiente [codigo fuente](https://goo.gl/rCTH5C)

# In[11]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nint main() {\n  int mat[][3] = {{1,2,3},{4,5,6},{7,8,9}};\n  /* Analisis del elemento mat[0][0] */\n  printf("mat: %p\\n", mat); // D\n  printf("*mat: %p\\n", *mat); // D\n  // -----------------------------------------------------\n  printf("mat[0]: %p\\n",mat[0]); // D\n  printf("&mat[0][0]: %p\\n",&mat[0][0]); // D\n  printf("**mat: %d\\n",**mat); // V\n  printf("*(mat[0]): %d\\n",*(mat[0])); // V\n  printf("*(&mat[0][0]): %d\\n",*(&mat[0][0])); // V\n  printf("---------------------\\n");\n  /* Analisis del elemento mat[1][0] */\n  printf("mat[1]: %p\\n",mat[1]); // D\n  printf("&mat[1][0]: %p\\n",&mat[1][0]); // D\n  printf("mat[1][0]: %d\\n",mat[1][0]); // V\n  printf("*mat[1]: %d\\n",*mat[1]); // V\n  printf("*(&mat[1][0]): %d\\n",*(&mat[1][0])); // V\n  printf("---------------------\\n");\n  /* Analisis del elemento mat[2][1] */\n  printf("&mat[2][1]: %p\\n",&mat[2][1]); // D\n  printf("mat[2] + 1: %p\\n",mat[2] + 1); // D\n  printf("mat[2][1]: %d\\n",mat[2][1]); // V\n  printf("*(mat[2] + 1): %d\\n",*(mat[2] + 1)); // V\n  printf("*(*(mat + 2) + 1): %d\\n",*(*(mat + 2) + 1)); // V\n  return 0;\n}')


# La salida del codigo anterior se muestra a continuación:
# 
# ![matrix_8](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/matrix_example.png?raw=true)
# 
# **Figura 8**. Salida del codigo anterior.
# 
# Teniendo en cuenta el resultado de la figura anterior y representando la matrix como un vector de arreglos se tiene la siguiente figura (notese que se resaltan los elementos asociados a las salidas en pantalla del programa anterior):
# 
# ![matrix_9](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/ejercicio_matrix.png?raw=true)
# 
# **Figura 9**. Representacion de la matrix como un vector de arrays.
# 
# Teniendo en cuenta lo anterior, la representación en memoria se muestra a continuación:
# 
# ![matrix_10](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/ejercicio_matrix_mem.png?raw=true)
# 
# **Figura 10**. Representacion en memoria de la matrix de la figura anterior.
# 
# La siguiente figura resalta la comparación de la salida en pantalla con el mapa de memoria resaltando las equivalencias a las que se llega:
# 
# ![matrix_11](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/comparacion.png?raw=true)
# 
# **Figura 11**. Equivalencias.
# 
# Teniendo en cuenta la figura anterior, se pueden llegar a las siguientes equivalencias mas generales, las cuales se muestran en la siguiente tabla:
# 
# <table>
# <tbody>
# <tr>
# <td><b>Equivalencias</b></td>
# <td><b>Expresión</b></td>
# </tr>
# <tr>
# <td><b>De valor</b></td>
# <td>
#   Obteniendo el valor de una matriz en la posicion (i,j):<br>
#   <br>
#   A[i][j] = *(A+i)[j] = *(*(A+i)+ j) = *(A[i] + j)
# </td>
# </tr>
# <tr>
# <td><b>De dirección</b></td>
# <td>
#   Obteniendo la direccion de una matriz en la posicion (i,j):<br>
#   <br>
#   &A[i][j] = (A+i)[j] = *(A+i) + j = A[i] + j <br>
#   <br>
#   <b>Otra alternativa</b>:<br>
#   &A[i][j] = &A[0][0] + i*N_COLUMNAS + j <br><br>
#   En lo que respecta a obtener el posición de una fila i, lo cual se da cuando j = 0:<br>
#   &A[i][0] = A[i] + 0 = A[i]
# </td>
# </tr>
# <tr>
# <td><b>Anotaciones</b></td>
# <td>
#   &A[0][0] = A = A[0] = &A[0]<br><br>
#   Pero ojo que las anteriores equivalencias no son intercambiables: <br>
#   <ul>
#   <li>&A[0][0] + 1, apunta a A[0][1]</li>
#   <li>A[0] + 1, apunta a A[0][1]</li>
#   <li>A + 1, apunta a A[1][0]</li>
#   <li>&A[0] + 1, apunta a A[1][0]</li>
#   </ul>
# </td>
# </tr>
# </tbody>
# </table>  
#   
# Es posible definir un arreglo de dos dimensiones como un apuntador a un grupo de arreglos de una dimensión, de modo que una declaración de un arreglo bidimensional puede ser hecha de la siguiente manera:
# 
# ```C
# T *(ptVar)[m];
# ```
# 
# Donde **T** está asociado al tipo de dato (el cual puede ser simple o compuesto) y **n** es el número de filas del array bidimensional y **m** es el número de elementos que habrá en la fila. La expresión anterior puede ser por lo tanto una alternativa a la declaración típica de matrices por ejemplo para el caso de una matriz de n filas por n columnas como la siguiente:
# 
# ```C
# T mat[n][m];
# ```
# 
# La expresión anterior se puede generalizar a arreglos de más elementos tal de modo que para una matriz de dimensión N:
# 
# ```C
# T mat[val1]...[val_N];
# ```
# 
# De modo que la expresión alternativa estará dada por:
# 
# ```C
# T *(ptVar)[val_2][val_3]...[val_N];
# ```
# 
# Donde T se refiere al tipo de dato y las expresiones val_1, val_2,..., val_N se refieren al número máximo de elementos asociados con cada uno de los N subíndices del array. 
# 
# Otra cosa importante es la presencia del paréntesis, este es necesario ya que si no está, no nos estaríamos refiriendo a un apuntador a un grupo de arrays  sino a un array de apuntadores, esto porque los [] tienen mayor precedencia que el *. Así según lo anterior:
# 
# ```C
# int (*pz)[2]; // Crea un apuntador a un array de 2 enteros.
# int *pax[2]; // Crea un array de dos punteros a enteros.
# ```
# 
# Para aterrizar el concepto anterior vamos a analizar el siguiente ejemplo.
# 
# **Ejemplos**
# 
# 1. Dado el siguiente fragmento de código, hacer el respectivo analisis:

# In[12]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nint main() {\n  int A[3][2] = {{1,2},{3,4},{5,6}};\n  int (*pz)[2];\n  pz = A;\n  printf("A[0][0]: %d\\n", A[0][0]); // V\n  printf("**pz: %d\\n", **pz); // V\n  printf("*pz[0]: %d\\n", *pz[0]); // V\n  printf("(*pz)[0]: %d\\n", (*pz)[0]); // V\n  printf("&A[0][0]: %p\\n", &A[0][0]); // M\n  printf("*pz: %p\\n", *pz); // M\n  printf("pz[0]: %p\\n", pz[0]); // M\n  printf("---------------------\\n");\n  printf("A[1][0]: %d\\n", A[1][0]); // V\n  printf("*pz[1]: %d\\n", *pz[1]); // V\n  printf("*(pz[1]+0): %d\\n", *(pz[1]+0)); // V\n  printf("*(*(pz + 1)+0): %d\\n", *(*(pz +1 )+0)); // V\n  printf("&A[1][0]: %p\\n", &A[1][0]); // M\n  printf("pz + 1: %p\\n", pz + 1); // M\n  printf("pz[1]: %p\\n", pz[1]); // M\n  printf("---------------------\\n");\n  printf("A[2][1]: %d\\n", A[2][1]);\n  printf("*(pz[2] + 1): %d\\n", *(pz[2] + 1));\n  printf("*(*(pz + 2) + 1): %d\\n", *(*(pz + 2) + 1));\n  printf("&A[2][1]: %p\\n", &A[2][1]);  \n  printf("pz[2] + 1: %p\\n", pz[2] + 1);\n  return 0;\n}')


# 
# La salida del código anterior se muestra a continuación:
# 
# ![matrix_12](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/ejemplo_analisis1.png?raw=true)
# 
# **Figura 12**. Resultado del ejemplo 1.
# 
# Por otro lado, la representacion en memoria y como arreglo de vectores de la matrix, con base en la figura anterior es se muestra a continuacion.
# 
# ![matrix_13](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/ejemplo_analisis1_1.png?raw=true)
# 
# **Figura 13**. Representacion en memomria de la matrix analizada en el ejemplo.
# 
# 2. Analizar el siguiente código:

# In[13]:


get_ipython().run_cell_magic('tutor', '-l c -k', '\nint main() {\n  int B[2][2]= {1, 2, 3, 4};\n  int (*p)[2];\n  p = B;\n  **p = -(*(p[0] + 1));\n  p++;\n  **p = *(*p + 1) + 1;\n  return 0;\n}')


# La siguiente tabla muestra el resultado de realizar la prueba de escritorio paso por paso (resaltando en negrita) la instruccion que esta ejecutandose. Asi mismo, se asumen que las direcciones estan en formato decimal y no hexadecimal.
# 
# 
# <table>
# <tbody>
# <tr>
# <td><b>Instrucciones</b></td>
# <td><b>Representación</b></td>
# <td><b>Efecto en memoria</b></td>
# </tr>
# <tr>
# <td>
#   int B[2][2]= {1, 2, 3, 4};<br>
#   <b>int (*p)[2];</b><br>
#   p = B;<br>
#   **p = -(*(p[0] + 1));<br>
#   p++;<br>
#   **p = *(*p + 1) + 1;<br>
# </td>
# <td> <img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/ejemplo_analisis2_1.png?raw=true" alt="2_1"> </td>
# <td> <img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/ejemplo_analisis2_mem1.png?raw=true" alt="2_1mem"> </td>
# </tr>
# <tr>
# <td>
#   int B[2][2]= {1, 2, 3, 4};<br>
#   int (*p)[2];<br>
#   <b>p = B;</b><br>
#   **p = -(*(p[0] + 1));<br>
#   p++;<br>
#   **p = *(*p + 1) + 1;<br>
# </td>
# <td> <img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/ejemplo_analisis2_2.png?raw=true" alt="2_2"> </td>
# <td> <img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/ejemplo_analisis2_mem2.png?raw=true" alt="2_2mem"> </td>
# </tr>
# <tr>
# <td>
#   int B[2][2]= {1, 2, 3, 4};<br>
#   int (*p)[2];<br>
#   p = B;<br>
#   <b>**p = -(*(p[0] + 1));</b><br>
#   p++;<br>
#   **p = *(*p + 1) + 1;<br>
# </td>
# <td> <img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/ejemplo_analisis2_3.png?raw=true.png" alt="2_3"> </td>
# <td> <img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/ejemplo_analisis2_mem3.png?raw=true" alt="2_3mem"> </td>
# </tr>  
# <tr>
# <td>
#   int B[2][2]= {1, 2, 3, 4};<br>
#   int (*p)[2];<br>
#   p = B;<br>
#   **p = -(*(p[0] + 1));<br>
#   <b>p++;</b><br>
#   **p = *(*p + 1) + 1;<br>
# </td>
# <td> <img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/ejemplo_analisis2_4.png?raw=true.png" alt="2_4"> </td>
# <td> <img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/ejemplo_analisis2_mem4.png?raw=true.png" alt="2_4mem"> </td>
# </tr>   
# <tr>
# <td>
#   int B[2][2]= {1, 2, 3, 4};<br>
#   int (*p)[2];<br>
#   p = B;<br>
#   **p = -(*(p[0] + 1));<br>
#   p++;<br>
#   <b>**p = *(*p + 1) + 1;</b><br>
# </td>
# <td> <img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/ejemplo_analisis2_5.png?raw=true.png" alt="2_5"> </td>
# <td> <img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/ejemplo_analisis2_mem5.png?raw=true" alt="2_5mem"> </td>
# </tr>    
# </tbody>
# </table>  
# 
# 3. Se desea crear un array de bidimensional de 10 filas por 20 columnas llamado x esto puede ser hecho, así:
# 
# ```C
# int (*x)[20]; // Apuntador a un grupo de 20 enteros contiguos de un array unidimensional 
# ```
# 
# O así:
# 
# ```C
# int x[10][20];  
# ```
# 
# Esto se muestra en la siguiente grafica:
# 
# ![matrix_14](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/matrix_ptr.png?raw=true)
# 
# **Figura 14**. Array bidimensional asociado a x.
# 
# Basicamente, lo que se quiere dar a entender con la grafica es que x apunta al primer array de 20 elementos, el cual es la primera fila (fila 0), del array original. De manera similar, (x + 1) apunta a los segundos 20 elementos del array (fila 1 del array original) y así sucesivamente hasta la última fila. Para clarificar esto simule el siguiente ejemplo y note lo que implica lo anterior:
# 

# In[ ]:


get_ipython().run_cell_magic('tutor', '-l c -k ', '\nint main() {\n  int (*y)[20];\n  int x[10][20];\n  y = x;\n  for(int i = 0; i < 10; i++) {\n    y = x + i;\n  }\n  return 0;\n}')


# 
# ![matrix_15](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/matrix_ptr_2.png?raw=true)
# 
# **Figura 15**. Array bidimensional asociado al codigo anterior.
# 
# 4. Considere una matriz de tres dimensiones con la siguiente declaración:
# 
# ```C
# float t[3][4][5];   
# ```
# 
# O así:
# 
# ```C
# float (*t)[4][5];     
# ```
# 
# En la declaración anterior, se definió a t como un apuntador a un grupo de 4x5 elementos contiguos de una matriz bidimensional. Por lo tanto según lo anterior, t apuntara a los primeros 4x5 elementos, t + 1 apuntara a los segundos 4x5 elementos y así sucesivamente.
# 
# En el siguiente ejemplo se aterriza el concepto:

# In[15]:


get_ipython().run_cell_magic('tutor', '-l c -k', '\nint main() {\n  float t[3][4][5]; \n  float (*ptr1)[4][5];\n  float (*ptr2)[4][5];\n  float (*ptr3)[4][5];\n  ptr1 = t;\n  ptr2 = t + 1;\n  ptr3 = t + 2;\n  return 0;\n}')


# La salida de muestra a continuación:
# 
# ![matrix_16](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/matrix_ptr_3.png?raw=true.png)
# 
# **Figura 16**. Array tridimensional asociado a t.

# ## 3. Empleo de apuntadores para acceder a los elementos de una matrix
# 
# Para acceder a un elemento particular dentro de un array particular se emplea el operador indirección (*). A continuación se muestra como 	en el caso de una matriz bidimesional. Para aclarar este concepto miremos el siguiente ejemplo:
# 
# **Ejemplo**: Supongase que se tiene un array entero de 10x20 y se desea acceder al elemento perteneciente a la fila 2 y la columna 5 (x[2][5]) . La forma de acceso es la mostrada a continuación:
# 
# ```C
# float *(*(x+2)+5);  
# ```
# Cuyo efecto es el mostrado en la siguiente figura:
# 
# ![matrix_17](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/acceso_array_ptr.png?raw=true)
# 
# **Figura 17**. Accediendo a una matrix por medio de la notacion apuntador.
# 
# Para acceder a dicho lugar de memoria es necesario tener en cuenta una serie de cosas:
# * ```x+2```: Puntero al vector correspondiente a la fila 2.
# * ```*(x+2)```: Apuntador al primer elemento de la fila 2.
# * ```*(x+2)+5```: Apuntador al elemento 5 en la fila 2.
# * ```*(*(x+2)+5)```: Elemento de la columna 5 y la fila 2, propiamente x[2][5].
# 
# Para aterrizar lo anterior, supongamos que declaramos una matrix global x[10][20] y deseamos llevar al elemento x[2][5] el valor de 10. ¿Como seria el procedimiento a seguir empleando la notacion apuntador?
# 
# ```C
# int x[10][20];
# 
# int main() {
#   *(*(x + 2) + 5) = 10; // x[2][5] = 10
#   return 0;
# }
# ```
# 
# La salida del [codido anterior](https://goo.gl/wrmfkY) es la siguiente:
# 
# ![matrix_18](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/ejemplo_matrix_acceso.png?raw=true)
# 
# **Figura 18**. Modificando el valor de una matrix a traves de la notacion apuntador.
# 
# 
# <table>
# <tbody>
# <tr>
# <td><b>Equivalencias</b></td>
# <td><b>Expresión</b></td>
# </tr>
# <tr>
# <td><b>De valor</b></td>
# <td>
#   Obteniendo el valor de una matriz en la posicion (i,j):<br>
#   <br>
#   A[i][j] = *(A+i)[j] = *(*(A+i)+ j) = *(A[i] + j)
# </td>
# </tr>
# <tr>
# <td><b>De dirección</b></td>
# <td>
#   Obteniendo la direccion de una matriz en la posicion (i,j):<br>
#   <br>
#   &A[i][j] = (A+i)[j] = *(A+i) + j = A[i] + j <br>
#   <br>
#   <b>Otra alternativa</b>:<br>
#   &A[i][j] = &A[0][0] + i*N_COLUMNAS + j <br><br>
#   En lo que respecta a obtener el posición de una fila i, lo cual se da cuando j = 0:<br>
#   &A[i][0] = A[i] + 0 = A[i]
# </td>
# </tr>
# <tr>
# <td><b>Anotaciones</b></td>
# <td>
#   &A[0][0] = A = A[0] = &A[0]<br><br>
#   Pero ojo que las anteriores equivalencias no son intercambiables: <br>
#   <ul>
#   <li>&A[0][0] + 1, apunta a A[0][1]</li>
#   <li>A[0] + 1, apunta a A[0][1]</li>
#   <li>A + 1, apunta a A[1][0]</li>
#   <li>&A[0] + 1, apunta a A[1][0]</li>
#   </ul>
# </td>
# </tr>
# </tbody>
# </table>  
#  

# **Ejemplo**
# Para comprender bien lo anterior codifique y simule el siguiente programa:

# In[16]:


get_ipython().run_cell_magic('tutor', '-l c -k', '/* zippo2.c --  zippo infovia a pointer variable */\n#include <stdio.h>\n\nint main(void)\n{\n    int zippo[4][2] = { {2,4} , {6,8} , {1,3} , {5, 7} };\n    int (*pz)[2];\n    pz = zippo;\n    printf("pz = %p, pz + 1 = %p\\n", pz, pz + 1); // D\n    printf("pz[0] = %p, pz[0] + 1 = %p\\n", pz[0], pz[0] + 1); // D\n    printf("*pz = %p, *pz + 1 = %p\\n", *pz, *pz + 1); // D\n    printf("pz[0][0] = %d\\n", pz[0][0]);  // V\n    printf("*pz[0] = %d\\n", *pz[0]); // V\n    printf("**pz = %d\\n", **pz); // V\n    printf("pz[2][1] = %d\\n", pz[2][1]); // V\n    printf("*(*(pz + 2) + 1) = %d\\n", *(*(pz + 2) + 1)); // V\n    return 0;\n}')


# Lleve a cabo la **prueba de escritorio** y compárela con la salida en pantalla del programa. ¿Cómo queda la matriz después de las instrucciones anteriormente mostradas?
# 
# ## 4. Arreglos de apuntadores
# 
# Un arreglo de apuntadores es un array cuyos elementos son apuntadores a algún tipo de dato. Estos, constituyen una forma alternativa de expresar un arreglo multidimensional. Por ejemplo un array de dos dimensiones:
# 
# ```C
# T mat[val_1][val_2];
# ```
# 
# Puede ser reescrito como un array de apuntadores de la siguiente manera:
# 
# ```C
# T *mat[val_1];
# ```
# 
# Luego, generalizando lo anterior para arreglos de N dimensiones tenemos que:
# 
# ```C
# T mat[val_2][val_3]...[val_N];
# ```
# 
# La forma alternativa será:
# 
# ```C
# T *mat[val_1][val_2]...[val_N-1];
# ```
# 
# Aquí **T** se refiere al tipo de dato y las expresiones **val_1**, **val_2**, ..., **val_N** se refieren al número máximo de elementos asociados con cada uno de los N subíndices del array. Note que a diferencia del caso anterior ya no se emplean paréntesis en este tipo de declaración por lo que el array contendrá apuntadores al tipo específico definido en la declaración.
# 
# **Ejemplo**: Supóngase que se tiene una matriz bidimensional x de 10 filas por 20 columnas. Esta definida como un vector de apuntadores sera: 
# 
# ```C
# int *x[10];
# ```
# 
# Aquí, **x[0]** apuntara al principio de la primera fila, **x[1]** al principio de la segunda, observe que a diferencia del caso anterior no fue necesario declarar el  número de elementos de cada columna de manera explícita. La siguiente figura muestra el efecto de la anterior declaración con más detalle:
# 
# ![matrix_15](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/matrix_ptr2.png?raw=true)
# 
# **Figura 19**. Representacion de la matrix.
# 
# Por otro lado, teniendo en cuenta lo anterior, si lo que se desea es acceder a un elemento individual de la matrix, tal como x[2][5]. Una forma equivalente será:
# 
# ```C
# int *(x[2]+5);
# ```
# 
# **Donde**:
# * ```x[2]```: Es un apuntador al primer elemento de la fila 2.
# *	```x[2] + 5```: Es un apuntador al elemento 5 dentro de la fila 2.
# *	```*(x[2]+5)```: Se refiere al contenido del elemento de la fila 2 y la columna 5, es decir x[2][5].
# *	```*(*(x + 2) + 5)```: Se refiere al contenido del elemento de la fila 2 y la columna 5, es decir x[2][5].
# 
# Lo anterior, se ilustra mas claramente en la siguiente figura: 
# 
# ![matrix_20](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/acceso_array_ptr2.png?raw=true)
# 
# **Figura 20**. Acceso a la matrix.
# 
# **Ejemplo**: Suponga que se tiene un array tridimensional de enteror de dimensiones 2x3x4. La forma de expresar este array como un array de apuntadores bidimensional es:
# 
# ```C
# int *t[2][3];
# ```
# 
# En el anterior codigo se genera una matrix de 6 apuntadores cada uno de los cuales esta apuntando a un vector unidimensional. Teniendo en cuenta lo anterior, se se desea acceder a un elemento individual tal como ``` t[1][1][2] ```  la forma de hacerlo empleando esta notación sera:
# 
# ```C
# int *(t[1][1] + 2); // Será lo mismo que t[1][1][2]
# ```
# 

# **Ejemplo**: a modo de repaso simule y analice el siguiente código:

# In[17]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n/* Matrix */\nint t[2][3][4];\n\n/* Declaracion de las funciones */\nvoid llenarMatrix(int M[][3][4]); \nvoid imprimirMatrix(int M[][3][4]);\nvoid imprimirDireccionesMatrix(int M[][3][4]);\n\n/* Funcion principal */\nint main() {\n  llenarMatrix(t);\n  *(t[1][1] + 2) = -4; // t[1][1][2] = -4; \n  // Recorriendo las direcciones de la matrix de apuntadores\n  // asociada\n  int *ptr;\n  for (int i = 0; i < 2; i++) {\n    for (int j = 0; j < 3; j++) {\n      ptr = t[i][j];\n      printf("t[%d][%d] = %p\\n",i,j,ptr);\n    }\n  }\n  printf("\\nMatrix:\\n");\n  imprimirMatrix(t);\n  printf("\\nDirecciones de la Matrix:\\n");\n  imprimirDireccionesMatrix(t);\n  return 0;   \n}\n\n/* Definicion de las funciones */\nvoid llenarMatrix(int M[][3][4]) {\n  int val = 1;\n  for(int i = 0; i < 2; i++) {\n    for(int j = 0; j < 3; j++) {\n      for(int k = 0; k < 4; k++) {\n        M[i][j][k] = val++;  \n      }\n    }\n  }  \n}\n\nvoid imprimirDireccionesMatrix(int M[][3][4]) {\n  for(int i = 0; i < 2; i++) {\n    for(int j = 0; j < 3; j++) {\n      for(int k = 0; k < 4; k++) {\n        printf("&M[%d][%d][%d] = %p\\n", i, j, k,M[i][j] + k);  \n      }      \n    }\n  }  \n}\n\nvoid imprimirMatrix(int M[][3][4]) {\n  printf("-------------------------\\n");\n  for(int i = 0; i < 2; i++) {\n    for(int j = 0; j < 3; j++) {\n      for(int k = 0; k < 4; k++) {\n        printf("%5d ", M[i][j][k]);  \n      }\n      printf("\\n");\n    }\n    printf("------------------------\\n");\n  }  \n}')


# La siguiente figura muestra la salida del programa y su representacion de la matrix. Notese como se almacena la matrix en memoria.
# 
# ![matrix_21](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/ptr_matrix3_output2.png?raw=true)
# 
# **Figura 21**. Salida del programa y representacion de la matrix.
# 
# En la siguiente figura, se compara la salida con la representacion de la matrix en el mapa de memoria. Notese, las equivalencias:
# 
# 
# ![matrix_22](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/ptr_matrix3_output3.png?raw=true)
# 
# **Figura 22**. Salida del programa y representacion en memoria de la matrix.
# 
# **Caso de aplicacion**: 
# 
# Una de las mayores aplicaciones de los arreglos a apuntadores es que permiten trabajar con jagged arrays (matrices irregulares). Un array de este tipo es un array bidimensional que posee un numero de columnas diferentes por cada fila tal y como se muestra en la siguiente figura:
# 
# ![matrix_23](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/irregular_matrix.png?raw=true)
# 
# **Figura 23**. Matrix irregular.
# 
# En el siguiente codigo se define la anterior matrix irregular. Adicionalmente, se imprimen en pantalla algunos de los valores asociados a esta:

# In[18]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nint main() {\n  int F0[] = {1,2,3,4};\n  int F1[] = {5,6};\n  int F2[] = {7,8,9};\n  int *P[3];\n  P[0] = F0;\n  P[1] = F1;\n  P[2] = F2;\n  printf("F0[2]: %d\\n", F0[2]);\n  printf("*P[0] + 2: %\\n", *P[0] + 2);\n  printf("**P + 2:  %d\\n", **P + 2);\n  printf("F2[1]: %d\\n", F2[1]);\n  printf("*P[2] + 1: %d\\n", *P[2] + 1 );\n  printf("*(*(P + 2) + 1): %d\\n", *(*(P + 2) + 1));\n  return 0;\n}')


# La salida del programa anterior se muestra en la siguiente figura, el resultado de la figura anterior se muestra en la siguiente figura (para la parte del mapa de memoria asuma las direcciones para las variabled dadas en la figura y que la arquitectura es de 32 bits):
# 
# ![matrix_24](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/irregular_matrix2.png?raw=true)
# 
# **Figura 24**. Salida del programa que manipula la Matrix irregular.
# 
# **Caso de aplicacion**: 
# 
# Los arreglos de apuntadores ofrecen a menudo un método conveniente para almacenar cadenas de caracteres.  En esta situación, cada elemento del array es un apuntador tipo carácter que indica el principio de una cadena de caracteres separada, por lo tanto un array de **n** elementos puede apuntar a diferentes cadenas de caracteres, de tal manera que cada cadena individual puede ser referenciada por su correspondiente apuntador. La siguiente figura muestra este hecho:
# 
# ```C
# char *myStrPtr[5] = { "If anything can go wrong, it will",
#                       "Nothing is foolproof",
#                       "Every solution breeds new problems."};
# ```
# 
# La representacion der arreglo de apuntadores tipo char descrito anteriormente se muestra a continuacion:
# 
# ![matrix_25](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/arreglos_apuntadores_char.png?raw=true)
# 
# **Figura 25**. Arreglo de apuntadores tipo char.
# 
# Ahora bien, para profundizar analice el siguiente código:
# 

# In[19]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nint main() {\n  char *myStrPtr[5] = { "Universidad de Antioquia",\n                         "Alma Mater",\n                         "De la patria."};\n  int i = 0;\n  while(myStrPtr[i] != NULL) {\n    printf("%s\\n",myStrPtr[i]);\n    i++;\n  }\n  return 0;\n}')


# La salida del codigo anterio se muestra a continuacion:
# 
# ![matrix_27](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/salida_char_ptrs.png?raw=true)
# 
# **Figura 27**. Ejemplo empleando un arreglo de apuntadores tipo char.
# 
# **Ejemplo**: A continuacion se muestra como accder y manipular matrices 3D (tomando como base el siguiente [enlace](https://www.codeproject.com/Articles/83080/Dynamic-Three-Dimensional-Arrays-in-C-C-C-Java)). Esto se explica por que en algun momento posterior puede ser de extrema utilidad, ademas, por que se resalta el uso de diferentes niveles de apuntadores. El codigo ejemplo se muestra a continución:

# In[20]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n/** Dimensiones de la matrix */\n\nconst int P = 2; // Planos\nconst int F = 2; // Filas\nconst int C = 3; // Columnas\n\n/** Declaracion de las funciones */\n\nvoid imprimirMatrix3D(int *** M3D);\n\n/** Funcion principal */\n\nint main() {\n  /* Vectores: Cada no de los cuales sera una fila de la matrix*/\n  int v0_0[] = {1,2,3};\n  int v0_1[] = {4,5,6};\n  int v1_0[] = {7,8,9};\n  int v1_1[] = {10,11,12};\n  /* Matrices 2D: Cada una sera un plano de la matrix 2D */\n  int *V0[2];  \n  V0[0] = v0_0;\n  V0[1] = v0_1;\n  int *V1[2];\n  V1[0] = v1_0;\n  V1[1] = v1_1;\n  /* Matrix 3D: Formada por 2 matrices 2D */\n  int **M[2];\n  M[0] = V0;\n  M[1] = V1;\n  /* Apuntador a la matrix 3D */\n  int ***Mptr = M;\n  /* Cambio de valores de la matrix a traves del apuntador*/\n  *(*(*(M + 0) + 1) + 2) = 0;  // M[0][1][2] = 0;\n  *(*(*(M + 1) + 0) + 1) = -5; // M[1][0][1] = -5;\n  *(*(M[1]+ 1) + 1) = -15;     // M[1][1][1] = -15;\n  /* Imprimiendo la matrix 3D */\n  imprimirMatrix3D(M);  \n  return 0;\n}\n\n/** Definicion de las funciones */\nvoid imprimirMatrix3D(int *** M3D) {\n  printf("-------------------------\\n");\n  for(int i = 0; i < P; i++) {\n    for(int j = 0; j < F; j++) {\n      for(int k = 0; k < C; k++) {\n        printf("%5d ", *(*(*(M3D + i) + j) + k));  \n      }\n      printf("\\n");\n    }\n    printf("------------------------\\n");\n  }      \n}')


# La salida en pantalla y las variables se muestran en la siguiente figura, note los niveles jerarquico empleados en los apuntadores:
# 
# ![matrix_28](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte3/imagenes/ptr_matrix3D_output.png?raw=true)
# 
# **Figura 28**. Matrix 3D y apuntadores.
# 

# ## 5. Enlaces de interés
# * https://www.geeksforgeeks.org/pass-2d-array-parameter-c/
# * https://www.programiz.com/c-programming/c-arrays-functions
# * https://www.programiz.com/c-programming/examples/matrix-multiplication-function
# * https://beginnersbook.com/2014/01/c-passing-array-to-function-example/
# * https://www.codeproject.com/Articles/83080/Dynamic-Three-Dimensional-Arrays-in-C-C-C-Java
# 
