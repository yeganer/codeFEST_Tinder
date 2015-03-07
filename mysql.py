#!/usr/bin/python

import _mysql as mysql
from MySQLdb.constants import FIELD_TYPE

class DBLink:
    def __init__(self, config):
        conv = {
                FIELD_TYPE.LONG: int,
                FIELD_TYPE.FLOAT: float,
                FIELD_TYPE.DOUBLE: float,
                FIELD_TYPE.CHAR: str}
        self.con = mysql.connect(host=config['ip'], user=config['user'], passwd=config['pw'], db=config['db'], conv=conv)
        self.result=0
        #print('connection established')
    def query(self, query):
        self.con.query(query)
        self.result = self.con.store_result()
        self.result = self.result.fetch_row(how=1, maxrows=0)
        #return self.con.use_result();
#    def __del__(self):
#        self.con.close()
    def fetch(self):
        for i in xrange(len(self.result)):
            yield self.result[i]
