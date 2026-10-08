import streamlit as st

name = st.text_input("What is your first name?")

if name:
    st.title(f"Welcome to {name}'s Tip Calculator")

    total_bill = st.number_input(
        "What is the total bill? ($)", min_value=0.0, step=1.0, format="%.2f"
    )
    tip_percentage = st.selectbox(
        "What percentage tip would you like to give?", [10, 12, 15]
    )
    number_of_people = st.number_input(
        "How many people are splitting the bill?", min_value=1, step=1
    )

    if st.button("Calculate"):
        bill_with_tip = total_bill * (1 + tip_percentage / 100)
        amount_per_person = bill_with_tip / number_of_people
        st.success(f"Each person should pay: ${amount_per_person:.2f}")
