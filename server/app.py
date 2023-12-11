from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.get('/messages')
def get_messages():
    data = Message.query.all()
    return [m.to_dict() for m in data], 200

@app.post('/messages')
def post_messages():
    try:
        message_dict = request.json
        new_m = Message(body = message_dict['body'], username = message_dict['username'])
        db.session.add(new_m)
        db.session.commit()
        return make_response(jsonify(message_dict), 201)
    except:
        return jsonify({'error': 'invalid message'}), 422
    

@app.patch('/messages/<int:id>')
def messages_by_id(id):
    patch_needer = Message.query.filter(id == id).first()
    new_body_suit = request.json
    try:
        setattr(patch_needer, 'body', new_body_suit['body'], )
        db.session.add(patch_needer)
        db.session.commit()
        return make_response(jsonify(new_body_suit), 200)
    except:
        return make_response(jsonify({'error': 'invalid message or user id'}), 404)

@app.delete('/messages/<int:id>')
def delete_by_id(id):
    try:
        m_to_delete = db.session.get(Message,id)
        db.session.delete(m_to_delete)
        db.session.commit()
        return make_response({}, 200)
    except:
        return make_response({'error': f'message {id} not found'}, 404)

if __name__ == '__main__':
    app.run(port=5555)
