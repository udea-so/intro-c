#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dannymrock/UdeA-SO-Lab/blob/master/lab0/lab0b/parte2/ptr_arrays.ipynb)

# In[ ]:


get_ipython().system('pip3 install tutormagic')


# In[ ]:


get_ipython().run_line_magic('load_ext', 'tutormagic')


# # Apuntadores y arreglos

# ---
# > **Objetivos**
# > * Conocer y utilizar los apuntadores para el uso eficiente de la memoria.
# > * Presentar el uso de las funciones y establecer cómo se realiza el paso de parámetros a funciones.
# > * Conocer y aplicar el concepto de arreglos de una y más dimensiones en la resolución de problemas mediante algoritmos.
# > * Conocer cómo es posible asignar de forma eficiente espacio en memoria.
# 
# ---

# ## 1. Conceptos previos - ¿Que sucede cuando se declara una variable?
# Cuando una variable se declara esta pasa a ocupar un lugar de memoria cuyo tamaño dependerá del número de bytes asociados al tipo de dato con el cual esta se declara. Suponiendo que se tienen las siguientes instrucciones en C:
# 
# ```C
# int i;
# i = 35;
# ```
# 
# La siguiente figura ilustra su representación en memoria:
# 
# ![alt text](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/var_memoria.png?raw=true)
# 
# **Figura 1**. Representación de una variable en memoria.
# 
# Desde el punto de vista del mapa de memoria y suponiendo que una variable tipo int ocupa 4 bytes tenemos el siguiente resultado por instrucción:
# 
# <table>
# <tbody>
# <tr>
# <td>&nbsp;Instrucción</td>
# <td>Representación en&nbsp;memoria&nbsp;</td>
# </tr>
# <tr>
# <td>int i;</td>
# <td><img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/rep_mapa_inst1.png?raw=true" alt="var_mm1"></td>
# </tr>
# <tr>
# <td>i = 35;</td>
# <td><img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/rep_mapa_inst2.png?raw=true" alt="var_mm2"></td>
# </tr>
# </tbody>
# </table>
# 
# Como se puede ver en la figura anterior, lo que se modifica cuando se hace manipulación sobre variables es el contenido almacenado en un lugar especifico de memoria. Entender esto es de vital importancia para manejar el próximo tema.

# ## 2. Entrando en materia - Algunos aspectos sobre los apuntadores
# 
# ### 2.1. ¿Que es un apuntador?
# 
# Un apuntador es una variable que almacena una **dirección de memoria y no un valor** como ocurre en el caso de las variables normales. La siguiente tabla resalta este hecho:
# 
# <table>
#     <tr>
#         <td colspan="2">Instrucciones</td>
#     </tr>
#     <tr>
#         <td><b>int *p;<br>
#             p = 1000;</b><br><br>
#             <b>Nota</b>: Supóngase que <b>el apuntador</b> se guarda en la posición 500.
#         </td>
#         <td>
#             <img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/rep_mapa_ptr_inst1.png?raw=true">
#         </td>
#     </tr>
#     <tr>
#         <td colspan="2">Mapa de memoria</td>
#     </tr>
#     <tr>
#         <td>
#           <b>int p;<br>
#             p = 1000;</b><br><br>
#             <b>Nota</b>: Supóngase que la <b>variable p</b> se guarda en posición 500.
#           </td>
#         <td>
#             <img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/rep_mapa_var_inst1_comp.png?raw=true"> 
#          </td>
#     </tr>
# </table>
# 
# Como se puede notar en la figura anterior, cuando el valor almacenado en el apuntador hará referencia a la dirección 1000 y no al valor de 1000, esto nos permitirá acceder a dicho lugar de memoria desde el apuntador. Más tarde veremos cómo. Así mismo, como un apuntador guarda una dirección de memoria y teniendo en cuenta que para el ejemplo se supone una arquitectura en la cual se manejan 32 bits ( equivalentes a 4 bytes), esto hará que una variable tipo apuntador sin importar el tipo de dato al que apunte tenga un tamaño de 4 bytes. (Este tamaño se define por la arquitectura. Por ejemplo si la maquina es de 64 bits entonces el tamaño ocupado por una variable tipo apuntador será de 8 bytes).
# 

# ### 2.2. ¿Como se declara un apuntador?
# 
# Un apuntador se declara de la siguiente manera (donde las cosas que se encuentran entre corchetes son opcionales):
# 
# ```C
# tipo *[modificadores_del_tipo] nombre [=valor inicial];
# ```
# Dónde:
# * **Tipo**: Tipo de dato al cual se desea apuntar, puede ser un tipo de dato simple (char, int, etc.) o un tipo de dato complejo como una estructura).
# * **Modificadores del tipo**: Puede contener cualquier combinación de los modificadores de tipo const, volatile y restrict.
# * **Nombre**: Nombre del apuntador.
# * **Valor inicial**: Valor inicial del apuntador. 
# 
# La siguiente figura muestra esto lo anterior en términos del mapa de memoria:
# 
# <table>
#     <tr>
#         <td><b>Instrucciones</b></td>
#         <td><b>Mapa de memoria</b></td>
#     </tr>
#     <tr>
#         <td><b>    
#         short i = 5; <br>
#         short *ptr = &i; 
#          </b> <br> <br>
#          <b>Nota</b>:
#         <ul>
#         <li>El tamaño de una variables short es de 2 bytes.</li>
#         <li>El tamaño de una variable tipo apuntador es de 4 bytes.</li>
#         <li>En el dibujo del mapa de memoria cada dirección aumenta de 1 en 1</li>
#         </ul> 
#         </td>       
#         <td>
#             <img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/rep_ptr_map1.png?raw=true"> 
#         </td>
#     </tr>
# </table>
# 
# Como se puede notar en la figura anterior, lo que se guarda en el apuntador es la dirección base (dirección del byte de menor peso) de la variable a la cual se apunta. Para el caso anterior, la variable i ocupa 2 bytes (103 y 104) sin embargo, en el apuntador se almacena la parte menos correspondiente al byte pesado (byte 103). 
# 
# Si observa la segunda instrucción anteriormente mostrada, la forma como se obtuvo la dirección de i fue por medio del operador dirección (&) antepuesto a la variable. La siguiente tabla se llena con base en la figura anterior:
# 
# 
# | Expresión	| Significado |	Valor |
# |-----------|-------------|-------|
# |i	| Contenido de i	|5|
# |&i	| Dirección de i	|103|
# |p	| Contenido del apuntador p	|103|
# |&p	| Dirección del apuntador p	|106|
# 
# Note en la tabla anterior y la figura previa que con & lo que se obtiene es dirección base de una variable no importa su tipo ya sea una variable normal (char, int, float, etc), apuntador u otro. A continuación se muestra una forma simplificada (tomada de la sección **Pointers basics** de [How Stuff Works](https://computer.howstuffworks.com/c22.htm)) para visualizar los apuntadores y las variables comunes de manera gráfica sin tener que recurrir al bosquejo del mapa de memoria previamente realizado. 
# 
# ![var_mem](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/apuntador2.png?raw=true)
# 
# **Figura 2**. Vista simplificada con variables y apuntadores.
# 
# Note la diferencia en la gráfica, en el dibujo el circulo representa una variable tipo apuntador y como tal almacena una dirección de memoria, la de i para el caso (103); por otro lado el vinculo entre el apuntador y la variable se representa por medio de la flecha. Finalmente, el contenido de la variable puede ser accedido o manipulado desde el símbolo i, o desde al desreferenciar el apuntador (usando *ptr), pero este sera un tema a tratar después.
# 
# Una forma aun mas simplificada e incluso mas conveniente al momento de hacer pruebas de escritorio se muestra a continuación. En esta solo se resalta el vinculo del apuntador con la variable:
# 
# ![var_mem](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/apuntador.png?raw=true)
# 
# **Figura 3**. Vista aun mas simplificada con variables y apuntadores.

