"""
Função para consumo de API, converter json para DataFrame e retorna um Dataframe
"""
import requests
import pandas as pd

def baixar_deputados():
    resp = requests.get("https://dadosabertos.camara.leg.br/api/v2/deputados")
    data = resp.json()

    df_data = pd.DataFrame(data["dados"])
    return df_data


def sumarizar_por_partido(entrada):
    sumarizado = entrada.groupby('siglaPartido').size().sort_values(ascending=False).reset_index()
    return sumarizado
