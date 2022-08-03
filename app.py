from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    det = 'Hello World!!! You are connected to machine '+ os.environ['KUBERNETES_SERVICE_HOST']
    return det
