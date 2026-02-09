import streamlit as st
from prediction_helper import predict  # Ensure this is correctly linked to your prediction_helper.py


st.set_page_config(
    page_title="Credit Predict: Loan Default Risk",
    page_icon="💳",
    layout="wide"
)


st.markdown("""
    <style>
    .main-title {
        font-size: 38px;
        font-weight: 800;
        color: #ffffff;
        padding: 12px 18px;
        border-radius: 12px;
        background: linear-gradient(90deg, #1f2937, #111827);
        text-align: center;
        margin-bottom: 25px;
    }

    .sub-text {
        font-size: 16px;
        color: #9ca3af;
        text-align: center;
        margin-top: -15px;
        margin-bottom: 25px;
    }

    .result-box {
        padding: 18px;
        border-radius: 14px;
        background: #0f172a;
        border: 1px solid #1e293b;
        margin-top: 15px;
    }

    .result-title {
        font-size: 22px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 10px;
    }

    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">💳 Credit Predict — Loan Default Risk Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Enter customer loan details to calculate default probability, credit score, and risk rating.</div>', unsafe_allow_html=True)


row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)


with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=18)

with row1[1]:
    income = st.number_input('Income', min_value=0, value=0)

with row1[2]:
    loan_amount = st.number_input('Loan Amount', min_value=0, value=0)

loan_to_income_ratio = loan_amount / income if income > 0 else 0
with row2[0]:
    st.text("Loan to Income Ratio:")
    st.text(f"{loan_to_income_ratio:.2f}")

with row2[1]:
    loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=0, step=1, value=36)

with row2[2]:
    avg_dpd_per_delinquency = st.number_input('Avg DPD', min_value=0, value=20)

with row3[0]:
    delinquency_ratio = st.number_input('Delinquency Ratio', min_value=0, max_value=100, step=1, value=30)

with row3[1]:
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio', min_value=0, max_value=100, step=1, value=30)

with row3[2]:
    num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)

with row4[0]:
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])

with row4[1]:
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])

with row4[2]:
    loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])


st.markdown("---")

if st.button('📌 Calculate Credit Risk'):
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )


    st.markdown(f"""
        <div class="result-box">
            <div class="result-title">📊 Risk Prediction Results</div>
            <h4>✅ Default Probability: <b>{probability:.2%}</b></h4>
            <h4>💳 Credit Score: <b>{credit_score}</b></h4>
            <h4>⭐ Rating: <b>{rating}</b></h4>
        </div>
    """, unsafe_allow_html=True)
