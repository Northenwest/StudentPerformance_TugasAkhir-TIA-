import joblib
import pandas as pd
import argparse

def interpret_performance_level(prediction, gpa, study_time, absences):
    """
    Memberikan interpretasi rinci tentang tingkat kinerja siswa berdasarkan 
    prediksi dan metrik utama
    """
    base_interpretation = {
        0: "Low Performance Level - Siswa mungkin memerlukan dukungan tambahan",
        1: "Medium Performance Level - Siswa mengalami kemajuan yang cukup",
        2: "High Performance Level - Siswa berprestasi dengan sangat baik"
    }
    
    # Get base interpretation
    result = base_interpretation[prediction]
    
    # Add specific recommendations based on metrics
    recommendations = []
    
    if study_time < 10:
        recommendations.append("Pertimbangkan untuk menambah waktu belajar mingguan")
    if absences > 5:
        recommendations.append("Berusahalah untuk mengurangi ketidakhadiran untuk meningkatkan performa")
    if gpa < 2.0:
        recommendations.append("IPK anda rendah lakukan metode pembelajaran lebih intensif dan lakukan perbaikan nilai")
    elif gpa < 3.0:
        recommendations.append("IPK anda saat ini cukup rendah lakukan perbaikan nilai")
    
    # Combine result with recommendations if any exist
    if recommendations:
        result += "\nRecommendations:\n- " + "\n- ".join(recommendations)
    
    return result

def single_prediction(model, input_data, scaler=None):
    input_df = pd.DataFrame([input_data])
    
    if scaler is not None:
        input_scaled = scaler.transform(input_df)
    else:
        input_scaled = input_df
        
    prediction = model.predict(input_scaled)
    return prediction

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Memprediksi tingkat kinerja berdasarkan fitur masukan.")
    # [Previous argument definitions remain the same]
    parser.add_argument('--Age', type=int, required=True, help="Age of the student")
    parser.add_argument('--Gender', type=int, required=True, choices=[0, 1], help="Gender (0: Female, 1: Male)")
    parser.add_argument('--Ethnicity', type=int, required=True, help="Ethnicity category (encoded numerically)")
    parser.add_argument('--ParentalEducation', type=int, required=True, help="Parental education level (encoded numerically)")
    parser.add_argument('--StudyTimeWeekly', type=int, required=True, help="Weekly study time in hours")
    parser.add_argument('--Absences', type=int, required=True, help="Number of absences")
    parser.add_argument('--Tutoring', type=int, required=True, choices=[0, 1], help="Participation in tutoring (0: No, 1: Yes)")
    parser.add_argument('--ParentalSupport', type=int, required=True, help="Parental support level (encoded numerically)")
    parser.add_argument('--Extracurricular', type=int, required=True, choices=[0, 1], help="Participation in extracurricular activities (0: No, 1: Yes)")
    parser.add_argument('--Sports', type=int, required=True, choices=[0, 1], help="Participation in sports (0: No, 1: Yes)")
    parser.add_argument('--Music', type=int, required=True, choices=[0, 1], help="Participation in music activities (0: No, 1: Yes)")
    parser.add_argument('--Volunteering', type=int, required=True, choices=[0, 1], help="Participation in volunteering activities (0: No, 1: Yes)")
    parser.add_argument('--GPA', type=float, required=True, help="GPA of the student")
    parser.add_argument('--GradeClass', type=float, required=True, help="Class grade of the student")

    args = parser.parse_args()

    sample_input = {
        'Age': args.Age,
        'Gender': args.Gender,
        'Ethnicity': args.Ethnicity,
        'ParentalEducation': args.ParentalEducation,
        'StudyTimeWeekly': args.StudyTimeWeekly,
        'Absences': args.Absences,
        'Tutoring': args.Tutoring,
        'ParentalSupport': args.ParentalSupport,
        'Extracurricular': args.Extracurricular,
        'Sports': args.Sports,
        'Music': args.Music,
        'Volunteering': args.Volunteering,
        'GPA': args.GPA,
        'GradeClass': args.GradeClass,
    }

    # Load model dan scaler
    model = joblib.load('C:\\VSCode\\__Project\\__ProjectStudiIndependen_1\\archive_2\\archive_2\\random_forest_model.pkl')
    scaler = joblib.load('C:\\VSCode\\__Project\\__ProjectStudiIndependen_1\\archive_2\\archive_2\\scalerRevisi1.pkl')

    # Prediksi tunggal
    result = single_prediction(model, sample_input, scaler)

    # Get detailed interpretation
    interpretation = interpret_performance_level(
        result[0],
        sample_input['GPA'],
        sample_input['StudyTimeWeekly'],
        sample_input['Absences']
    )
    
    print("\nPrediction Results:")
    print("------------------")
    print(interpretation)