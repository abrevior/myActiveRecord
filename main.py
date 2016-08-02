import mysql
from schema import Schema

tableField = {
    'id':Schema().primaryKey(11).column,
    'age':Schema().integer(11).column,
    'count':Schema().integer(11).notNull().column
}
print(tableField.get('id'))
print(tableField.get('age'))
print(Schema().getSchema(tableField))