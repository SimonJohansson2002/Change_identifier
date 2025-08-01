from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def init():
    return render_template('main.html')

@app.route('/restructurings')
def go_restructuring():
    return render_template('restructuring.html')

@app.route('/strategy-changes')
def go_strategy():
    return render_template('strategy.html')

@app.route('/sentiments')
def go_sentiment():
    return render_template('sentiment.html')

if __name__=='__main__':
    app.run(debug=True)