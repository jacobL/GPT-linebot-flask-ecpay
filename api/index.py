from flask import Flask, request, abort 
import json
from datetime import datetime,timedelta
 
app = Flask(__name__) 
 
@app.route('/')
def home():
    return 'Hello, World!'
@app.route('/gg')
def gg():
    return 'Hello, GG!'
if __name__ == "__main__":
    app.run()
