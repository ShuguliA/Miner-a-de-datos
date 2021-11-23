#!/usr/bin/env python
# coding: utf-8

# PANDAS

# Pandas es una librería de Python para el análisis de datos. Iniciado por Wes McKinney en 2008 debido a la necesidad de una herramienta de análisis cuantitativo potente y flexible, pandas se ha convertido en una de las bibliotecas de Python más populares.

# 
# Aquí se muestran los cinco primeros datos 

# In[4]:


import pandas as pd
df=pd.read_csv("Website Phishing.csv")
df.head()


# Aquí muestra los dos primeros datos de nuestro dataframe

# In[2]:


df.head(2)


# Aquí se toma al azar un dato de nuestro dataframe

# In[3]:


df.sample()


# Numpy

# Numpy, abreviatura de python numérico, es el paquete fundamental para la computación científica en python, se basa en Numeric array. Todas las matrices en NumPy están indexadas empezando por 0 y terminando en M-1
# siguiendo la convención de Python.

# In[11]:


import seaborn as sns 
import pandas 


# Aquí visualizamos los datos con un diagrama de líneas y pandas

# In[12]:


df=pd.read_csv("Website Phishing.csv")
  
sns.lineplot( df['SFH'], df['Result'])


# Utilizamos el parámetro de tono para trazar el gráfico

# In[13]:


import seaborn 
import pandas 
  
data = pandas.read_csv("Website Phishing.csv") 
  
seaborn.scatterplot(data['SSLfinal_State'],data['web_traffic'])


# Trama del enjambre con pandas y seaborn

# In[16]:


import seaborn  
  
seaborn.set(style = 'whitegrid')  
  
data = pandas.read_csv( "Website Phishing.csv" ) 
seaborn.swarmplot(x = data["URL_Length"])  


# Scipy

# SciPy es una libreria informática científica de código abierto para el lenguaje de programación Python. SciPy es una biblioteca de rutinas numéricas para el lenguaje de programación Python que proporciona bloques de construcción fundamentales para modelar y resolver problemas científicos

# In[ ]:


import pandas as pd
df=pd.read_csv("Website Phishing.csv")

