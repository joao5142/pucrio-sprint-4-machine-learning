import pickle
from sklearn.ensemble import RandomForestClassifier


class Model:

    def __init__(self):
        """Inicializa o modelo"""
        self.model = None

    def carrega_modelo(self, path):
        """ Carrega o modelo salvo em formato .pkl """
        if path.endswith('.pkl'):
            with open(path, 'rb') as file:
                self.model = pickle.load(file)
        else:
            raise Exception('Formato de arquivo nao suportado')
        return self.model

    def treinar(self, X_train, Y_train, n_estimators=200, seed=7):
        """ Treina um RandomForestClassifier com os parametros usados no notebook.
        Espera receber dados ja balanceados (apos SMOTE).
        """
        self.model = RandomForestClassifier(n_estimators=n_estimators,
                                            random_state=seed)
        self.model.fit(X_train, Y_train)
        return self.model

    def preditor(self, X_input):
        """ Realiza a predicao com base no modelo treinado """
        if self.model is None:
            raise Exception('Modelo nao carregado. Use carrega_modelo() ou treinar() primeiro.')
        return self.model.predict(X_input)
