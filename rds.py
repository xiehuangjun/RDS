import pymysql, os

mysql = pymysql.connect(user = "root", password = "123456789", port = 3306, host = "hj-database.c9utezksdmjh.us-east-1.rds.amazonaws.com")
cur = mysql.cursor()
cur.execute('''CREATE DATABASE Test;''')

cur.execute('''CREATE TABLE IF NOT EXISTS Test.information (
                Student_id CHAR(50) NOT NULL PRIMARY KEY,
                Name CHAR(50) NOT NULL
                )ENGINE = InnoDB DEFAULT CHARSET = utf8 COLLATE = utf8_unicode_ci;''')

cur.execute('''INSERT INTO Test.information ( Student_id, Name) VALUES
                                            ("M10902208", "HJ")''')

mysql.commit()
cur.close()
