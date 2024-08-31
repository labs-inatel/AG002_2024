import pandas as pd


def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print('Dados carregados com sucesso!')
        return data
    except FileNotFoundError:
        print(f'Erro: O arquivo {file_path} não foi encontrado.')
    except Exception as e:
        print(f'Erro inesperado: {e}')


file_path = '../../data/raw/wholesale.csv'

# Carregando os dados
data = load_data(file_path)

# Verificando se os dados foram carregados com sucesso
if data is not None:
    print(data.head())
