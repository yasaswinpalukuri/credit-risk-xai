# Day 03 - 2025-06-12

## ✅ Tasks Done
- Loaded WoE-cleaned dataset from Day 02
- Selected high-value features (categorical + numeric)
- Encoded categorical columns using LabelEncoder
- Performed train-test split with stratification
- Trained two baseline models:
  - Logistic Regression
  - Decision Tree Classifier
- Evaluated models using classification report and AUC
- Saved trained models using `joblib` to `models/` directory
- Created an automated training script: `src/train.py`

## 🧠 Concepts Learned
- Importance of balancing target class in train-test split
- How to evaluate classifiers with precision, recall, F1, AUC
- Logistic Regression as a strong interpretable baseline
- Saving/loading models for reproducibility and deployment
- Python script automation for consistent model training

## ❓Doubts
- Should we apply SMOTE or class weights for imbalance?
- Should we one-hot encode categorical features for tree models?

## 🔁 Tomorrow’s Plan
- Perform hyperparameter tuning (GridSearchCV)
- Add confusion matrix + ROC curve plots
- Possibly compare with Random Forest or LightGBM
- Update README with model results
