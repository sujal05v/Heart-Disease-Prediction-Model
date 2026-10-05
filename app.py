<<<<<<< HEAD
import streamlit as st
import pandas as pd
import joblib


# ============================================================
# 1. LOAD MODEL, SCALER AND COLUMNS
# ============================================================

model = joblib.load("Logistic_Regression.pkl")
scaler = joblib.load("Scaler.pkl")
expected_columns = joblib.load("columns.pkl")


# ============================================================
# 2. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)


# ============================================================
# 3. TITLE
# ============================================================

st.title("❤️ Heart Disease Prediction")

st.markdown(
    "### Enter the patient's details to predict the possibility of heart disease."
)

st.info(
    "This application is an ML-based prediction tool for educational purposes."
)


# ============================================================
# 4. PATIENT INFORMATION
# ============================================================

st.header("👤 Patient Information")


age = st.slider(
    "Age",
    min_value=18,
    max_value=100,
    value=40
)


sex = st.selectbox(
    "Sex",
    ["Male", "Female"]
)


# ============================================================
# 5. BASIC HEART INFORMATION
# ============================================================

st.header("🫀 Heart Information")


resting_bp = st.number_input(
    "Resting Blood Pressure (RestingBP)",
    min_value=50.0,
    max_value=250.0,
    value=120.0,
    step=1.0
)


cholesterol = st.number_input(
    "Cholesterol",
    min_value=0.0,
    max_value=700.0,
    value=200.0,
    step=1.0
)


fasting_bs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl?",
    ["No", "Yes"]
)


max_hr = st.number_input(
    "Maximum Heart Rate (MaxHR)",
    min_value=50.0,
    max_value=250.0,
    value=150.0,
    step=1.0
)


oldpeak = st.number_input(
    "Oldpeak",
    min_value=-5.0,
    max_value=10.0,
    value=0.0,
    step=0.1
)


# ============================================================
# 6. CHEST PAIN TYPE
# ============================================================

st.header("💓 Chest Pain")


chest_pain = st.selectbox(
    "Chest Pain Type",
    [
        "ASY",
        "ATA",
        "NAP",
        "TA"
    ]
)


# ============================================================
# 7. RESTING ECG
# ============================================================

st.header("📊 Resting ECG")


resting_ecg = st.selectbox(
    "Resting ECG",
    [
        "Normal",
        "ST",
        "LVH"
    ]
)


# ============================================================
# 8. EXERCISE ANGINA
# ============================================================

exercise_angina = st.selectbox(
    "Exercise Induced Angina",
    [
        "No",
        "Yes"
    ]
)


# ============================================================
# 9. ST SLOPE
# ============================================================

st.header("📈 ST Slope")


st_slope = st.selectbox(
    "ST Slope",
    [
        "Flat",
        "Up",
        "Down"
    ]
)


# ============================================================
# 10. PREDICTION BUTTON
# ============================================================

