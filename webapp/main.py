from flask import Flask, redirect, url_for, request, render_template
from structure import databases, tables

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'Simon',
    'password': 'jfyu_1&ofQnsp1^d6FJ',
    'database': 'your_database'
}

@app.route('/')
def init():
    return render_template('main.html')

@app.route('/screener')
def go_screener():
    return render_template('screener.html')

@app.route('/livenews')
def go_livenews():
    table_name = 'screener'
    mydb, mycursor = databases.access_db('jfyu_1&ofQnsp1^d6FJ', 'deltalert')

    news_items = tables.get_limited_rows(mycursor, table_name, 5, columns=['Date', 'Company ID', 'Summary', 'Guidance'])
    
    return render_template("livenews.html", news=news_items)

if __name__=='__main__':
    app.run(debug=True)