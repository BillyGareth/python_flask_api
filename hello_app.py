from flask import jsonify, request, Flask
import json as json
#from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route('/hello',methods=['POST'])
def hello():
    message = request.get_json(force=True)
    name = message['name']
    response = {
        'greeting': 'Hello ,' + name +'!....'
    }
    return jsonify(response)
if __name__=='__main__':
    app.run()