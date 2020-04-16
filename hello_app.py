from flask import jsonify, request, Flask

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