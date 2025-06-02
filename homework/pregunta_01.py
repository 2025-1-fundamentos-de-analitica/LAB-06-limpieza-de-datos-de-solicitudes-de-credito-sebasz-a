"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import os
import pandas as pd


def clean_text(column):
    """
    Funcion que recibe una columna y reemplaza guiones por espacios
    """
    column = column.str.lower().str.replace(r'[-_]', ' ', regex=True).str.strip()
    return column

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    # leer el dataset
    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=';')
    df.pop("Unnamed: 0")

    # eliminar registros incompletos
    df = df.dropna()
    # eliminar registros duplicados
    df = df.drop_duplicates()

    # limpieza
    # normalizar texto
    text_columns = ["sexo", "tipo_de_emprendimiento", "idea_negocio", "línea_credito"]
    df[text_columns] = df[text_columns].apply(clean_text)
    df["barrio"] = df["barrio"].str.lower().str.replace(r'[-_]', ' ', regex=True)

    # normalizar las fechas a un solo formato
    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].str.strip()
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True, format="mixed")

    # normalizar el monto
    df["monto_del_credito"] = df["monto_del_credito"].str.translate(str.maketrans({',': '', '$': ''}))
    df["monto_del_credito"] = df["monto_del_credito"].str.strip().replace(r'\.00$', '', regex=True)
    df["monto_del_credito"] = df["monto_del_credito"].astype(int)

    # eliminar nuevos duplicados
    df = df.drop_duplicates()

    # guardar el dataset
    if not os.path.exists("files/output"):
        os.mkdir("files/output")
    df.to_csv("files/output/solicitudes_de_credito.csv", sep=';')

print(pregunta_01())