# ### 2.3. Manipulación de memoria mediante apuntadores
# 
# Una de las aplicaciones más importantes es el acceso directo a memoria para su manipulación. Para ello, se manejan dos operadores importantes los cuales el operador referencia (&) y el operador des-referencia (*).
# 
# ### 2.3.1. Referenciar un apuntador
# 
# Consiste en asociar el apuntador a una dirección específica (durante la declaración o después de esta), para esto se suele usar el operador & para obtener la dirección de la variable en cuestión. A continuación se muestra la forma como normalmente se hace esto:
# 
# ```C
# apuntador = &variable;
# ```
# También es posible referenciar un apuntador pasándole el valor que se tiene en otro apuntador. Note que no se hizo uso del operador & en este caso:
# 
# ```C
# apuntador = &variable;
# ```
# Todo apuntador debe inicializarse antes de usarse. Si esto no se hace, cuando intente usarlo para hacer alguna operación en memoria el programa sacara un error. Un puntero que no ha sido inicializado se conoce como **Wild pointer**.
# 
# ### 2.3.2. Des-referenciar un apuntador
# Para poder acceder al lugar de memoria que está siendo apuntado por el puntero y realizar operaciones de lectura y escritura sobre esta dirección de memoria se debe des-referenciar el apuntador. Para ello se hace uso del operador des-referencia (*) después de la declaración del apuntador. El contenido del lugar de memoria apuntado (lectura) se obtiene de la siguiente manera:
# 
# ```C
# variable = *apuntador;
# ```
# Ahora si lo que se desea hacer es escribir en el lugar de memoria apuntado se hace lo siguiente:
# 
# ```C
# *apuntador = variable;
# ```

# **Ejemplo 1**
# 
# Suponga que se tiene el siguiente fragmento de código fuente:

# In[24]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nint main() {\n  int i,j;\n  int *p; //Apuntador a un entero\n  p = &i;\n  *p = 5;\n  return 0;\n}')


# También tenga en cuenta lo siguientes enunciados:
# * Suponga que i y j son de 4 bytes y ocupan las direcciones base 1000 y 1004.
# * El apuntador p ocupa las direccione base 2000.
# * Así mismo la arquitectura es de 64 bits por lo que el espacio ocupado por el apuntador sera de 8 bytes.
# 
# Muestre la ejecución paso a paso del código anterior resaltando la evolución en memoria.
# 
# **Solución**: Las instrucciones que se están evaluando en un momento dado se resaltan en la siguiente tabla
# 
# <table>
#     <tr>
#         <td><b>Instrucciones ejecutadas</b></td>
#         <td><b>Contenido del mapa de memoria</b></td>
#         <td><b>Visualización al estilo HowStuffWorks</b></td>
#     </tr>
#     <tr>
#         <td>
#             <b>
#             int i,j;</br>
#             int *p; //Apuntador a un entero</br></b>
#             p = &i;</br>
#             *p = 5;</br>
# </td>
#         <td><img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/ptr_ejem2_map1.png?raw=true"></td>
#         <td><img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/ptr_ejem2_hsw1.png?raw=true"></td>
#     </tr>
#     <tr>
#         <td>        
#         int i,j;</br>
#         int *p; //Apuntador a un entero</br>
#         <b>p = &i;</br></b>
#         *p = 5;</br>    
#         </td>
#         <td><img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/rep_ptr_map2.png?raw=true"></td>
#         <td><img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/ptr_ejem2_hsw2.png?raw=true"></td>
#     </tr>
#     <tr>
#         <td>        
#         int i,j;</br>
#         int *p; //Apuntador a un entero</br>
#         p = &i;</br>
#         <b>*p = 5;</br></b>     
#         </td>
#         <td><img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/rep_ptr_map3.png?raw=true"></td>
#         <td><img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/ptr_ejem2_hsw3.png?raw=true"></td>
#     </tr>
# </table>
# 
# Note que en la última instrucción resaltada el cambio del contenido de la sección de memoria asociado a la variable i no se realizó desde esta (i = 5) sino desde el apuntador p (*p = 5) el cual previamente se puso a apuntar a dicho lugar de memoria (p = &i).
# 

# **Ejemplo 2**
# 
# A continuación se muestra otro ejemplo en el cual se resalta que es posible que varios apuntadores estén apuntando a un mismo lugar de memoria. Tenga en cuenta lo siguientes enunciados:
# * Suponga que i y j son de 4 bytes y ocupan las direcciones base 1000 y 1008.
# * Los apuntadores p, q y r ocupan las direcciones base 2000, 3000 y 4000.
# * Así mismo la arquitectura es de 32 bits por lo que el espacio ocupado por el apuntador será de 4 bytes.
# 
# El codigo asociado se muestra a continuación:

# In[25]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nint main() {\n  int i;\n  int *p,*q,*r;\n  p = &i;\n  q = &i;\n  r = p; \n  return 0;\n}')


# **Solución**: la siguiente tabla muestra con detalle los resultados:
# 
# <table>
#     <tr>
#         <td><b>Instrucciones ejecutadas</b></td>
#         <td><b>Contenido del mapa de memoria</b></td>
#         <td><b>Visualización al estilo HowStuffWorks</b></td>
#     </tr>
#     <tr>
#         <td>
#           int i = 5; </br>
#           int *p,*q,*r; </br>
#           p = &i; </br>
#           q = &i; </br>
#           r = p; </br>
#         </td>
#         <td><img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/rep_ptr2_map.png?raw=true"></td>
#         <td><img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/rep_ptr2_hsw.png?raw=true"></td>
#     </tr>
# </table>

