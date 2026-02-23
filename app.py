from flask import Flask

app = Flask(__name__) 

@app.route('/')
def hello_world():
    return 'Welcome to the Ticketing System API'

@app.route('/tickets', methods=['GET'])
def returnAllTickets():
    return 'Here are all tickets'

@app.route('/tickets', methods=['POST'])
def createTicket():
    return 'Ticket created successfully'

if __name__ == '__main__':
    app.run(debug=True)