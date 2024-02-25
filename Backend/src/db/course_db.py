from src.api.db_ultil import *


def get_courses(username):
    query = """
    SELECT courses.course_code, sections.section_code, admins.username AS course_admin, courses.course_name
    FROM courses
    JOIN course_enrollment ON courses.course_code = course_enrollment.course_code
    JOIN sections ON course_enrollment.section_id = sections.id
    JOIN users AS admins ON sections.course_admin_username = admins.username
    WHERE course_enrollment.student_username = %s;
    """
    return exec_get_all(query, (username,))

def get_section_id(course_code, section_code):
    print(course_code, section_code)
    query = "SELECT id FROM sections WHERE course_code = %s AND section_code = %s;"
    return exec_get_all(query, (course_code, section_code))[0][0]
