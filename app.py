from flask import Flask, render_template, request, jsonify

from lib import *

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/permanize', methods=['POST', 'OPTIONS'])
def my_service():
	request.get_json(force=True)
	print(request.json)
	text = request.json['text']
	if 'apikey' in request.json and len(request.json['apikey'])>0:
		return jsonify(text=replaceText(text,request.json['apikey']))
	else:
		return jsonify(text=replaceText(text,False))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8012)
