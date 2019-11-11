from flask import Flask,render_template, request
import mysql.connector

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('login.html')

@app.route('/re_s')
def reg_s():
    return render_template('register.html')

@app.route('/re_t')
def reg_t():
    return render_template('register_teacher.html')

@app.route('/msg')
def mssg():
    return render_template('admin_msg.html')


@app.route('/re_s', methods=['POST'])
def regi_s():
    conn=mysql.connector.connect(host='localhost', db='db5', user='root', password='')
    fn=str(request.form['r1'])
    ln=str(request.form['r2'])
    em=str(request.form['r3'])
    yr=str(request.form['r4'])
    br=str(request.form['r5'])
    pw=str(request.form['r6'])
    cur=conn.cursor()
    cur.execute("insert into students values ('""','"+fn+"','"+ln+"','"+em+"','"+yr+"','"+br+"','"+pw+"','false')")
    conn.commit()
    return render_template('student.html')

@app.route('/re_t', methods=['POST'])
def regi_t():
    conn=mysql.connector.connect(host='localhost',db='db5', user='root', password="")
    fn=str(request.form['a1'])
    ln=str(request.form['a2'])
    em=str(request.form['a3'])
    br=str(request.form['a4'])
    sb=str(request.form['a5'])
    pw=str(request.form['a6'])
    cur=conn.cursor()
    cur.execute("insert into teacher values ('""','"+fn+"','"+ln+"','"+em+"','"+br+"','"+sb+"','"+pw+"','false')")
    conn.commit()
    return render_template('teacher.html')

@app.route('/log_in', methods=['POST'])
def logcode():
    em=str(request.form['p1'])
    pw=str(request.form['p2'])
    conn=mysql.connector.connect(host="localhost", db="db5", user="root", password="")
    cur=conn.cursor()
    cur.execute("select * From log_in where email='"+em+"' and password='"+pw+"'")
    ar=cur.fetchone()
    if (ar[2]=="admin"):
        return render_template("admin.html",user=ar)
    elif(ar[2]=="student"):
       return  render_template("after_login_student.html", user=ar)
    elif(ar[2]=="teacher"):
       return  render_template("after_login_teacher.html", user=ar)

@app.route('/trlist')
def teacher():
    conn=mysql.connector.connect(host='localhost', db='db5', user='root', password='')
    cur=conn.cursor()
    cur.execute("select * from teacher")
    ar = cur.fetchall()
    return render_template('teacher_list.html', data=ar)

@app.route('/stulist')
def student():
    conn=mysql.connector.connect(host='localhost', db='db5', user='root', password='')
    cur=conn.cursor()
    cur.execute("select * from students")
    ar = cur.fetchall()
    return render_template('student_list.html', data=ar)

@app.route('/msglist')
def msglist():
    conn=mysql.connector.connect(host='localhost', db='db5', user='root', password='')
    cur=conn.cursor()
    cur.execute("select * from msg")
    ar = cur.fetchall()
    return render_template('admin_msg.html', data=ar)


@app.route('/upd')
def update():
    conn= mysql.connector.connect(host='localhost', db='db5', user='root', password='')
    cur=conn.cursor()
    id=request.args.get('id')
    cur.execute("update teacher set status='true' where id="+id)
    conn.commit()
    cur.execute("select * from teacher where id="+id)
    arl=cur.fetchone()
    em=str(arl[3])
    pwd=str(arl[6])
    cur.execute("insert into log_in values('"+em+"','"+pwd+"','teacher')")
    conn.commit()
    cur.execute("select * from teacher")
    ar = cur.fetchall()
    return render_template('teacher_list.html')



@app.route('/upddt')
def del_t():
    conn= mysql.connector.connect(host='localhost', db='db5', user='root', password='')
    cur=conn.cursor()
    id=request.args.get('id')
    cur.execute("update teacher set status='false' where id="+id)
    conn.commit()
    return render_template('teacher_list.html')


@app.route('/upds')
def update_st():
    conn= mysql.connector.connect(host='localhost', db='db5', user='root', password='')
    cur=conn.cursor()
    id=request.args.get('id')
    cur.execute("update students set status='true' where id="+id)
    conn.commit()
    cur.execute("select * from students where id="+id)
    arl=cur.fetchone()
    em=str(arl[3])
    pwd=str(arl[6])
    cur.execute("insert into log_in values('"+em+"','"+pwd+"','student')")
    conn.commit()
    cur.execute("select * from students")
    ar = cur.fetchall()
    return render_template('student_list.html')

@app.route('/updds')
def del_st():
    conn= mysql.connector.connect(host='localhost', db='db5', user='root', password='')
    cur=conn.cursor()
    id=request.args.get('id')
    cur.execute("update students set status='false' where id="+id)
    conn.commit()
    return render_template('student_list.html')








@app.route('/msg', methods=['POST'])
def msg():
    conn=mysql.connector.connect(host='localhost',db='db5', user='root', password="")
    em=str(request.form['s1'])
    br=str(request.form['s2'])
    yr=str(request.form['s3'])
    msg=str(request.form['s4'])
    cur=conn.cursor()
    cur.execute("insert into msg values ('""','"+em+"','"+br+"','"+yr+"','"+msg+"')")
    conn.commit()
    return render_template('login.html')





if __name__ == '__main__':
    app.run()
