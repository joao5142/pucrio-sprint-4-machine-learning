import pickle
from sklearn.pipeline import Pipeline as SklearnPipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler


class Pipeline:

    def __init__(self):
        """Inicializa o pipeline"""
        self.pipeline = None

    def carrega_pipeline(self, path):
        """ Carrega um pipeline salvo em formato .pkl """
        with open(path, 'rb') as file:
            self.pipeline = pickle.load(file)
        return self.pipeline

    def construir(self, modelo, normalizacao='standard'):
        """ Constroi um pipeline com normalizacao e modelo
        """
        steps = []

        if normalizacao == 'standard':
            steps.append(('StandardScaler', StandardScaler()))
        elif normalizacao == 'minmax':
            steps.append(('MinMaxScaler', MinMaxScaler()))

        steps.append(('modelo', modelo))
        self.pipeline = SklearnPipeline(steps)
        return self.pipeline
