from flask import request, Flask, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    print("---------------- Hello world -------------")
    # return '<p>Hello World</p>'
    return {
        "msg": "success",
        "data": "welcome to use flask.."
    }

@app.route('/data')
def process_data():
    print('Data received \n %s' %str(request.data, 'UTF-8'))

    result = {"message": "Data received and processed successfully"}
    return jsonify(result)

@app.route('/data.action')
def post_data():
    print('Data received \n %s' %str(request.data, 'UTF-8'))

    result = {"message": "Data received and processed successfully"}
    return jsonify(result)

def run_api():
    app.run(host='0.0.0.0',port=49144,threaded=False)

if __name__ == '__main__':
   run_api()