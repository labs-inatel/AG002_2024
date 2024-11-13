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


def preprocess_data(df):
    # convertendo para números inteiros
    df['Channel'] = df['Channel'].replace({'HoReCa': 0, 'Retail': 1})
    df['Region'] = df['Region'].replace({'Lisbon': 0, 'Oporto': 1, 'Other': 2})

    # reordenando as colunas
    ordered_columns = ['Region', 'Fresh', 'Milk', 'Grocery',
                       'Frozen', 'Detergents_Paper', 'Delicatessen', 'Channel']
    df = df.reindex(columns=ordered_columns)

    return df


def processing_data(input_data, output_data):
    try:
        data = load_data(input_data)
    except FileNotFoundError:
        return print(f"Erro: O arquivo '{input_file_path}' não foi encontrado.")
    except pd.errors.EmptyDataError:
        return print("Erro: O arquivo está vazio.")
    except pd.errors.ParserError:
        return print("Erro: Erro na leitura do arquivo.")

    # preprocessando e salvando o conjunto de dados convertido
    data = preprocess_data(data)

    try:
        data.to_csv(output_data, index=False)
        print("Dados pré-processados com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")


# carregando os dados
dataset = '../data/raw/Wholesale.csv'
input_data = load_data(dataset)

# leitura dos dados
print(input_data)

output_data = '../data/processed/Wholesale_preprocessed.csv'
processing_data(dataset,output_data)


