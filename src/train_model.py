import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report


def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print('Dados carregados com sucesso!')

        if data.isnull().sum().any():
            print("Há valores ausentes nos dados. Realizando preenchimento...")
            data_preprocessed = data.dropna()
        return data_preprocessed

    except FileNotFoundError:
        print(f'Erro: O arquivo {file_path} não foi encontrado.')
    except Exception as e:
        print(f'Erro inesperado: {e}')


def evaluate_decision_tree(train_data, test_data):
    X_train = train_data.drop('Channel', axis=1) # features
    y_train = train_data['Channel']  # target
    X_test = test_data.drop('Channel', axis=1)
    y_test = test_data['Channel']

    # treinando o modelo de Decision Tree
    model = DecisionTreeClassifier(random_state=42) 
    model.fit(X_train, y_train) 
    y_pred = model.predict(X_test)

    print("Relatório de classificação para Decision Tree:")
    print(classification_report(y_test, y_pred))


train_data= '../data/processed/Wholesale_train.csv'
test_data = '../data/processed/Wholesale_test.csv'

# carregando e processando dados
train_data = load_data(train_data)
test_data = load_data(test_data)

# treinando o modelo com o conjunto de treinamento e 
# classificando amostras do conjunto de testes
evaluate_decision_tree(train_data, test_data)