# ### 2.4. Usos de los apuntadores
# 
# ### 2.4.1. Funciones y apuntadores
# 
# Como se vio en la primera parte del laboratorio, existen dos maneras de hacer llamados a funciones, por referencia y por valor. Cuando se realiza un **llamado por valor**; se trabaja sobre una copia de la variable pasada como argumento y por lo tanto la variable original (la que se pasó como argumento) no se modifica. Por otro lado, cuando se realiza un **llamado por referencia** al estar accediendo al lugar de memoria en el que se encuentra la variable pasada como argumento es posible modificar el valor original de la variable pasada como argumento. La siguiente tabla compara un poco la diferencia entre referencia y valor:
# 
# <table>
#     <tr>
#         <td><b>Ítem analizado</b></td>
#         <td><b>Llamada por valor</b></td>
#         <td><b>Llamada por referencia</b></td>
#     </tr>
#     <tr>
#         <td><b>Declaración</b></td>
#         <td>void swap(int i, int j);</td>
#         <td>void swap(int *i, int *j);</td>
#     </tr>
#     <tr>
#         <td><b>Definición</b></td>
#         <td>
#           void swap(int i, int j) { </br>
#             &nbsp;&nbsp;&nbsp;int t; </br>
#             &nbsp;&nbsp;&nbsp;t = x; </br>
#             &nbsp;&nbsp;&nbsp;i = j; </br>
#             &nbsp;&nbsp;&nbsp;j = t; </br>
#           } </br>
#         </td>
#         <td>
#            int v1 = 1, v2 = 2; </br>
#            swap(v1, v2); </br>
#         </td>
#     </tr>
#     <tr>
#         <td><b>Invocación</b></td>
#         <td>
#             void swap(int *i, *int j) { </br>
#                &nbsp;&nbsp;&nbsp;int t; </br>
#                &nbsp;&nbsp;&nbsp;t = *i; </br>
#                &nbsp;&nbsp;&nbsp;*i = *j; </br>
#                &nbsp;&nbsp;&nbsp;*j = t; </br>
#             }   </br>
#         </td>
#         <td>
#            int v1 = 1, v2 = 2; </br>
#            swap(&v1, &v2); </br>
#         </td>
#     </tr>
# </table>
# 
# El paso de funciones por referencia es de extrema utilidad cuando los argumentos que se están pasando a la función son pesados ya que esto evita que se tengan que hacer copias de dichos argumentos que en el peor de los casos pueden ocasionar que el programa colapse por llenar **stack**. También, mediante el uso de apuntadores, es posible superar la restricción que se tiene en la cual una función no puede retornar más de un elemento; así, por medio de referencias es posible retornar un array por ejemplo.
# 
# Para indicar que una función será pasada por referencia, se emplean apuntadores en la cabecera de la función, esto porque lo que se pasa como argumento es la dirección de memoria. Por ejemplo:
# 
# ```C
# tipo_retorno f(tipo_1 *pName_1,tipo_2 *pName_2,...,tipo_N *pName_N) 
# ```
# Para aterrizar un poco más lo anterior, supongamos esta función:
# 
# ```C
# void swap(int *i, int *j) {
#     int t;
#     t = *i;
#     *i = *j;
#     *j = t;
# }
# ```
# Como se pueden notar en la definición de la función anterior, en este caso ambos argumentos son pasados por referencia. 
# 
# Ahora en lo que respecta a la invocación si lo que se pasa es como parámetro es una variable como tal se debe hacer uso del operador **&** para obtener la dirección de dicha variable y así inicializar el apuntador que funciona como argumento. Por otro lado si lo que se está pasando es un apuntador a una variable, no es necesario usar el operador **&** ya que el valor almacenado en este será una dirección de memoria. La siguiente tabla ilustra esto:
# 
# <table>
#     <tr>
#         <td><b>Caso</b></td>
#         <td><b>Invocación</b></td>
#         <td><b>Observaciones</b></td>
#     </tr>
#     <tr>
#         <td>Se está pasando una variable a una función que se llama por referencia</td>
#         <td>
#             int a = 5, b = 10; </br>
#             swap(&a,&b); </br>
#         </td>
#         <td>Es necesario usar el operador & para obtener la dirección de memoria de las variables y así poder inicializar lo apuntadores que funcionan como argumentos.</td>
#     </tr>
#     <tr>
#         <td>Se está pasando apuntador a una función que se llama por referencia</td>
#         <td>
#             int a = 5, b = 10; </br>
#             int *px = &a, *py; </br>
#             py = &b;  </br>
#             swap(px,py); </br>
#         </td>
#         <td>Como lo que se pasan son apuntadores previamente inicializados, estos ya tienen la dirección de memoria de la variable que será pasada como argumento de la función, por lo tanto no es necesario usar el operador &.</td>
#     </tr>
# </table>
# 
# La siguiente figura (tomada de [HowStuffWorks](http://computer.howstuffworks.com/c26.htm)) muestra cómo trabaja una función por referencia:
# 
# ![call_ref](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/call_ref.png?raw=true)
# 
# **Figura 4**. Llamado por referencia.
# 
# Para aclarar un poco observe el siguiente código:

# In[26]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nvoid swap (int *x, int *y);\nvoid swap (int x, int y);\n\nint main() {\n    int x = 5, y = 10;\n    printf("---------------------------------------------------\\n");\n    printf("Llamada por valor \\n");\n    printf("Antes del swap -> x = %d, y = %d\\n",x,y);\n    swap(x, y);\n    printf("Después del swap -> x = %d, y = %d\\n",x,y);\n    printf("---------------------------------------------------\\n");\n    printf("Llamada por referencia " << endl;\n    printf("Antes del swap -> x = %d, y = %d\\n",x,y);\n    swap(&x, &y);\n    printf("Después del swap -> x = %d, y = %d\\n",x,y);\n    printf("---------------------------------------------------\\n");\n    return 0;\n}\n\nvoid swap(int *px, int *py) {\n    int temp;\n    temp = *px;\n    *px = *py;\n    *py = temp;    \n}')


