import joblib
import pandas as pd

# Load model dan scaler
model = joblib.load('C:\\VSCode\\__Project\\__ProjectStudiIndependen_1\\archive_2\\archive_2\\random_forest_model.pkl')
scaler = joblib.load('C:\\VSCode\\__Project\\__ProjectStudiIndependen_1\\archive_2\\archive_2\\scalerRevisi1.pkl')  
print(type(scaler))
print(type(model))

# Fungsi untuk melakukan prediksi tunggal
def single_prediction(model, sample_input, scaler):
    # Konversi input ke DataFrame (pastikan input dalam bentuk 2D)
    input_df = pd.DataFrame([sample_input])  

    # Scaling data jika scaler disediakan
    if scaler is not None:
        input_scaled = scaler.transform(input_df)
    else:
        input_scaled = input_df

    # Prediksi menggunakan model
    prediction = model.predict(input_scaled)
    return prediction

# Contoh input data
sample_input = {
    'Age': 17,
    'Gender': 1,      
    'Ethnicity': 2,      
    'ParentalEducation': 2,              
    'StudyTimeWeekly': 22,       
    'Absences': 1,                
    'Tutoring': 2,                 
    'ParentalSupport': 3,                
    'Extracurricular': 2,        
    'Sports': 2,            
    'Music': 2,                
    'Volunteering': 2,         
    'GPA': 3.89,           
    'GradeClass': 2.0,         
}

# Prediksi
result = single_prediction(model, sample_input, scaler)

# Interpretasi hasil
performance_mapping = {0: "Low", 1: "Medium", 2: "High"}
performance_level = performance_mapping[result[0]]
print("Prediksi:", performance_level)
