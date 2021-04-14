# import pymysql
#
# conn = pymysql.connect(host='localhost', database='eardoor',
#                        user='eardoor', password='14841484')
#
# sql = f'SELECT Records FROM records WHERE Name=\'Smark\';'
# # print(sql)
#
# cursor = conn.cursor()
# cursor.execute(sql)
# raw = cursor.fetchone()[0]
#
# print(raw)

from utils.database import Database

db = Database(host='localhost', database='eardoor',
                      user='eardoor', password='14841484', table='records')


print(db.select_records("Smark"))
print(db.update_records("Smark", '["123"]'))
