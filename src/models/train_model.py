import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report


def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f'Dados carregados com sucesso de {file_path}!')
        return data
    except FileNotFoundError:
        print(f'Erro: O arquivo {file_path} não foi encontrado.')
    except Exception as e:
        print(f'Erro inesperado: {e}')


def preprocess_data(df):
    if df.isnull().sum().any():
        print("Há valores ausentes nos dados. Realizando preenchimento...")
        df = df.dropna()
    return df


def train_and_evaluate_naive_bayes(train_data, test_data):
    X_train = train_data.drop('Channel', axis=1)
    y_train = train_data['Channel']
    X_test = test_data.drop('Channel', axis=1)
    y_test = test_data['Channel']

    # Treinando o modelo Naïve Bayes
    model = GaussianNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("Relatório de Classificação para Naïve Bayes:")
    print(classification_report(y_test, y_pred))


def main():
    train_data_path = '../../data/processed/Wholesale_train.csv'
    test_data_path = '../../data/processed/Wholesale_test.csv'

    # Carregar e processar dados
    train_data = load_data(train_data_path)
    test_data = load_data(test_data_path)

    if train_data is not None and test_data is not None:
        train_data = preprocess_data(train_data)
        test_data = preprocess_data(test_data)

        train_and_evaluate_naive_bayes(train_data, test_data)


main()