# 
# La salida del programa sera la siguiente:
# ```
# ---------------------------------------------------
# Llamada por valor 
# Antes del swap -> x = 5, y = 10
# Después del swap -> x = 5, y = 10
# ---------------------------------------------------
# Llamada por referencia 
# Antes del swap -> x = 5, y = 10
# Después del swap -> x = 10, y = 5
# ---------------------------------------------------
# ```
# Una función también puede retornar un apuntador cuando es invocada, para hacer esto, en la definición y declaración de la función se debe indicar que la función retornara un apuntador lo cual se hace precediendo el nombre de la función por un asterisco (Ver parte resaltada e rojo a continuación). A continuación se muestra la forma que debe llevar la función para este caso:
# 
# ```C
# tipo_retorno *f(parámetros...) 
# ```
# 
# Observe el siguiente fragmento de código, el cual consiste en una función que obtiene el valor mayor de un vector mediante apuntadores devolviendo la dirección del elemento mayor mediante un apuntador:
# 
# ```C
# int *mayor(int *a, int n) {
#   int i;
#   int *m = a;
#   a++;
#   for (i = 1; i < n; ++i )
#     if(*m < *a) {
#       m = a;
#       a++;
#     }
#   return m;
# }
# ```
# La declaración de la función anterior se muestra a continuación:
# 
# ```C
# int *mayor(int *a, int n); 
# ```
# Otra forma de declaración puede ser:
# 
# ```C
# int *mayor(int *, int n); 
# ```
# 
# Recuerde lo importante en la declaración de la función es indicarle al compilador como van a usarse los parámetros.
# 
# Así mismo, note también, que lo realimente importante es que se declaró un apuntador a un tipo de dato específico, se inicializo, se actualizo y luego se retornó este, en general en la definición de la función se sigue la siguiente plantilla:
# 
# ```C
# tipo *funcion(tipo *arg1,...) {
#   tipo *ptr;  // Declaración del apuntador
#   ptr = &arg; // Inicialización del apuntador
#   
#   /** Operaciones **/
#   ...  
#   return ptr; // Retorno del apuntador
# }
# ```
# 
# A continuación se puede simular el código anterior:

# In[27]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nint *mayor(int *a,int n); // Declaracion\n\nint main() {\n    int a[6] = {1,2,5,9,-1,3};\n    int *p;\n    p = mayor(a,5); // Invocación\n    printf("El elemento mayor del vector es: %d\\n",*p);\n    return 0;\n}\n\n// Definición\nint *mayor(int *a,int n) {\n  int i;\n  int *m = a;\n  a++;\n  for (i = 1; i < n; ++i )\n    if(*m < *a) {\n      m = a;\n      a++;\n    }\n  return m;\n}')


# La siguiente figura muestra el estado de ejecución del programa antes de hacer el retorno de la subrutina mayor:
# 
# ![ret_ptr](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/retorno_prt.png?raw=true
# )
# 
# **Figura 5**. Funcion retornando un apuntador.
# 
# La salida del programa anterior en pantalla es la siguiente:
# 
# ```
# El elemento mayor del vector es: 9
# ```

# ### 2.4.2. Apuntadores y vectores
# 
# #### 2.4.2.1. Vectores
# 
# Un arreglo es un conjunto o colección indexada que permite manejar elementos que son del mismo tipo de dato como un solo objeto. A continuación se muestran algunos ejemplos ([enlace simulación](https://goo.gl/8qAgxY)) en los cuales se lleva a cabo la devlaración e inicialización de un vector:
# 
# <table>
#     <tr>
#         <td><b>Declaración del arreglo</b></td>
#         <td><b>Representación en memoria</b></td>
#     </tr>
#     <tr>
#         <td>int veci[4] = {2, 4, 6, 8};</td>
#         <td><img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/vec_int.png?raw=true"></td>
#     </tr>
#     <tr>
#         <td>float vecf[] = {2.657, 7.9, 2.003, 1.1, 5.8, 8.54, 9.5, 4.09};</td>
#         <td><img src=".https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/vec_float.png?raw=true"></td>
#     </tr>
#     <tr>
#         <td>char mess1[10] = "Hola";</td>
#         <td><img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/vec_char1.png?raw=true"></td>
#     </tr>
#     <tr>
#         <td>mess2[] = {'H','o','l','a','\0'};</td>
#         <td><img src="https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/vec_char2.png?raw=true"></td>
#     </tr>
# </table>
# 
# Notese, que cuando no se pasa el **tamaño** en la declaracion entre corchetes; este es deducido de la lista de inicializacion (pasada entre llaves) o la cadena de caracteres (string) pasada al declarar. En sí, se sigue la siguiente forma:
# 
# **Forma 1**: Pasando el tamaño:
# 
# ```C
# tipo arrayName[TAM] = {valor1, valor2, ...};
# ```
# **Nota**: La cantidad de elementos de la lista de inicialización no puede superar el tamaño (TAM) del arreglo. 
# 
# **Forma 2**: Pasando el tamaño:
# 
# ```C
# tipo arrayName[] = {valor1, valor2, ...};
# ```
# 
# Por otro lado, cuando solo se declaran los arreglos pero no se inicializan, es obligatorio colocar entre corchetes el **tamaño**. La forma de hacer esto se muestra a continuación:
# 
# ```C
# tipo arrayName[TAM];
# ```
# 
# El siguiente codigo muestra el caso en el que solo se declaran varios vectores de diferentes tipos tanto globales como locales:

# In[28]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n// Variables globales\nint A[3];\ndouble B[4];\n\nint main() {\n  // Variables locales\n  char C[6];\n  int D[2];\n  return 0;\n}')


# Observe la diferencia en el valor inicial de los arreglos globales respecto a los locales:
# 
# ![array_no_init](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/array_no_inicializado.png?raw=true)
# **Figura 6**. Representación en memoria de arreglos no inicializados.
# 

# **Forma 2**: Pasando el tamaño:
# 
# En lo que respecta a la manipulacion de arreglos, es igual que en java. El uso de estructuras repetitivas para el manejo de los sibindices en el arreglo es empleado. En los siguientes ejemplos se tiene ilustra esto de manera rapida.
# 
# **Ejemplos**
# 
# 1. Hacer un progama que llene un arreglo de 10 elementos con los multiplos del 10 (1, 10, 20, etc.).

# In[29]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n#define TAM 10\n\nint main() {\n  int A[TAM];\n  int num = 1;\n  // Inicializando el arreglo\n  for(int i = 0; i < TAM; i++) {\n    A[i] = 10*num;\n    num++;     \n  }\n  // Imprimiendo el arreglo\n  printf("A = [ ");\n  for(int i = 0; i < TAM; i++) {\n    printf("%d ", A[i]);     \n  }\n  printf("]");\n  return 0;\n}')


# La aplicacion arroja el siguiente resultado:
# 
# ![array_ciclos1](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/array_ciclos1.png?raw=true)
# **Figura 7**. Empleo de ciclos para manipulación de arrays.
# 
# 2. Hacer cree dos arreglos (A y B), luego, inicialice el arreglo A con numeros aleatorios entre el 1 y el 20, y finalmente lleve al arreglo B los elementos del arreglo A en orden inverso.
# 

# In[31]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n#include <stdlib.h> // required to use \'rand()\'\n#include <time.h>  // required to use \'srand(time(NULL))\'\n#define TAM 10\n\nint main() {\n  srand(time(NULL)); // required for "randomness"\n  int A[TAM], B[TAM];\n  int limSup = 20, limInf = 1;  \n  // Inicializando el arreglo\n  for(int i = 0; i < TAM; i++) {\n    A[i] = rand()%limSup + limInf; // generate a number \n                                   // between limInf and limSup\n     \n  }\n  // Imprimiendo el arreglo A\n  printf("A = [ ");\n  for(int i = 0; i < TAM; i++) {\n    printf("%d ", A[i]);   \n    B[TAM - (i + 1)] = A[i];\n  }\n  printf("]\\n"); \n  // Imprimiendo el arreglo B\n  printf("B = [ ");\n  for(int i = 0; i < TAM; i++) {\n    printf("%d ", B[i]);   \n  }\n  printf("]\\n");\n  return 0;  \n}')


