import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import FunctionTransformer, StandardScaler, OneHotEncoder

# Define drop functionality
def drop_columns(df, columns_to_drop=['id']):
    return df.drop(columns=columns_to_drop, axis=1)

# Define individual feature engineering functions
def add_pulse_pressure(df):
    df['pulse_pressure'] = df['ap_hi'] - df['ap_lo']
    return df

def add_mean_arterial_pressure(df):
    df['map'] = df['ap_lo'] + (df['ap_hi'] - df['ap_lo']) / 3
    return df

def add_pulse_map_interaction(df):
    df['pulse_map_interaction'] = df['pulse_pressure'] * df['map']
    return df

def add_glucose_chol_interaction(df):
    df['gluc_chol'] = df['gluc'] * df['cholesterol']
    return df

def add_bp_chol_interaction(df):
    df['bp_chol'] = (df['ap_hi'] + df['ap_lo']) * df['cholesterol']
    return df

def add_bmi(df):
    df['bmi'] = df['weight'] / ((df['height'] / 100) ** 2)
    return df

def add_age_bmi_interaction(df):
    df['age_bmi_interaction'] = df['age'] * df['bmi']
    return df

# Custom transformer to output a DataFrame with updated column names
class DataFrameTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, column_transformer, scaling_cols, encoding_cols):
        self.column_transformer = column_transformer
        self.scaling_cols = scaling_cols
        self.encoding_cols = encoding_cols

    def fit(self, X, y=None):
        self.column_transformer.fit(X)
        return self

    def transform(self, X):
        # Transform data using the ColumnTransformer
        transformed_array = self.column_transformer.transform(X)

        # Get feature names for numeric and categorical columns
        num_feature_names = self.column_transformer.named_transformers_['num'].get_feature_names_out()
        cat_feature_names = self.column_transformer.named_transformers_['cat'].get_feature_names_out()

        # Combine feature names
        feature_names = list(num_feature_names) + list(cat_feature_names)

        # Return a DataFrame with updated column names
        return pd.DataFrame(transformed_array, columns=feature_names, index=X.index)

# Function to create the final pipeline
def cardio_data_pipeline():
    # lists for numerical and categorical columns
    scaling_num_cols = ['age', 'height', 'weight', 'ap_hi', 'ap_lo', 
                'pulse_pressure', 'map', 'pulse_map_interaction', 'gluc_chol', 
                'bp_chol', 'bmi', 'age_bmi_interaction']

    encoding_cat_cols = ['gender', 'cholesterol', 'gluc', 'smoke', 'alco', 'active']
    unwanted_cols = ['id'] # unwanted columns to be dropped

    # Create the column transformer
    column_transformer = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), scaling_num_cols),
            ('cat', OneHotEncoder(), encoding_cat_cols)
        ]
    )

    # Define preprocessing pipeline
    preprocessing_pipeline = Pipeline(steps=[
        ('drop_columns', FunctionTransformer(drop_columns, kw_args={'columns_to_drop': unwanted_cols})),
        ('cleaning', FunctionTransformer(lambda df: df.dropna())),
        ('feature_engineering', Pipeline([
            ('pulse_pressure', FunctionTransformer(add_pulse_pressure)),
            ('mean_arterial_pressure', FunctionTransformer(add_mean_arterial_pressure)),
            ('pulse_map_interaction', FunctionTransformer(add_pulse_map_interaction)),
            ('glucose_chol_interaction', FunctionTransformer(add_glucose_chol_interaction)),
            ('bp_chol_interaction', FunctionTransformer(add_bp_chol_interaction)),
            ('bmi', FunctionTransformer(add_bmi)),
            ('age_bmi_interaction', FunctionTransformer(add_age_bmi_interaction))
        ]))
    ])

    # Create final pipeline
    final_pipeline = Pipeline(steps=[
        ('preprocessing', preprocessing_pipeline),
        ('dataframe_transformer', DataFrameTransformer(
            column_transformer=column_transformer,
            scaling_cols=scaling_num_cols,
            encoding_cols=encoding_cat_cols
        ))
    ])

    return final_pipeline

# Test usage
if __name__ == "__main__":
    # load the dataset
    from cardiovascular_disease_prediction.dataset import load_dataset
    df = load_dataset()
    
    try:
        pipeline = cardio_data_pipeline()
        transformed_df = pipeline.fit_transform(df)
        print("Transformation successful!")
        print(f"Transformed DataFrame shape: {transformed_df.shape}")
    except Exception as e:
        print(f"Error in pipeline transformation: {e}")
        print(f"DataFrame shape: {df.shape}")
        print(f"DataFrame columns: {df.columns}")
        

