import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

def load_data(dataset):
    try:
        data = pd.read_csv(dataset)
        print('Dados carregados com sucesso!')

        if data.isnull().sum().any():
            print("Há valores ausentes nos dados. Realizando preenchimento...")
            data_preprocessed = data.dropna()
        return data_preprocessed

    except FileNotFoundError:
        print(f'Erro: O arquivo {dataset} não foi encontrado.')
    except Exception as e:
        print(f'Erro inesperado: {e}')

def evaluate_decision_tree(train_data, test_data):
    X_train = train_data.drop('Channel', axis=1)
    y_train = train_data['Channel']
    X_test = test_data.drop('Channel', axis=1)
    y_test = test_data['Channel']

    model = DecisionTreeClassifier(random_state=42, max_depth=5, min_samples_leaf=10, class_weight='balanced')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("Relatório de classificação para Decision Tree:")
    print(classification_report(y_test, y_pred))

    return model, X_train.columns

def classify_user_input(model, column_names):
    try:
        dados_usuario = []
        for column in column_names:
            dado = float(input(f"Insira o valor para {column}: "))
            dados_usuario.append(dado)

        dados_usuario_df = pd.DataFrame([dados_usuario], columns=column_names)
        resultado = model.predict(dados_usuario_df)

        if resultado[0] == 0:
            print("O canal de vendas previsto é: HoReCa")
        else:
            print("O canal de vendas previsto é: Retail")

    except ValueError:
        print("Erro: Insira valores válidos para os dados.")

def test_model_predictions(model, column_names, test_data, expected_results):
    test_df = pd.DataFrame(test_data, columns=column_names)
    predictions = model.predict(test_df)

    for i, (prediction, expected) in enumerate(zip(predictions, expected_results)):
        prediction_label = "HoReCa" if prediction == 0 else "Retail"
        expected_label = "HoReCa" if expected == 0 else "Retail"

        print(f"Teste {i + 1}:")
        print(f"  Dados de Entrada: {test_data[i]}")
        print(f"  Previsão do Modelo: {prediction_label}")
        print(f"  Resultado Esperado: {expected_label}")
        print(f"  Teste {'Passou' if prediction == expected else 'Falhou'}\n")
