import argparse
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from mlflow.models import infer_signature

def main(args):
    # MLFlow 설정
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment("creditcard_experiment")

    # 데이터 로드
    df = pd.read_csv("./data/creditcard.csv")

    X = df.drop(columns="Class")
    y = df["Class"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 데이터 전처리
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Logistic Regression 실험
    with mlflow.start_run(run_name="LogisticRegression"):
        model = LogisticRegression(max_iter=args.max_iter)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        acc = accuracy_score(y_test, preds)
        prec = precision_score(y_test, preds)
        rec = recall_score(y_test, preds)

        mlflow.log_param("model", "LogisticRegression")
        mlflow.log_param("max_iter", args.max_iter)
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("precision", prec)
        mlflow.log_metric("recall", rec)

        signature = infer_signature(X_train, preds)
        mlflow.sklearn.log_model(model, "model", signature=signature)

    # Random Forest 실험
    with mlflow.start_run(run_name="RandomForest"):
        model = RandomForestClassifier(n_estimators=args.n_estimators)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        acc = accuracy_score(y_test, preds)
        prec = precision_score(y_test, preds)
        rec = recall_score(y_test, preds)

        mlflow.log_param("model", "RandomForest")
        mlflow.log_param("n_estimators", args.n_estimators)
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("precision", prec)
        mlflow.log_metric("recall", rec)

        signature = infer_signature(X_train, preds)
        mlflow.sklearn.log_model(model, "model", signature=signature)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max_iter", type=int, default=1000)
    parser.add_argument("--n_estimators", type=int, default=100)
    args = parser.parse_args()

    main(args)
