from flask import Flask, render_template, jsonify
import time as t

app = Flask(__name__)

lastButtonPress = 0

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/but<int:button_id>', methods=['GET'])
def button_clicked(button_id):
    global lastButtonPress # not allowed to modify a global variable in a function unless you do this
    print(f"Button {button_id} Clicked!")
    lastButtonPress = button_id # update the info of what button was pressed last
    return render_template('index.html')

@app.route("/lastbut")
def lastbut():
    global lastButtonPress # not allowed to modify a global variable in a function unless you do this
    temp = lastButtonPress
    lastButtonPress = 0 # reset the thing when the info is handed over
    return str(temp) # must return a string not a number, this is web stuff

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True) #this is so we dont have to do the specialized initiation command

#yea after ill the python function syntax i read to achieve these beautiful functions, i have no idea
#whats going wrong


