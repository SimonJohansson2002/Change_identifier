from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def init():
    return render_template('main1.html')

@app.route('/screener')
def go_screener():
    return render_template('screener.html')

@app.route('/livenews')
def go_livenews():
    return render_template('livenews.html')

if __name__=='__main__':
    app.run(debug=True)