# La simulación de la aplicacion arroja el siguiente resultado:
# 
# ![array_ciclos2](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/array_ciclos2.png?raw=true)
# 
# **Figura 8**. Otro ejemplo de empleo de ciclos para manipulación de arrays.
# 
# Es posible pasar **arreglos** como argumentos de funciones. Basicamente para el caso se tienen en cuenta los mismos 3 aspectos que se mencionaron previamente al tratar las funciones de manera introductoria, pero hay una leve diferencia cuando se emplean arreglos y es propiamente en la parte de la declaracion y la definicion donde se nota esto. Veamos la forma:
# 
# **Definición de la función**
# 
# ```C
# return_type function_name (data type array[],...) {
#   local declarations;
#   function statements;
# }
# ```
# **Declaración de la función**
# 
# ```C
# return_type function_name (data type arrayParam[],...) 
# ```
# 
# **Invocación de la función**
# ```C
# [return_type var = ] function_name (arrayArg[],...) 
# ```
# 
# **Ejemplo**
# 1. Observe el ejemplo 2 anteriormente analizado, muestra cada uno de los componentes (definición, declaracón e invocación) de lo que sería una función para imprimir entero un vector de cualquier tamaño.
# 
# * **Definición de la función**
# 
# ```C
# // Definicion de la funcion para imprimir un array de cualquier tamaño
# void imprimirVector(int V[],int tam) {
#   printf("[ ");
#   for(int i = 0; i < tam; i++) {
#     printf("%d ", V[i]);   
#   }
#   printf("]\n");
# }
# ```
# * **Declaración de la función**
# 
# ```C
# // Declaracion de la funcion para imprimir un array de cualquier tamaño
# void imprimirVector(int V[],int tam);
# ```
# 
# * **Invocación de la función**
# ```C
# // Invocacion para imprimir 
# int X[] = {1, 2, 3, 4};
# imprimirVector(X, 4); // Salida --> [ 1 2 3 4 ]
# ```
# 
# 2. Observe el ejemplo 2 anteriormente analizado e implementelo en forma modular empleando funciones.
# 

# In[30]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n#include <stdlib.h> // required to use \'rand()\'\n#include <time.h>  // required to use \'srand(time(NULL))\'\n#define TAM 10\n\nvoid imprimirVector(int V[],int tam);\nvoid generarVectorAleatorio(int V[], int tam, int vInf, int vSup);\nvoid copiaReversa(int destino[], int origen[], int tam) ;\n\nint main() {\n  srand(time(NULL)); // required for "randomness"\n  int A[TAM], B[TAM];\n  int limSup = 20, limInf = 1;  \n  generarVectorAleatorio(A, TAM, 1, 20);\n  copiaReversa(B, A, TAM);\n  // Imprimiendo el arreglo A\n  printf("A = ");\n  imprimirVector(A, TAM);\n  // Imprimiendo el arreglo B\n  printf("B = ");\n  imprimirVector(B, TAM);\n  return 0;  \n}\n\nvoid generarVectorAleatorio(int V[], int tam, int vInf, int vSup) {\n  for(int i = 0; i < tam; i++) {\n    V[i] = rand()%vSup + vInf;            \n  }\n}\n\nvoid imprimirVector(int V[],int tam) {\n  printf("[ ");\n  for(int i = 0; i < tam; i++) {\n    printf("%d ", V[i]);   \n  }\n  printf("]\\n");\n}\n\nvoid copiaReversa(int destino[], int origen[], int tam) {\n  for(int i = 0; i < tam; i++) {\n    destino[tam - (i + 1)] = origen[i];   \n  }\n}')


# La siguiente figura muestra el resultado del código anterior:
# 
# ![funciones_arrays](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/funciones_arrays.png?raw=true)
# 
# **Figura 9**. Manipulando arreglos con funciones.

# #### 2.4.2.1. Apuntadores y vectores
# 
# Como los apuntadores son variables es posible realizar operaciones matemáticas sobre ellos, sin embargo debido a que lo almacenado en  estos son direcciones de memoria no todas las operaciones convencionales que se podrían hacer sobre una variable normal son posibles. La siguiente tabla muestra las operaciones validas:
# 
# <table>
#     <tr>
#         <td><b>Operación</b></td>
#         <td><b>Anotaciones</b></td>
#     </tr>
#     <tr>
#         <td>Añadir o sustraer un entero de un apuntador.</td>
#         <td>Esto hace  que el puntero apunte a otro lugar de memoria diferente al que inicialmente estaba apuntando esto debido a la modificación de lo que se encuentra almacenado en este.</td>
#     </tr>
#     <tr>
#         <td>Sustraer un apuntador de otro.</td>
#         <td>Cuando se realiza esta operación, los dos apuntadores deben ser del mismo tipo. </td>
#     </tr>
#     <tr>
#         <td>Comparar dos apuntadores.</td>
#         <td>La comparación es comúnmente empleada para comparar cualquier puntero con el puntero a <b>NULL</b> usando los operadores de igualdad (<b>==</b> o <b>!=</b>).</td>
#     </tr>
# </table>
# 
# Las tres operaciones anteriormente descritas son generalmente útiles para apuntadores que se refieren a los elementos de un array. Recordemos que un array consiste de un conjunto de variables del mismo tipo las cuales pueden ser accedidas bajo un mismo nombre usando subíndices. Cuando se declara un array lo que sucede en memoria es que se reservan un conjunto de posiciones contiguas en memoria tal y como se muestra en la siguiente figura: 
# 
# ![array_hsw](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/array_hsw.png?raw=true)
# 
# **Figura 10**. Diferencia entre una variable normal y un vector.
# 
# Para ilustrar lo anterior suponga lo que tiene dos apuntadores, p1 y p2 los cuales están apuntando a los elementos de un array a como el siguiente:
# 
# ![array_a](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/array_a.png?raw=true)
# 
# **Figura 11**. Arreglo a.
# 
# * p1 apunta al elemento i del array (a[i]).
# 
# ![array_a_p1](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/array_a_p1.png?raw=true)
# 
# **Figura 12**. Arreglo a y apuntador p1.
# 
# * Si n es un entero, entonces la expresión **p2 = p1 + n** hace que **p2** apunta al elemento **a[i+n]**. Ojo que **i+n** debe estar dentro del índice del array (es decir **0 <= i+n <= Tamaño del array - 1**). La siguiente figura muestra el caso para **n = 2**, es decir que **p2** apuntara al elemento **a[i+2]**
# 
# ![array_a_p1_p2](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/array_a_p1_p2.png?raw=true)
# 
# **Figura 13**. Arreglo a y apuntadores p1 y p2.
# 
# * La resta **p2 – p1** da el número de elementos del array entre los dos apuntadores. Para el caso de la gráfica anterior **2**.
# * La comparación **p1 < p2** es cierta si el elemento referenciado por p2 tiene un índice más grande que el referenciado por **p1**, de otro lado la comparación es **falsa**. Donde para la figura anterior el resultado es **cierto**.
# 
# Lo anterior muestra que existe una relación entre la forma de escribir un array con subíndices y escribirlo con apuntadores aritmética de apuntadores. Para aterrizar un poco lo anterior analicemos la siguiente tabla:
# 
# <table>
#     <tr>
#         <td><b>Relación entre índices y array</b></td>
#         <td><b>En resumen</b></td>
#     </tr>
#     <tr>
#         <td>El nombre de un arreglo es <b>realmente un apuntador al primer elemento en el array</b>, así si a es un arreglo unidimensional entonces la dirección del primer elemento del array es <b>&a[0]</b> o simplemente <b>a</b>.</td>
#         <td>&a[0]↔a</td>
#     </tr>
#     <tr>
#         <td>La dirección del elemento **i** del array puede ser expresada como <b>&a[i]</b> o como <b>a + i</b>, por lo tanto existen dos manera de escribir la dirección de cualquier elemento del array.</td>
#         <td>&a[i]↔a+i</td>
#     </tr>
#     <tr>
#         <td><b>a[i]</b> o <b>*(a+i)</b> representan el contenido que hay en la dirección en cuestión</td>
#         <td>a[i]↔*(a+i)</td>
#     </tr>
# </table>
# 
# Para entender un poco lo anterior suponga que se ejecutan las siguientes instrucciones:
# 

