
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_ml_model(df: pd.DataFrame, label_column: str) -> dict:
    """
    Train a RandomForestClassifier on uploaded dataset and return evaluation metrics.
    """
    try:
        X = df.drop(columns=[label_column])
        y = df[label_column]
        X = pd.get_dummies(X)  # Basic encoding

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        clf = RandomForestClassifier(n_estimators=100, random_state=42)
        clf.fit(X_train, y_train)

        preds = clf.predict(X_test)
        report = classification_report(y_test, preds, output_dict=True)
        return report
    except Exception as e:
        return {"error": str(e)}
