from flask import app
from flask import render_template
from DailyLogs.models  import Item

@app.route('/')
@app.route('/home')
def homepage():
    return render_template("index.html")

@app.route('/status')
def satus_page():
    items=Item.query.all()
    return render_template('market.html', items=items)


def status_update():
    items =[
        {'id':1, 'task': "Work on Project 1", 'logs':"1 hr", 'progress': "COMPLETED"},
        {'id':2, 'task': "Learning Machine Language", 'logs':"2 hr", 'progress': "INCOMPLETE"},        
        {'id':3, 'task': "Atend a meeting", 'logs':"2 hr", 'progress': "INCOMPLETED"},
    ]


    con = sql.connect("database.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("select * from students")
   
    rows = cur.fetchall()
    return render_template("status.html",rows = rows)
    return render_template('status.html', items=items)



if __name__== "__main__":
    app.run(debug=True) 