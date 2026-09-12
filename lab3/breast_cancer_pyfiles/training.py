

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


def build_model(max_iter=1000):

    model = make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=max_iter)
    )
    return model


def train_model(model, X_train, Y_train):
   
    model.fit(X_train, Y_train)
    return model
