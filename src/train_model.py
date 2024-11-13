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
    X_train = train_data.drop('Channel', axis=1)  # features
    y_train = train_data['Channel']  # target
    X_test = test_data.drop('Channel', axis=1)
    y_test = test_data['Channel']

    # treinando o modelo de Decision Tree
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("Relatório de classificação para Decision Tree:")
    print(classification_report(y_test, y_pred))

    # Retornar o modelo treinado e os nomes das colunas
    return model, X_train.columns


def classify_user_input(model, column_names):
    try:
        # Solicitar dados ao usuário
        dados_usuario = []
        for column in column_names:
            dado = float(input(f"Insira o valor para {column}: "))
            dados_usuario.append(dado)

        # Criar um DataFrame com os dados fornecidos e as mesmas colunas do modelo
        dados_usuario_df = pd.DataFrame([dados_usuario], columns=column_names)

        # Fazer a previsão
        resultado = model.predict(dados_usuario_df)

        if resultado[0] == 0:
            print("O canal de vendas previsto é: HoReCa")
        else:
            print("O canal de vendas previsto é: Retail")
    
    except ValueError:
        print("Erro: Insira valores válidos para os dados.")


train_data = '../data/processed/Wholesale_train.csv'
test_data = '../data/processed/Wholesale_test.csv'

# Carregando e processando dados
train_data = load_data(train_data)
test_data = load_data(test_data)

# Treinando o modelo com o conjunto de treinamento e classificando amostras do conjunto de testes
model, column_names = evaluate_decision_tree(train_data, test_data)

# Classificando a entrada do usuário com base no modelo treinado
classify_user_input(model, column_names)
