import streamlit as st
from datetime import date
import json

st.title("This is a simple demo application.")
name = st.text_input("Name")
sex = st.radio("Sex", ["Male", "Female"])
dob = st.date_input("Date of Birth", min_value=date(1920, 1, 1), max_value=date.today())

# Calculate age based on DOB
today = date.today()
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
age_display = st.text_input("Age", value=str(age), disabled=True)

# Address fields
street = st.text_input("Street Address")
city = st.text_input("City")
postcode = st.text_input("Postcode")

# Submit button
if st.button("Submit"):
    # Create a dictionary with all the form data
    form_data = {
        "name": name,
        "sex": sex,
        "date_of_birth": dob.strftime("%Y-%m-%d"),
        "age": age,
        "street_address": street,
        "city": city,
        "postcode": postcode
    }
    
    # Display the data as a JSON string
    st.subheader("Submitted Information:")
    st.json(form_data)



