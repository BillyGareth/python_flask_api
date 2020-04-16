# Python_Flask_Api
In recent years REST (REpresentational State Transfer) has emerged as the standard architectural design for web services and web APIs
Central to the concept of RESTful web services is the notion of resources. Resources are represented by URIs. 
The clients send requests to these URIs using the methods defined by the HTTP protocol, and possibly as a result of that the state of the affected resource changes.

#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
    
[further studies in flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
