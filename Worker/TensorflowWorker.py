from Utils.database import get_talent_info
from Utils.Prediction import predict_rating, predict_salary, predict_performance

def get_talent(talent_id):
    result = get_talent_info(talent_id)
    pre_rating = predict_rating(result["role_id"], result["skill_set"], result["development"],
                                result["culture"], result["outstanding"], result["attitude"])
    pre_performance = predict_performance(pre_rating)
    pre_salary = predict_salary(pre_performance, result["role_id"], result["working_year"])
    pre_salary_next_three_month = []
    pre_return_next_three_month = [pre_performance, pre_performance, pre_performance]

    for i in range(1, 4):
        pre_salary_next_three_month.append(predict_salary(pre_performance, result["role_id"], result["working_year"]+i))

    talent_results = {
        "talent_id": talent_id,
        "pre_rating": pre_rating,
        "pre_performance": pre_performance,
        "pre_salary": pre_salary,
        "pre_salary_next_three_month": pre_salary_next_three_month,
        "pre_return_next_three_month": pre_return_next_three_month,
        "next_interview_percentage": get_next_interview_percentage(pre_performance)
    }

    return talent_results

def get_next_interview_percentage(pre_performance):
    return pre_performance




