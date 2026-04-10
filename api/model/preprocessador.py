from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import numpy as np


class PreProcessador:

    def __init__(self):
        """Inicializa o preprocessador"""
        pass

    def separa_teste_treino(self, dataset, percentual_teste, seed=7):
        """ Divide os dados em treino e teste usando holdout.
        """
        X_train, X_test, Y_train, Y_test = self.__preparar_holdout(dataset,
                                                                    percentual_teste,
                                                                    seed)
        return (X_train, X_test, Y_train, Y_test)

    def __preparar_holdout(self, dataset, percentual_teste, seed):
        """ Divide os dados em treino e teste usando o metodo holdout. """
        dados = dataset.values
        X = dados[:, 0:-1]
        Y = dados[:, -1]
        return train_test_split(X, Y, test_size=percentual_teste, random_state=seed)

    def balancear_dados(self, X_train, Y_train, seed=7):
        """ Aplica SMOTE para balancear as classes no conjunto de treino.
        Usado pois o dataset de agua e desbalanceado (mais nao-potavel do que potavel).
        """
        smote = SMOTE(random_state=seed)
        X_bal, Y_bal = smote.fit_resample(X_train, Y_train)
        return X_bal, Y_bal

    def preparar_form(self, form):
        """ Prepara os dados recebidos do front para serem usados no modelo. """
        X_input = np.array([
            form.ph,
            form.hardness,
            form.solids,
            form.chloramines,
            form.sulfate,
            form.conductivity,
            form.organic_carbon,
            form.trihalomethanes,
            form.turbidity,
        ])
        X_input = X_input.reshape(1, -1)
        return X_input
