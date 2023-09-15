import pickle 
import streamlit as st 
import numpy as np 
loaded_model = pickle.load(open("C:/Users/pbesw/Downloads/credit_card_fraud_lgbm.sav","rb"))

def ccf(input):
    input_as = np.asarray(input)
    main_input = input_as.reshape(1,-1)
    prediction = loaded_model.predict(main_input)
    return prediction[0]
def main():
    st.title("Fraud Prediction")
    col1,col2,col3,col4, = st.columns([7,7,7,7])
    col5, col6 = st.columns([1,1])
    with col1:
        V_1   = st.number_input("V1")
        V5   = st.number_input("V5")
        V9   = st.number_input("V9")
        V13   = st.number_input("V13")
        V17   = st.number_input("V17")
        V21   = st.number_input("V21")
        V25   = st.number_input("V25")
    with col2:
        V2   = st.number_input("V2")
        V6   = st.number_input("V6")
        V10   = st.number_input("V10")
        V14   = st.number_input("V14")
        V18   = st.number_input("V18")
        V22   = st.number_input("V22")
        V26   = st.number_input("V26")
    with col3:
        V3   = st.number_input("V3")
        V7   = st.number_input("V7")
        V11   = st.number_input("V11")
        V15   = st.number_input("V15")
        V19   = st.number_input("V19")
        V23   = st.number_input("V23")
        V27   = st.number_input("V27")
    with col4:
        V4   = st.number_input("V4")
        V8   = st.number_input("V8")
        V12   = st.number_input("V12")
        V16   = st.number_input("V16")
        V20   = st.number_input("V20")
        V24   = st.number_input("V24")
        V28   = st.number_input("V28")
    Amount  = st.number_input("Amount")
    Time = st.number_input("Time")

    Class = " "

    if st.button("Predict"):
        Class = ccf([Time,V_1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount])
    
    st.success(Class)

if __name__ == "__main__":
    main()

    
    