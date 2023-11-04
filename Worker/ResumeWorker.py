import os
from Utils.ResumeProcess import check_resume_exist_and_read
from Utils.OpenAI import match_resume_outstanding_percentage, match_resume_development_percentage, match_resume_skill_percentage
from Utils.database import insert_talent_characteristics, insert_talent
def save_resume_pdf_file(file):
    filename = os.path.join('../Resume', file.filename)
    file.save(filename)
    return filename

def read_resume_pdf_file(file_path):
    resume_text = check_resume_exist_and_read(file_path)
    return resume_text

def process_resume(file_path, apply_role_id):
    resume_text = read_resume_pdf_file(file_path)
    skill_set_mark = match_resume_skill_percentage(resume_text, apply_role_id)
    development_mark = match_resume_development_percentage(resume_text)
    outstanding_mark = match_resume_outstanding_percentage(resume_text)
    return skill_set_mark, development_mark, outstanding_mark

def process_record(file_path, apply_role_id, talent_id):
    skill_set_mark, development_mark, outstanding_mark = process_resume(file_path, apply_role_id)
    insert_talent_characteristics(talent_id, skill_set_mark, development_mark, 1, outstanding_mark, 1)

def process_talent(file, name, phone, email, age, working_year, salary, apply_role_id):
    talent_id = insert_talent(name, phone, email, age, working_year, salary)
    filename = save_resume_pdf_file(file)
    process_record(filename, apply_role_id, talent_id)
    return talent_id


