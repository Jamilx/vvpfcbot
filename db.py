
import sqlite3


global conn
global cursor

class BotDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """Проверяем, есть ли юзер в базе"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        """Достаем id юзера в базе по его user_id"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]
    def new_user(self, user_id):
            day = "Понеділок"
            self.cursor.execute("INSERT INTO `recs` (`user_id_recs`, `day`) VALUES (?,?)", (user_id, day))
            day = "Вівторок"
            self.cursor.execute("INSERT INTO `recs` (`user_id_recs`, `day`) VALUES (?,?)", (user_id, day))
            day = "Середа"
            self.cursor.execute("INSERT INTO `recs` (`user_id_recs`, `day`) VALUES (?,?)", (user_id, day))
            day = "Четверг"
            self.cursor.execute("INSERT INTO `recs` (`user_id_recs`, `day`) VALUES (?,?)", (user_id, day))
            day = "П\'ятниця"
            self.cursor.execute("INSERT INTO `recs` (`user_id_recs`, `day`) VALUES (?,?)", (user_id, day))
            return self.conn.commit()

    def add_user(self, user_id, first_name, last_name, username):
        """Добавляем юзера в базу"""
        self.cursor.execute("INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `username`) VALUES (?,?,?,?)", (user_id, first_name, last_name, username))
        BotDB.new_user(self, user_id)
        return self.conn.commit()

    def add_all_info(self, user_id_recs, day, item, item1, item2, item3, item4,item_z,item1_z,item2_z,item3_z,item4_z):
        self.cursor.execute("INSERT INTO `recs` (`user_id_recs`, `day`, `item`, `item1`, `item2`, `item3`, `item4`,`item_z`,`item1_z`,`item2_z`,`item3_z`,`item4_z`) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (user_id_recs,day,item, item1, item2, item3, item4,item_z,item1_z,item2_z,item3_z,item4_z))
        return self.conn.commit()

    def cheking(self, user_id_recs, day, item, item1, item2, item3, item4,item_z,item1_z,item2_z,item3_z,item4_z):
        user_id = user_id_recs
        a = []
        for value in self.cursor.execute(f"SELECT * FROM recs WHERE `user_id_recs` = ?",  (user_id,)).fetchall():
            b = [user_id_recs, day]
            id = value[0]
            a.append(value[1])
            a.append(value[2])
            #print(a)
            #print(b)

            if a == b:

                self.cursor.execute(f"UPDATE recs SET `user_id_recs`=?,`day`=?, `item`=?, `item1`=?, `item2`=?, `item3`=?, `item4`=?, \
                                                                                `item_z`=?,`item1_z`=?,`item2_z`=?,`item3_z`=?,`item4_z`=? WHERE id = {id}",\
                                                                    (user_id_recs,day,item, item1, item2, item3, item4,item_z,item1_z,item2_z,item3_z,item4_z))
                #print('update')
                return self.conn.commit()
            a.clear()



    def see_schud(self, user_id_recs, day):
        user_id = user_id_recs
        av = []
        lest = []
        for value in self.cursor.execute(f"SELECT * FROM recs WHERE `user_id_recs` = ?",  (user_id,)).fetchall():
            bv = [user_id_recs, day]
            av.append(value[1])
            av.append(value[2])
            lest.append(value)
            g = value[3]
            #print(av)
            #print(bv)
            if av == bv: #Есть запись
                if g == None:
                    self.conn.commit()
                    return False
                else:
                    #   `id`      `user_id_recs`    `day`    , `item`    `item1`,     `item2`,   `item3`,   `item4`
                    #  value0         value1        value2    ,value3     value4,      value5,    value6,    value7
                    # `item_z`   `item1_z`,   `item2_z`,    `item3_z`,  `item4_z`
                    #  value8      value9,     value10,      value11,    value12
                    g ='   РОЗКЛАД НА '+value[2]+'\n\n'+ \
                       '┏━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓'+'\n'+ \
                       '┃'+'                    '+value[3]+'\n'+ \
                       '┃ 1️⃣Пара    ━━━━━━━━━━━━━━━━━━━━━━━'+'\n'+ \
                       '┃'+'                    '+value[8]+'\n'+\
                       '┣━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━┫'+'\n'+ \
                       '┃'+'                    '+value[4]+'\n'+ \
                       '┃ 2️⃣Пара    ━━━━━━━━━━━━━━━━━━━━━━━'+'\n'+ \
                       '┃'+'                    '+value[9]+'\n'+ \
                       '┣━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━┫' +'\n'+\
                       '┃'+'                    '+value[5]+'\n'+ \
                       '┃ 3️⃣Пара    ━━━━━━━━━━━━━━━━━━━━━━━'+'\n'+\
                       '┃'+'                    '+value[10]+'\n'+ \
                       '┣━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━┫'+'\n' \
                       '┃'+'                    '+value[6]+'\n'+ \
                       '┃ 4️⃣Пара    ━━━━━━━━━━━━━━━━━━━━━━━'+'\n'+\
                       '┃'+'                    '+value[11]+'\n'+\
                       '┣━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━┫'+'\n' \
                       '┃'+'                   '+value[7]+'\n'+ \
                       '┃ 5️⃣Пара    ━━━━━━━━━━━━━━━━━━━━━━━'+'\n'\
                       '┃'+'                    '+value[12]+'\n'+ \
                       '┗━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━┛'
                    #print(g)
                    self.conn.commit()
                    return g
            av.clear()
            lest.clear()

    def close(self):
        """Закрываем соединение с БД"""

        self.connection.close()

