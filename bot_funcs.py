import sqlite3


def check_user(user_id):
    db = sqlite3.connect('base.db')
    cur = db.cursor()

    cur.execute("SELECT user_id FROM usersInfo")
    dirrt_users = cur.fetchall()
    users = []

    for user in dirrt_users:
        users.append(user[0])
    
    if user_id in users:
        return 1
    
    else:
        cur.execute(f"INSERT INTO usersInfo VALUES({user_id}, 0)")
        db.commit()
        db.close()
        return 0     


def update_song(user_id):
    db = sqlite3.connect('base.db')
    cur = db.cursor()

    cur.execute(f"SELECT songs FROM usersInfo WHERE user_id = {user_id}")
    user_song = cur.fetchone()[0]

    cur.execute(f'UPDATE usersInfo SET songs = {user_song + 1} WHERE user_id == {user_id}')
    print('data was updated')

    db.commit()
    db.close()


def get_stat(user_id):
    db = sqlite3.connect('base.db')
    cur = db.cursor()

    cur.execute(f"SELECT songs FROM usersInfo WHERE user_id == {user_id}")
    songs = cur.fetchone()[0]

    return songs

    db.commit()
    db.close()


def newsletter_list():
    db = sqlite3.connect('base.db')
    cur = db.cursor()

    cur.execute("SELECT user_id FROM usersInfo")
    dirrt_users = cur.fetchall()
    users = []

    for user in dirrt_users:
        users.append(user[0])

    return users

    db.commit()
    db.close()
