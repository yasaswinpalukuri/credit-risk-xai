# Day 06 – 2025-06-15

## ✅ Tasks Completed
- Implemented SHAP explainability for:
  - Logistic Regression (`logistic_model_tuned.pkl`)
  - Decision Tree (`tree_model_tuned.pkl`)
- Generated and saved:
  - Global feature importance (SHAP beeswarm)
  - Local explanation (SHAP waterfall for 1 instance)
- Used `shap.Explainer(...)` with model.predict for tree model
- Saved all visualizations to `/models/` directory

---

## 🐞 Errors Faced & Resolutions

### ❌ Issue 1: `FileNotFoundError` for relative paths
- `data/processed/...` and `models/...` failed in notebook
- ✅ Resolved by prefixing paths with `"../"` when accessing from `notebooks/`

---

### ❌ Issue 2: `shap_values.shape != X.shape`
- Occurred during use of classic `.shap_values()` from `TreeExplainer`
- SHAP added extra column (likely bias or padding) → caused shape mismatch

### ❌ Issue 3: Even after slicing with `[:, :-1]` or aligning with `X.shape[1]`, SHAP summary still failed
- Because model was likely a `Pipeline` or contained preprocessing
- SHAP could not align values with raw `X`

---

### ✅ Final Fix:
- Used **modern `shap.Explainer(model.predict, X)` API**
- This wraps the model safely (even pipelines)
- Produces a clean `shap.Explanation` object
- Resolved all shape issues
- Both `summary_plot` and `waterfall` now render properly

---

## 📁 Outputs Saved to `/models/`
- `shap_beeswarm_logreg.png`
- `shap_waterfall_logreg_sample0.png`
- `shap_beeswarm_tree.png`
- `shap_waterfall_tree_sample0.png`

---

## 📚 Concepts Learned
- SHAP needs `X` shape to match SHAP value matrix
- Tree models often need slicing or `model.predict` for stable results
- SHAP’s modern `Explainer` class avoids many legacy errors

---

## 🔜 Tomorrow's Plan: Day 07 – Streamlit Dashboard
- Build frontend for scoring interface
- Upload CSV + get predictions
- Show SHAP explanations for customer predictions
- Visual model comparison (LogReg vs Tree)
- Deploy locally