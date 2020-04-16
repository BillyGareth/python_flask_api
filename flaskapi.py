from flask import Flask
app = Flask(__name__)

@app.route('/test')
def first_api():
    return 'testing the output of a flask api_web linked'

if __name__ == '__main__':
    app.run()
