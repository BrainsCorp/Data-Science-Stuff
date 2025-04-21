
def train_model(X_train, y_train, model, params=None):
    """
    Train the given model using the provided training data.

    Args:
        X_train (pd.DataFrame): The training features.
        y_train (pd.Series): The training labels.
        model (sklearn.base.BaseEstimator): The model to train.
        params (dict, optional): Hyperparameters for the model. Defaults to None.

    Returns:
        sklearn.base.BaseEstimator: The trained model.
    """
    if params:
        model.set_params(**params)
    
    model.fit(X_train, y_train)
    
    return model