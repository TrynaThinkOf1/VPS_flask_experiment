from flask import Flask, render_template, request
import time as t

app = Flask(__name__)

lastButtonPress = 0
rec_text = ""

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/but<int:button_id>', methods=['GET'])
def button_clicked(button_id):
    global lastButtonPress
    print(f"Button {button_id} Clicked!")
    lastButtonPress = button_id
    return render_template('index.html')

# Updated route to handle text input via GET request
@app.route('/print_text', methods=['GET'])
def print_text():
    global rec_text
    text = request.args.get('input')  # Get the 'input' parameter from the URL
    rec_text = text
    print(f"Received text: {text}")
    return render_template('index.html')

@app.route('/text')
def received_text():
	global rec_text
	temp = rec_text
	rec_text = ""
	return temp

@app.route("/lastbut")
def lastbut():
    global lastButtonPress
    temp = lastButtonPress
    lastButtonPress = 0
    return str(temp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
