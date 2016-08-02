import pymysql
from warnings import filterwarnings
from datetime import datetime


class myOrm(object):
    def writeLog(self, errorClass, e):
        message = "Error class: %s |" \
                  " Error number: %i |" \
                  " Error message: %s |" \
                  " Time: %s ;\n" % (str(errorClass),
                                     e.args[0],
                                     e.args[1],
                                     datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
        with open('mysql.log', 'a') as file_log:
            file_log.writelines(message)
            file_log.close()

    def connect(self):
        filterwarnings('ignore', category=pymysql.Warning)
        try:
            self.connection = pymysql.connect(host='localhost',
                                              user='root',
                                              passwd='root',
                                              db='python')
            if self.connection is not None:
                print('Connection done!')
                self.drop_table_query = self.connection.query('DROP TABLE IF EXISTS `%s`', (str('user')))
                self.connection.commit()
                self.cursor = self.connection.cursor()
        except pymysql.Error as e:
            print('Connection failed!!!')
            self.writeLog(pymysql.Error, e)

    def dropTable(self, table):
        try:
            # self.cursor.execute(self.drop_table_query)
            self.connection.commit()
        except pymysql.Error as e:
            self.writeLog(pymysql.Error, e)
            print('Drop failed')


            # table_user = ("CREATE TABLE IF NOT EXISTS `user` ("
            #               "`id` integer(11) auto_increment,"
            #               "`name` varchar(50) not null,"
            #               "`surname` varchar(50) not null,"
            #               "`password` varchar(20) not null,"
            #               "PRIMARY KEY(`id`))")
            # cursor.execute(table_user)
            # connection.commit()
            #
            # insert_serega = ("INSERT INTO `user`(`name`, `surname`, `password`) VALUES ('serega','kolesnk','lololo')")
            # cursor.execute(insert_serega)
            # connection.commit()
            #
            #
            # def select_user():
            #     select_data = ("SELECT * FROM `user` where `user_type` like 'man'")
            #     cursor.execute(select_data)
            #     return cursor
            #
            # connection.close()


start = myOrm()
start.connect()
start.dropTable("user")
# CREATE TABLE IF NOT EXISTS `user` ("
# "`id` integer(11) auto_increment,"
# "`name` varchar(50) not null,"
# "`surname` varchar(50) not null,"
# "`password` varchar(20) not null,"
# "PRIMARY KEY(`id`));#")