# In[32]:


get_ipython().run_cell_magic('tutor', '-l c -k', "#include <stdio.h>\n\nint main() {\n  char b[] = {'h', 'o', 'l', 'a','\\0'};\n  *(b+2) = *b;\n  char *p1 = b;\n  char *p2 = b + 3;\n  p2 = p2 - 1;\n  p1 = p2 - 1;\n  *p2 = *(b + 1) + 1;\n  p2 = &b[1];\n  return 0;\n}")


# ## 3. Aritmetica de punteros
# Como se dijo previamente, un apuntador almacena un direccion de memoria asociada a un dato. Tambien, se mostro como es posible hacer uso de apuntadores para barrer y manipular arrays. La existencia diferentes tipos de datos en C (char, int, float, double, ...) con un tamaño en bytes asociado repercute en los valores almancenados en el apuntador. Para aclarar esto un poco observemos las siguientes graaficas.
# 
# En la figura 10 se muestra un array de datos tipo **short** comparado con uno tipo **char**. Los datos tipo short tienen un tamaño de 2 bytes de modo que cada miembro consecutivo del array tipo short (A) tendra una direccion aumentada 2 bytes respecto a miembro anterior; segun lo anterior, si la direccion del elemento A[0] es 0x1000 (&A[0] = 0x1000), la dirección del miembro A[1] será 0x1000 + 2bytes = 0x1000 + 16bits = 0x1010. Por otro lado, en el caso del arreglo char B, la direccion solo cambiar de uno en uno. Asi, si &B[0] = 0x1000, entonces &B[1] = 0x1008. De modo que se puede llegar a una expresión mas general como la siguiente:
# 
# 
# ![array_p](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/arit_pointer.png?raw=true)
# 
# **Figura 14**. Arrays y apuntadores.
# 
# 
# ```
# dir[i] = dir[j] +/- n*(sizeof(type)*8) bits
# 
# Donde n es la diferencia entre los indices j e i
# ```
# 
# Tomando nuevamente la grafica 10, vemos que &A[3] = &A[0] + 3*(sizeof(short)*8) = 0x1000 + 3*2*8 = 0x1000 + 48 = 0x1000 + 0x30 = 0x1030. 
# De modo similar B[1] = B[2] - 1*(sizeof(char)*8)= 0x1000 - 1*(1*8) = 0x1000 + 8 = 0x1000 + 0x0008 = 0x1008.
# 
# A continuación se muestran unos cuantos ejemplos para clarificar esto:

# **Ejemplos**
# 
# 1. Supongase que se tiene el siguiente código:
# 
# ```C
# char A[] = {'h', 'o', 'l', 'a','\0'};
# short B[] = {1,2,3};
# ```
# 
# Asumiendo que un dato tipo short ocupa 2 bytes de memoria y uno char 1 byte. Dibuje en el mapa de memoria los vectores anteriormente resaltados. Las direcciones base son 100 para el vector A y 200 para el vector B. Asi mismo, para el caso las direcciones serán manejadas en decimal.
# 
# **Representacion en memoria con un ancho a 4 bytes**
# En la siguiente figura se muestra la representacion en memoria en la cual se manejan 4 bytes de ancho.
# 
# ![array_hsw](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/mm_char_short1.png?raw=true)
# 
# **Figura 15**. Representación a 4 bytes de ancho.
# 
# **Representacion en memoria con un ancho a 1 byte**
# En la siguiente figura se muestra la representacion en memoria en la cual se manejan 1 byte de ancho.
# 
# ![array_hsw2](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/mm_char_short2.png?raw=true)
# 
# **Figura 16**. Representación a 1 byte de ancho.

# 2. Supongase que se tiene el siguiente codigo fuente:

# In[33]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nint V[4];\nint main() {\n  print("%d\\n",sizeof(int));\n  print("%p\\n",V);\n  int *p1 = V;\n  *p1 = 3;\n  int p2 = &V[0];\n  int p2 += 2;\n  *p2 = 1;\n  p1 = p2 - 1;\n  *p1 = -(*p2);\n  *(p2 + 1) = 2;\n  return 0;\n}')


# Responda las siguientes preguntas:
# * ¿Cual es la direccion base del vector V y de cada uno de sus elementos?
# * ¿Cuando se acaba la ejecucion que valor queda almacenado en los apuntadores p1 y p2?
# * ¿Cual es el contenido del vector cuando culmina el programa?
# 
# Es posible acceder a cada uno de los elementos del arreglo por medio del índice o de manera alternativa usando apuntadores y es allí donde entra en juego la aritmética de punteros ya que por medio de las operaciones de adición y sustracción nos podemos mover a las diferentes posiciones del array para luego poder acceder a sus elementos. Para entender más esto suponga que tiene la siguiente porción de codigo en la cual se manipula un vector empleando la notación con subíndices:
# 

# In[34]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nint main() {\n  int a[6]={1,0,4,7,8,10};\n  int i,suma = 0;\n  a[0]=2;\n  a[3]=10;\n  for(i = 1;i<6;i++) {\n    if(i%2==0) {\n      a[i] = -a[i];\n    }\n    else {\n      a[i]=a[i]+1;\n    }\n  }\n  return 0;\n}')


