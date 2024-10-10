from flask import Flask, render_template
import time as t

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/secret_page")
def secret_lab():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000) #this is so we dont have to do the specialized initiation command

#yea after ill the python function syntax i read to achieve these beautiful functions, i have no idea
#whats going wrong


