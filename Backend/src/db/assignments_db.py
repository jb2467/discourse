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
    query = "INSERT INTO assignments (assignment_name, section_id, username) VALUES (%s, %s, %s)"
    for x in students:
        data = (assignment_name, section_id, x[0])
        exec_commit(query, data)
def get_students_in_section(course_code, section_code):
        section_id = get_section_id(course_code, section_code)
        query = """
        SELECT student_username
        FROM course_enrollment
        JOIN sections ON course_enrollment.section_id = %s
        """
        return exec_get_all(query, (section_id,))[0]
