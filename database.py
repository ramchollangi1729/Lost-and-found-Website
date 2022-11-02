import sqlite3
import hashlib
import datetime
import MySQLdb
from flask import session
from datetime import datetime

def db_connect():
    _conn = MySQLdb.connect(host="localhost", user="root",
                            passwd="North@123", db="collegeproduct")
    c = _conn.cursor()

    return c, _conn

# -------------------------------Loginact-----------------------------------------------------------------
def admin_loginact(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from admin where username='" +
                      username+"' and password='"+password+"'")
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))

def user_loginact(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from user where username='" +
                      username+"' and password='"+password+"' ")
        data = c.fetchall()
        # for a in data:
        #   session['uname'] = a[0]
       
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))


#-------------------------------------register---------------------------------------------------
def user_reg(username, password, email, rollno, department):
    try:
        c, conn = db_connect()
        print(username, password, email, rollno, department)
        j = c.execute("insert into user (username, password, email, rollno, department) values ('"+username +
                      "','"+password+"','"+email+"','"+rollno+"','"+department+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    
    
def lost_act(username, rollno, phone, product, department):
    try:
        c, conn = db_connect()
        print(username, rollno, phone, product, department)
        status="lost"
        j = c.execute("insert into lostproduct (username, rollno, phone, product, department,status) values ('"+username +
                      "','"+rollno+"','"+phone+"','"+product+"','"+department+"','"+status+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    
    
def status_act(username, product, status):
    try:
        c, conn = db_connect()
        print(username, product, status)
        j = c.execute("update lostproduct set status='"+status+"' where username='"+username+"' and product='"+product+"'  ")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
#--------------------------------------------view----------------------------------------------

def viewlost():
    c, conn = db_connect()
    c.execute("select * from lostproduct where status='lost'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result


def viewfound():
    c, conn = db_connect()
    c.execute("select * from lostproduct where status='found'")
    result = c.fetchall()
    conn.close()
    print(result)
    return result


def admin_vp():
    c, conn = db_connect()
    c.execute("select * from lostproduct where status='found'")
    result = c.fetchall()
    conn.close()
    print(result)
    return result




def updateact(a,d):
    c, conn = db_connect()
    c.execute("select * from lostproduct where username='"+a+"' and product='"+d+"'  ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result






def delete_act(a,d):
    c, conn = db_connect()
    j = c.execute("delete from lostproduct where username='"+a+"' and product='"+d+"' ")
    conn.commit()
    conn.close()
    return j


# ----------------------------------------------Update Items------------------------------------------


if __name__ == "__main__":
    print(db_connect())
