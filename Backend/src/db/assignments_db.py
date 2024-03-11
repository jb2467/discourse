from src.db.course_db import get_section_id
from src.api.db_ultil import *

def get_assignments(data):

    query = """
    SELECT assignment_name 
    FROM assignments 
    JOIN sections ON assignments.section_id = sections.id
    JOIN courses ON sections.course_code = courses.course_code
    WHERE username = %s AND courses.course_code = %s AND sections.section_code = %s;
    """
    return exec_get_all(query, data)

def add_assignment(assignment_name, course_code, section_code):
    students = get_students_in_section(course_code, section_code)
    section_id = get_section_id(course_code, section_code)
    print(section_id, 'section_id')
    query = "INSERT INTO assignments (assignment_name, section_id, username) VALUES (%s, %s, %s)"
    for x in students:
        print(x[0], 'student')
        data = (assignment_name, section_id, x[0])
        exec_commit(query, data)

    print(exec_get_all("SELECT * FROM assignments WHERE section_id = %s",(section_id,) ))

def get_students_in_section(course_code, section_code):
    section_id = get_section_id(course_code, section_code)
    print(course_code, 'course_code')
    print(section_code, 'section_code')
    query = """
    SELECT student_username
    FROM course_enrollment
    WHERE section_id = %s
    """
    return exec_get_all(query, (section_id,))
