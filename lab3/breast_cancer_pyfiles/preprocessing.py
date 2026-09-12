
from sklearn.model_selection import train_test_split


def split_data(x, y, test_size=0.2, random_state=42):

    X_train, X_test, Y_train, Y_test = train_test_split(
        x,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )
    return X_train, X_test, Y_train, Y_test


def describe_split(Y_train, Y_test):

    print("training size", len(Y_train))

    print("\n Training prop")
    print(Y_train.value_counts(normalize=True).sort_index())

    print("\n Test prop")
    print(Y_test.value_counts(normalize=True).sort_index())
