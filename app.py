from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    priority = db.Column(db.String(20))
    status = db.Column(db.String(20), default='open')
    language = db.Column(db.String(10))

with app.app_context():
    db.create_all()

@app.route('/tickets', methods=['GET'])
def returnAllTickets():
    tickets = Ticket.query.all()
    return jsonify([{
        'id': t.id,
        'title': t.title,
        'description': t.description,
        'priority': t.priority,
        'status': t.status,
        'language': t.language
    } for t in tickets])

@app.route('/tickets', methods=['POST'])
def createTicket():
    data = request.get_json()
    ticket = Ticket(
        title=data['title'],
        description=data.get('description'),
        priority=data.get('priority'),
        status=data.get('status', 'open'),
        language=data.get('language')
    )
    db.session.add(ticket)
    db.session.commit()
    return jsonify({'message': 'Ticket created'}), 201

if __name__ == '__main__':
    app.run(debug=True host='0.0.0.0')