from datetime import date
import calendar
import streamlit as st

dob = st.date_input("enter your date of birth:",value=date(2000,6,22),
                    min_value=date(1930,6,22),
                    max_value=date.today())

if st.button("age calculate:"):
    today = date.today()

    age = today.year - dob.year

    if (today.month, today.day)<(dob.month,dob.day):
        age -=1

    st.success(f"your age is {age}")
