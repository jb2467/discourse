from src.api.db_ultil import *

def get_users():
    query = "SELECT * FROM users"
    return exec_get_all(query)
def add_user(data):
    return exec_commit("INSERT INTO users(username, password, email, session_key) VALUES (%s, %s, %s, %s)", data)
def get_user(username,email):
    return exec_get_all("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
def get_user_password(username):
    return exec_get_all("SELECT password FROM users WHERE username = %s", (username,))
def update_session_key(key,username):
    exec_commit("UPDATE users SET session_key =%s WHERE username =%s",(key,username))
def get_session_key(username):
    return exec_get_all("SELECT session_key FROM users WHERE username = %s", (username,))