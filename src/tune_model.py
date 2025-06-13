import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, roc_curve, confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import joblib
import os

# Load the data
df = pd.read_csv("data/processed/credit_data_with_risk.csv")
df['Risk'] = df['Risk'].map({'Good': 0, 'Bad': 1})

# Encode categorical variables
cat_cols = ['Saving accounts', 'Checking account', 'Housing', 'Purpose']
le = LabelEncoder()
for col in cat_cols:
    df[col] = le.fit_transform(df[col])

# Feature selection
features = cat_cols + ['Age', 'Credit amount', 'Duration']
X = df[features]
y = df['Risk']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# GridSearchCV for Logistic Regression
params_lr = {
    'C': [0.01, 0.1, 1, 10],
    'penalty': ['l2'],
    'solver': ['liblinear']
}
lr = LogisticRegression()
grid_lr = GridSearchCV(lr, params_lr, cv=5, scoring='roc_auc')
grid_lr.fit(X_train, y_train)
best_lr = grid_lr.best_estimator_
print("Best Logistic Regression Params:", grid_lr.best_params_)

# Evaluate
y_pred = best_lr.predict(X_test)
y_proba = best_lr.predict_proba(X_test)[:, 1]

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("AUC:", roc_auc_score(y_test, y_proba))

# Save models folder if needed
os.makedirs("models", exist_ok=True)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title("Confusion Matrix - Logistic Regression")
plt.savefig("models/confusion_matrix_logreg.png")
plt.close()

# ROC Curve
fpr, tpr, _ = roc_curve(y_test, y_proba)
plt.plot(fpr, tpr, label='AUC = {:.2f}'.format(roc_auc_score(y_test, y_proba)))
plt.plot([0, 1], [0, 1], '--', color='gray')
plt.title("ROC Curve - Logistic Regression")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.savefig("models/roc_curve_logreg.png")
plt.close()

# Save tuned model
joblib.dump(best_lr, "models/logistic_model_tuned.pkl")