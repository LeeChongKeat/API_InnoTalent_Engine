import openai
import json

from database import get_department_skill_requirements


def init_api_key():
    with open("../config.json", "r") as config_file:
        config = json.load(config_file)
        openai.api_key = ["OpenAI"]["key"]

def match_resume_skill_percentage(resume_text, role_id):
    init_api_key()
    skill_list = get_department_skill_requirements(role_id)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"I have provided you with a list of skills: {skill_list}. Please identify any matching skills in the "
               f"given paragraph: {resume_text}. Count the matches and reply with the total number found only",
        max_tokens=1000
    )
    return response.choices[0].text.strip()

def match_resume_development_percentage(resume_text):
    init_api_key()
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"In the provided paragraph ({resume_text}), identify the latest education background, "
               f"any professional background, competitions, and events. Assign a rating of 10 points for a bachelor's "
               f"degree, 20 points for a master's degree, and 40 points for a Ph.D. For each identified professional "
               f"background, assign 20 points. For any course study entry,assign 10 points. Finally, calculate the "
               f"total points by summing up all the scores, just return the total points",
        max_tokens=1000
    )
    total_mark = int(response.choices[0].text.strip())
    if total_mark >= 100:
        return 5
    elif total_mark > 80:
        return 4
    elif total_mark > 60:
        return 3
    elif total_mark > 40:
        return 2
    return 1

def match_resume_outstanding_percentage(resume_text):
    init_api_key()
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"In the provided paragraph ({resume_text}), identify any competition entry, assign 20 points, and if "
               f"won, assign 40 points. Participation in any event is worth 10 points. Finally, calculate the total "
               f"points by summing up all the scores, just return the total points",
        max_tokens=1000
    )
    total_mark = int(response.choices[0].text.strip())
    if total_mark >= 100:
        return 5
    elif total_mark > 80:
        return 4
    elif total_mark > 60:
        return 3
    elif total_mark > 40:
        return 2
    return 1
