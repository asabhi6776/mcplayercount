from flask import Flask, jsonify, render_template, request
from mcstatus import JavaServer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_players', methods=['POST'])
def get_players():
    try:
        server_address = request.form['serverAddress']
        server = JavaServer.lookup(server_address)
        status = server.status()
        player_count = status.players.online
        return jsonify({'server_address': server_address, 'online_players': player_count})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
