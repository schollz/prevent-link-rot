from flask import Flask, render_template, request, jsonify

from lib import *

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return render_template('base.html')

@app.route('/permanize', methods=['GET', 'OPTIONS'])
def my_service():
        text = request.args.get('text', '')
        return jsonify(text=replaceText(text))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8012)