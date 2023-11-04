import numpy as np
from keras.models import load_model

def predict_salary(performance, role_id, working_year):
    model = load_model('../AIModel/salary_model.h5')
    input_data = np.array([[performance, role_id, working_year]])
    predicted_salary = model.predict(input_data)
    return predicted_salary[0][0]

def predict_performance(rating):
    model = load_model('../AIModel/performance_model.h5')
    input_data = np.array([[rating]])
    predicted_performance = model.predict(input_data)
    return predicted_performance[0][0]

def predict_rating(role_id, skill_set, development, culture, outstanding, attitude):
    model = load_model('../AIModel/performance_model.h5')
    nor_skill_set = normalize(skill_set)
    nor_development = normalize(development)
    nor_culture = normalize(culture)
    nor_outstanding = normalize(outstanding)
    nor_attitude = normalize(attitude)
    input_data = np.array([[role_id, nor_skill_set, nor_development, nor_culture, nor_outstanding, nor_attitude]])
    predicted_rating = model.predict(input_data)
    return predicted_rating[0][0]

def normalize(value):
    return value / 5