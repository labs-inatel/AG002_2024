import pandas as pd


# Convertendo os valores do conjunto de dados convertidos para números inteiros (Mapeamento)
def preprocess_data(df):
    df['Channel'] = df['Channel'].replace({'HoReCa': 0, 'Retail': 1})
    df['Region'] = df['Region'].replace({'Lisbon': 0, 'Oporto': 1, 'Other': 2})

    ordered_columns = ['Region', 'Fresh', 'Milk', 'Grocery',
                       'Frozen', 'Detergents_Paper', 'Delicatessen', 'Channel']
    df = df.reindex(columns=ordered_columns)

    return df


def processing_data():
    input_file_path = '../../data/raw/Wholesale.csv'
    output_file_path = '../../data/processed/Wholesale_processed.csv'

    # Carregando o arquivo
    try:
        data = pd.read_csv(input_file_path)
    except FileNotFoundError:
        return print(f"Erro: O arquivo '{input_file_path}' não foi encontrado.")
    except pd.errors.EmptyDataError:
        return print("Erro: O arquivo está vazio.")
    except pd.errors.ParserError:
        return print("Erro: Erro na leitura do arquivo.")

    # Preprocessando e salvando o conjunto de dados convertido
    data = preprocess_data(data)

    try:
        data.to_csv(output_file_path, index=False)
        print("Dados pré-processados com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")


processing_data()
