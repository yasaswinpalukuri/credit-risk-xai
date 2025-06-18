# Day 05 - 2025-06-13 (Part 2)

## ✅ Tasks Done
- Rewrote all code to consistently save model outputs to the correct root-level `models/` directory
- Tuned Decision Tree with GridSearchCV
- Evaluated Decision Tree model:
  - AUC score
  - Classification report
  - Confusion matrix (saved as PNG)
  - ROC curve (saved as PNG)
- Compared ROC curves between Logistic Regression and Decision Tree
- Saved all plots and best model artifacts to `/models/`
- Verified file structure and committed clean output

## 🧠 Concepts Learned
- How to avoid path issues in notebooks by using `os.path.join`
- Importance of organizing saved artifacts for deployment or presentation
- How to compare classifiers visually using AUC and ROC

## 🔁 Tomorrow’s Plan
- Add SHAP explainability for Logistic Regression & Decision Tree
- Begin building Streamlit app for credit scoring interface
- Update README.md with visuals and model summary table