# Por otro lado el siguiente codigo, hace exactamente lo mismo mediante la notacion de apuntadores:
# 

# In[35]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nint main() {\n  int a[6]={1,0,4,7,8,10};\n  int *ptr;        // Declaracion del apuntador\n  ptr = &a[0];    // Inicializacion del apuntador. (ptr = a)\n  *ptr = 2;    // a[0] = 2\n  ptr = &a[3];    // Ahora ptr esta apuntando al elemento a[3]\n  *ptr=10;    //a[3] = 10\n  ptr = &a[1];    // Ahora ptr esta apuntando al elemento a[1]\n  for(int i = 1;i < 6;i++) {\n    if(i%2==0) {\n      *ptr = -(*ptr); \n    }\n    else {\n      *ptr = *ptr + 1;\n    }\n    ptr++;    //Cambio del valor del apuntador para barrer el arreglo\n  }\n  return 0;\n}')


# La conclusión a la que se llega depues de simular es que existe una correspondencia entre como accedo a un vector mediante la notacion con subindices y la notacion con apuntadores. La siguiente tabla muestra esta relación:
# 
# | Notación subíndice	| Notación puntero |
# |-----------|-------------|
# |&A[0]	| A |
# |&A[i]	| A + i |
# |A[0]	| *A |
# |A[i]	| *(A + i) |
# 
# Teniendo en cuenta **la tabla de equivalencia** anteriormente mostrada podemos pasar arreglos como parametros de funciones y manipularlos en las instrucciones del cuerpo de la instruccion, esto en resumen, no es mas que hacer un cambio de los corchetes **[]** por el asterirco (propio de los apuntadores) para la parametro asociado al vector. Veamos esto usando ejemplos.
# 
# <table>
#     <tr>
#         <td><b>Notación</b></td>
#         <td><b>Empleando subindices</b></td>
#         <td><b>Empleando apuntadores</b></td>
#     </tr>
#     <tr>
#         <td><b>Declaración</b></td>
#         <td>void imprimirVector(int V[],int tam);</td>
#         <td>void imprimirVector(int *V,int tam);</td>
#     </tr>   
#     <tr>
#         <td><b>Definición</b></td>
#         <td>             
#           void imprimirVector(int V[],int tam) {</br>
#              &nbsp;&nbsp;&nbsp;printf("[ ");</br>
#              &nbsp;&nbsp;&nbsp;for(int i = 0; i < tam; i++) {</br>
#              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   printf("%d ", V[i]); </br>  
#              &nbsp;&nbsp;&nbsp;}</br>
#              &nbsp;&nbsp;&nbsp;printf("]\n");</br>
#           }</br>
#         </td>
#         <td>        
#            void imprimirVector(int *V,int tam) {</br>
#              &nbsp;&nbsp;&nbsp;printf("[ ");</br>
#              &nbsp;&nbsp;&nbsp;for(int i = 0; i < tam; i++) {</br>
#              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   printf("%d ", *(V + i)); </br>  
#              &nbsp;&nbsp;&nbsp;}</br>
#              &nbsp;&nbsp;&nbsp;printf("]\n");</br>
#           }</br>
#         </td>
#     </tr>
#     <tr>
#         <td><b>Invocación</b></td>
#         <td>
#             int A[] = {1, 2, 3}; </br>
#             imprimirVector(A, 3); </br>
#         </td>
#         <td>
#            int A[] = {1, 2, 3}; </br>
#            imprimirVector(A, 3); </br>
#         </td>
#     </tr>
# </table>
# 
# En el siguiente [enlace](https://goo.gl/onVv3v) se encuentra el anterior para simular. Pordrá notar que los resultados no cambian.

# ## 4. Apuntadores a apuntadores
# 
# Es posible poner apuntar un apuntador a un apuntador, lo cual se indica con la cantidad de asteriscos colocados en la declaración del apuntador, así la declaración realizada en las siguientes líneas de código:
# ```C
# char ch; /*Un caracter*/
# char *pch; /*Un apuntado a un dato tipo caracter*/
# char **pch; /*Un apuntador a un apuntador a un caracter*/
# ```
# suponiendo que:
# * El tamaño de ocupado por una variable apuntador es de 8 bytes.
# * El tamaño ocupado por una variable tipo char es de 1 byte.
# * Las direcciones de las variables ch, pch y ppch son 0xFFF000BCC, 0xFFF000BD0 y 0xFFF000BD8 respectivamente.
# 
# El resultado de ejecutar las instrucciones anteriores muestra un resultado similar al de la siguiente figura:
# 
# ![ptr_to_ptr](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/ptr_to_ptr_ambas.png?raw=true)
# 
# **Figura 17**. Resultado de la ejecución del codigo anterior.
# 
# Notese que aun no se han inicializado las variables (variable normal, apuntador y apuntador a apuntador). A continuación de muestra un código de inicializacion y su respectivo efecto:
# 
# ```C
# pch = &ch; /*Inicializacion del apuntador*/
# ppch = &pch; /*Inicializacion del apuntador al apuntador*/
# ```
# 
# ![ptr_to_ptr__mem_2_3](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/ptr_to_ptr_mem_2_3.png?raw=true)
# 
# **Figura 18**. Resultado de la ejecución del codigo anterior.
# 
# Notese del codigo anterior que a un apuntador a un apuntador se le debe pasar la dirección de memoria del apuntador al que está siendo inicializado.
# 
# La siguiente tabla muestra una lista de equivalencias entre los valores almacenados en las variables anteriormente creadas:
# 
# 
# | Ítem	| Equivalencia en código |
# |-----------|-------------|
# |Lugar de memoria accedido (variable ch)	| ch = *pch = **ppch |
# |Dirección de la variable ch (&ch)	| &ch = pch = *ppch |
# |Dirección de memoria del apuntador (&pch)	| &pch = ppch |
# |Dirección de memoria del apuntador al apuntador (&ppch)	| &ppch |
# 
# Aplicando la anterior equivalencia en la figura 14 tenemos (Tenga muy claro el operador direccion (&)):
# 1. ch = *pch = **ppch = ?
# 2. &ch = pch = *ppch = 0xFFF000BCC
# 3. &pch = ppch = 0xFFF000BD0
# 4. &ppch = 0xFFF000BD8
# 
# La anterior tabla implica que si yo quiero cambiar el valor de ch lo puedo hacer ya modificando la variable como tal (ch = valor) o desreferenciando el apuntador que la apunta (*pch = valor)  o desreferenciando el apuntador del apuntador que la apunta (**ppch = valor), a continuación se muestran las tres equivalencias. A continuación se muestra esto:
# 
# **Forma 1**: modificando la variable directamente
# 
# ```C
# ch = 'A';
# ```
# 
# **Forma 2**: modificando la variable por medio del apuntador
# 
# ```C
# *pch = 'A';
# ```
# 
# **Forma 3**: modificando la variable por medio del apuntador al apuntador
# 
# ```C
# **ppch = 'A';
# ```

