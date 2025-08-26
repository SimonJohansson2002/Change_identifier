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

    news_items = tables.get_limited_rows(mycursor, table_name, 5, columns=['Date', 'Company ID', 'Industry', 'Summary'])
    
    return render_template("livenews.html", news=news_items)

@app.route('/company/<company_id>')
def company_details(company_id):
    table_name = 'screener'
    mydb, mycursor = databases.access_db('jfyu_1&ofQnsp1^d6FJ', 'deltalert')

    # Example: fetch details for that company (you can customize this query)
    company_data = tables.get_rows(mycursor, table_name, 4, company_id)

    return render_template("company.html", company=company_data)

if __name__=='__main__':
    app.run(debug=True)