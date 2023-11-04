from flask import Flask, request
from Worker.ResumeWorker import process_talent
from Worker.TensorflowWorker import get_talent
import os

app = Flask(__name__)

@app.route('/api/InnoTalent/SubmitApplication', methods=['POST'])
def insert_data():
    file = request.files['file']
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    email = data.get('email')
    age = data.get('age')
    working_year = data.get('working_year')
    salary = data.get('salary')
    apply_role_id = data.get('apply_role_id')
    talent_id = process_talent(file, name, phone, email, age, working_year, salary, apply_role_id)
    return talent_id

@app.route('/api/InnoTalent/Get/<int:talent_id>', methods=['GET'])
def get(talent_id):
    return get_talent(talent_id)


if __name__ == '__main__':
    app.run(debug=True)