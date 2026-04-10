import pandas as pd


class Carregador:

    def __init__(self):
        """Inicializa o carregador"""
        pass

    def carregar_dados(self, url: str, atributos: list):
        """ Carrega e retorna um DataFrame. Preenche valores ausentes com 0,
        conforme tratamento aplicado no notebook de treinamento.
        """
        dataset = pd.read_csv(url, names=atributos, header=0,
                              skiprows=0, delimiter=',')
        dataset = dataset.fillna(0)
        return dataset
