from flask import Flask, render_template, jsonify, request
import time as t

app = Flask(__name__)

lastButtonPress = 0
rec_text = "bla"

@app.route("/")
def hello_world():
	return render_template('index.html')

@app.route('/but<int:button_id>', methods=['GET'])
def button_clicked(button_id):
	global lastButtonPress # not allowed to modify a global variable in a function unless you do this
	print(f"Button {button_id} Clicked!")
	lastButtonPress = button_id # update the info of what button was pressed last
	return render_template('index.html')

@app.route('/print_text', methods=['GET'])
def print_text():
    global rec_text
    text = request.args.get('input')  # Get the 'input' parameter from the URL
    rec_text = text
    print(f"Received text: {text}")
    return render_template('index.html')

@app.route('/text', methods=['GET'])
def received_text():
	global rec_text
	rec_text = request.args.get('sjfldak')
	return "thanks"

@app.route('/seetext')
def seetext():
    return rec_text

@app.route("/lastbut")
def lastbut():
	global lastButtonPress # not allowed to modify a global variable in a function unless you do this
	temp = lastButtonPress
	lastButtonPress = 0 # reset the thing when the info is handed over
	return str(temp) # must return a string not a number, this is web stuff

if __name__ == "__main__":
	 app.run(host="0.0.0.0", port=5000, debug=False) #this is so we dont have to do the specialized initiation command
