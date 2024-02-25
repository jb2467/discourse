from src.db.course_db import get_courses, get_section_id
from src.api.db_ultil import *

def get_server_channels(server_name):
    query = """
    SELECT channels.channel_name FROM servers
    JOIN channels ON servers.server_name = channels.server_name
    WHERE channels.server_name = %s

    """
    return exec_get_all(query, (server_name,))

def get_messages(server_name, channel_name):
    query = """
    SELECT chats.message, chats.username FROM chats
    JOIN users ON chats.username = users.username
    JOIN channels ON chats.channel_id = channels.id
    JOIN servers ON channels.server_name = servers.server_name
    WHERE servers.server_name = %s AND channels.channel_name = %s
    """
    return exec_get_all(query, (server_name, channel_name))