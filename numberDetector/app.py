from flask import Flask, request
from numberDetect import carNum

app = Flask(__name__)

@app.route('/')
@app.route('/carNum', methods=['POST'])
def send_carNum():
    carNum = request.form.get()
    return carNum

if __name__ == 'main' :
    app.run(host='127.0.0.1', port=5000, debug=True)   