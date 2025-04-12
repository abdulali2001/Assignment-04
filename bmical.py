# BMI Calculator
import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="😊", layout="centered")

st.title("Project8: BMI Calculator In Python")
st.markdown("""
## Apna Body Mass Index (BMI) calculate karein. Neeche apna **weight aur height** enter karein.
""")

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight (kg):", min_value=1.0, format="%.2f")
with col2:
    height_m = st.number_input("Height (m):", min_value=0.1, format="%.2f")  # Height in meters now

if height_m > 0 and weight > 0:
    bmi = weight / (height_m ** 2) #bmi formula

    st.subheader("Aapka BMI hai:")
    st.markdown(f"**{bmi:.2f}**", unsafe_allow_html=True)

    if bmi < 18.5:
        st.error("underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("normal weight")
    elif 25 <= bmi < 29.9:
        st.warning("overweight")
    else:
        st.error("Obsity🚨")
else:
    st.info("please enter a valid weight and height")
