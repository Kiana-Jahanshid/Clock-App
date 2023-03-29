import sqlite3 

class Database :
    def __init__(self):
        self.con = sqlite3.connect("alarmlist.db")
        self.cursor = self.con.cursor()


    def get_alarm_from_db(self):
        alarm = self.cursor.execute("SELECT * FROM alarms").fetchall()
        return alarm 
    
    def add_new_alarm(self , active , new_title   ,new_time  , new_date ):
        try:
            self.cursor.execute(f"INSERT INTO alarms(active , title  ,time  ,date ) VALUES('{active}', '{new_title}' ,'{new_time}' , '{new_date}')")
            self.con.commit() 
            return True
        except:
            return False
        


    def remove_alarm(self , id):
        try:
            self.cursor.execute(f"DELETE FROM alarms WHERE ID={id}")
            self.con.commit()
            return True
        except:
            return False

    def edit_alarm(self, id, alarm_title , alarm_time , alarm_date):
        try:
            self.cursor.execute(f"UPDATE alarms SET title ='{alarm_title}' , time='{alarm_time}' , date='{alarm_date}' WHERE ID ='{id}' ")
            self.con.commit()
            return True
        except:
            return False
               
    def alarm_done(self , alarm_title):
        self.cursor.execute(f"UPDATE alarms SET active ={1} WHERE title ='{alarm_title}' ")
        self.con.commit()
        