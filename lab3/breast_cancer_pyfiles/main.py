import data_loader
import plotting
import preprocessing
import training
import evaluation


def main():
    # 1. Load data
    x, y, data = data_loader.load_data()
    print(x.head())
    print(x.columns)
    data_loader.describe_data(x, y, data)

    class_distribution = data_loader.get_class_distribution(y, data)
    print(class_distribution)

    # 2. Plot class distribution
    plotting.plot_class_distribution(class_distribution)

    # 3. Train/test split
    X_train, X_test, Y_train, Y_test = preprocessing.split_data(x, y)
    preprocessing.describe_split(Y_train, Y_test)

    # 4. Build and train model
    model = training.build_model()
    model = training.train_model(model, X_train, Y_train)

    # 5. Predict probabilities
    probab = evaluation.get_probabilities(model, X_test)
    print(probab[:5])
    print(probab[:5].sum(axis=1))

    # 6. Build results frame and apply a single threshold
    results = evaluation.build_results_frame(Y_test, probab)
    print(results.head(10))

    results = evaluation.add_prediction_at_threshold(results, threshold=0.50)
    print(results[["Actual_class", "P_malignant", "predicted_label"]])

    # 7. Compare malignant counts across thresholds
    evaluation.count_predicted_malignant(results, thresholds=[0.3, 0.5, 0.7])

    # 8. Full metric sweep across thresholds
    metrics_df = evaluation.evaluate_thresholds(
        Y_test, results, thresholds=[0.1, 0.3, 0.5, 0.7, 0.9]
    )
    print(metrics_df.round(4))

    # Optional: visualize metrics vs threshold
    plotting.plot_metric_curve(metrics_df)
    print("Done")


if __name__ == "__main__":
    main()
