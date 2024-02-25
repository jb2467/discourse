from src.api.db_ultil import exec_commit


def add_messages(message, username, channel_id):
    query = """
    INSERT INTO chats (message, username, channel_id)
    VALUES (%s, %s, %s)
    """
    exec_commit(query, (message, username, channel_id))