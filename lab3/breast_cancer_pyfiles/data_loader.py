import pandas as pd
from sklearn.datasets import load_breast_cancer


def load_data():
    data = load_breast_cancer()

    x = pd.DataFrame(data=data.data, columns=data.feature_names)
    y = pd.Series((data.target == 0).astype(int), name="malignant")

    return x, y, data


def describe_data(x, y, data):
    print("shape of data", x.shape)
    print("shape of target", y.shape)
    print(data.target_names)
    print(y.value_counts())


def get_class_distribution(y, data):

    class_counts = y.value_counts().sort_index()
    class_probabilities = y.value_counts(normalize=True).sort_index()

    class_distribution = pd.DataFrame({
        "Class": data.target_names,
        "Count": class_counts.values,
        "Probability": class_probabilities.values
    })

    return class_distribution
