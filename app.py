from flask import Flask
app = Flask(__name__)

@app.route('/')
def version1():
    return 'version1'
