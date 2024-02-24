from src.api.db_ultil import *

def get_courses():
    query = "SELECT * FROM courses"
    return exec_get_all(query)