from train_model import load_data, evaluate_decision_tree, test_model_predictions

if __name__ == "__main__":
    train_data_path = '../data/processed/Wholesale_train.csv'
    test_data_path = '../data/processed/Wholesale_test.csv'

    train_data = load_data(train_data_path)
    test_data = load_data(test_data_path)
    
    model, column_names = evaluate_decision_tree(train_data, test_data)

    test_data_samples = [
        [2, 6353, 8808, 7684, 2405, 3516, 7844],  # Retail
        [2, 13265, 1196, 4221, 6404, 507, 1788],  # HoReCa
    ]
    
    expected_results = [0, 1]  # 0 = HoReCa, 1 = Retail

    test_model_predictions(model, column_names, test_data_samples, expected_results)
