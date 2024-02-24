from src.api.db_ultil import *


def get_courses(username):
    query = """
    SELECT courses.course_code, sections.section_code, courses.course_name
    FROM courses
    JOIN course_enrollment ON courses.course_code = course_enrollment.course_code
    JOIN users ON course_enrollment.student_username = users.username
    JOIN sections ON courses.course_code = sections.course_code
    WHERE users.username = %s;
    """
    return exec_get_all(query, (username,))
