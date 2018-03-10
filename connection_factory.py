# -*- coding: UTF-8 -*-

import MySQLdb
"""FACTORY"""

class Connection_Factory(Object)

    def get_connection():
        connection=MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="root",
            db="python-design-patterns-2")

        return connection