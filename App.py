import streamlit as st
import pandas as pd
import sklearn
import pickle


print(f"Streamlit version: {st.__version__}")
print(f"Pandas version: {pd.__version__}")
print(f"Scikit-learn version: {sklearn.__version__}")

# Load trained pipeline
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Page config
st.set_page_config(
    page_title='Diabetes Detection',
    page_icon='🩺',
    layout='centered'
)

# Title
st.title('🩺 Diabetes Detection App')
st.write('Enter patient details below to predict diabetes risk.')

# Input fields
pregnancies = st.number_input('Pregnancies', min_value=0, step=1)
glucose = st.number_input('Glucose', min_value=0)
blood_pressure = st.number_input('Blood Pressure', min_value=0)
skin_thickness = st.number_input('Skin Thickness', min_value=0)
insulin = st.number_input('Insulin', min_value=0)
bmi = st.number_input('BMI', min_value=0.0, format='%.2f')
dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, format='%.3f')
age = st.number_input('Age', min_value=1, step=1)

# Prediction button
if st.button('Predict'):
    input_df = pd.DataFrame({
        'Pregnancies': [pregnancies],
        'Glucose': [glucose],
        'BloodPressure': [blood_pressure],
        'SkinThickness': [skin_thickness],
        'Insulin': [insulin],
        'BMI': [bmi],
        'DiabetesPedigreeFunction': [dpf],
        'Age': [age]
    })

    prediction = pipe.predict(input_df)[0]

    if prediction == 1:
        st.error("⚠️ High Risk of Diabetes Detected")
        st.write("Please consult a healthcare professional.")
    else:
        st.success("✅ Low Risk of Diabetes")
        st.write("Your health indicators look normal.")


