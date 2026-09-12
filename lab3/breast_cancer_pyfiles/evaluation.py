import pandas as pd
from sklearn.metrics import confusion_matrix


def get_probabilities(model, X_test):
    return model.predict_proba(X_test)


def build_results_frame(Y_test, probab):
    results = pd.DataFrame({
        "Actual_class": Y_test.values,
        "P_malignant": probab[:, 0],
        "P_benign": probab[:, 1]
    })
    return results


def add_prediction_at_threshold(results, threshold=0.50):

    results["Predicted_malignant"] = (
        results["P_malignant"] >= threshold
    ).astype(int)

    results["predicted_label"] = results["Predicted_malignant"].map({
        1: "Malignant",
        0: "Benign"
    })
    return results


def count_predicted_malignant(results, thresholds=(0.3, 0.5, 0.7)):
    for threshold in thresholds:
        predictions = (results["P_malignant"] >= threshold).astype(int)
        print(
            f"threshold = {threshold} "
            f"malignant= {predictions.sum()}"
        )


def evaluate_thresholds(Y_test, results, thresholds=(0.1, 0.3, 0.5, 0.7, 0.9)):

    actual_malignant = (Y_test.values == 0).astype(int)
    metric_results = []

    for threshold in thresholds:
        predicted_malignant = (results["P_malignant"] >= threshold).astype(int)

        print("\n")
        cm = confusion_matrix(actual_malignant, predicted_malignant, labels=[1, 0])
        print("threshold==", threshold)
        print(cm)

        tp = cm[0, 0]
        fn = cm[0, 1]
        fp = cm[1, 0]
        tn = cm[1, 1]

        accuracy = (tp + tn) / (tp + tn + fp + fn)
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1_score = (
            2 * (precision * sensitivity) / (precision + sensitivity)
            if (precision + sensitivity) > 0 else 0
        )
        specificity = tn / (tn + fp) if (tn + fp) > 0 else 0

        metric_results.append({
            "Threshold": threshold,
            "TP": tp,
            "FP": fp,
            "FN": fn,
            "TN": tn,
            "Accuracy": accuracy,
            "Precision": precision,
            "sensitivity": sensitivity,
            "F1_Score": f1_score,
            "Specificity": specificity
        })

    metrics_df = pd.DataFrame(metric_results)
    return metrics_df
