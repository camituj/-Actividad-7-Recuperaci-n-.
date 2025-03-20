
import pandas as pd
import numpy as np
import os

def cargar_archivo(archivo):
    extension = os.path.splitext(archivo)[-1].lower()
    
    if extension == ".csv":
        return pd.read_csv(archivo)
    elif extension == ".html":
        return pd.read_html(archivo)[0]
    else:
        raise ValueError("Hola, acabas de ingresar un documento que desconozco, con extensión: ", extension)

def sustituir_nulos(df):
    columnas_numericas = df.select_dtypes(include=[np.number]).columns
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]   #la verdad los escribí porque no recuerdo profe como era lo de los corchetes para los primos. 
    
    for i, col in enumerate(df.columns):
        if df[col].isnull().any():
            if col in columnas_numericas:
                df[col].fillna(1111111 if i in primos else 1000001, inplace=True)
            else:
                df[col].fillna("Valor Nulo", inplace=True)
    return df

def identificar_nulos(df):
    nulos_por_columna = df.isnull().sum()
    total_nulos = df.isnull().sum().sum()
    return nulos_por_columna, total_nulos

def identificar_atipicos(df):
    columnas_numericas = df.select_dtypes(include=[np.number]).columns
    
    for col in columnas_numericas:
        Quartil1 = df[col].quantile(0.25)
        Quartil3 = df[col].quantile(0.75)
        RanfoIntercuatilico = Quartil3 - Quartil1
        limite_inferior = Quartil1 - 1.5 * RanfoIntercuatilico
        limite_superior = Quartil3 + 1.5 * RanfoIntercuatilico
    
        valores_corregidos = []

        for valor in df[col]:
            if valor < limite_inferior or valor > limite_superior:
                valores_corregidos.append("Valor Atípico")
            else:
                valores_corregidos.append(valor)
        
        df[col] = valores_corregidos
    
    return df
    