if st.button(
    "🔍 Predict Heart Disease",
    use_container_width=True
):

    # ========================================================
    # 11. CONVERT USER INPUT INTO MODEL FEATURES
    # ========================================================

    input_data = {

        "Age": age,

        "RestingBP": resting_bp,

        "Cholesterol": cholesterol,

        "FastingBS": 1 if fasting_bs == "Yes" else 0,

        "MaxHR": max_hr,

        "Oldpeak": oldpeak,

        # --------------------------
        # Sex
        # --------------------------

        "Sex_M": 1 if sex == "Male" else 0,

        # --------------------------
        # Chest Pain
        # --------------------------

        "ChestPainType_ATA":
            1 if chest_pain == "ATA" else 0,

        "ChestPainType_NAP":
            1 if chest_pain == "NAP" else 0,

        "ChestPainType_TA":
            1 if chest_pain == "TA" else 0,

        # --------------------------
        # Resting ECG
        # --------------------------

        "RestingECG_Normal":
            1 if resting_ecg == "Normal" else 0,

        "RestingECG_ST":
            1 if resting_ecg == "ST" else 0,

        # --------------------------
        # Exercise Angina
        # --------------------------

        "ExerciseAngina_Y":
            1 if exercise_angina == "Yes" else 0,

        # --------------------------
        # ST Slope
        # --------------------------

        "ST_Slope_Flat":
            1 if st_slope == "Flat" else 0,

        "ST_Slope_Up":
            1 if st_slope == "Up" else 0
    }


    # ========================================================
    # 12. CREATE DATAFRAME
    # ========================================================

    input_df = pd.DataFrame([input_data])


    # ========================================================
    # 13. MATCH EXACT TRAINING COLUMNS
    # ========================================================

    input_df = input_df.reindex(
        columns=expected_columns,
        fill_value=0
    )


    # ========================================================
    # 14. SCALE THE INPUT
    # ========================================================

    input_scaled = scaler.transform(input_df)


    # ========================================================
    # 15. MODEL PREDICTION
    # ========================================================

    prediction = model.predict(input_scaled)[0]


    # ========================================================
    # 16. PREDICTION PROBABILITY
    # ========================================================

    probability = model.predict_proba(input_scaled)[0][1]


    # ========================================================
    # 17. SHOW RESULT
    # ========================================================

    st.markdown("---")

    st.header("🔍 Prediction Result")


    if prediction == 1:

        st.error(
            "⚠️ Higher Possibility of Heart Disease"
        )

        st.metric(
            "Heart Disease Probability",
            f"{probability * 100:.2f}%"
        )

    else:

        st.success(
            "✅ Lower Possibility of Heart Disease"
        )

        st.metric(
            "Heart Disease Probability",
            f"{probability * 100:.2f}%"
        )


    # ========================================================
    # 18. DEBUG INFORMATION
    # ========================================================

    with st.expander("🔧 View Model Input"):

        st.write("Input Data Before Scaling:")

        st.dataframe(input_df)

        st.write("Expected Model Columns:")

        st.write(expected_columns)

        st.write("Raw Prediction:")

        st.write(prediction)

        st.write("Prediction Probability:")

        st.write(probability)


# ============================================================
# 19. DISCLAIMER
# ============================================================

st.markdown("---")

st.warning(
    "⚠️ This application is for educational and machine-learning "
    "demonstration purposes only. It is not a medical diagnosis."
=======
import streamlit as st
import pandas as pd
import joblib


# ============================================================
# 1. LOAD MODEL, SCALER AND COLUMNS
# ============================================================

model = joblib.load("Logistic_Regression.pkl")
scaler = joblib.load("Scaler.pkl")
expected_columns = joblib.load("columns.pkl")


# ============================================================
# 2. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)


# ============================================================
# 3. TITLE
# ============================================================

st.title("❤️ Heart Disease Prediction")

st.markdown(
    "### Enter the patient's details to predict the possibility of heart disease."
)

st.info(
    "This application is an ML-based prediction tool for educational purposes."
)


# ============================================================
# 4. PATIENT INFORMATION
# ============================================================

st.header("👤 Patient Information")


age = st.slider(
    "Age",
    min_value=18,
    max_value=100,
    value=40
)


sex = st.selectbox(
    "Sex",
    ["Male", "Female"]
)


# ============================================================
# 5. BASIC HEART INFORMATION
# ============================================================

st.header("🫀 Heart Information")


resting_bp = st.number_input(
    "Resting Blood Pressure (RestingBP)",
    min_value=50.0,
    max_value=250.0,
    value=120.0,
    step=1.0
)


cholesterol = st.number_input(
    "Cholesterol",
    min_value=0.0,
    max_value=700.0,
    value=200.0,
    step=1.0
)


fasting_bs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl?",
    ["No", "Yes"]
)


max_hr = st.number_input(
    "Maximum Heart Rate (MaxHR)",
    min_value=50.0,
    max_value=250.0,
    value=150.0,
    step=1.0
)


oldpeak = st.number_input(
    "Oldpeak",
    min_value=-5.0,
    max_value=10.0,
    value=0.0,
    step=0.1
)


# ============================================================
# 6. CHEST PAIN TYPE
# ============================================================

st.header("💓 Chest Pain")


chest_pain = st.selectbox(
    "Chest Pain Type",
    [
        "ASY",
        "ATA",
        "NAP",
        "TA"
    ]
)


# ============================================================
# 7. RESTING ECG
# ============================================================

