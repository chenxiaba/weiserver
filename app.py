#!/usr/bin/python
# APP   : Messnote Server v0.1 
# author: chenxiaba
# date  : 2015.09.07

from flask import Flask , request, jsonify, make_response, abort
from redis import Redis 

#sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_declarative import Address, Base, Person

#database
engine = create_engine('sqlite:///messnote.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def index():
    redis.incr('hits')
    return 'Hello World! I have  been seen %s times' % redis.get('hits')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Login Succuss!"
    else:
        return "Please login first."

@app.route('/notes', methods = ['GET', 'POST'])
def handle_notes():
    if request.method == 'POST':
        #new note
        data = request.get_data()
        return  jsonify({'req_data':data})
    
    notes = [
        {
            "id" :1,
        }
    ]
    return  jsonify({'notes': notes})

@app.route('/notes/<int:note_id>', methods = ['GET'])
def note(note_id):
    abort(404)
    return "Notes page: %d" % note_id

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}), 404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)
    
