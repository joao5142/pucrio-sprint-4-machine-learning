from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


class Avaliador:

    def __init__(self):
        """Inicializa o avaliador"""
        pass

    def avaliar(self, model, X_test, Y_test):
        """ Faz uma predicao e avalia o modelo retornando acuracia,
        matriz de confusao e relatorio de classificacao.
        """
        predicoes = model.predict(X_test)

        acuracia = accuracy_score(Y_test, predicoes)
        matriz = confusion_matrix(Y_test, predicoes)
        relatorio = classification_report(Y_test, predicoes)

        return acuracia, matriz, relatorio
