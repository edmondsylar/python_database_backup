from flask import Flask, render_template, request
from controllers.db import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/backup', methods=['POST', 'GET'])
def backup():
    if request.method == 'POST':
        return render_template('index.html', error='Only accepts get requests')
    elif request.method == 'GET':
        # lets call a function to backup the databases here.
        response = export_db('ukwelys')
        print(response)
        return render_template('index.html', msg=response)



if __name__ == "__main__":
    app.run(debug=True, port=5000)