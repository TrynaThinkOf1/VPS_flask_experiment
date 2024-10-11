from flask import Flask, render_template, jsonify
import time as t

app = Flask(__name__)

lastButtonPress = 0

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/but<int:button_id>', methods=['GET'])
def button_clicked(button_id):
    global lastButtonPress
    print(f"Button {button_id} Clicked!")
    lastButtonPress = button_id # update the info of what button was pressed last
    return render_template('index.html')

@app.route("/lastbut")
def lastbut():
    global lastButtonPress
    temp = lastButtonPress
    lastButtonPress = 0
    return str(temp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
