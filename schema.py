


class Schema(object):

    def __init__(self):
        self.column = {}
        self.sqlColumn = ''

    def integer(self,length):
        self.column['INTEGER']  = 11
        return self

    def notNull(self):
        self.column['NOT NULL'] = True
        return self

    def primaryKey(self,length):
        self.column['PRIMARY KEY'] = length
        return self

    def autoIncrement(self):
        self.column['AUTO_INCREMENT'] = True
        return self

    def getSchema(self,tableField):
        for field in tableField:
            print(tableField[field])
            if tableField[field].get('PRIMARY KEY') != None :
                self.sqlColumn += ' INTEGER(%i) NOT NULL AUTO_INCREMENT PRIMARY KEY(`%s`)' % (tableField[field].get('PRIMARY KEY'),field)
            elif tableField[field].get('INTEGER') != None :
                self.sqlColumn += ' INTEGER(%i)' % (tableField[field].get('INTEGER'))
            if tableField[field].get('NOT NULL') :
                self.sqlColumn += ' NOT NULL'
            if tableField[field].get('AUTO_INCREMENT') :
                self.sqlColumn += ' AUTO_INCREMENT'

            self.sqlColumn += '\n'
        return self.sqlColumn

