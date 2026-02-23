from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
import time 
import sqlalchemy

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

def connect_with_retry():
    retries = 10
    while retries > 0:
        try:
            with app.app_context():
                db.create_all()
            print("Database connected successfully")
            return
        except sqlalchemy.exc.OperationalError:
            retries -= 1
            print(f"Database not ready, retrying... ({retries} attempts left)")
            time.sleep(3)
    raise Exception("Could not connect to database after multiple retries")

connect_with_retry()

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
    app.run(debug=True, host='0.0.0.0')