import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title=Churn What-If Tool, layout=centered)

@st.cache_resource
def load_model()
    return joblib.load(tree_model.pkl)

model = load_model()

st.title(Churn What-If Tool)
st.write(Adjust the customer profile and inspect the predicted churn risk.)

total_trans_ct = st.slider(Total Transactions, 0, 150, 50)
total_trans_amt = st.slider(Total Transaction Amount, 0, 10000, 2000)
months_inactive = st.slider(Months Inactive (12 months), 0, 12, 2)
contacts_count = st.slider(Contacts Count (12 months), 0, 10, 2)
relationship_count = st.slider(Total Relationship Count, 1, 6, 3)

input_data = pd.DataFrame({
    Total_Trans_Ct [total_trans_ct],
    Total_Trans_Amt [total_trans_amt],
    Months_Inactive_12_mon [months_inactive],
    Contacts_Count_12_mon [contacts_count],
    Total_Relationship_Count [relationship_count]
})

prob = model.predict_proba(input_data)[0]
pred = model.predict(input_data)[0]
leaf = model.apply(input_data)[0]

st.subheader(Prediction)
st.write(fProbability of No Churn {prob[0].2%})
st.write(fProbability of Churn {prob[1].2%})
st.write(fLeaf  Segment {leaf})

if pred == 1
    st.error(Predicted class Churn)
else
    st.success(Predicted class No Churn)

with st.expander(Input data)
    st.dataframe(input_data, use_container_width=True)