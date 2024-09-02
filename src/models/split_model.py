import pandas as pd
from sklearn.model_selection import train_test_split


def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print('Dados carregados com sucesso!')
        return data
    except FileNotFoundError:
        print(f'Erro: O arquivo {file_path} não foi encontrado.')
    except Exception as e:
        print(f'Erro inesperado: {e}')


def split_data(df, test_size=0.2, random_state=42):
    X = df.drop('Channel', axis=1)
    y = df['Channel']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state)

    train_data = pd.concat([X_train, y_train.reset_index(drop=True)], axis=1)
    test_data = pd.concat([X_test, y_test.reset_index(drop=True)], axis=1)

    return train_data, test_data


def main():
    file_path = '../../data/processed/Wholesale_processed.csv'

    data = load_data(file_path)

    # Verificando se os dados foram carregados com sucesso
    if data is not None:
        train_data, test_data = split_data(data)

        train_data.to_csv(
            '../../data/processed/Wholesale_train.csv', index=False)
        test_data.to_csv(
            '../../data/processed/Wholesale_test.csv', index=False)

        print('Dados separados e salvos com sucesso!')


main()
