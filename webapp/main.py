from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def init():
    return render_template('main.html')

@app.route('/screener')
def go_sentiment():
    return render_template('screener.html')

if __name__=='__main__':
    app.run(debug=True)