import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('Stroke.mdl')

def predict_stroke(gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status):
    # Convert categorical inputs to binary
    gender = 1 if gender == "Nam" else 0
    ever_married = 0 if ever_married == "Chưa" else 1
    hypertension = 0 if hypertension == "Không" else 1
    heart_disease = 0 if heart_disease == "Không" else 1
    work_type_mapping = {"Tư nhân": 2, "Tự làm": 3, "Nhà nước": 1, "Trẻ em": 4, "Chưa từng làm": 0}
    work_type = work_type_mapping[work_type]
    Residence_type = 1 if Residence_type == "Thành thị" else 0
    smoking_status_mapping = {"Không biết": 0, "Không bao giờ hút": 2, "Hút trước đây": 1, "Vẫn đang hút": 3}
    smoking_status = smoking_status_mapping[smoking_status]
    
    # Perform prediction
    new_patient = np.array([[gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status]])
    prediction = model.predict(new_patient)
    
    return prediction

def main():
    st.title("Ứng dụng dự đoán đột quỵ")

    # Input fields
    gender = st.selectbox('Giới tính', ["Nam", "Nữ"])
    age = st.number_input('Tuổi', value=50, min_value=0, max_value=150, step=1)
    hypertension = st.selectbox('Huyết áp cao', ["Không", "Có"])
    heart_disease = st.selectbox('Bệnh tim mạch', ["Không", "Có"])
    ever_married = st.selectbox('Tình trạng hôn nhân', ["Chưa", "Đã"])
    work_type = st.selectbox('Nghề nghiệp', ["Tư nhân", "Tự làm", "Nhà nước", "Trẻ em", "Chưa từng làm"])
    Residence_type = st.selectbox('Nơi cư trú', ["Thành thị", "Nông thôn"])
    avg_glucose_level = st.number_input('Đường huyết trung bình', value=100.0, min_value=0.0, max_value=300.0, step=0.1)
    bmi = st.number_input('Chỉ số BMI', value=25.0, min_value=0.0, max_value=100.0, step=0.1)
    smoking_status = st.selectbox('Tình trạng hút thuốc', ["Không biết", "Không bao giờ hút", "Hút trước đây", "Vẫn đang hút"])
    
    # Prediction button
    if st.button("Dự đoán"):
        result = predict_stroke(gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status)
        if result == 0:
            st.success("Bệnh nhân không bị đột quỵ!")
        else:
            st.success("Bệnh nhân có bị đột quỵ!")

if __name__ == '__main__':
    main()
