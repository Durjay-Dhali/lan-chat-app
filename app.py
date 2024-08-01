from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# To store messages
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    message = request.form['message']
    messages.append(message)
    return jsonify(success=True)

@app.route('/messages')
def get_messages():
    return jsonify(messages=messages)

if __name__ == '__main__':
    app.run(debug=True)