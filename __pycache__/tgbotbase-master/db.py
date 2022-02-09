from multiprocessing.dummy import Value
import sqlite3
from unittest import result

class BotDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exits(self, user_id):
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def add_user(self, user_id):
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        return self.conn.commit()

    def add_schedule(self, user_id, week_day, item):
        self.cursor.execute("INSERT INTO `schedule` (`user_id`, `week_day`, `item`) VALUES (?,?,?)", (self.get_user_id(user_id), 
        week_day, item))
        return self.conn.commit()
        
    def get_schedule(self, user_id, within ="*"):

        result = self.cursor.execute("ELECT * FROM `schedule` WHERE `user_id` = ? ORDER BY 'date`",
        self.get_user_id(user_id))

        return result.fetchall()

    def close(self):
        self.conn.close()