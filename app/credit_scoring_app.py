import streamlit as st
import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt
from PIL import Image

# --- Load model ---
model = joblib.load("models/logistic_model_tuned.pkl")

# --- Streamlit App ---
st.title("💳 Credit Risk Scoring App")

# --- Input Section ---
st.header("📥 Enter Applicant Details")
st.set_page_config(page_title="Credit Risk Scorer", layout="wide")
st.title("💳 Credit Risk Prediction with Explainable AI")
st.markdown("An ML-powered Streamlit app to assess loan risk with full interpretability.")

saving = st.selectbox("Saving Accounts", ['little', 'moderate', 'rich', 'quite rich'])
checking = st.selectbox("Checking Account", ['none', 'little', 'moderate', 'rich'])
housing = st.selectbox("Housing", ['own', 'free', 'rent'])
purpose = st.selectbox("Purpose", ['car', 'furniture', 'radio/TV', 'education', 'business', 'other'])
age = st.slider("Age", 18, 75, 30)
credit_amount = st.number_input("Credit Amount", 100, 20000, 1000)
duration = st.slider("Duration (Months)", 6, 72, 12)

# --- Encode manually ---
input_data = pd.DataFrame({
    'Saving accounts': [saving],
    'Checking account': [checking],
    'Housing': [housing],
    'Purpose': [purpose],
    'Age': [age],
    'Credit amount': [credit_amount],
    'Duration': [duration]
})

# Simple encoding map (matches training logic)
label_map = {
    'Saving accounts': ['little', 'moderate', 'rich', 'quite rich'],
    'Checking account': ['none', 'little', 'moderate', 'rich'],
    'Housing': ['own', 'free', 'rent'],
    'Purpose': ['car', 'furniture', 'radio/TV', 'education', 'business', 'other']
}
for col in label_map:
    input_data[col] = input_data[col].apply(lambda x: label_map[col].index(x))

# --- Predict ---
if st.button("🔍 Predict Risk"):
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]
    st.subheader("📊 Prediction Result")
    st.success(f"Risk: {'Bad' if prediction == 1 else 'Good'} ({proba:.2%} probability)")

    # --- SHAP Explanation ---
    st.subheader("📈 Explanation (SHAP)")
    explainer = shap.Explainer(model.predict, input_data)
    shap_values = explainer(input_data)

    fig = plt.figure()
    shap.plots.waterfall(shap_values[0], show=False)
    st.pyplot(fig)

# --- SHAP Global Visualization ---
st.markdown("---")
st.subheader("🌍 SHAP Global Interpretability")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Top Feature Impact (Global)**")
    shap_summary = Image.open("models/shap_summary_tree.png")
    st.image(shap_summary, use_column_width=True)

with col2:
    st.markdown("**Local Explanation: Sample 0**")
    shap_local = Image.open("models/shap_waterfall_tree_sample0.png")
    st.image(shap_local, use_column_width=True)

st.caption("🔎 SHAP helps explain how each feature pushes predictions toward Good or Bad credit decisions.")