import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, roc_auc_score

def plot_evaluation_metrics(model, X_test, y_true, model_name):
    """
    Plot evaluation metrics for the model.
        Confusion Matrix Heatmap
        ROC Curve
        Feature Importance Bar Plot
    """
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None

    fig, axes = plt.subplots(1, 3, figsize=(20, 6))
    fig.suptitle(f'{model_name} Evaluation Metrics', fontsize=16)
    
    # Confusion Matrix
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0])
    axes[0].set_title('Confusion Matrix')
    axes[0].set_xlabel('Predicted')
    axes[0].set_ylabel('True')
    axes[0].set_xticklabels(['No Disease', 'Disease'])
    axes[0].set_yticklabels(['No Disease', 'Disease'])
    
    # ROC Curve
    fpr, tpr, thresholds = roc_curve(y_true, y_pred)
    roc_auc = roc_auc_score(y_true, y_proba) if y_proba is not None else None
    if roc_auc is not None:
        axes[1].plot(fpr, tpr, color='blue', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
        axes[1].plot([0, 1], [0, 1], color='red', lw=2, linestyle='--')
        axes[1].set_title('Receiver Operating Characteristic (ROC) Curve')
        axes[1].set_xlabel('False Positive Rate')
        axes[1].set_ylabel('True Positive Rate')
        axes[1].legend(loc='lower right')
        axes[1].set_xlim([0.0, 1.0])
        axes[1].set_ylim([0.0, 1.05])
    else:
        print('ROC Curve not available for this model.')
    
    # ---- Feature Importances ----
    if hasattr(model, "feature_importances_"):  # Tree-based models
        importances = model.feature_importances_
    elif hasattr(model, "coef_"):  # Linear models
        importances = np.abs(model.coef_[0])  # Take absolute value
    else:
        importances = None  # Skip for models without feature importance

    if importances is not None:
        ax = axes[2]
        feature_importance_df = (
            pd.DataFrame({"Feature": model.feature_names_in_, "Importance": importances})
            .sort_values(by="Importance", ascending=False)
            .head(10)  # Show top 10 features
        )
        sns.barplot(
            x="Importance", y="Feature", data=feature_importance_df, palette="viridis", hue='Feature', ax=ax
        )
        ax.set_title(f"{model_name} - Feature Importances")
        ax.set_xlabel("Importance")
        ax.set_ylabel("Feature")
    
    plt.tight_layout()
    plt.show()

