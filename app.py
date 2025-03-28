from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

@app.route('/')
def index():
    session['number'] = random.randint(1, 100)  # Generate a number between 1 and 100
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    user_guess = int(request.form.get('guess'))
    target_number = session.get('number')

    if user_guess < target_number:
        return jsonify({'message': 'Too low! Try again.'})
    elif user_guess > target_number:
        return jsonify({'message': 'Too high! Try again.'})
    else:
        session.pop('number', None)  # Reset game
        return jsonify({'message': 'Correct! You guessed the number.', 'reset': True})

if __name__ == '__main__':
    app.run(debug=True)
