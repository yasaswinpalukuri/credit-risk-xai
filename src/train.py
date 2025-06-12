import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, roc_auc_score
import joblib
import os

# Load the data
df = pd.read_csv("data/processed/credit_data_with_risk.csv")
df['Risk'] = df['Risk'].map({'Good': 0, 'Bad': 1})

# Encode categorical features
cat_cols = ['Saving accounts', 'Checking account', 'Housing', 'Purpose']
le = LabelEncoder()
for col in cat_cols:
    df[col] = le.fit_transform(df[col])

# Feature selection
features = cat_cols + ['Age', 'Credit amount', 'Duration']
X = df[features]
y = df['Risk']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Train models
lr = LogisticRegression()
dt = DecisionTreeClassifier()

lr.fit(X_train, y_train)
dt.fit(X_train, y_train)

# Evaluate models
print("Logistic Regression:")
print(classification_report(y_test, lr.predict(X_test)))
print("AUC:", roc_auc_score(y_test, lr.predict_proba(X_test)[:, 1]))

print("\nDecision Tree:")
print(classification_report(y_test, dt.predict(X_test)))
print("AUC:", roc_auc_score(y_test, dt.predict_proba(X_test)[:, 1]))

# Save models
os.makedirs("models", exist_ok=True)
joblib.dump(lr, "models/logistic_model.pkl")
joblib.dump(dt, "models/tree_model.pkl")
