import sqlite3


db = sqlite3.connect('base.db')
cur = db.cursor()

cur.execute("""CREATE TABLE usersInfo(
    user_id integer,
    songs integer
)""")

# cur.execute('INSERT INTO usersInfo VALUES(1339, 0)')  # adding some info in table

# cur.execute('SELECT good_captcha FROM usersInfo')
# print(cur.fetchall())

# cur.execute("SELECT * FROM usersInfo WHERE user_id = 1337")
# item = cur.fetchall()[0]
# print(item[0])

# def update_info(id):
#     db = sqlite3.connect('base.db')
#     cur = db.cursor()

#     cur.execute(f"UPDATE usersInfo SET good_captcha = + 1 WHERE user_id == {id}")  # update some info

#     db.commit()
#     db.close()

# cur.execute("SELECT user_id FROM usersInfo")
# print(cur.fetchall())  # print all ids

db.commit()

db.close()
