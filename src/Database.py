import mysql.connector

class Database(object):
    def __init__(self, user, passwd):
        self.__conn = mysql.connector.connect(
                user=user, password=passwd, host='localhost', database='sci_db',
                auth_plugin='mysql_native_password'
        )
        version_table = self.__query_fetchall(
                "SHOW VARIABLES LIKE \"%version%\"")
        self.version_error = True
        for entry in version_table:
            if (entry['Variable_name'] == 'version' and
            int(entry['Value'][0]) > 7):
                self.version_error = False

    def __concat(self, fields):
        tmp_str = ""
        tmp_len = len(fields)
        for i in range(0, tmp_len):
            tmp_str += fields[i]
            if (i != tmp_len-1):
                tmp_str += ", "
        return tmp_str

    def __concat_format(self, fields):
        tmp_str = ""
        tmp_len = len(fields)
        for i in range(0, tmp_len):
            tmp_str += "'" + fields[i] + "'"
            if (i != tmp_len-1):
                tmp_str += ", "
        return tmp_str

    def __concat_values(self, fields, values):
        tmp_str = ""
        tmp_len = len(fields)
        for i in range(0, tmp_len):
            tmp_str += fields[i] + " = '" + values[i] + "'"
            if (i != tmp_len-1):
                tmp_str += ", "
        return tmp_str

    def __concat_values_and(self, fields, values):
        text = self.__concat_values(fields, values)
        for i in range(len(text)):
            if text[i] == ",":
                text = text[:i] + " AND" + text[i+1:]
        return text
    
    def __concat_like(self, fields, values):
        tmp_str = ""
        tmp_len = len(fields)
        for i in range(0, tmp_len):
            tmp_str += fields[i] + " LIKE \"%" + values[i] + "%\""
            if (i != tmp_len-1):
                tmp_str += " OR "
        return tmp_str

    def __query_exec(self, query):
        db_dict = self.__conn.cursor(dictionary=True)
        db_dict.execute(query)
        return db_dict

    def __query_commit(self, query):
        db_dict = self.__query_exec(query)
        self.__conn.commit()
        db_dict.close()
    
    def __query_fetchall(self, query):
        db_dict = self.__query_exec(query)
        db_data = db_dict.fetchall()
        db_dict.close()
        return db_data
    
    def last_insert_id(self):
        return self.__query_fetchall("SELECT LAST_INSERT_ID()")

    def select(self, table, fields, where_fields = None, where_values = None,
            order_by = None, limit = None, offset = None, like = None):
        db_query = "SELECT " + self.__concat(fields) + " FROM " + table
        if (where_fields != None and where_values != None):
            db_query += " WHERE "
            if (like):
                db_query += self.__concat_like(where_fields, where_values) 
            else:
                db_query += self.__concat_values_and(where_fields, where_values) 
            where = True
        if (order_by != None):
            db_query += " ORDER BY " + order_by
        if (limit != None):
            db_query += " LIMIT " + limit
        if (offset != None):
            db_query += " OFFSET " + offset
        return self.__query_fetchall(db_query)

    def insert(self, table, fields, values):
        db_query = "INSERT INTO " + table + " (" 
        db_query += self.__concat(fields) + ") VALUES ("
        db_query += self.__concat_format(values) + ")" 
        self.__query_commit(db_query)

    def delete(self, table, where_fields, where_values):
        db_query = "DELETE FROM " + table + " WHERE "
        db_query += self.__concat_values(where_fields, where_values)
        self.__query_commit(db_query)

    def update(self, table, set_fields, set_values,
            where_fields, where_values):
        db_query = "UPDATE " + table + " SET " 
        db_query += self.__concat_values(set_fields, set_values) + " WHERE "
        db_query += self.__concat_values(where_fields, where_values)
        self.__query_commit(db_query)

    def close(self):
        self.__conn.close()

