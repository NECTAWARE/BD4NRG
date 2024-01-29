from flask import Flask, request
from NECTAWARE import API as N
app = Flask(__name__)

@app.route('/')
def api():
	return N(request.args)