# **Ejemplo**:
# Simule el siguiente codigo y saque conclusiones:

# In[36]:


get_ipython().run_cell_magic('tutor', '-l c -k', "#include <stdio.h>\n\nint main() {\n  char ch;\n  char *pch, **ppch;\n  char ***pppch = &ppch;\n  pch = &ch;\n  ppch = &pch;\n  ***pppch = 'A';\n  **ppch = *pch + 1;\n  ch = **ppch + 3;\n  return 0;\n}")


# ## 5. Apuntadores genericos y casts
# 
# Un apuntador generico o void pointer es un tipo especial de apuntador que puede apuntar a cualquier tipo de dato.
# Su unica limitación es que el dato apuntado no puede ser desreferenciado directamente (el operador * no puede ser usado en este tipo de apuntadores) pues para el caso, la longitud del tipo de dato al que se apunta no puede ser determinada lo hace necesario un casting para hacer que el aputador generico pueda apuntar a un tipo de dato concreto (el cual si puede ser referenciado).
# 
# ```C  
#   /* Declaracion de variables*/
#   tipo1 var1_1, var1_2,...;
#   ... 
#   tipoN varN_1, varN_2,...;
#   /* Declaracion apuntador generico*/
#   void *ptr;
#   /* Referencia a una variable tipo tipo1 */
#   ptr = &var1_1; // var es una variable de cualquier tipo
#   /* Desreferencia a una variable tipo tipo1*/
#   var1_2 = *((tipo1 *)ptr); // cast
#   /* Referencia a una variable tipo tipoN */
#   ptr = &varN_1; // var es una variable de cualquier tipo
#   /* Desreferencia a una variable tipo tipo1*/
#   varN_2 = *((tipoN *)ptr); // cast
#   ...
# ```
# 
# En si el cast es de la forma:
# 
# ```C 
# *((tipo *)ptr)
# ```
# 
# A continuación se muestran algunos ejemplos para aclarar lo anteriormente mencionado.
# 
# **Ejemplos**
# 
# 1. Analice el siguiente codigo:

# In[37]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nint main() {\n  int a = 5;\n  double b = 3.1415;\n  void *vp;\n  vp = &a;\n  printf("a = %d\\n", *((int *)vp)); // Cast a (int *)\n  vp = &b;\n  printf("b = %lf\\n", *((double *)vp)); // Cast (double *)\n  return 0;\n}')


# 2. Analice el siguiente codigo:

# In[38]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nvoid swapChar(char *a, char *b);\nvoid swapFloat(float *a, float *b);\n\nint main() {\n  char w = \'w\', x = \'a\';\n  float y = 2.3, z = -0.5;\n  printf("---- Caracteres ----\\n");\n  printf("Antes: w = %c, x = %c\\n", w, x);\n  swapChar(&w, &x);\n  printf("Despues: w = %c, x = %c\\n", w, x);\n  printf("---- Reales ----\\n");\n  printf("Antes: y = %.2f, z = %.2f\\n", y, z);\n  swapFloat(&y, &z);\n  printf("Despues: y = %.2f, z = %.2f\\n", y, z);  \n  return 0;\n}\n\nvoid swapChar(char *a, char *b) {\n  char temp;\n  temp = *a;\n  *a = *b;\n  *b = temp;\n}\n\nvoid swapFloat(float *a, float *b) {\n  float temp;\n  temp = *a;\n  *a = *b;\n  *b = temp;\n}')


# La salida del código anterior se muestra a continuación:
# 
# ![void_ptr_fun_no_gen](https://github.com/repos-SO-UdeA/laboratorios/blob/master/lab1/teoria/parte2/imagenes/swap_no_generico.png?raw=true)
# 
# **Figura 20**. Funciones por referencia normales.
# 
# **Reto**: Hacer la función que permita hacer el intercambio entre dos cadenas de caracteres
# 
# 3. Analice el siguiente código

# In[39]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nswap2(void *x, void *y, int size);\n\nint main() {\n  char w = \'w\', x = \'a\';\n  float y = 2.3, z = -0.5;\n  char s1[] = "abcd", s2[]="wxyz";\n  printf("---- Caracteres ----\\n");\n  printf("Antes: w = %c, x = %c\\n", w, x);\n  swap2(&w, &x, sizeof(char));\n  printf("Despues: w = %c, x = %c\\n", w, x);\n  printf("---- Reales ----\\n");\n  printf("Antes: y = %.2f, z = %.2f\\n", y, z);\n  swap2(&y, &z, sizeof(float));\n  printf("Despues: y = %.2f, z = %.2f\\n", y, z); \n  printf("---- Cadenas ----\\n");\n  printf("Antes: s1 = %s, s2 = %s\\n", s1, s2);\n  swap2(s1, s2, sizeof(s1));\n  printf("Despues: s1 = %s, s2 = %s\\n", s1, s2);   \n  return 0;\n}\n\nint swap2(void *x, void *y, int size) {\n  void *tmp;\n  if ((tmp = malloc(size)) == NULL) {\n    return -1;\n  }\n  memcpy(tmp, x, size); \n  memcpy(x, y, size); \n  memcpy(y, tmp, size);\n  free(tmp);\n  return 0;\n}')


# Notese respecto al codigo del ejemplo 2 que se tiene al usar apuntadores genericos, pues una misma funcion puede soportar diferentes tipos de datos. La función **memcpy** empleada en el ejemplo anterior puede ser estudiada con mas detalle en el siguiente [enlace](https://www.tutorialspoint.com/c_standard_library/c_function_memcpy.htm).

# ## 6. Enlaces de interés
# * https://www.geeksforgeeks.org/data-types-in-c/
# * https://www.programiz.com/c-programming/c-enumeration
# * http://people.duke.edu/~tkb13/courses/ncsu-csc230/lecture/
# * https://www.geeksforgeeks.org/dangling-void-null-wild-pointers/
# * https://www.geeksforgeeks.org/tag/c-pointers/
# * https://www.geeksforgeeks.org/double-pointer-pointer-pointer-c/
# * https://www.eskimo.com/~scs/cclass/int/sx8.html
# * https://www.tutorialspoint.com/cprogramming/c_pointer_to_pointer.htm
# * https://boredzo.org/pointers/
# * https://beginnersbook.com/2014/01/c-pointer-to-pointer/
# * https://www.tutorialspoint.com/cprogramming/index.htm
# * http://gsd.web.elte.hu/lectures/c-en/c-lecture-9/
# * http://math.pnw.edu/~rlkraft/cs123-2009/homework/hw3/hw3.html
