import mysql.connector
import json

def get_mysql_connection():
    with open("../config.json", "r") as config_file:
        config = json.load(config_file)

    connection = mysql.connector.connect(
        host=config["database"]["host"],
        user=config["database"]["user"],
        password=config["database"]["password"],
        database=config["database"]["database_name"]
    )
    return connection

def insert_talent_characteristics(talent_id, skill_set, development, culture,outstanding, attitude):
    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = ("INSERT INTO talent_characteristics (talentId, skill_set, development, culture,outstanding, attitude) VALUES (%s, %s, "
             "%s, %s, %s, %s)")
    cursor.execute(query, (talent_id, skill_set, development, culture,outstanding, attitude))
    connection.commit()
    connection.close()

def insert_talent(name, phone, email, age, working_year, salary):
    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = ("INSERT INTO talent (name, phone, email, age, working_year, salary) VALUES (%s, %s, "
             "%s, %s, %s, %s)")
    cursor.execute(query, (name, phone, email, age, working_year, salary))
    connection.commit()
    inserted_id = cursor.lastrowid
    connection.close()
    return inserted_id

def get_talent_info(talent_id):
    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = ("SELECT t.id, t.name, t.phone, t.email, t.age, t.working_year, t.salary, "
             "c.skill_set, c.development, c.culture, c.outstanding, c.attitude "
             "FROM talent AS t "
             "LEFT JOIN talent_characteristics AS c ON t.id = c.talentId "
             "WHERE t.id = %s")
    cursor.execute(query, talent_id)
    data = cursor.fetchall()
    connection.close()
    results = []
    for row in data:
        results.append({
            'id': row[0],
            'name': row[1],
            'phone': row[2],
            'email': row[3],
            'age': row[4],
            'working_year': row[5],
            'salary': row[6],
            'skill_set': row[7],
            'development': row[8],
            'culture': row[9],
            'outstanding': row[10],
            'attitude': row[11]
        })
    return results[0]

def get_department_skill_requirements(role_id):
    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = ("SELECT skill "
             "FROM skill_requirements "
             "WHERE role_id = %s")
    cursor.execute(query, role_id)
    data = cursor.fetchall()
    connection.close()
    result = ""
    for row in data:
        result = result + row[0]
    return result


