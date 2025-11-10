from flask import Flask, render_template, request, jsonify
from main import check_password_strength

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_password():
    try:
        data = request.get_json()
        password = data.get('password', '')
        name = data.get('name', '')
        
        strength, feedback = check_password_strength(password, name)
        
        return jsonify({
            'strength': strength,
            'feedback': feedback
        })
    except Exception as e:
        return jsonify({
            'strength': 'Error',
            'feedback': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

