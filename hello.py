from flask import Flask, render_template, jsonify
import time as t

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/button/<int:button_id>', methods=['GET'])
def button_clicked(button_id):
	print(f"Button {button_id} Clicked!")
	return f"Button {button_id} Clicked!"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True) #this is so we dont have to do the specialized initiation command

#yea after ill the python function syntax i read to achieve these beautiful functions, i have no idea
#whats going wrong


