
#!/usr/local/bin/python
# -*-coding: utf-8 -*-
import MySQLdb, os

#NSER='123.196.114.149'
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='ee4346tyh',port=3306)
    cur=conn.cursor()
    conn.select_db('test')
    count=cur.execute("select * from t")
    results=cur.fetchall()

    for r in results:
        sql="%s" % r
        if sql == "2":
                out='123.196.114.134;check_mysql;0;Mysql is running!!!\n'
                out_file=file('out.txt', 'w')
                out_file.write(out)
                out_file.close()

    cur.close()
    conn.close()
except:
                out_error='123.196.114.134;check_mysql;1;Mysql is warning!!!\n'
                out_file=file('out.txt', 'w')
                out_file.write(out_error)
                out_file.close()

cmd = '/usr/local/bin/send_nsca -H 123.196.114.149  -to 10 -d ";" -c /etc/send_nsca.cfg  < /usr/local/shell/nagios_check/python/out.txt'
os.system(cmd)