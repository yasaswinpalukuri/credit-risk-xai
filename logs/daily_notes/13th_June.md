# Day 04 - 2025-06-13

## ✅ Tasks Done
- Created a new script `src/tune_model.py` for automated model tuning and evaluation
- Applied GridSearchCV to tune hyperparameters for Logistic Regression
- Evaluated the best model using:
  - Classification report
  - AUC score
  - Confusion Matrix (saved as PNG)
  - ROC Curve (saved as PNG)
- Saved the tuned model as `logistic_model_tuned.pkl` inside the `models/` directory

## 🧠 Concepts Learned
- How to use GridSearchCV to optimize model performance
- Why AUC is a better metric than accuracy for imbalanced classification
- How to visually assess performance using confusion matrix and ROC curve
- Saving model artifacts and visualizations for deployment or presentation

## ❓Doubts
- Should we tune Decision Tree or use ensemble models next?
- Should we compare LightGBM or Random Forest performance?

## 🔁 Tomorrow’s Plan
- Tune Decision Tree (or optionally Random Forest)
- Compare all model metrics side by side
- Start designing Streamlit app or scoring API (FastAPI)