st.header("📊 Resting ECG")


resting_ecg = st.selectbox(
    "Resting ECG",
    [
        "Normal",
        "ST",
        "LVH"
    ]
)


# ============================================================
# 8. EXERCISE ANGINA
# ============================================================

exercise_angina = st.selectbox(
    "Exercise Induced Angina",
    [
        "No",
        "Yes"
    ]
)


# ============================================================
# 9. ST SLOPE
# ============================================================

st.header("📈 ST Slope")


st_slope = st.selectbox(
    "ST Slope",
    [
        "Flat",
        "Up",
        "Down"
    ]
)


# ============================================================
# 10. PREDICTION BUTTON
# ============================================================

if st.button(
    "🔍 Predict Heart Disease",
    use_container_width=True
):

    # ========================================================
    # 11. CONVERT USER INPUT INTO MODEL FEATURES
    # ========================================================

    input_data = {

        "Age": age,

        "RestingBP": resting_bp,

        "Cholesterol": cholesterol,

        "FastingBS": 1 if fasting_bs == "Yes" else 0,

        "MaxHR": max_hr,

        "Oldpeak": oldpeak,

        # --------------------------
        # Sex
        # --------------------------

        "Sex_M": 1 if sex == "Male" else 0,

        # --------------------------
        # Chest Pain
        # --------------------------

        "ChestPainType_ATA":
            1 if chest_pain == "ATA" else 0,

        "ChestPainType_NAP":
            1 if chest_pain == "NAP" else 0,

        "ChestPainType_TA":
            1 if chest_pain == "TA" else 0,

        # --------------------------
        # Resting ECG
        # --------------------------

        "RestingECG_Normal":
            1 if resting_ecg == "Normal" else 0,

        "RestingECG_ST":
            1 if resting_ecg == "ST" else 0,

        # --------------------------
        # Exercise Angina
        # --------------------------

        "ExerciseAngina_Y":
            1 if exercise_angina == "Yes" else 0,

        # --------------------------
        # ST Slope
        # --------------------------

        "ST_Slope_Flat":
            1 if st_slope == "Flat" else 0,

        "ST_Slope_Up":
            1 if st_slope == "Up" else 0
    }


    # ========================================================
    # 12. CREATE DATAFRAME
    # ========================================================

    input_df = pd.DataFrame([input_data])


    # ========================================================
    # 13. MATCH EXACT TRAINING COLUMNS
    # ========================================================

    input_df = input_df.reindex(
        columns=expected_columns,
        fill_value=0
    )


    # ========================================================
    # 14. SCALE THE INPUT
    # ========================================================

    input_scaled = scaler.transform(input_df)


    # ========================================================
    # 15. MODEL PREDICTION
    # ========================================================

    prediction = model.predict(input_scaled)[0]


    # ========================================================
    # 16. PREDICTION PROBABILITY
    # ========================================================

    probability = model.predict_proba(input_scaled)[0][1]


    # ========================================================
    # 17. SHOW RESULT
    # ========================================================

    st.markdown("---")

    st.header("🔍 Prediction Result")


    if prediction == 1:

        st.error(
            "⚠️ Higher Possibility of Heart Disease"
        )

        st.metric(
            "Heart Disease Probability",
            f"{probability * 100:.2f}%"
        )

    else:

        st.success(
            "✅ Lower Possibility of Heart Disease"
        )

        st.metric(
            "Heart Disease Probability",
            f"{probability * 100:.2f}%"
        )


    # ========================================================
    # 18. DEBUG INFORMATION
    # ========================================================

    with st.expander("🔧 View Model Input"):

        st.write("Input Data Before Scaling:")

        st.dataframe(input_df)

        st.write("Expected Model Columns:")

        st.write(expected_columns)

        st.write("Raw Prediction:")

        st.write(prediction)

        st.write("Prediction Probability:")

        st.write(probability)


# ============================================================
# 19. DISCLAIMER
# ============================================================

st.markdown("---")

st.warning(
    "⚠️ This application is for educational and machine-learning "
    "demonstration purposes only. It is not a medical diagnosis."
>>>>>>> 8d287220de2b846f216862d9241541ef3ddd93e9
)