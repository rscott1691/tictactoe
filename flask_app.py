from flask import Flask, render_template, jsonify, request
from tictactoe import TicTacToe  # Import your Tic-Tac-Toe game logic

app = Flask(__name__)

# Initialize a new Tic-Tac-Toe game
game = TicTacToe()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def make_move():
    data = request.get_json()
    row, col = data['row'], data['col']
    result = game.make_move(row, col)  # Logic for making a move
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
